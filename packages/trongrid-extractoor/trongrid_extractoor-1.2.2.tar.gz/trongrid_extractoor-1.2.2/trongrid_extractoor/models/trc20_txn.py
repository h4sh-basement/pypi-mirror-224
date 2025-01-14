"""
Dataclass representing one TRC20 token transfer.
"""
from dataclasses import asdict, dataclass, fields
from typing import Any, Dict, List, Optional, Tuple, Union

import pendulum

from trongrid_extractoor.config import log
from trongrid_extractoor.models.tron_event import TronEvent
from trongrid_extractoor.helpers.address_helpers import hex_to_tron
from trongrid_extractoor.helpers.rich_helpers import console
from trongrid_extractoor.helpers.string_constants import DATA, RESULT, TRANSFER
from trongrid_extractoor.helpers.time_helpers import ms_to_datetime

# Some tokens use src/dst/wad instead of from/to/value
FROM_TO_AMOUNT = ('from', 'to', 'amount')
FROM_TO_VALUE = ('from', 'to', 'value')
SRC_DST_WAD = ('src', 'dst', 'wad')
CSV_FIELDS = 'token_address,from_address,to_address,amount,transaction_id,event_index,ms_from_epoch,block_number'.split(',')


@dataclass(kw_only=True)
class Trc20Txn(TronEvent):
    from_address: str
    to_address: str
    amount: int

    def __post_init__(self):
        super().__post_init__()
        self.amount = int(float(self.amount))
        self.from_address = hex_to_tron(self.from_address) if self.from_address.startswith('0x') else self.from_address
        self.to_address = hex_to_tron(self.to_address) if self.to_address.startswith('0x') else self.to_address

    @classmethod
    def from_event_dict(cls, row: Dict[str, Union[str, float, int]]) -> 'Trc20Txn':
        # Check the 'result_type' to see if it's from/to/value or src/dst/wad keys.
        txn_from, txn_to, txn_amount = cls.identify_txn_keys(row['result_type'])
        event = TronEvent.from_event_dict(row)

        return cls(
            from_address=row[RESULT][txn_from],
            to_address=row[RESULT][txn_to],
            amount=int(float(row[RESULT][txn_amount])),
            **{k: v for k, v in asdict(event).items()}
        )

    @classmethod
    def extract_from_wallet_transactions(cls, response: dict[str, Any]) -> List['Trc20Txn']:
        """Extract a list of txns from the Trongrid response object."""
        txns = [
            cls(
                event_name=TRANSFER,
                token_address=row['token_info']['address'],
                from_address=row['from'],
                to_address=row['to'],
                amount=float(row['value']) / 10**row['token_info']['decimals'],
                ms_from_epoch=float(row['block_timestamp']),
                transaction_id=row['transaction_id'],
                event_index=row['event_index']
            )
            for row in response['data']
        ]

        log.debug(f"Extracted {len(txns)} txns from the response...")
        return txns

    @classmethod
    def csv_fields(cls) -> List[str]:
        return CSV_FIELDS

    @classmethod
    def csv_header_row_length(cls) -> int:
        """When this class is exported to a CSV this would be the size of an empty file."""
        return len(','.join(cls.csv_fields())) + 1

    def as_dict(self, keys: Optional[List[str]] = None) -> Dict[str, Any]:
        """Get a dict representation that's ready for CSV writing."""
        keys = keys or self.csv_fields()
        return {k: v for k, v in asdict(self).items() if k in keys}

    def __str__(self) -> str:
        msg = f"Token: {self.token_address[0:10]}..., From: {self.from_address[0:10]}..."
        msg += f", To: {self.to_address[0:10]}..., ID: {self.transaction_id[0:10]}.../{self.event_index}"
        msg += f", Amount: {self.amount} (at {self.datetime})"
        return msg

    @staticmethod
    def identify_txn_keys(result_type: Dict[str, str]) -> Tuple[str, str, str]:
        if sorted(result_type.keys()) == sorted(SRC_DST_WAD):
            return SRC_DST_WAD
        elif sorted(result_type.keys()) == sorted(FROM_TO_AMOUNT):
            return FROM_TO_AMOUNT
        else:
            return FROM_TO_VALUE

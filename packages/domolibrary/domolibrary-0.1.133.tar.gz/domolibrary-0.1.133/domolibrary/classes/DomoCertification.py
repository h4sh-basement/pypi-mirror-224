# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/classes/50_DomoCertification.ipynb.

# %% auto 0
__all__ = []

# %% ../../nbs/classes/50_DomoCertification.ipynb 2
import datetime as dt
from dataclasses import dataclass
from enum import Enum
import domolibrary.utils.convert as cd
import domolibrary.utils.DictDot as util_dd


class DomoCertificationState(Enum):
    CERTIFIED = 'certified'
    PENDING = 'PENDING'


@dataclass
class DomoCertification:
    certification_state: DomoCertificationState
    last_updated: dt.datetime
    certification_type: str
    certification_name: str

    @classmethod
    def _from_json(cls, obj):
        dd = util_dd.DictDot(obj) if isinstance(obj, dict) else obj
        return cls(certification_state=DomoCertificationState[dd.state].value or dd.state,
                   last_updated=cd.convert_epoch_millisecond_to_datetime(
                       dd.lastUpdated),
                   certification_type=dd.processType,
                   certification_name=dd.processName
                   )


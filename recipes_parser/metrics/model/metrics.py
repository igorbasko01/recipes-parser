from datetime import datetime
from dataclasses import dataclass


@dataclass
class MetricLong:
    name: str
    value: int


@dataclass
class MetricDate:
    name: str
    date: datetime
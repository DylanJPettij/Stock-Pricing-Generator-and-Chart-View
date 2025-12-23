from datetime import datetime 
from dataclasses import dataclass

@dataclass
class OHLCData: 
    High: float
    Low: float
    Open: float
    Close: float
    Volume: float
    timestamp: datetime
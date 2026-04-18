from pydantic import BaseModel


class ScannerConfig(BaseModel):
    max_batch_targets: int = 100
    minimum_check_count: int = 1000
    enterprise_mode: bool = True


CONFIG = ScannerConfig()

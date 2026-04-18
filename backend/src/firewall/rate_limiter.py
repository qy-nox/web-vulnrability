from collections import defaultdict
from time import time


class AdaptiveRateLimiter:
    def __init__(self, window_seconds: int = 60, request_limit: int = 120) -> None:
        self.window_seconds = window_seconds
        self.request_limit = request_limit
        self._requests = defaultdict(list)

    def is_allowed(self, key: str) -> bool:
        now = time()
        bucket = self._requests[key]
        self._requests[key] = [stamp for stamp in bucket if now - stamp <= self.window_seconds]
        if len(self._requests[key]) >= self.request_limit:
            return False
        self._requests[key].append(now)
        return True

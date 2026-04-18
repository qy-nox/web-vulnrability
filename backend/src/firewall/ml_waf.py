from src.firewall.behavioral_analyzer import BehavioralAnalyzer
from src.firewall.rate_limiter import AdaptiveRateLimiter


class MLWAF:
    def __init__(self) -> None:
        self.rate_limiter = AdaptiveRateLimiter()
        self.behavioral = BehavioralAnalyzer()

    def should_block(self, identity: str, signal: dict) -> bool:
        if not self.rate_limiter.is_allowed(identity):
            return True
        return self.behavioral.classify(signal) == "malicious"

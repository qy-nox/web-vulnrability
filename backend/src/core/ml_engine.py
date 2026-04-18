from dataclasses import dataclass


@dataclass
class MLRiskSignal:
    anomaly_score: float
    behavior_risk: float


class MLEngine:
    def evaluate_target(self, target: str) -> MLRiskSignal:
        entropy_like = (sum(ord(c) for c in target) % 100) / 100
        return MLRiskSignal(
            anomaly_score=round(entropy_like, 2),
            behavior_risk=round(1 - entropy_like / 2, 2),
        )

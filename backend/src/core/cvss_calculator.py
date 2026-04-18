from dataclasses import dataclass


@dataclass
class CVSSVector:
    attack_complexity: float = 0.77
    privileges_required: float = 0.85
    user_interaction: float = 0.85
    scope: float = 1.0
    confidentiality: float = 0.56
    integrity: float = 0.56
    availability: float = 0.56


class CVSSCalculator:
    def calculate_base_score(self, vector: CVSSVector) -> float:
        impact = 1 - ((1 - vector.confidentiality) * (1 - vector.integrity) * (1 - vector.availability))
        exploitability = (
            8.22
            * vector.attack_complexity
            * vector.privileges_required
            * vector.user_interaction
            * vector.scope
        )
        score = min(10.0, round((impact * 6.42) + exploitability, 1))
        return score

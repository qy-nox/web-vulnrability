from typing import Dict


class BehavioralAnalyzer:
    def classify(self, request_profile: Dict[str, float]) -> str:
        score = sum(request_profile.values())
        if score > 8:
            return "malicious"
        if score > 4:
            return "suspicious"
        return "benign"

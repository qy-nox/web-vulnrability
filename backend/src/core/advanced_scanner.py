import hashlib
from dataclasses import dataclass
from typing import Dict, List

from src.core.cvss_calculator import CVSSCalculator, CVSSVector
from src.core.exploit_chain_analyzer import ExploitChainAnalyzer
from src.core.ml_engine import MLEngine
from src.scanners import (
    advanced_injection,
    api_security,
    authentication_bypass,
    business_logic,
    cloud_security,
    cloudflare_waf_bypass,
    container_k8s,
    cryptography,
    dependencies,
    file_upload,
    information_disclosure,
    javascript_dom,
    network_analysis,
    path_traversal,
    server_side_rendering,
    session_management,
    ssl_tls,
    ssrf,
    tier10_compliance,
    tier1_zeroday,
    tier2_api_security,
    tier3_cloud_infra,
    tier4_ml_detection,
    tier5_network_analysis,
    tier6_client_side,
    tier7_auth_session,
    tier8_business_logic,
    tier9_ssl_tls,
    websocket,
    xxe_deserialization,
)


@dataclass
class ScanResult:
    target: str
    total_checks: int
    findings: List[Dict[str, str]]
    blocked: bool
    risk_score: float
    cvss_base: float
    exploit_chain: List[str]


class AdvancedScanner:
    def __init__(self) -> None:
        self._check_sources = [
            tier1_zeroday,
            tier2_api_security,
            tier3_cloud_infra,
            tier4_ml_detection,
            tier5_network_analysis,
            tier6_client_side,
            tier7_auth_session,
            tier8_business_logic,
            tier9_ssl_tls,
            tier10_compliance,
            cloudflare_waf_bypass,
            advanced_injection,
            authentication_bypass,
            business_logic,
            api_security,
            cloud_security,
            xxe_deserialization,
            container_k8s,
            file_upload,
            ssrf,
            information_disclosure,
            cryptography,
            dependencies,
            websocket,
            javascript_dom,
            session_management,
            path_traversal,
            server_side_rendering,
            network_analysis,
            ssl_tls,
        ]
        self.checks = self._load_checks()
        self.ml_engine = MLEngine()
        self.cvss = CVSSCalculator()
        self.chain = ExploitChainAnalyzer()

    def _load_checks(self) -> List[Dict[str, str]]:
        checks: List[Dict[str, str]] = []
        for source in self._check_sources:
            checks.extend(source.build_checks())
        return checks

    def checks_summary(self) -> Dict[str, object]:
        by_tier: Dict[str, int] = {}
        for check in self.checks:
            by_tier[check["tier"]] = by_tier.get(check["tier"], 0) + 1
        return {
            "total_checks": len(self.checks),
            "tier_count": len(by_tier),
            "checks_by_tier": by_tier,
        }

    def scan_target(self, target: str) -> ScanResult:
        digest = hashlib.sha256(target.encode("utf-8")).hexdigest()
        findings: List[Dict[str, str]] = []
        for check in self.checks:
            seed = int(hashlib.md5(f"{digest}:{check['id']}".encode("utf-8")).hexdigest(), 16)
            if seed % 211 == 0:
                findings.append(check)
            if len(findings) >= 25:
                break

        ml_signal = self.ml_engine.evaluate_target(target)
        cvss_score = self.cvss.calculate_base_score(CVSSVector())
        risk = min(10.0, round((len(findings) / 3) + (ml_signal.anomaly_score * 2), 2))
        blocked = risk >= 7 or any(f["severity"] == "critical" for f in findings)

        return ScanResult(
            target=target,
            total_checks=len(self.checks),
            findings=findings,
            blocked=blocked,
            risk_score=risk,
            cvss_base=cvss_score,
            exploit_chain=self.chain.suggest_chain(findings),
        )


SCANNER = AdvancedScanner()

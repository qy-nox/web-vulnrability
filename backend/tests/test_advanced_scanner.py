from src.core.advanced_scanner import SCANNER


def test_scanner_has_1000_plus_checks() -> None:
    summary = SCANNER.checks_summary()
    assert summary["total_checks"] >= 2500
    assert summary["tier_count"] >= 20


def test_scan_result_contains_enterprise_fields() -> None:
    result = SCANNER.scan_target("https://example.com")
    assert result.total_checks >= 2500
    assert 0 <= result.risk_score <= 10
    assert isinstance(result.exploit_chain, list)

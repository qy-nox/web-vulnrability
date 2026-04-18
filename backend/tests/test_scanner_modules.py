from importlib import import_module


MODULE_NAMES = [
    "cloudflare_waf_bypass",
    "advanced_injection",
    "authentication_bypass",
    "business_logic",
    "api_security",
    "cloud_security",
    "xxe_deserialization",
    "container_k8s",
    "file_upload",
    "ssrf",
    "information_disclosure",
    "cryptography",
    "dependencies",
    "websocket",
    "javascript_dom",
    "session_management",
    "path_traversal",
    "server_side_rendering",
    "network_analysis",
    "ssl_tls",
]


def test_required_scanner_modules_build_checks() -> None:
    for module_name in MODULE_NAMES:
        module = import_module(f"src.scanners.{module_name}")
        checks = module.build_checks()
        assert checks, f"{module_name} returned no checks"
        first = checks[0]
        assert "payload" in first
        assert "detection_logic" in first
        assert "exploitation_technique" in first
        assert "remediation" in first
        assert "test_case" in first

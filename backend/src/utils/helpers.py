from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    value = url.strip()
    if value.startswith(("http://", "https://")):
        return value
    return f"https://{value}"


def host_from_url(url: str) -> str:
    parsed = urlparse(normalize_url(url))
    return parsed.netloc

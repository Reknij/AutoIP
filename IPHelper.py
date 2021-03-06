from requests import get, exceptions


def GetIPV4():
    try:
        result = get("https://ipv4.jsonip.com/", timeout=5).json()
    except Exception as e:
        return "error"
    return result.get("ip")
import re

def parse_log(log_text):

    issues = {
        "Authentication Failure": 0,
        "DHCP Timeout": 0,
        "Disconnection": 0,
        "Association Failure": 0
    }

    patterns = {
        "Authentication Failure": r"authentication failed|auth fail",
        "DHCP Timeout": r"dhcp timeout",
        "Disconnection": r"disconnect|deauth",
        "Association Failure": r"association failed"
    }

    for issue, pattern in patterns.items():
        matches = re.findall(pattern, log_text, re.IGNORECASE)
        issues[issue] = len(matches)

    return issues
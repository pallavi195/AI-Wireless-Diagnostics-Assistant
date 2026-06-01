def analyze_issues(issues):

    analysis = []

    if issues["Authentication Failure"] > 0:
        analysis.append(
            "Authentication failures detected. Possible causes include incorrect credentials, WPA/WPA2 mismatch, or access point configuration issues."
        )

    if issues["DHCP Timeout"] > 0:
        analysis.append(
            "DHCP timeouts detected. The client may be unable to obtain an IP address from the DHCP server."
        )

    if issues["Disconnection"] > 0:
        analysis.append(
            "Frequent disconnections observed. Check signal strength, interference, and access point stability."
        )

    if issues["Association Failure"] > 0:
        analysis.append(
            "Association failures detected. The client may be unable to establish a connection with the access point."
        )

    total = sum(issues.values())

    if total <= 2:
        severity = "Low"
    elif total <= 4:
        severity = "Medium"
    else:
        severity = "High"

    return f"""
Network Health Analysis

Severity: {severity}

Findings:
{chr(10).join(['- ' + item for item in analysis])}

Recommendations:
- Verify wireless configuration
- Check DHCP server availability
- Inspect signal strength
- Review access point logs
"""
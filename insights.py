def generate_network_insights(stats):

    insights = []

    if stats["UDP"] > stats["TCP"]:
        insights.append(
            "Network traffic is primarily UDP-based."
        )

    if stats["DNS"] > 20:
        insights.append(
            "High DNS activity detected."
        )

    if stats["DHCP"] == 0:
        insights.append(
            "No DHCP exchanges observed during capture."
        )

    total = (
        stats["TCP"]
        + stats["UDP"]
        + stats["DNS"]
        + stats["DHCP"]
    )

    insights.append(
        f"Total packets analyzed: {total}"
    )

    return "\n".join(insights)
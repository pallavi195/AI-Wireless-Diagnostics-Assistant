import streamlit as st
from parser import parse_log
from analyzer import analyze_issues
from report import create_report
from pcap_parser import analyze_pcap
from insights import generate_network_insights

# Global variables
stats = None
insights = None

st.title("AI Wireless Diagnostics Assistant")

# Uploaders
uploaded_file = st.file_uploader(
    "Upload Wi-Fi Log",
    type=["txt"]
)

uploaded_pcap = st.file_uploader(
    "Upload PCAP File",
    type=["pcap", "pcapng"]
)

# ======================================
# PCAP ANALYSIS
# ======================================

if uploaded_pcap:

    st.header("Packet Capture Analysis")

    with open("temp.pcapng", "wb") as f:
        f.write(uploaded_pcap.getbuffer())

    try:

        stats = analyze_pcap("temp.pcapng")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "TCP Packets",
                stats["TCP"]
            )

            st.metric(
                "UDP Packets",
                stats["UDP"]
            )

        with col2:
            st.metric(
                "DNS Packets",
                stats["DNS"]
            )

            st.metric(
                "DHCP Packets",
                stats["DHCP"]
            )

        total_packets = (
            stats["TCP"]
            + stats["UDP"]
            + stats["DNS"]
            + stats["DHCP"]
        )

        st.subheader(
            f"Total Packets Analyzed: {total_packets}"
        )

        insights = generate_network_insights(stats)

        st.subheader("AI Network Insights")

        st.write(insights)

    except Exception as e:

        st.error(
            f"PCAP Analysis Failed: {e}"
        )

# ======================================
# WIFI LOG ANALYSIS
# ======================================

if uploaded_file:

    log_text = uploaded_file.read().decode()

    issues = parse_log(log_text)

    st.header("Wi-Fi Log Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Authentication Failures",
            issues["Authentication Failure"]
        )

        st.metric(
            "DHCP Timeouts",
            issues["DHCP Timeout"]
        )

    with col2:

        st.metric(
            "Disconnections",
            issues["Disconnection"]
        )

        st.metric(
            "Association Failures",
            issues["Association Failure"]
        )

    total_issues = sum(
        issues.values()
    )

    if total_issues <= 2:

        severity = "Low"

    elif total_issues <= 4:

        severity = "Medium"

    else:

        severity = "High"

    st.subheader(
        f"Network Severity: {severity}"
    )

    if st.button("Run AI Analysis"):

        result = analyze_issues(
            issues
        )

        st.subheader(
            "AI Diagnosis"
        )

        st.write(
            result
        )

        pdf_file = create_report(
            issues,
            result,
            stats,
            insights,
            severity
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📄 Download Full Network Report",
                data=file,
                file_name="Wireless_Report.pdf",
                mime="application/pdf"
            )
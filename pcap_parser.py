import pyshark
import asyncio

def analyze_pcap(file_path):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    capture = pyshark.FileCapture(
        file_path,
        eventloop=loop
    )

    stats = {
        "TCP": 0,
        "UDP": 0,
        "DNS": 0,
        "DHCP": 0
    }

    for packet in capture:

        try:

            if "TCP" in packet:
                stats["TCP"] += 1

            if "UDP" in packet:
                stats["UDP"] += 1

            if "DNS" in packet:
                stats["DNS"] += 1

            if "DHCP" in packet:
                stats["DHCP"] += 1

        except:
            pass

    capture.close()

    return stats
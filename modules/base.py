import os

from abc import ABC
from typing import Any

class BaseModule(ABC):

    def analyze_packets(self, pcap_file: str) -> dict[str, Any]:

        return self._handle_local_analysis(pcap_file)

    def _handle_local_analysis(self, pcap_file: str) -> dict[str, Any]:

        # Validate file exists
        if not os.path.exists(pcap_file):
            return {
                "error": f"PCAP file not found: {pcap_file}",
                "pcap_file": pcap_file,
            }

        # Validate file extension
        if not pcap_file.lower().endswith((".pcap", ".pcapng", ".cap")):
            return {
                "error": f"File '{pcap_file}' is not a supported PCAP file (.pcap/.pcapng/.cap)",
                "pcap_file": pcap_file,
            }

        try:
            return self._analyze_protocol_file(pcap_file)
        except Exception as e:
            return {
                "error": f"Failed to analyze PCAP file '{pcap_file}': {str(e)}",
                "pcap_file": pcap_file,
            }


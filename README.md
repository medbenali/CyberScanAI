# CyberScanAI 


<p align="center">
<img src = "https://github.com/medbenali/CyberScanAI/blob/main/images/logo/CyberScanAI.png" alt="CyberScanAI logo" width="300"/>
</p>

[![Python 3](https://img.shields.io/badge/python-3-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-GPL%20v3-red.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![PyPI - Version](https://img.shields.io/pypi/v/cyberscanai.svg)](https://pypi.org/project/cyberscanai)


CyberScanAI is an open source AI Agent Tool for Penetration Testing and Network Forensics.

CyberScanAI is a MCP (Model Context Protocol) Server connects LLMs to tools and prompts for intelligent AI analyzing Networks.


Screenshots
----

![Screenshot](https://github.com/medbenali/CyberScanAI/blob/main/images/demo/demo.png)


### Key Features 

- **MCP Server**:  Stateless MCP Server Expose tools, resources, and prompts to LLMs
- **MCP Tools**: Expose Tools to LLMs
- **Prompts Analysis**: Networking, Security and Forensics
- **Protocols Analysis**: DNS, DHCP, ICMP, TCP, SIP
- **PCAP files Analysis**: Analyse PCAP files
- **Interactive User Interface (UI)**: Realtime UI rendered in conversation


Operating Systems Supported
---- 

- Windows XP/7/8/8.1/10/11
- GNU/Linux
- MacOSX


Installation
----

You can install CyberScanAI with [Pip](https://pypi.org/project/cyberscanai)


```bash
$ pip install cyberscanai
```

CyberScanAI works out of the box with [Python](http://www.python.org/download/) version **3.1.x**.

# The CyberScanAI Module Usage

[CyberScanAI](https://github.com/medbenali/CyberScanAI) connecting LLMs to tools and prompts and data for intelligent Network Analysis. 

You can test the installation CyberScanAI in your machine:

```bash
$ cyberscanai -h 
```
---


## CyberScanAI MCP Server

Start CyberScanAI as a stateless MCP Server :

CyberScanAI by default the transport is stdio and load all modules.

```bash
$ cyberscanai 
```
CyberScanAI CLI usage : 

```bash
$ cyberscanai [--modules MODULES] [--transport {stdio,http}] [--host HOST] [--port PORT]
```

### Modules

### All Modules (by default)

```bash
$ cyberscanai --modules dns,dhcp,icmp,tcp,sip
```

### DNS Analysis Module

```bash
$ cyberscanai --modules dns
```

### DHCP Analysis Module

```bash
$ cyberscanai --modules dhcp
```

### ICMP Analysis Module

```bash
$ cyberscanai --modules icmp
```

### TCP Analysis Module

```bash
$ cyberscanai --modules tcp
```

### SIP (VOIP) Analysis Module

```bash
$ cyberscanai --modules sip
```

### Transport

### stdio (by default)

```bash
$ cyberscanai 
```

### HTTP Transport 

```bash
$ cyberscanai --transport http
```

### HTTP Transport with custom host and port

```bash
$ cyberscanai --transport http --host 192.168.1.1 --port 9090
```

## Tools

CyberScanAI supports different Network Analysis Tools.

![Tools](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/tools.png)

### DNS Analysis Tools

Complete DNS traffic analysis : 

- Extract DNS queries and responses
- Track query frequency
- Detect DNS anomalies and security issues

### DHCP Analysis Tools

Complete DHCP traffic analysis : 

- Extract DHCP translations
- Identify DHCP clients and servers
- Detect DHCP anomalies and security issues

### ICMP Analysis Tools

Complete ICMP traffic analysis : 

- Analyse ping request and replies
- Identify network connectivity issues
- Detect ICMP attacks issues


### TCP Analysis Tools

Complete TCP traffic analysis : 

- ANALYSE Client-Server vs Server-Client traffic
- Detect connection issues and behaviors
- Detect TCP anomalies and security issues

### SIP (VOIP) Analysis Tools

Complete SIP traffic analysis : 

- Extract SIP requests
- Support VOIP troubleshooting
- Detect VOIP security and forensics reconstruction


## Prompts

CyberScanAI provides specialised prompts to guide LLM analysis.

![Prompts](https://github.com/medbenali/CyberScanAI/blob/main/images/prompts/prompts.png)


### DNS Prompts

- Threat detection
- Behavioral Analysis
- Infrastructure Assessment 

### DHCP Prompts

- Security Threats
- DHCP Attacks
- Client Anomalies

### ICMP Prompts

- ICMP Attacks
- Network Connectivity
- Reconstruction Detection


### TCP Prompts

- Attack Detection
- Anomaly Identification
- Forensics Evidence


### SIP (VOIP) Prompts

- Registration Abuse
- Toll Fraud
- Timeline Reconstruction


## CyberScanAI MCP Client

Now, after run the **CyberScanAI MCP Server**

You can use **CyberScanAI MCP Server** tools and prompts to AI intelligent analyse for packets (dns,dhcp,icmp,tcp and sip) from captured pcap file.

Run the **CyberScanAI Client** with MCP Inspector


```bash
npm install -g @modelcontextprotocol/inspector
npx @modelcontextprotocol/inspector cyberscanai
```

### DNS Analysis Tools

![ToolsDNSAnalysis](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/dns.png)

```json
{
  "file": "PCAP_Files/dns.cap",
  "analysis_timestamp": "2026-04-17T12:11:56.592133",
  "total_packets_in_file": 249,
  "dns_packets_found": 14,
  "dns_packets_analyzed": 14,
  "statistics": {
    "queries": 7,
    "responses": 7,
    "unique_domains_queried": 7,
    "unique_domains": [
      "www.winpcap.org",
      "www.google-analytics.com",
      "www.expoactive.com",
      "www.google.com",
      "pagead2.googlesyndication.com",
      "chrissanders.org",
      "wireshark.org"
    ]
  },
  "packets": [
    {
      "packet_number": 1,
      "timestamp": "2006-12-16T19:22:34.013605",
      "source_ip": "192.168.0.114",
      "destination_ip": "205.152.37.23",
      "protocol": "UDP",
      "dns_id": 25608,
      "flags": {
        "is_response": false,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": false
      },
      "questions": [
        {
          "name": "chrissanders.org",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [],
      "summary": "Ether / IP / UDP / DNS Qry b'chrissanders.org.'"
    },
    {
      "packet_number": 2,
      "timestamp": "2006-12-16T19:22:34.125726",
      "source_ip": "205.152.37.23",
      "destination_ip": "192.168.0.114",
      "protocol": "UDP",
      "dns_id": 25608,
      "flags": {
        "is_response": true,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": true
      },
      "questions": [
        {
          "name": "chrissanders.org",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [
        {
          "name": "chrissanders.org",
          "type": 1,
          "class": 1,
          "ttl": 14400,
          "address": "208.113.140.24"
        }
      ],
      "summary": "Ether / IP / UDP / DNS Ans 208.113.140.24"
    },
    {
      "packet_number": 3,
      "timestamp": "2006-12-16T19:22:35.160668",
      "source_ip": "192.168.0.114",
      "destination_ip": "205.152.37.23",
      "protocol": "UDP",
      "dns_id": 23048,
      "flags": {
        "is_response": false,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": false
      },
      "questions": [
        {
          "name": "www.google-analytics.com",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [],
      "summary": "Ether / IP / UDP / DNS Qry b'www.google-analytics.com.'"
    },
    {
      "packet_number": 4,
      "timestamp": "2006-12-16T19:22:35.188490",
      "source_ip": "205.152.37.23",
      "destination_ip": "192.168.0.114",
      "protocol": "UDP",
      "dns_id": 23048,
      "flags": {
        "is_response": true,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": true
      },
      "questions": [
        {
          "name": "www.google-analytics.com",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [
        {
          "name": "www.google-analytics.com",
          "type": 5,
          "class": 1,
          "ttl": 1626,
          "cname": "b'www-google-analytics.l.google.com.'"
        },
        {
          "name": "www-google-analytics.l.google.com",
          "type": 1,
          "class": 1,
          "ttl": 200,
          "address": "216.239.51.99"
        },
        {
          "name": "www-google-analytics.l.google.com",
          "type": 1,
          "class": 1,
          "ttl": 200,
          "address": "216.239.51.104"
        }
      ],
      "summary": "Ether / IP / UDP / DNS Ans b'www-google-analytics.l.google.com.'"
    },
    {
      "packet_number": 5,
      "timestamp": "2006-12-16T19:22:35.216450",
      "source_ip": "192.168.0.114",
      "destination_ip": "205.152.37.23",
      "protocol": "UDP",
      "dns_id": 51209,
      "flags": {
        "is_response": false,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": false
      },
      "questions": [
        {
          "name": "pagead2.googlesyndication.com",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [],
      "summary": "Ether / IP / UDP / DNS Qry b'pagead2.googlesyndication.com.'"
    },
    {
      "packet_number": 6,
      "timestamp": "2006-12-16T19:22:35.216911",
      "source_ip": "192.168.0.114",
      "destination_ip": "205.152.37.23",
      "protocol": "UDP",
      "dns_id": 21262,
      "flags": {
        "is_response": false,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": false
      },
      "questions": [
        {
          "name": "www.expoactive.com",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [],
      "summary": "Ether / IP / UDP / DNS Qry b'www.expoactive.com.'"
    },
    {
      "packet_number": 7,
      "timestamp": "2006-12-16T19:22:35.242690",
      "source_ip": "205.152.37.23",
      "destination_ip": "192.168.0.114",
      "protocol": "UDP",
      "dns_id": 51209,
      "flags": {
        "is_response": true,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": true
      },
      "questions": [
        {
          "name": "pagead2.googlesyndication.com",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [
        {
          "name": "pagead2.googlesyndication.com",
          "type": 5,
          "class": 1,
          "ttl": 46880,
          "cname": "b'pagead2.google.com.'"
        },
        {
          "name": "pagead2.google.com",
          "type": 5,
          "class": 1,
          "ttl": 392313,
          "cname": "b'pagead.l.google.com.'"
        },
        {
          "name": "pagead.l.google.com",
          "type": 1,
          "class": 1,
          "ttl": 37,
          "address": "72.14.211.104"
        },
        {
          "name": "pagead.l.google.com",
          "type": 1,
          "class": 1,
          "ttl": 37,
          "address": "72.14.211.99"
        }
      ],
      "summary": "Ether / IP / UDP / DNS Ans b'pagead2.google.com.'"
    },
    {
      "packet_number": 8,
      "timestamp": "2006-12-16T19:22:35.811703",
      "source_ip": "205.152.37.23",
      "destination_ip": "192.168.0.114",
      "protocol": "UDP",
      "dns_id": 21262,
      "flags": {
        "is_response": true,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": true
      },
      "questions": [
        {
          "name": "www.expoactive.com",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [
        {
          "name": "www.expoactive.com",
          "type": 5,
          "class": 1,
          "ttl": 300,
          "cname": "b'expoactive.com.'"
        },
        {
          "name": "expoactive.com",
          "type": 1,
          "class": 1,
          "ttl": 300,
          "address": "72.3.133.240"
        }
      ],
      "summary": "Ether / IP / UDP / DNS Ans b'expoactive.com.'"
    },
    {
      "packet_number": 9,
      "timestamp": "2006-12-16T19:22:47.202144",
      "source_ip": "192.168.0.114",
      "destination_ip": "205.152.37.23",
      "protocol": "UDP",
      "dns_id": 6159,
      "flags": {
        "is_response": false,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": false
      },
      "questions": [
        {
          "name": "wireshark.org",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [],
      "summary": "Ether / IP / UDP / DNS Qry b'wireshark.org.'"
    },
    {
      "packet_number": 10,
      "timestamp": "2006-12-16T19:22:47.293308",
      "source_ip": "205.152.37.23",
      "destination_ip": "192.168.0.114",
      "protocol": "UDP",
      "dns_id": 6159,
      "flags": {
        "is_response": true,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": true
      },
      "questions": [
        {
          "name": "wireshark.org",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [
        {
          "name": "wireshark.org",
          "type": 1,
          "class": 1,
          "ttl": 14400,
          "address": "128.121.50.122"
        }
      ],
      "summary": "Ether / IP / UDP / DNS Ans 128.121.50.122"
    },
    {
      "packet_number": 11,
      "timestamp": "2006-12-16T19:22:48.084630",
      "source_ip": "192.168.0.114",
      "destination_ip": "205.152.37.23",
      "protocol": "UDP",
      "dns_id": 37644,
      "flags": {
        "is_response": false,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": false
      },
      "questions": [
        {
          "name": "www.winpcap.org",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [],
      "summary": "Ether / IP / UDP / DNS Qry b'www.winpcap.org.'"
    },
    {
      "packet_number": 12,
      "timestamp": "2006-12-16T19:22:48.085521",
      "source_ip": "192.168.0.114",
      "destination_ip": "205.152.37.23",
      "protocol": "UDP",
      "dns_id": 56845,
      "flags": {
        "is_response": false,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": false
      },
      "questions": [
        {
          "name": "www.google.com",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [],
      "summary": "Ether / IP / UDP / DNS Qry b'www.google.com.'"
    },
    {
      "packet_number": 13,
      "timestamp": "2006-12-16T19:22:48.137861",
      "source_ip": "205.152.37.23",
      "destination_ip": "192.168.0.114",
      "protocol": "UDP",
      "dns_id": 37644,
      "flags": {
        "is_response": true,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": true
      },
      "questions": [
        {
          "name": "www.winpcap.org",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [
        {
          "name": "www.winpcap.org",
          "type": 1,
          "class": 1,
          "ttl": 4736,
          "address": "128.121.79.138"
        }
      ],
      "summary": "Ether / IP / UDP / DNS Ans 128.121.79.138"
    },
    {
      "packet_number": 14,
      "timestamp": "2006-12-16T19:22:48.139437",
      "source_ip": "205.152.37.23",
      "destination_ip": "192.168.0.114",
      "protocol": "UDP",
      "dns_id": 56845,
      "flags": {
        "is_response": true,
        "authoritative": false,
        "truncated": false,
        "recursion_desired": true,
        "recursion_available": true
      },
      "questions": [
        {
          "name": "www.google.com",
          "type": 1,
          "class": 1
        }
      ],
      "answers": [
        {
          "name": "www.google.com",
          "type": 5,
          "class": 1,
          "ttl": 393857,
          "cname": "b'www.l.google.com.'"
        },
        {
          "name": "www.l.google.com",
          "type": 1,
          "class": 1,
          "ttl": 120,
          "address": "72.14.209.104"
        },
        {
          "name": "www.l.google.com",
          "type": 1,
          "class": 1,
          "ttl": 120,
          "address": "72.14.209.99"
        }
      ],
      "summary": "Ether / IP / UDP / DNS Ans b'www.l.google.com.'"
    }
  ]
}
```

### DHCP Analysis Tools

![ToolsDHCPAnalysis](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/dhcp.png)

```json
{
  "file": "PCAP_Files/dhcp.pcap",
  "total_packets": 4,
  "dhcp_packets_found": 4,
  "dhcp_packets_analyzed": 4,
  "statistics": {
    "unique_clients_count": 1,
    "unique_servers_count": 1,
    "unique_clients": [
      "00:0b:82:01:fc:42"
    ],
    "unique_servers": [
      "192.168.0.1"
    ],
    "message_type_counts": {
      "DISCOVER": 1,
      "OFFER": 1,
      "REQUEST": 1,
      "ACK": 1
    },
    "transaction_count": 2,
    "transactions": {
      "0x00003d1d": [
        {
          "packet_number": 1,
          "message_type": "DISCOVER",
          "timestamp": "1102274184.317453"
        },
        {
          "packet_number": 2,
          "message_type": "OFFER",
          "timestamp": "1102274184.317748"
        }
      ],
      "0x00003d1e": [
        {
          "packet_number": 3,
          "message_type": "REQUEST",
          "timestamp": "1102274184.387484"
        },
        {
          "packet_number": 4,
          "message_type": "ACK",
          "timestamp": "1102274184.387798"
        }
      ]
    }
  },
  "packets": [
    {
      "packet_number": 1,
      "timestamp": "1102274184.317453",
      "src_ip": "0.0.0.0",
      "dst_ip": "255.255.255.255",
      "src_port": 68,
      "dst_port": 67,
      "op": "Request",
      "transaction_id": "0x00003d1d",
      "client_ip": "0.0.0.0",
      "your_ip": "0.0.0.0",
      "server_ip": "0.0.0.0",
      "relay_ip": "0.0.0.0",
      "client_mac": "00:0b:82:01:fc:42",
      "options": {
        "parameter_request_list": [
          1,
          3,
          6,
          42
        ]
      },
      "message_type": "DISCOVER",
      "message_type_code": 1,
      "client_id": "01:00:0b:82:01:fc:42",
      "requested_ip": "0.0.0.0"
    },
    {
      "packet_number": 2,
      "timestamp": "1102274184.317748",
      "src_ip": "192.168.0.1",
      "dst_ip": "192.168.0.10",
      "src_port": 67,
      "dst_port": 68,
      "op": "Reply",
      "transaction_id": "0x00003d1d",
      "client_ip": "0.0.0.0",
      "your_ip": "192.168.0.10",
      "server_ip": "192.168.0.1",
      "relay_ip": "0.0.0.0",
      "client_mac": "00:0b:82:01:fc:42",
      "options": {
        "subnet_mask": "255.255.255.0",
        "renewal_time": "1800 seconds",
        "rebinding_time": "3150 seconds",
        "lease_time": "3600 seconds"
      },
      "message_type": "OFFER",
      "message_type_code": 2,
      "renewal_time": 1800,
      "rebinding_time": 3150,
      "lease_time": 3600,
      "server_id": "192.168.0.1"
    },
    {
      "packet_number": 3,
      "timestamp": "1102274184.387484",
      "src_ip": "0.0.0.0",
      "dst_ip": "255.255.255.255",
      "src_port": 68,
      "dst_port": 67,
      "op": "Request",
      "transaction_id": "0x00003d1e",
      "client_ip": "0.0.0.0",
      "your_ip": "0.0.0.0",
      "server_ip": "0.0.0.0",
      "relay_ip": "0.0.0.0",
      "client_mac": "00:0b:82:01:fc:42",
      "options": {
        "parameter_request_list": [
          1,
          3,
          6,
          42
        ]
      },
      "message_type": "REQUEST",
      "message_type_code": 3,
      "client_id": "01:00:0b:82:01:fc:42",
      "requested_ip": "192.168.0.10",
      "server_id": "192.168.0.1"
    },
    {
      "packet_number": 4,
      "timestamp": "1102274184.387798",
      "src_ip": "192.168.0.1",
      "dst_ip": "192.168.0.10",
      "src_port": 67,
      "dst_port": 68,
      "op": "Reply",
      "transaction_id": "0x00003d1e",
      "client_ip": "0.0.0.0",
      "your_ip": "192.168.0.10",
      "server_ip": "0.0.0.0",
      "relay_ip": "0.0.0.0",
      "client_mac": "00:0b:82:01:fc:42",
      "options": {
        "renewal_time": "1800 seconds",
        "rebinding_time": "3150 seconds",
        "lease_time": "3600 seconds",
        "subnet_mask": "255.255.255.0"
      },
      "message_type": "ACK",
      "message_type_code": 5,
      "renewal_time": 1800,
      "rebinding_time": 3150,
      "lease_time": 3600,
      "server_id": "192.168.0.1"
    }
  ]
}
```

### ICMP Analysis Module

![ToolsICMPAnalysis](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/icmp.png)

```json
{
  "file": "PCAP_Files/icmp.pcap",
  "analysis_timestamp": "2026-04-17T12:27:53.686138",
  "total_packets": 16,
  "icmp_packets_found": 16,
  "icmp_packets_analyzed": 16,
  "statistics": {
    "icmp_type_counts": {
      "Echo Request": 8,
      "Echo Reply": 8
    },
    "unique_sources_count": 3,
    "unique_destinations_count": 3,
    "unique_sources": [
      "192.168.0.1",
      "192.168.0.114",
      "72.14.207.99"
    ],
    "unique_destinations": [
      "192.168.0.1",
      "192.168.0.114",
      "72.14.207.99"
    ],
    "echo_sessions": 1,
    "echo_pairs": {
      "768": {
        "requests": 8,
        "replies": 8
      }
    },
    "unreachable_destinations_count": 0,
    "unreachable_destinations": []
  },
  "packets": [
    {
      "packet_number": 1,
      "timestamp": "2006-12-29T04:10:10.660442",
      "src_ip": "192.168.0.114",
      "dst_ip": "192.168.0.1",
      "ip_version": 4,
      "ttl": 128,
      "packet_size": 74,
      "icmp_type": 8,
      "icmp_code": 0,
      "icmp_type_name": "Echo Request",
      "icmp_id": 768,
      "icmp_seq": 256,
      "checksum": 18780,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 2,
      "timestamp": "2006-12-29T04:10:10.661527",
      "src_ip": "192.168.0.1",
      "dst_ip": "192.168.0.114",
      "ip_version": 4,
      "ttl": 127,
      "packet_size": 74,
      "icmp_type": 0,
      "icmp_code": 0,
      "icmp_type_name": "Echo Reply",
      "icmp_id": 768,
      "icmp_seq": 256,
      "checksum": 20828,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 3,
      "timestamp": "2006-12-29T04:10:11.657215",
      "src_ip": "192.168.0.114",
      "dst_ip": "192.168.0.1",
      "ip_version": 4,
      "ttl": 128,
      "packet_size": 74,
      "icmp_type": 8,
      "icmp_code": 0,
      "icmp_type_name": "Echo Request",
      "icmp_id": 768,
      "icmp_seq": 512,
      "checksum": 18524,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 4,
      "timestamp": "2006-12-29T04:10:11.659425",
      "src_ip": "192.168.0.1",
      "dst_ip": "192.168.0.114",
      "ip_version": 4,
      "ttl": 127,
      "packet_size": 74,
      "icmp_type": 0,
      "icmp_code": 0,
      "icmp_type_name": "Echo Reply",
      "icmp_id": 768,
      "icmp_seq": 512,
      "checksum": 20572,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 5,
      "timestamp": "2006-12-29T04:10:12.657243",
      "src_ip": "192.168.0.114",
      "dst_ip": "192.168.0.1",
      "ip_version": 4,
      "ttl": 128,
      "packet_size": 74,
      "icmp_type": 8,
      "icmp_code": 0,
      "icmp_type_name": "Echo Request",
      "icmp_id": 768,
      "icmp_seq": 768,
      "checksum": 18268,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 6,
      "timestamp": "2006-12-29T04:10:12.659529",
      "src_ip": "192.168.0.1",
      "dst_ip": "192.168.0.114",
      "ip_version": 4,
      "ttl": 127,
      "packet_size": 74,
      "icmp_type": 0,
      "icmp_code": 0,
      "icmp_type_name": "Echo Reply",
      "icmp_id": 768,
      "icmp_seq": 768,
      "checksum": 20316,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 7,
      "timestamp": "2006-12-29T04:10:13.657282",
      "src_ip": "192.168.0.114",
      "dst_ip": "192.168.0.1",
      "ip_version": 4,
      "ttl": 128,
      "packet_size": 74,
      "icmp_type": 8,
      "icmp_code": 0,
      "icmp_type_name": "Echo Request",
      "icmp_id": 768,
      "icmp_seq": 1024,
      "checksum": 18012,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 8,
      "timestamp": "2006-12-29T04:10:13.659619",
      "src_ip": "192.168.0.1",
      "dst_ip": "192.168.0.114",
      "ip_version": 4,
      "ttl": 127,
      "packet_size": 74,
      "icmp_type": 0,
      "icmp_code": 0,
      "icmp_type_name": "Echo Reply",
      "icmp_id": 768,
      "icmp_seq": 1024,
      "checksum": 20060,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 9,
      "timestamp": "2006-12-29T04:10:16.794628",
      "src_ip": "192.168.0.114",
      "dst_ip": "72.14.207.99",
      "ip_version": 4,
      "ttl": 128,
      "packet_size": 74,
      "icmp_type": 8,
      "icmp_code": 0,
      "icmp_type_name": "Echo Request",
      "icmp_id": 768,
      "icmp_seq": 1280,
      "checksum": 17756,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 10,
      "timestamp": "2006-12-29T04:10:16.875473",
      "src_ip": "72.14.207.99",
      "dst_ip": "192.168.0.114",
      "ip_version": 4,
      "ttl": 232,
      "packet_size": 74,
      "icmp_type": 0,
      "icmp_code": 0,
      "icmp_type_name": "Echo Reply",
      "icmp_id": 768,
      "icmp_seq": 1280,
      "checksum": 19804,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 11,
      "timestamp": "2006-12-29T04:10:17.796100",
      "src_ip": "192.168.0.114",
      "dst_ip": "72.14.207.99",
      "ip_version": 4,
      "ttl": 128,
      "packet_size": 74,
      "icmp_type": 8,
      "icmp_code": 0,
      "icmp_type_name": "Echo Request",
      "icmp_id": 768,
      "icmp_seq": 1536,
      "checksum": 17500,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 12,
      "timestamp": "2006-12-29T04:10:17.858014",
      "src_ip": "72.14.207.99",
      "dst_ip": "192.168.0.114",
      "ip_version": 4,
      "ttl": 232,
      "packet_size": 74,
      "icmp_type": 0,
      "icmp_code": 0,
      "icmp_type_name": "Echo Reply",
      "icmp_id": 768,
      "icmp_seq": 1536,
      "checksum": 19548,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 13,
      "timestamp": "2006-12-29T04:10:18.797110",
      "src_ip": "192.168.0.114",
      "dst_ip": "72.14.207.99",
      "ip_version": 4,
      "ttl": 128,
      "packet_size": 74,
      "icmp_type": 8,
      "icmp_code": 0,
      "icmp_type_name": "Echo Request",
      "icmp_id": 768,
      "icmp_seq": 1792,
      "checksum": 17244,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 14,
      "timestamp": "2006-12-29T04:10:18.859585",
      "src_ip": "72.14.207.99",
      "dst_ip": "192.168.0.114",
      "ip_version": 4,
      "ttl": 232,
      "packet_size": 74,
      "icmp_type": 0,
      "icmp_code": 0,
      "icmp_type_name": "Echo Reply",
      "icmp_id": 768,
      "icmp_seq": 1792,
      "checksum": 19292,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 15,
      "timestamp": "2006-12-29T04:10:19.798127",
      "src_ip": "192.168.0.114",
      "dst_ip": "72.14.207.99",
      "ip_version": 4,
      "ttl": 128,
      "packet_size": 74,
      "icmp_type": 8,
      "icmp_code": 0,
      "icmp_type_name": "Echo Request",
      "icmp_id": 768,
      "icmp_seq": 2048,
      "checksum": 16988,
      "icmp_code_name": "Code 0"
    },
    {
      "packet_number": 16,
      "timestamp": "2006-12-29T04:10:19.859920",
      "src_ip": "72.14.207.99",
      "dst_ip": "192.168.0.114",
      "ip_version": 4,
      "ttl": 232,
      "packet_size": 74,
      "icmp_type": 0,
      "icmp_code": 0,
      "icmp_type_name": "Echo Reply",
      "icmp_id": 768,
      "icmp_seq": 2048,
      "checksum": 19036,
      "icmp_code_name": "Code 0"
    }
  ]
}
```


### TCP Analysis Tools

#### TCP Analysis Connection  

![ToolsTCPAnalysisConnection](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/tcp_connection.png)

```json
{
  "file": "PCAP_Files/tcp-con-lost.pcap",
  "analysis_timestamp": "2026-04-17T12:36:54.802604",
  "total_packets": 9,
  "tcp_packets_found": 9,
  "filter": {
    "server_ip": null,
    "server_port": null
  },
  "summary": {
    "total_connections": 1,
    "successful_handshakes": 0,
    "failed_handshakes": 1,
    "established_connections": 0,
    "reset_connections": 0,
    "normal_close": 0,
    "active_connections": 1
  },
  "connections": [
    {
      "client": "10.3.71.7:1043",
      "server": "10.3.30.1:1048",
      "state": "active",
      "handshake_completed": false,
      "syn_count": 0,
      "syn_ack_count": 0,
      "ack_count": 9,
      "rst_count": 0,
      "fin_count": 0,
      "data_packets": 9,
      "retransmissions": 7,
      "close_reason": "active",
      "packet_count": 9
    }
  ],
  "issues": [
    "7 retransmissions detected",
    "1 failed handshakes"
  ]
}
```



#### TCP Analysis Anomalies

![ToolsTCPAnalysisAnomalies](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/tcp-anomalies.png)

```json
{
  "file": "PCAP_Files/tcp-anomalies.pcap",
  "analysis_timestamp": "2026-04-17T12:55:20.772116",
  "filter": {
    "server_ip": "192.168.1.1",
    "server_port": 80
  },
  "statistics": {
    "total_connections": 0,
    "total_packets": 0,
    "handshake": {
      "successful": 0,
      "failed": 0,
      "incomplete": 0
    },
    "flags": {
      "syn": 0,
      "syn_ack": 0,
      "rst": 0,
      "fin": 0,
      "ack": 0
    },
    "rst_distribution": {
      "by_source": {},
      "by_direction": {
        "to_server": 0,
        "from_server": 0,
        "unknown": 0
      },
      "connections_with_rst": []
    },
    "retransmissions": {
      "total": 0,
      "by_connection": {},
      "rate": 0
    },
    "connection_states": {
      "established": 0,
      "reset": 0,
      "closed": 0,
      "unknown": 0
    }
  },
  "patterns": [],
  "summary": {
    "total_patterns": 0,
    "by_category": {},
    "notable_observations": []
  }
}
```

#### TCP Analysis Retransmission

![ToolsTCPAnalysisRetransmission](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/tcp-retransmission.png)

```json
{
  "file": "PCAP_Files/tcp-retransmission.pcap",
  "analysis_timestamp": "2026-04-17T12:42:29.250132",
  "total_packets": 0,
  "total_retransmissions": 0,
  "retransmission_rate": 0,
  "threshold": 0.02,
  "exceeds_threshold": false,
  "by_connection": [],
  "summary": {
    "worst_connection": "",
    "worst_retrans_rate": 0,
    "connections_above_threshold": 0
  }
}
```


#### TCP Analysis Traffic

![ToolsTCPAnalysisTraffic](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/tcp-traffic.png)

```json
{
  "file": "PCAP_Files/tcp-traffic.pcap",
  "analysis_timestamp": "2026-04-23T09:58:35.223370",
  "server": "10.3.30.1:1048:any",
  "client_to_server": {
    "packet_count": 0,
    "byte_count": 0,
    "syn_count": 0,
    "rst_count": 0,
    "fin_count": 0,
    "data_packets": 0,
    "retransmissions": 0
  },
  "server_to_client": {
    "packet_count": 0,
    "byte_count": 0,
    "syn_count": 0,
    "rst_count": 0,
    "fin_count": 0,
    "data_packets": 0,
    "retransmissions": 0
  },
  "analysis": {
    "asymmetry_ratio": 0,
    "primary_rst_source": "balanced",
    "data_flow_direction": "server_heavy",
    "interpretation": "Balanced RST distribution."
  }
}
```


### SIP (VOIP) Analysis Tools

![ToolsSIPAnalysis](https://github.com/medbenali/CyberScanAI/blob/main/images/tools/sip.png)

```json
{
  "file": "PCAP_Files/sip.pcap",
  "analysis_timestamp": "2026-04-17T13:01:15.089593",
  "total_packets_in_file": 84,
  "sip_packets_found": 7,
  "sip_packets_analyzed": 7,
  "statistics": {
    "requests": 3,
    "responses": 4,
    "methods": {
      "ACK": 1,
      "BYE": 1,
      "INVITE": 1
    },
    "response_classes": {
      "1xx": 2,
      "2xx": 2
    },
    "unique_call_ids": 1,
    "call_ids": [
      "158936656982201062716@10.33.6.100"
    ],
    "transports": {
      "TCP": 7
    },
    "user_agents": [
      "GW/v.6.20A.027.012",
      "IPP/v.6.20A.027.012"
    ]
  },
  "packets": [
    {
      "packet_number": 1,
      "timestamp": "2011-07-28T13:54:46.562096",
      "source_ip": "10.33.6.100",
      "destination_ip": "10.33.6.101",
      "source_port": 64802,
      "destination_port": 5060,
      "transport": "TCP",
      "message_type": "request",
      "start_line": "INVITE sip:201@10.33.6.101;user=phone SIP/2.0",
      "call_id": "158936656982201062716@10.33.6.100",
      "cseq": "1 INVITE",
      "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
      "to": "<sip:201@10.33.6.101;user=phone>",
      "contact": "<sip:101@10.33.6.100:5060;transport=tcp>",
      "user_agent": "IPP/v.6.20A.027.012",
      "server": "",
      "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1589375893;alias",
      "content_type": "application/sdp",
      "content_length": 228,
      "body_length": 217,
      "known_sip_port": true,
      "headers": {
        "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1589375893;alias",
        "max-forwards": "70",
        "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
        "to": "<sip:201@10.33.6.101;user=phone>",
        "call-id": "158936656982201062716@10.33.6.100",
        "cseq": "1 INVITE",
        "contact": "<sip:101@10.33.6.100:5060;transport=tcp>",
        "supported": "em,timer,replaces,path,resource-priority,sdp-anat",
        "allow": "REGISTER,OPTIONS,INVITE,ACK,CANCEL,BYE,NOTIFY,PRACK,REFER,INFO,SUBSCRIBE,UPDATE",
        "user-agent": "IPP/v.6.20A.027.012",
        "content-type": "application/sdp",
        "content-length": "228"
      },
      "summary": "Ether / IP / TCP 10.33.6.100:64802 > 10.33.6.101:sip PA / Raw",
      "method": "INVITE",
      "request_uri": "sip:201@10.33.6.101;user=phone",
      "sip_version": "SIP/2.0"
    },
    {
      "packet_number": 2,
      "timestamp": "2011-07-28T13:54:46.602589",
      "source_ip": "10.33.6.101",
      "destination_ip": "10.33.6.100",
      "source_port": 5060,
      "destination_port": 64802,
      "transport": "TCP",
      "message_type": "response",
      "start_line": "SIP/2.0 100 Trying",
      "call_id": "158936656982201062716@10.33.6.100",
      "cseq": "1 INVITE",
      "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
      "to": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
      "contact": "",
      "user_agent": "",
      "server": "GW/v.6.20A.027.012",
      "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1589375893;alias",
      "content_type": "",
      "content_length": 0,
      "body_length": 0,
      "known_sip_port": true,
      "headers": {
        "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1589375893;alias",
        "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
        "to": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
        "call-id": "158936656982201062716@10.33.6.100",
        "cseq": "1 INVITE",
        "supported": "em,timer,replaces,path,early-session,resource-priority",
        "allow": "REGISTER,OPTIONS,INVITE,ACK,CANCEL,BYE,NOTIFY,PRACK,REFER,INFO,SUBSCRIBE,UPDATE",
        "server": "GW/v.6.20A.027.012",
        "content-length": "0"
      },
      "summary": "Ether / IP / TCP 10.33.6.101:sip > 10.33.6.100:64802 PA / Raw",
      "status_code": 100,
      "reason_phrase": "Trying"
    },
    {
      "packet_number": 3,
      "timestamp": "2011-07-28T13:54:46.621123",
      "source_ip": "10.33.6.101",
      "destination_ip": "10.33.6.100",
      "source_port": 5060,
      "destination_port": 64802,
      "transport": "TCP",
      "message_type": "response",
      "start_line": "SIP/2.0 180 Ringing",
      "call_id": "158936656982201062716@10.33.6.100",
      "cseq": "1 INVITE",
      "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
      "to": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
      "contact": "<sip:201@10.33.6.101:5060;transport=tcp>",
      "user_agent": "",
      "server": "GW/v.6.20A.027.012",
      "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1589375893;alias",
      "content_type": "",
      "content_length": 0,
      "body_length": 0,
      "known_sip_port": true,
      "headers": {
        "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1589375893;alias",
        "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
        "to": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
        "call-id": "158936656982201062716@10.33.6.100",
        "cseq": "1 INVITE",
        "contact": "<sip:201@10.33.6.101:5060;transport=tcp>",
        "supported": "em,timer,replaces,path,early-session,resource-priority",
        "allow": "REGISTER,OPTIONS,INVITE,ACK,CANCEL,BYE,NOTIFY,PRACK,REFER,INFO,SUBSCRIBE,UPDATE",
        "server": "GW/v.6.20A.027.012",
        "content-length": "0"
      },
      "summary": "Ether / IP / TCP 10.33.6.101:sip > 10.33.6.100:64802 PA / Raw",
      "status_code": 180,
      "reason_phrase": "Ringing"
    },
    {
      "packet_number": 4,
      "timestamp": "2011-07-28T13:54:50.905636",
      "source_ip": "10.33.6.101",
      "destination_ip": "10.33.6.100",
      "source_port": 5060,
      "destination_port": 64802,
      "transport": "TCP",
      "message_type": "response",
      "start_line": "SIP/2.0 200 OK",
      "call_id": "158936656982201062716@10.33.6.100",
      "cseq": "1 INVITE",
      "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
      "to": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
      "contact": "<sip:201@10.33.6.101:5060;transport=tcp>",
      "user_agent": "",
      "server": "GW/v.6.20A.027.012",
      "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1589375893;alias",
      "content_type": "application/sdp",
      "content_length": 225,
      "body_length": 214,
      "known_sip_port": true,
      "headers": {
        "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1589375893;alias",
        "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
        "to": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
        "call-id": "158936656982201062716@10.33.6.100",
        "cseq": "1 INVITE",
        "contact": "<sip:201@10.33.6.101:5060;transport=tcp>",
        "supported": "em,timer,replaces,path,early-session,resource-priority",
        "allow": "REGISTER,OPTIONS,INVITE,ACK,CANCEL,BYE,NOTIFY,PRACK,REFER,INFO,SUBSCRIBE,UPDATE",
        "server": "GW/v.6.20A.027.012",
        "content-type": "application/sdp",
        "content-length": "225"
      },
      "summary": "Ether / IP / TCP 10.33.6.101:sip > 10.33.6.100:64802 PA / Raw",
      "status_code": 200,
      "reason_phrase": "OK"
    },
    {
      "packet_number": 5,
      "timestamp": "2011-07-28T13:54:50.933132",
      "source_ip": "10.33.6.100",
      "destination_ip": "10.33.6.101",
      "source_port": 64802,
      "destination_port": 5060,
      "transport": "TCP",
      "message_type": "request",
      "start_line": "ACK sip:201@10.33.6.101:5060;transport=tcp SIP/2.0",
      "call_id": "158936656982201062716@10.33.6.100",
      "cseq": "1 ACK",
      "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
      "to": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
      "contact": "<sip:101@10.33.6.100:5060;transport=tcp>",
      "user_agent": "IPP/v.6.20A.027.012",
      "server": "",
      "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1600323074;alias",
      "content_type": "",
      "content_length": 0,
      "body_length": 0,
      "known_sip_port": true,
      "headers": {
        "via": "SIP/2.0/TCP 10.33.6.100;branch=z9hG4bKac1600323074;alias",
        "max-forwards": "70",
        "from": "<sip:101@10.33.6.100>;tag=1c1589367133",
        "to": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
        "call-id": "158936656982201062716@10.33.6.100",
        "cseq": "1 ACK",
        "contact": "<sip:101@10.33.6.100:5060;transport=tcp>",
        "supported": "em,timer,replaces,path,resource-priority",
        "allow": "REGISTER,OPTIONS,INVITE,ACK,CANCEL,BYE,NOTIFY,PRACK,REFER,INFO,SUBSCRIBE,UPDATE",
        "user-agent": "IPP/v.6.20A.027.012",
        "content-length": "0"
      },
      "summary": "Ether / IP / TCP 10.33.6.100:64802 > 10.33.6.101:sip PA / Raw",
      "method": "ACK",
      "request_uri": "sip:201@10.33.6.101:5060;transport=tcp",
      "sip_version": "SIP/2.0"
    },
    {
      "packet_number": 6,
      "timestamp": "2011-07-28T13:54:53.057152",
      "source_ip": "10.33.6.101",
      "destination_ip": "10.33.6.100",
      "source_port": 5060,
      "destination_port": 64802,
      "transport": "TCP",
      "message_type": "request",
      "start_line": "BYE sip:101@10.33.6.100:5060;transport=tcp SIP/2.0",
      "call_id": "158936656982201062716@10.33.6.100",
      "cseq": "1 BYE",
      "from": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
      "to": "<sip:101@10.33.6.100>;tag=1c1589367133",
      "contact": "",
      "user_agent": "GW/v.6.20A.027.012",
      "server": "",
      "via": "SIP/2.0/TCP 10.33.6.101;branch=z9hG4bKac359152811;alias",
      "content_type": "",
      "content_length": 0,
      "body_length": 0,
      "known_sip_port": true,
      "headers": {
        "via": "SIP/2.0/TCP 10.33.6.101;branch=z9hG4bKac359152811;alias",
        "max-forwards": "70",
        "from": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
        "to": "<sip:101@10.33.6.100>;tag=1c1589367133",
        "call-id": "158936656982201062716@10.33.6.100",
        "cseq": "1 BYE",
        "supported": "em,timer,replaces,path,early-session,resource-priority",
        "allow": "REGISTER,OPTIONS,INVITE,ACK,CANCEL,BYE,NOTIFY,PRACK,REFER,INFO,SUBSCRIBE,UPDATE",
        "user-agent": "GW/v.6.20A.027.012",
        "reason": "Q.850 ;cause=16 ;text=\"local\"",
        "content-length": "0"
      },
      "summary": "Ether / IP / TCP 10.33.6.101:sip > 10.33.6.100:64802 PA / Raw",
      "method": "BYE",
      "request_uri": "sip:101@10.33.6.100:5060;transport=tcp",
      "sip_version": "SIP/2.0"
    },
    {
      "packet_number": 7,
      "timestamp": "2011-07-28T13:54:53.088359",
      "source_ip": "10.33.6.100",
      "destination_ip": "10.33.6.101",
      "source_port": 64802,
      "destination_port": 5060,
      "transport": "TCP",
      "message_type": "response",
      "start_line": "SIP/2.0 200 OK",
      "call_id": "158936656982201062716@10.33.6.100",
      "cseq": "1 BYE",
      "from": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
      "to": "<sip:101@10.33.6.100>;tag=1c1589367133",
      "contact": "<sip:101@10.33.6.100:5060;transport=tcp>",
      "user_agent": "",
      "server": "IPP/v.6.20A.027.012",
      "via": "SIP/2.0/TCP 10.33.6.101;branch=z9hG4bKac359152811;alias",
      "content_type": "",
      "content_length": 0,
      "body_length": 0,
      "known_sip_port": true,
      "headers": {
        "via": "SIP/2.0/TCP 10.33.6.101;branch=z9hG4bKac359152811;alias",
        "from": "<sip:201@10.33.6.101;user=phone>;tag=1c342958875",
        "to": "<sip:101@10.33.6.100>;tag=1c1589367133",
        "call-id": "158936656982201062716@10.33.6.100",
        "cseq": "1 BYE",
        "contact": "<sip:101@10.33.6.100:5060;transport=tcp>",
        "supported": "em,timer,replaces,path,resource-priority",
        "allow": "REGISTER,OPTIONS,INVITE,ACK,CANCEL,BYE,NOTIFY,PRACK,REFER,INFO,SUBSCRIBE,UPDATE",
        "server": "IPP/v.6.20A.027.012",
        "content-length": "0"
      },
      "summary": "Ether / IP / TCP 10.33.6.100:64802 > 10.33.6.101:sip PA / Raw",
      "status_code": 200,
      "reason_phrase": "OK"
    }
  ]
}
```


Contact
----

#### BEN ALI Mohamed 

##### Email : mohamed.benali@esprit.tn

##### LinkedIn : https://linkedin.com/in/medbenali



    








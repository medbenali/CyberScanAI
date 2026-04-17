#!/usr/bin/python
# -*- coding utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor Boston,
#  MA 02110-1301, USA.
#
#  Author: Mohamed BEN ALI

import argparse
import textwrap
import sys
import platform

from libs.colorama import *
from libs import FileUtils

from modules.dns import DNSModule
from modules.dhcp import DHCPModule
from modules.icmp import ICMPModule
from modules.tcp import TCPModule
from modules.sip import SIPModule

from fastmcp import FastMCP


if platform.system() == 'Windows':
    from libs.colorama.win32 import *

__version__ = '1.1.1'
__description__ = '''\
  ___________________________________________

  CyberScanAI | v.''' + __version__ + '''
  Author: BEN ALI Mohamed
  ___________________________________________
'''


def header():
    MAYOR_VERSION = 1
    MINOR_VERSION = 1
    REVISION = 1
    VERSION = {
        "MAYOR_VERSION": MAYOR_VERSION,
        "MINOR_VERSION": MINOR_VERSION,
        "REVISION": REVISION
    }

    PROGRAM_BANNER = open(FileUtils.buildPath('banner.txt')).read().format(**VERSION)
    message = Style.BRIGHT + Fore.RED + PROGRAM_BANNER + Style.RESET_ALL
    write(message)

def usage():
    print('''\n \033[92m CyberScanAI v.1.1.1 http://github/medbenali/CyberScanAI
    It is the end user's responsibility to obey all applicable laws.
    It is just for server testing script. Your ip is visible. \n
      ___________________________________________

      CyberScanAI | v.1.1.1   
      Author: BEN ALI Mohamed
      ___________________________________________


    \n \033[0m''')


def write(string):
    if platform.system() == 'Windows':
        sys.stdout.write(string)
        sys.stdout.flush()
        sys.stdout.write('\n')
        sys.stdout.flush()
    else:
        sys.stdout.write(string + '\n')
        sys.stdout.flush()
        sys.stdout.flush()

def main():

    global transport, host, port
    parser = argparse.ArgumentParser(description="CyberScanAI By BEN ALI Mohamed",
                                     formatter_class = argparse.RawTextHelpFormatter)

    parser.add_argument("-v", "--version", action="version", version=__version__)

    parser.add_argument(
        "--modules",
        help=textwrap.dedent('''
            select module to analyse packets:
                   dns:  analyse dns  packets
                   dhcp: analyse dhcp packets
                   icmp: analyse icmp packets
                   tcp:  analyse tcp  packets
                   sip: analyse sip packets

            '''))

    parser.add_argument(
        "--transport",
        default="stdio",
        choices=["stdio", "http"],
        help="Transport type (default: stdio)",
    )

    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host for HTTP transport (default: 127.0.0.1)",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port for HTTP transport (default: 8080)",
    )

    args = parser.parse_args()

    try:

        header()
        usage()

        # Create CyberScanAI MCP Server
        mcp = FastMCP("CyberScanAI MCP Server By BEN ALI Mohamed 🚀",
                      version="1.1.1")

        # Initialize modules

        if args.modules:

            module_list = args.modules.split(",")
            modules = {}

            if "dns" in module_list:
                modules["dns"] = DNSModule()
            if "dhcp" in module_list:
                modules["dhcp"] = DHCPModule()
            if "icmp" in module_list:
                modules["icmp"] = ICMPModule()
            if "tcp" in module_list:
                modules["tcp"] = TCPModule()
            if "sip" in module_list:
                modules["sip"] = SIPModule()

        else:
            modules = {
            "dns": DNSModule(),
            "dhcp": DHCPModule(),
            "icmp": ICMPModule(),
            "tcp": TCPModule(),
            "sip": SIPModule()
                }

        # Register tools
        register_tools(mcp,modules)

        # Setup prompts
        for module in modules.values():
            module.setup_prompts(mcp)

        # Run CyberScanAI MCP Server
        if args.transport:
            transport = args.transport
        if args.host:
            host = args.host
        if args.port:
            port = args.port

        run_server(mcp, transport, host, port)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\n[*] You Pressed Ctrl+C. Exiting")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def run_server(mcp: FastMCP, transport: str, host: str, port: int):

    if transport == "http":
        mcp.run(
            transport="http",
            host=host,
            port=port,
            show_banner=False,
        )
    else:
        mcp.run(show_banner=False)


def register_tools(mcp: FastMCP,modules):

    for module_name, module in modules.items():
        if module_name == "dns":
            mcp.tool(module.analyze_dns_packets)
        elif module_name == "dhcp":
            mcp.tool(module.analyze_dhcp_packets)
        elif module_name == "icmp":
            mcp.tool(module.analyze_icmp_packets)
        elif module_name == "tcp":
            mcp.tool(module.analyze_tcp_connections)
            mcp.tool(module.analyze_tcp_anomalies)
            mcp.tool(module.analyze_tcp_retransmissions)
            mcp.tool(module.analyze_traffic_flow)
        elif module_name == "sip":
            mcp.tool(module.analyze_sip_packets)


if __name__ == "__main__":

    main()





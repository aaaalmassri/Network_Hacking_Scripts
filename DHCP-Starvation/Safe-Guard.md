# DHCP Starvation Attack Safeguards

Author: Abdelrahman Adel
Date: 2022

## Overview

This README provides essential safeguards and countermeasures against DHCP starvation attacks. DHCP starvation attacks aim to exhaust the available DHCP IP address pool and disrupt network operations. By implementing the safeguards and guidelines described below, you can strengthen your network's resilience against such attacks.

## DHCP Starvation Attack

A DHCP starvation attack occurs when an attacker floods a DHCP server with DHCPDISCOVER requests, causing it to exhaust its available IP address leases. This can lead to network disruptions and unauthorized devices obtaining IP addresses.

## Safeguards and Countermeasures

### Enable DHCP Snooping

1. **Enable DHCP Snooping**: DHCP snooping is a security feature that filters DHCP traffic to ensure that only legitimate DHCP servers can assign IP addresses. Enable DHCP snooping on your network devices, such as switches, to prevent rogue DHCP servers.

### Port Security

1. **Implement Port Security**: Port security allows you to restrict the number of MAC addresses that can be learned on a switch port. Configure port security to limit the number of devices that can connect to a port.

### Enable IP Source Guard

1. **Enable IP Source Guard**: IP Source Guard restricts IP traffic on untrusted Layer 2 access ports to only allow traffic from known and trusted IP addresses.

### Implement Dynamic ARP Inspection

1. **Implement Dynamic ARP Inspection (DAI)**: DAI validates ARP packets to ensure that they have valid IP-to-MAC address bindings. DAI prevents ARP spoofing attacks and unauthorized IP address assignments.

### DHCP Rate Limiting

1. **Implement DHCP Rate Limiting**: Configure your network devices to limit the rate at which DHCPDISCOVER packets can be sent to the DHCP server, preventing an overload of requests.

### Intrusion Detection System (IDS)

1. **Deploy an Intrusion Detection System (IDS)**: An IDS can detect abnormal network behavior and patterns associated with DHCP starvation attacks. Monitor your network with an IDS to identify and respond to suspicious activity.

### Network Segmentation

1. **Implement Network Segmentation**: Divide your network into segments or VLANs. By doing so, you can isolate DHCP servers from untrusted segments, reducing the attack surface.

## License

This documentation is provided under the MIT license, allowing you to use and modify it freely. However, ensure that you follow ethical guidelines and relevant laws when implementing network security safeguards.

## Note

Please use these safeguards responsibly and ensure that you follow ethical guidelines and relevant laws when implementing network security features. Network security is a crucial aspect of maintaining a reliable and secure network environment.

By implementing these safeguards, you can significantly reduce the risk of DHCP starvation attacks and enhance your network's security.

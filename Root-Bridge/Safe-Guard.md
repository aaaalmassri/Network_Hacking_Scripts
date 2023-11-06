# BPDU Guard Feature Configuration

Author: Abdelrahman Adel
Date: 2022

## Overview

This README provides guidance on configuring the BPDU Guard feature in Cisco switches. BPDU Guard is a critical network security feature that helps protect against unauthorized network devices and misconfigurations. Enabling BPDU Guard on your switches can enhance network stability and security.

## Enable BPDU Guard Feature in the Switch

BPDU Guard is a protective feature that detects the other side of a portfast interface to ensure it is a "Single-Node" device. If BPDU Guard discovers that the other side is not a "Single-Node" device due to misconfiguration or a hacking attempt, it will disable the connection on that specific interface.

## BPDU Guard Configuration in Cisco Switches

To configure BPDU Guard in Cisco switches, follow these steps:

1. Enter Enable Mode: `enable`
2. Start Configuration Terminal: `configure terminal`
3. Choose the Interface ID: `interface range Interface-ID`
4. Set Interface to Access Mode: `switchport mode access`
5. Enable Port Fast Feature in the Interface: `spanning-tree portfast`
6. Enable BPDU Guard in the Interface: `spanning-tree bpduguard enable`

## BPDU Guard Default Configuration

To enable BPDU Guard as the default configuration for all Port Fast interfaces, follow these steps:

1. Enter Enable Mode: `enable`
2. Start Configuration Terminal: `configure terminal`
3. Enable Port Fast Feature in Each Access Mode Interface by Default: `spanning-tree portfast default`
4. Enable BPDU Guard in Each Port-Fast Interface by Default: `spanning-tree portfast bpduguard default`

## BPDU Guard Feature Disable Configuration

To disable the BPDU Guard feature on a specific interface, follow these steps:

1. Enter Enable Mode: `enable`
2. Start Configuration Terminal: `configure terminal`
3. Choose the Interface ID: `interface range f0/n`
4. Disable Port Fast Feature in the Interface: `no spanning-tree portfast`
5. Disable BPDU Guard in the Interface: `spanning-tree bpduguard disable`

## BPDU Guard Default Feature Disable Configuration

To disable the BPDU Guard feature as the default configuration, follow these steps:

1. Enter Enable Mode: `enable`
2. Start Configuration Terminal: `configure terminal`
3. Disable Port Fast Feature Default Mode: `no spanning-tree portfast default`
4. Disable BPDU Guard Default Feature: `no spanning-tree portfast bpduguard default`

By understanding and configuring BPDU Guard effectively, you can strengthen the security of your network and reduce the risk of unauthorized network devices disrupting network stability.

## License

This documentation is provided under the MIT license, allowing you to use and modify it freely. However, ensure that you follow ethical guidelines and relevant laws when configuring network security features.

## Note

Please use BPDU Guard and network security features responsibly and only in controlled, authorized environments. Unauthorized or malicious use can have legal and ethical consequences.

Happy networking and stay secure in the world of network operations and cybersecurity.

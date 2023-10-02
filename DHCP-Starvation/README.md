- DHCP Starvation "Exhaustion (DOS) Attack" :

- Attack Idea : 
    - This attack perform Network-DOS by grab all the IP addresses in the DHCP addresses-pool, making other devices not
      able to get addresses using DHCP service and access the network .

    - Script Anatomy :
      .1. check.checkIPaddr : Must be set to False, To not check the "response IP address against sending IP address", Because we don't sure that Dst-address is the address which will replay back . 
      .2. Create DHCP discover message frame with dst-IP = broadcast-IP address .
      .3. Src-MAC is random MAC address .
      .4. Src-IP is = 0.0.0.0
      .5. Dst-IP = broadcast-IP address .
      .6. Src-Port 68 "Default Client DHCP-Port " .
      .7. Dst-Port 67 "Default DHCP-Server Port" .
      .8. DHCP message type is "Discover".

- Attack Process :
- sendp(dhcp_message_frame, loop=True, verbose=True)

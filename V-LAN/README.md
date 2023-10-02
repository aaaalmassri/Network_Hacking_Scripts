
 -> VLAN's Hacking :

   - VLAN's Hacking using forge DTP-messages, which should be disabled in the switch configuration or should be set to access mode in case of security.

   - DTP is two parts "dynamic desirable, dynamic auto", in both cases should be disabled .

   - DTP send its message each 30 seconds, and it's timeout time is 300 seconds "10 messages", after time out will set the switch port to default administrative status which in case of "dynamic desirable is trunk" and in "dynamic auto it's same as the another side of the interface" .

   - RPVST+ Multicast MAC Address : 01:00:0c:cc:cc:cd

   - This attack based on :
   .1. Sniff DTP-message .

   .2. Change DTP-message setting "forge message":
    .2.1. Change src MAC address to my MAC address .
    .2.2. Change desirable status to "trunk" in the other side of the interface .


   .3. Re-send forge-message to the network .
    .3.1. Changing the desirable status will make the switch to forward all the traffic because the interface becomes trunk "trunk interfaces forward the traffic after tagging it" .


   .4. This attack will be able to read "Broadcast Packets", in case of uin-cast packets was send in the target-network in this case need to perform "Man-In-Middle Attack" or "VLAN-Hopping Attack" to be able to send message from on  VLAN  to another one . 

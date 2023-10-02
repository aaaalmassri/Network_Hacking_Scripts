
 - Enable BPDU Guard feature in the switch :
  .1. BPDU Guard feature will discover the other side of portfast interface if it not an "Single-Node" device .
  .2. In case of miss configuration or in hacking attempt, if the BPDU Guard feature discovered that the other side of portfast interface is not an "Single-Node" device will disable the connectio on this interface .


  - BPDU Guard Configuration In Cisco Switches :
  .1. enable : Enter Enable Mode .
  .2. configure terminal : Start Configuration Terminal .
  .3. interface range Interface-ID : Choose Interface ID "Number" .
  .4. switchport mode access : Should Set Interface In Access Mode .
  .5. spanning-tree portfast : Enable Port Fast Feature In This Interface First .
  .6. spanning-tree bpduguard enable : Enable BPDU Guard In This Specific Interface .


  - BPDU Guard Default Configuration :
  .1. enable : Enter Enable Mode .
  .2. configure terminal : Start Configuration Terminal .
  .3. spanning-tree portfast default : Enable Port Fast Feature In Each Access Mode Interface By Default .
  .4. spanning-tree portfast bpduguard default : Enable BPDU Guard In Each Port-Fast Interface By Default .


 - BPDU Guard Feature Disable Configuration :
 .1. enable : Enter Enable Mode .
 .2. configure terminal : Start Configuration Terminal .
 .3. interface range f0/n : Set Interface ID "Number" .
 .4. no spanning-tree portfast : Disable Port Fast Feature In This Specific Interface .
 .5. spanning-tree bpduguard disable : Disable BPDU Guard In This Specific Interface .



 - BPDU Guard Default Feature Disable Configuration :
 .1. enable : Enter Enable Mode .
 .2. configure terminal : Start Configuration Terminal .
 .3. no spanning-tree portfast default : Disable Port Fast Feature Default Mode .
 .4. no spanning-tree protfast bpduguard default : Disable BPDU Guard Default Feature .

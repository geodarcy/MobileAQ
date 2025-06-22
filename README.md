## Mobile Air Quality Monitor project
This project is an attempt to create a mobile platform for collecting air quality data.

| Hardware                                     | Date Purchased | Price (CAD) | Notes                                                                                                                                                                   |  
|----------------------------------------------|----------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| Air Gradient Open Air Outdoor Monitor O-1PST | March 2025     |             |  
| Raspberry Pi 5                               | April 2025     |             |                                                                                                                                                                         |
| power supply                                 | not purchased  |             | - check power requirements of Raspberry Pi and air quality monitor, will need to supply power for 2+ hours, can be kept warm in winter in a bag with a hot water bottle |
### TODO
- test if Raspberry Pi will still create a hotspot when not connected to Ethernet
  - check air quality monitor can connect
  - check laptop can connect and use remote desktop
    - launch data collection script
    - check writing to database
- write Python code to either listen for data or request data
- write Python code to write to InfluxDB
  - check if timestamp is time of data or time of writing to database
- check manual export of InfluxDB to csv for post-processing in R
### Issues encountered
- air quality monitor won't connect when hotspot is created through the Raspberry Pi GUI
  - one line in terminal needed to create hotspot
    - air quality monitor can still fail to connect. Need to:
      - reset monitor
      - use phone to enter ssid/password
      - use laptop to verify script is running and data are being written to database
- tried to use Arduino to collect data automatically from the air quality monitor
  - could not solve how to find all necessary libraries, especially sdkconfig.h
 
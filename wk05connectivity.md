# Hardware Connectivity Status Update
## Recent and current progress
We are utilizing four distinct sensors: the Temperature sensor (TEMP006), Pulse Oximetry sensor (MAX30102), Accelerometer sensor (ADXL345), and Sound sensor. These sensors are each integrated with their individual PCBs and Raspberry Pis for seamless data collection and processing.

Purpose of sensors and connectivity:
1. Temperature Sensor (TEMP006):
   - This sensor is primarily employed for measuring temperature. In our project, we utilize it to monitor the body temperature of infants.
   - The setup employs the TMP006 temperature sensor, a Raspberry Pi, an LED, a transistor, and resistors for a cohesive system. The TMP006 derives power from the 
     Raspberry Pi's 3.3V supply and connect to its ground. It exchanges data via GPIO2 (SDA) and GPIO3 (SCL). Optionally, it can trigger temperature alerts via 
     GPIO17. The transistor's base links to GPIO18 for control, while the emitter connects to the Raspberry Pi's ground, and the collector links to the LED. The 
     2.2k-ohm resistor regulates the transistor's base current, connecting the TMP006's SDA/SCL junction to the transistor base. Additionally, a 220-ohm resistor 
     safeguards the LED from overcurrent, connecting the TMP006's ALERT/SCL junction to the LED's anode. This setup enables real-time temperature monitoring and 
     alerts, with the Raspberry Pi activating the LED through the transistor when specific conditions are met, forming the core of our monitoring and alert system.
   
2.  Pulse Oximetry Sensor (MAX30102):
   - The MAX30102 sensor is designed to monitor vital health parameters such as blood oxygen levels and heart rate.
   - The microcontroller sends commands and data requests to the MAX30102 by switching the SCL and SDA pins according to the I2C protocol.  The sensor responds by 
     sending requested data or status data back to the microcontroller via the SDA pin. The INT pin can be configured to generate an interruption during certain 
     events, such as when new data is available for acquisition. This reduces the need for constant polling of the microcontroller, making the data acquisition 
     process more efficient. The Raspberry Pi 4, with its processing power, receives data from the MAX30102 sensor via circuit traces. This data is then processed 
     by software algorithms and converted into understandable heart rate and oxygen saturation values. The PCB ensures reliable data transmission and improves the 
     overall functionality of the Baby Health Monitor system.

3. Accelerometer Sensor (ADXL345):
   - This sensor specializes in detecting body motion and acceleration, offering valuable insights into an infant's movements and activity.
   - The setup involves a Raspberry Pi 4, an LED, two resistors (220Ω and 2.2kΩ), a transistor, an 8-pin header, and an ADXL345 Triple Axis Accelerometer Sensor, 
     working together seamlessly. The Raspberry Pi 4, acting as the brain of the system, utilizes GPIO Pin 17 to control the LED. When powered on, a high signal 
     from GPIO Pin 17 flows through the 220Ω resistor, illuminating the LED. In parallel, the Raspberry Pi 4 establishes communication with the ADXL345 sensor 
     through the I2C protocol. This sensor, designed to measure acceleration forces across three dimensions, collects data and relays it to the Raspberry Pi 4. The 
     Raspberry Pi  4 undertakes the vital role of processing the acceleration data. In this symphony of components and signals, our system functions harmoniously, 
     offering valuable insights into acceleration forces and signaling through the LED.
   
4. Sound Sensor(LM393):
   - Our sound sensor is dedicated to capturing audio data and assessing noise levels, specifically tracking instances of infant crying or loud noises.
   - The Baby Health Monitor's connectivity setup seamlessly unites vital hardware components to ensure precise sound monitoring. The LM393 sensor serves as the 
     primary data source, capturing sound levels and converting them into electrical signals. This sensor is intricately linked to the Raspberry Pi, acting as the 
     central processing unit. A critical NPN transistor functions as a reliable switch for LED control, while 2.2kΩ and 220Ω resistors optimize the transistor and 
     protect the LED. These components are securely mounted on a PCB, fostering efficient interactions. In practice, the LM393 sensor captures the ambient sound and 
     sends it to the Raspberry Pi for analysis using complex algorithms, ultimately displaying vital sound-related data through controlled LED brightness. This 
     setup creates a user-friendly system for real-time sound monitoring, enhancing infant care.

     
Future Integration:
Our future plans involve consolidating all these sensors onto a single PCB. This integrated PCB will serve as the central data collection hub, connecting to Firebase for real-time data transmission to a mobile application. This unified approach will enhance the efficiency and usability of our monitoring system.

## Problems and hyperlinks/URLs to potential solutions
We are trying to understand  how to build a successful connection of the PCB to the mobile app via Firebase.   

## Financial
### Expenditures since the previous report
| Item Name |Brief Description | Budgeted Costs |Actual Costs|
| -------- | -------- | -------- | ---------- |
|N/A | N/A| N/A | N/A |
|Total | N/A | N/A | N/A |

### Planned future expenses
| Item Name |Brief Description | Budgeted Costs |Actual Costs|
| -------- | -------- | -------- | ---------- |
|N/A | N/A | N/A |N/A |
|Total | N/A | N/A | N/A |

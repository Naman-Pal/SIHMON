# CENG 355: Smart Infant Health MONitor (SIHMON)
Title Page (1st odd page not numbered, X.0 sections begin on odd pages, otherwise double-sided and numbered)  

## Declaration of Joint Authorship   

### Table of Contributions
The table below indicates the contribution of each member to all sections of the Technical Report. Columns 3 through 6 denote the contribution in terms of pages, and hence the percentage of the section completed; 1 column per student. The bottom row summarizes the overall contribution of all members toward the Technical Report. 

<!-- 
My contributions to the report include the following sections: Firmware (Python program running on the Hardware), Hardware connectivity and testing, schematic, breadboard circuit, Printed Circuit Board (PCB), executive summary, introduction, conclusion, background, results and discussions, Appendix, formatting the report, and adding and removing sections.  

You will notice from the OACETT Guidelines pages 3 and 4 and from the PowerPoint presentation Joint Declaration Directions https://learn.humber.ca/ultra/courses/_235686_1/outline/file/_17191432_1 that a table is required describing how each team member contributed to each major section of the document. This can be done at either the Heading 1 and Heading 2 levels. This must be on a separate page above the joint declaration statements. 
- Heading 1: the major sections e.g. 1.0 Introduction, 2.0 Hardware Development Platform Report, etc
- Heading 2: the level 1 subsection e.g., 1.1, 1.2, 1.3, 2.1, 2.2.
-->

| Section | Total Number of Pages | (A) Naman Pal | (B) Eshan Salwan | (C) Satinder Kaur | (D) Zoyeba Mahbub |
| --- | --- | --- | --- | --- | --- |  
| Preliminaries | 4 | 2 50% | 1 25% | 0.75 13% | 0.75 12% |  
| Introduction | 4 | 4 100% | 0 0% | 0 0% | 0 0% |  
| Hardware | x | 5 z% | y z% | y z% | y z% |  
| Mobile Application Report | x | y z% | y z% | y z% | y z% |  
| Integration | x | y z% | y z% | y z% | y z% |  
| Results and Discussions | 3 | 3 100% | 0 0% | 0 0% | 0 0% |  
| Conclusion | 0.75 | 0.75 100% | 0 0% | 0 0% | 0 0% |  
| Appendix | 0.5 | 0.5 100% | 0 0% | 0 0% | 0 0% |
| References | 1 | 0.5 50% | 0.25 25% | 0.25 25% | 0.25 25% |  
| Total | x | 5 25% | 5 25% | 5 25% | 5 25% |  


### Declarations
I, Naman Pal, the founding Team Leader of BioBytes, and the Project Manager of SIHMON (Smart Infant Health MONitor), confirm that this breakdown of authorship represents my contribution to the work submitted for assessment and my contribution is my own work and is expressed in my own words. Any uses made within the Technology Report of the works of any other author, separate from the work group, in any form (ideas, equations, figures, texts, tables, programs), are properly acknowledged at the point of use. A list of the references used is included.

I, Zoyeba Mahbub, confirm that this breakdown of authorship represents my contribution to the work submitted for assessment and my contribution is my own work and is expressed in my own words. Any uses made within the Technology Report of the works of any other author, separate from the work group, in any form (ideas, equations, figures, texts, tables, programs), are properly acknowledged at the point of use. A list of the references used is included.

I, Satinder Kaur, confirm that this breakdown of authorship represents my contribution to the work submitted for assessment and my contribution is my own work and is expressed in my own words. Any uses made within the Technology Report of the works of any other author, separate from the work group, in any form (ideas, equations, figures, texts, tables, programs), are properly acknowledged at the point of use. A list of the references used is included.

I, Eshan Salwan, confirm that this breakdown of authorship represents my contribution to the work submitted for assessment and my contribution is my own work and is expressed in my own words. Any uses made within the Technology Report of the works of any other author, separate from the work group, in any form (ideas, equations, figures, texts, tables, programs), are properly acknowledged at the point of use. A list of the references used is included.

## <a name="proposal">Project Proposal and Specifications</a>   
[Link to the proposal](ceng355wk01proposal.md).   

## Executive Summary   
Introducing SIHMON (Smart Infant Health MONitor), a vital tool for parents navigating the challenges of infant care, especially those concerning Sudden Infant Death Syndrome (SIDS). SIHMON consists of two key parts:   

 - BioSensor Bracelet: 
A wearable for infants packed with sensors (heart rate, oxygen levels, temperature, movement, and sound monitoring). This bracelet is connected to the database (Google Firebase), and provides continuous health data.   

 - Android App with Firebase: 
The companion app, linked to the bracelet via Firebase, processes and displays real-time health information. It goes beyond data display, offering insightful analyses for parents and caregivers. The insights can be tailored to the infant, based on any pre-existing health conditions, environment, and daily routines.   

SIHMON's strength lies in the bracelet's data collection and the app's interpretation. It goes beyond technology, aiming to give parents peace of mind through timely alerts based on health anomalies detected by SIHMON.   

Looking ahead, SIHMON could reshape how we approach healthcare, fostering collaboration between parents and healthcare pros. Its adaptability opens doors for broader healthcare applications.   

In essence, SIHMON is a straightforward yet impactful solution. It envisions a future where parents can confidently navigate parenthood, armed with a reliable tool that transcends technological barriers for genuine peace of mind. SIHMON is more than a monitor; it's a bridge to a safer, more connected world for our littlest ones.   



## Table of Contents

[Declaration of Joint Authorship](#declaration-of-joint-authorship)   
[Project Proposal and Specifications](#proposal)   
[Executive Summary](#executive-summary)   
[Table of Contents](#table-of-contents)   
[List of Figures](#list-of-figures)   

[1.0 Introduction](#10-introduction)   
[1.1 Background](#11-background)   
[1.2 Project Requirements and Specifications](#12-project-requirements-and-specifications)   
[1.3 Project Schedule](#13-project-schedule)   

[2.0 Hardware Development Platform Report/Build Instructions](#20-hardware-development-platform-reportbuild-instructions)  
[2.1 Parts, Components, Materials](#21-parts-components-materials)  
[2.1.1 Tools, Facilities, and Safety](#211-tools-facilities-and-safety)   
[2.1.2 Time Expenditure](#212-time-expenditure)  
[2.1.3 PCB Bill of Materials](#213-pcb-bill-of-materials)  
[2.1.4 Overall Budget (incl. shipping, duty, taxes)](#214-overall-budget-incl-shipping-duty-taxes)  
[2.2 Schematic](#22-schematic)  
[2.3 Breadboard](#23-breadboard)  
[2.4 Printed Circuit Board](#24-printed-circuit-board)  
[2.5 Enclosure](#25-enclosure)  
[2.5.1 Laser Cutting](#251-laser-cutting)  
[2.5.2 3D Printing](#252-3d-printing)  
[2.6 Image/Firmware](#26-imagefirmware)  
[2.7 Connectivity/Testing](#27-connectivitytesting)  

[3.0 Mobile Application Report](#30-mobile-application-report)  
[3.1 Layout](#31-layout)  
[3.1.1 Splash Screen with Drawable Image](#311-splash-screen-with-drawable-image)  
[3.1.2 App Icon](#312-app-icon)   
[3.1.3 User Sign-Up/Registration, Login Activity, Reset/Lost Password](#313-user-sign-upregistration-login-activity-resetlost-password)  
[3.1.4 Data Visualization Activity](#314-data-visualization-activity)  
[3.1.5 Action Control Activity](#315-action-control-activity)  
[3.1.6 About](#316-about)  
[3.1.7 Help](#317-help)  
[3.1.8 Settings](#318-settings)  
[3.2 Flow Diagram](#32-flow-diagram)  
[3.2.1 Toast Message](#321-toast-message)  
[3.2.2 Exit Confirmation Dialog](#322-exit-confirmation-dialog)  
[3.3 Navigation Drawer](#33-navigation-drawer)  
[3.4 End-User Considerations](#34-end-user-considerations)  
[3.4.1 User Interface](#341-user-interface)  
[3.5 Firebase Authentication](#35-firebase-authentication) 
[3.5.1 Backend - Push/Pull from Firebase Database](#351-backend--pushpull-from-firebase-database)  
[3.6 Internationalization](#36-internationalization)  
[3.7 Test Cases](#37-test-cases)  

[4.0 Integration](#40-integration)  
[4.1 Enterprise Wireless Connectivity](#41-enterprise-wireless-connectivity)  
[4.2 Database Configuration](#42-database-configuration)  
[4.3 Network and Security Considerations](#43-network-and-security-considerations)  
[4.4 Unit Testing](#44-unit-testing)  
[4.5 Production Testing](#45-production-testing)  
[4.6 Challenges/Problems](#46-challengesproblems)  
[4.7 Solutions](#47-solutions)  

[5.0 Results and Discussion](#50-results-and-discussion)   
[5.1 Research on Infant Health Worldwide](#research)   
[5.2 Similar products available in the market](#similar_products)   

[6.0 Conclusions](#60-conclusions)   

[7.0 Appendix](#70-appendix)  
[7.1 Firmware Code](#71-firmware-code)  
[7.2 Mobile Application Code](#72-mobile-application-code)  

[8.0 References](#80-references)  

## List of Figures   
[Figure 1: Gantt Chart 1](#fig1)  
[Figure 2: Gantt Chart 2](#fig2)  
[Figure 3: Project Schedule 1](#fig3)  
[Figure 4: Project Schedule 2](#fig4)  
[Figure 5: Figure 5: Collective Schematic Design](#fig5)  
[Figure 6.1: adxl345 accelerometer sensor breadboard testing](#fig6.1)  
[Figure 6.2: adxl345 with LED breadboard testing](#fig6.2)  
[Figure 7.1: tmp006 temperature sensor and LED breadboard testing](#fig7.1)  
[Figure 7.2: tmp006 temperature sensor breadboard testing with Raspberry Pi](#fig7.2)  
[Figure 8.1: max30102 pulse and oximeter sensor breadboard testing using finger](#fig8.1)  
[Figure 8.2: max30102 pulse and oximeter with Raspberry Pi](#fig8.2)  
[Figure 9: lm393 sound sensor breadboard testing](#fig9)  
[Figure 10.1: PCB View in Fritzing Software](#fig10.1)  
[Figure 10.2: PCB in Gerber Format on the JLCPCB website](#fig10.2)  
[Figure 10.3: Unassembled PCB from JLCPCB](#fig10.3)  
[Figure 10.4: PCB after assembly: includes 4 sensors, resistors, transistor, short pin headers, LED, and connection with Raspberry Pi](#fig10.4)  
[Figure 11: Layout of the mobile application](#fig11)
[Figure 11.1: Splash Screen of the mobile application](#fig11.1)
[Figure 11.2: Registration page of the mobile application](#fig11.2)
[Figure 11.3: Login Page of the mobile application](#fig11.3)
[Figure 11.4: About Us Screen of the mobile application](#fig11.4)
[Figure 11.5: Settings Screen of the mobile application](#fig11.5)
[Figure 11.6: Mobile Application Flow](#fig11.6)

## 1.0 Introduction   
### 1.1 Background   
Our vision is to provide parents/caregivers, with a convenient way to monitor their infant’s health in real-time. With the baby wearing the bracelet, parents can track their baby's critical health metrics and receive alerts if the metrics cross a certain threshold. Inspired by the increasing deaths worldwide caused by SIDS (Sudden Infant Death Syndrome), SIHMON was created (Smart Infant Health MONitor). SIHMON will revolutionize the Healthcare Industry by providing a user-friendly interface to monitor the health information of the infant, understand trends, and share information with healthcare professionals. Even non-technical caregivers can easily navigate our app. Ultimately, we aim to help parents/caregivers ensure their baby's well-being and give them peace of mind. This report dives into the development methodologies and strategies, including the software and hardware used to bring the idea of SIHMON to reality. We have used an iterative approach to build this report.

### 1.2 Project Requirements and Specifications   
#### 1.2.1 Hardware Requirements: -
- Raspberry Pi 3 Model B Kit: SoC computer + Power Adapter + Ethernet cable + Ethernet to USB adapter
- The 4 sensors: adxl345 (accelerometer), tmp006 (temperature), max30102 (pulse and oximeter), and lm393 (sound)
- Soldered PCB (Printed Circuit Board) with resistors, transistor, and LED: designed and soldered for SIHMON by BioBytes
- 40-pin stacking header for Raspberry Pi
- Hardware Case: created for SIHMON by BioBytes
### 1.3 Project Schedule   
Final Gantt Charts: Indlude the 2 latest updates to the Mobile App 
###### <a name="fig1">Figure 1: Gantt Chart 1</a>     
![image](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/098c8d50-4f4b-49fb-bded-e09b8a8cff35)
###### <a name="fig2">Figure 2: Gantt Chart 2</a>    
![image](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/7edb27fa-0f3e-45ce-a586-d64881f1b9fa)

Final Schedule: 2 Latest Sprint Plans
###### <a name="fig3">Figure 3: Project Schedule 1</a>     
![image](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/33ec83aa-266c-4d3d-a302-41649e27751b)
###### <a name="fig4">Figure 4: Project Schedule 2</a>     
![image](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/8ad69c1a-97be-4e0e-ba37-841f52a5c109)


## 2.0 Hardware Development Platform Report/Build instructions   
### 2.1 Parts, Components, Materials   
#### 2.1.1 Tools, Facilities, and Safety   
#### 2.1.2 Time Expenditure   
#### 2.1.3 PCB Bill of Materials   
#### 2.1.4 Overall Budget (incl. shipping, duty, taxes)   
### 2.2 Schematic   
###### <a name="fig5">Figure 5: Collective Schematic Design</a>     

The schematic circuit design was completed on Fritzing PC software and laid the foundation for the breadboard and hence the PCB circuit.   
![Schematic View](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/82e7b46b-07fc-4149-bcec-60ad6d77be41)

### 2.3 Breadboard   
The breadboard circuit was extensively used to test the circuits and sensors. Every sensor was tested individually before assembling them onto the PCB.   

###### <a name="fig6.1">Figure 6.1: adxl345 accelerometer sensor breadboard testing</a>     
![Sensor testing picture 3](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/a7d28919-b1b4-4d71-b8bf-20df09e7203f)
###### <a name="fig6.2">Figure 6.2: adxl345 with LED breadboard testing</a>     
![image](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/0e0e88fa-92df-4040-a812-154719fe6073)
###### <a name="fig7.1">Figure 7.1: tmp006 temperature sensor and LED breadboard testing</a>     
![LED](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/cec45bdc-3eca-4be9-af97-8a9e0a747d84)
###### <a name="fig7.2">Figure 7.2: tmp006 temperature sensor breadboard testing with Raspberry Pi</a>     
![PI](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/154cb657-83c6-44c1-ad5f-2538c8d68da9)
###### <a name="fig8.1">Figure 8.1: max30102 pulse and oximeter sensor breadboard testing using finger</a>     
![w finger](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/7180bd8d-c992-420b-941e-3f820219f166)
###### <a name="fig8.2">Figure 8.2: max30102 pulse and oximeter with Raspberry Pi</a>     
![w pi](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/0cce92cf-6512-441a-8f7c-30b2c9858882)
###### <a name="fig9">Figure 9: lm393 sound sensor breadboard testing</a>     
![WhatsApp Image 2023-11-28 at 09 24 58](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/a86ee815-86a9-4900-839d-57dea8ee8c61)

### 2.4 Printed Circuit Board   
After rigorously and successfully testing all the sensors on a breadboard, each circuit was tested on the PCB. The Fritzing software was used to build the PCB design. 
###### <a name="fig10.1">Figure 10.1: PCB View in Fritzing Software</a>     
![PCB View](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/cafe0a56-8a6f-419c-8b30-12b104b90955)   
JLCPCB, a well-known Chinese PCB manufacturer, produced the PCBs. The design was sent to JLCPCB in Gerber format. 
###### <a name="fig10.2">Figure 10.2: PCB in Gerber Format on the JLCPCB website</a>     
![Gerber View](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/37bfbe9f-8e8d-4b63-90d6-997300b11087)   
###### <a name="fig10.3">Figure 10.3: Unassembled PCB from JLCPCB</a>     
![unz](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/7ad4ed43-4457-4faf-972a-4695bc36d2ff)   
One PCB was assembled per sensor by soldering resistors, transistors, LED, and a short pin header onto each PCB. Short pin headers were soldered onto the PCB instead of the sensors themselves so that sensors could be attached or removed sensors, hence making it easier to troubleshoot any potential errors. and successfully tested all 4 circuits. Hence, all 4 sensors were combined into one PCB and tested the final circuit.   
###### <a name="fig10.4">Figures 10.4.1 and 10.4.2: PCB after assembly: includes 4 sensors, resistors, transistor, short pin headers, LED, and connection with Raspberry Pi</a>     
![as2z](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/8fbb4bfd-a01d-4df6-ac9f-fafe25a3ce31)    
![as1z](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/0a773493-3250-4506-9092-09e1d2dc94bb)   

#### 2.4.1 Independent   
#### 2.4.2 Combined   
### 2.5 Enclosure     
#### Design and Material Selection
The enclosure was designed using CorelDRAW, a vector graphics editor, to achieve an intricate design suitable for laser cutting.3mm acrylic material was chosen due to its transparency, sturdiness, and laser-friendly properties, allowing for a clear view of the internal components while protecting them.

![image](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/105024283/3ae148f4-b9ec-4693-a295-600a1a1c0cd4)
#### Fabrication Process, Assembly and Features
The design was sent to Humber's Laser Cut Studio for precision cutting. Post-cutting, the enclosure was assembled with features tailored for functionality:

- Cable Management: Openings were included to facilitate power and peripheral connections to the Raspberry Pi.

- Network Connectivity: Accommodations were made to allow for Ethernet adapter connection without compromising the case's structure.

- Ventilation: Holes were strategically placed for airflow to prevent overheating.

- Sensor Accessibility: The design features a dedicated cutout aligned with the microphone of the sound sensor, permitting unobstructed sound detection. A top opening allows easy access to the sensors, ensuring convenience in monitoring and maintenance tasks.
### 2.6 Image/firmware   
### 2.7 Connectivity/testing   

## 3.0 Mobile Application Report   
### 3.1 Layout
In the mobile application, Navigation Drawer Layout is being used. It consists of a list of menu items for different app features, including 'Temperature,' 'Sleep Monitor,' 'Pulse Oximeter,' 'About Us,' and 'Give Feedback,' enabling easy navigation between the app's main functionalities.
###### <a name="fig11">Figure 11: Layout of the mobile application</a>  
<img src="https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/133720897/2f9046b0-a8a7-40a6-a77c-4cab13cfbc38.png" alt="Layout of the mobile application" width="200" height="400" depth="100">

#### 3.1.1 Splash screen 
The splash screen of the "Infant Health Monitor" app presents a welcoming graphic featuring a stethoscope, signaling the app's health-tracking purpose. It includes the app's name and a tagline highlighting the product's aim to serve modern, health-conscious families. Designed with an attractive background color, the screen captivates users for a deliberate three seconds, engaging them with the app's features before transitioning to the login interface.
###### <a name="fig11.1">Figure 11.1: Splash Screen</a>
<img src="https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/133720897/7d2f9aa0-d187-488c-b313-f0c1d448fed3.jpeg" alt="Splash Screen" width="200" height="400" depth="100">

#### 3.1.2 App icon  
The app icon for "Infant Health" features a heart with a pulse line running through it, clearly symbolizing the app’s focus on monitoring vital health signs. The icon is simple yet effective, utilizing medical imagery to communicate the app's purpose.
###### <a name="fig11.1">Figure 11.1: App Icon</a>
<img src="https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/133720897/ac973a5b-7165-4d66-b0ed-31ef0b2ffd16.png"  alt="App Icon" width="200" height="200" depth="100">

#### 3.1.3 User sign-up/registration, Login
- The registration page of the app is designed for simplicity and ease of use, requesting essential information like full name, email, password, confirmation of password, and phone number. It features clear fields for each entry, and a prominent "Sign up" button to complete the registration process. A convenient link to switch to the login page is provided for users who already have an account.

- The login page follows a similar design ethos, with fields for email and password and a "Remember me" option for user convenience. There's also a "Login" button and an alternative option to sign in with Google, offering users multiple ways to access their account. 

These pages are integrated with Firebase, ensuring secure data handling and user authentication.
###### <a name="fig11.2">Figure 11.2: Registration Page</a>
<img src="https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/133720897/ccd0eb76-49c0-4c33-8a26-30ac36cc1b1c" alt="Registration Page" width="200" height="400" depth="100">

###### <a name="fig11.3">Figure 11.3: Login Page</a>
<img src="https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/133720897/8529bc6f-cd91-4387-8803-6cd459cba834" alt="Login Page" width="200" height="400" depth="100">

#### 3.1.4 Data Visualization Activity  
The application's data visualization uses line charts to display key health metrics—temperature, movement, and pulse oximetry—highlighting crucial high and low values for easy trend analysis and infant well-being monitoring.

#### 3.1.5 Action Control Activity   
The action control activity centers around setting threshold values, which is crucial for personalized health monitoring. Users can adjust the minimum and maximum ranges for temperature, heart rate, and oxygen saturation (SpO2), as well as establish movement sensitivity. These settings are instrumental for configuring the app to send alerts based on individual health criteria, ensuring that users are promptly informed about significant deviations in an infant’s health metrics.

#### 3.1.6 About  
The "About Us" section of the application articulates the core objective of facilitating infant health monitoring, outlining the functionality of the smart bracelet and its integration with the mobile app for real-time updates and alerts. It features a section that introduces the development team, adding a personal touch with illustrated avatars and names, which enhances user trust. 
###### <a name="fig11.4">Figure 11.4: About</a>
<img src="https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/133720897/2c18510e-138c-4eb0-9d89-8a334995588e" alt="About Us Screen" width="200" height="400" depth="100">

#### 3.1.7 Emergency  
The 'Emergency' feature in the toolbar menu is a critical functionality designed for urgent situations. When accessed, it allows the user to make an immediate call to 911, ensuring rapid assistance can be sought during potential crises.

#### 3.1.8 Settings 
The settings screen in the application is a comprehensive control panel that allows users to customize their experience. It provides options to manage notifications, enable a portrait orientation lock, and set sound alerts. It features sliders for setting threshold values for various health indicators such as movement, temperature, heart rate, and oxygen saturation levels—critical for receiving personalized alerts. Additional settings include feedback submission, informational access to 'About Us', and a logout function for user security.
###### <a name="fig11.5">Figure 11.5: Settings</a>
<img src="https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/133720897/1fbf982f-6a03-456a-9a41-6d26965d4379" alt="Settings Screen" width="200" height="400" depth="100">

### 3.2 Flow diagram  
The flow of the mobile application is strategically designed to ensure a smooth user journey from start to finish. Upon launching the app, users are greeted with a splash screen, followed by a login page. Once authenticated, they land on the home screen, which serves as a gateway to various features accessible through the navigation drawer and the toolbar. The navigation drawer offers detailed monitoring options like temperature and sleep, while the toolbar provides quick access to user profile settings and emergency contacts, encapsulating a comprehensive user experience.
###### <a name="fig11.6">Figure 11.6: Mobile Application Flow</a>
<img src="https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/133720897/4f2c7a2f-488a-4df3-812a-2136da0f6cb3" alt="Flow Diagram of mobile application" width="200" height="500" depth="200">

#### 3.2.1 Toast message   
#### 3.2.2 Exit confirmation dialog   
### 3.3 Navigation drawer   
### 3.4 End-user Considerations   
#### 3.4.1 User interface   
### 3.5 Firebase authentication   
In the app, Firebase Authentication is used to make secure authentication easy while improving the sign-in and onboarding experience for end users. It provides endless scalability, supporting login for email and password accounts, Google, Twitter, and Facebook.
#### 3.5.1 Backend- push/pull from Firebase database   
### 3.6 Internationalization   
### 3.7 Test cases
In this project test cases are utilized to test the proper functionality of specific components of the app. The app uses a navigation drawer to enhance end users' UI experience, specific test cases are made to ensure the user is getting the expected result.

## 4.0 Integration   
### 4.1 Enterprise wireless connectivity   
### 4.2 Database configuration   
The database architecture is built on Firebase's ecosystem, utilizing both Firestore and the Realtime Database to manage user profiles, authentication, and sensor data.
#### User Authentication and Profiles
Firebase Authentication is utilized to manage user access and credentials, ensuring security and a seamless user experience. Upon successful login, user profiles are stored within the Firestore database, which is designed for richer, more complex data structures.
#### Sensor Data Management
The Realtime Database offers a highly efficient platform for handling the live sensor data stream. Each sensor's data is nested under a 'sensor' key, ensuring an organized and scalable data model.
#### Record Retention and Cloud Functions
Sensor records are retained in the Firestore database for a period of 7 days. This duration is programmatically managed using Firebase Cloud Functions, which also facilitate the transfer of real-time readings from the Realtime Database to Firestore. The functions include:

- **createDailyRecord**: Initializes a new record for daily data capture.

- **deleteOldRecords**: Scheduled to clean up records older than 7 days.

- **updateMovementRecord**: Triggers upon movement data update in the Realtime Database.

- **updateOxygenRecord**: Activates when new oxygen saturation data is received.

- **updatePulseRecord**: Responds to changes in the heart rate data.

- **updateTemperatureRecord**: Captures updates to temperature readings.

This configuration ensures up-to-date health monitoring with a manageable historical data footprint.

### 4.3 Network and Security Considerations   
In developing the monitor, a paramount concern is the secure and reliable transmission of sensitive health data from the BioSensor bracelet to the mobile application. This section outlines the key network and security measures implemented to ensure the integrity, confidentiality, and availability of data.
#### Network Infrastructure and Connectivity
- **Stable Connectivity**: SIHMON requires a consistent and stable network connection, utilizing wireless protocols such as Wi-Fi. This ensures real-time data transmission from the BioSensor bracelet to the Firebase database and the mobile application.
  
#### Data Security and Privacy
- **Secure User Authentication**: The mobile application incorporates robust authentication protocols. Using methods such as MAuth and token-based authentication, we ensure that only authorized users have access to the health data.
- **Firebase Connection with JSON Key**: To facilitate secure communication with Firebase, a JSON key is used. This key provides a secure way to authenticate and connect the Raspberry Pi to the Firebase database, ensuring end-to-end encryption and data integrity.

### 4.4 Unit Testing   
### 4.5 Production Testing 
The aim of production testing is to validate the SIHMON system against its design specifications. This ensures functionality, operational reliability, and user requirement fulfillment across all components of the system.
- Hardware Testing: Hardware components underwent rigorous validation processes. Each sensor, circuit board, and connectivity interface was tested for functionality. Stress tests were conducted to ascertain durability and resilience under high operational loads.
- **Software Testing**: Software components, including firmware and the mobile application, were subject to in-depth code reviews to detect vulnerabilities and potential bugs. Unit tests were performed to ensure individual functions performed as intended.
- **Integration Testing**: Comprehensive system integration testing verified the seamless operation of hardware and software components together. This included ensuring accurate data capture by the sensors, transmission to the Raspberry Pi, and appropriate logging within the Firebase database.
- **Interface Testing**: The mobile application's user interface was evaluated for usability, responsiveness, and accuracy in displaying sensor data. The Firebase database interface was also tested to confirm correct data storage, retrieval, and real-time update capabilities.
- **Performance Testing**: System performance was assessed under typical and peak loads, focusing on data processing and transmission efficiency. Latency measurements were taken to evaluate the communication speed between the BioSensor bracelet, Firebase database, and the mobile application.
- **Environmental Testing**: The BioSensor bracelet was exposed to a variety of environmental conditions it might encounter during real-world operation, to test its adaptability and reliability.
### 4.6 Challenges/Problems   

The development team faced several technical challenges that required deep analysis and resolution. A systematic overview of the encountered difficulties and their implications on the project trajectory is as follows:

- **Sensor Integration Complexity**: The combination of diverse sensors into a unified hardware framework posed significant challenges. These pertained to electrical compatibility and the maintenance of consistent data communication protocols, vital for the precision and stability of the sensor outputs within the confines of the BioSensor bracelet's compact form factor.

- **Ensuring Software Reliability**: The software development for both embedded firmware and the companion mobile application demanded a thorough debugging process. This iterative procedure was critical to addressing unexpected system failures and achieving a robust operational environment.

- **Data Management Efficacy**: The construction of a fault-tolerant data management pipeline, extending from sensor data capture to processing on the Raspberry Pi, and subsequent storage on Firebase, needed acute focus on data integrity and synchronization, a non-trivial task given the real-time nature of the data involved.

- **Connectivity Assurance**: Guaranteeing consistent and secure connectivity was a non-negotiable requirement, given the sensitive nature of health data. The team encountered challenges related to network dropouts and the safeguarding of data transmission across potentially unsecured networks.

- **User Interface (UI) Optimization**: The UI design process for the mobile application was iterative, focusing on achieving an optimal balance between intuitive usability for non-technical end-users and the provision of comprehensive functionality.

The team's approach to these challenges was characterized by proactive engagement and the application of interdisciplinary expertise, augmented by constructive user feedback. The resolution of these issues was pivotal to the maturation of SIHMON into a solution that effectively serves the needs of its user base. The experience gained has substantially fortified the team's proficiency and will be of significant value in subsequent endeavors.


### 4.7 Solutions   

## 5.0 Results and Discussion   
### <a name="research">5.1 Research on Infant Health Worldwide</a>
There are several 
- SIDS: Sudden Infant Death Syndrome. ![Figure 2: How-to-Protect-the-child-from-SIDS](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/5795caeb-0ffc-4240-8e5a-332ec3118474)
###### Figure 2: SIDS Poster: retrieved from www.drthindhomeopathy.com

  SIDS is the leading cause of death in infants between one month and one year of age in the United States alone, where approximately 2500 children per year die as a result of SIDS[^1][^2][^3][^4].

[^1]: UpToDate.com . Available at :https://www.uptodate.com/contents/sudden-infant-death-syndrome-sids-beyond-the-basics/print#:~:text=SIDS%20is%20the%20leading%20cause,as%20a%20result%20of%20SIDS.

[^2]: MayoClinic. (2023). Sudden Infant Death Syndrome (SIDS). Available at :https://www.mayoclinic.org/diseases-conditions/sudden-infant-death-syndrome/symptoms-causes/syc-20352800#:~:text=Sudden%20infant%20death%20syndrome%20is,often%20die%20in%20their%20cribs.   

[^3]: Ben-Joseph E. & Nemours Kids Health. (2022). Sudden Infant Death Syndrome (SIDS). Available at :https://kidshealth.org/en/parents/sids.html

[^4]: Childrenshospital.org. (n.d.). What you need to know about SIDS. Available at :https://www.childrenshospital.org/conditions/sudden-infant-death-syndrome-sids


- Gastrointestinal issues: 
  It is the second leading cause of death in infants under 5 years of age. It is widespread for babies to have gastrointestinal complications for a variety of reasons including diet, physical activity, and even sleep. However, common problems like diarrhea can seriously dehydrate the infant, often leading to underdeveloped organs, malnutrition, and even death [^5]. The worst part is most parents would never realize their baby is developing these complications, as this requires continuous monitoring of the baby's health, especially after meals. If not treated early, these often develop into bigger digestive issues as the baby grows.

[^5]: who.int. (2017). Diarrhoeal disease. Available at :https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease
  
- Heart Defects: 
  About 40,000 babies are born with Heart defects each year in the US alone[^6]. Such babies are vulnerable to more serious complications like respiratory diseases, poor brain and organ development, and malnutrition[^7]. Such babies' health has to be monitored to ensure the baby's proper development, especially during the early stages of their lives.

[^6]: marchofdimes.org. (2019). Congenital Heart Defects and CHDs. Available at :https://www.marchofdimes.org/find-support/topics/planning-baby/congenital-heart-defects-and-critical-chds   

[^7]: cdc.gov. (2023). Congenital Heart Defects. Available at :https://www.cdc.gov/ncbddd/heartdefects/facts.html#:~:text=CHDs%20are%20present%20at%20birth,formed%20parts%20of%20the%20heart   

- Respiratory infections: 
  Babies commonly develop respiratory infections under the age of 5. If not diagnosed and monitored properly, they lead to lifelong respiratory complications, limiting the baby's ability for physical activities, and hence deeply affecting their futures. Not just that, respiratory infections cause 5.02 deaths per 1000 live births in the US alone[^8].
  
[^8]: National Library of Medicine (US Govt.). (2019). Mortality Associated With Acute Respiratory Infections Among Children at Home. Available at :https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6325348/

- Prematurely born babies: 
  An estimated 13.4 million babies were born pre-term in 2020, with nearly 1 million dying from preterm complications worldwide. It is not feasible for all parents to keep their children in the ICU for months. Monitoring such babies' sleep, heart rates, and oxygen levels during different times of the day can make all the difference.

[^9]: who.int. (2023). 152 million babies born preterm in the last decade. Available at :https://www.who.int/news/item/09-05-2023-152-million-babies-born-preterm-in-the-last-decade#:~:text=An%20estimated%2013.4%20million%20babies,37%20weeks%20of%20pregnancy)%20worldwide.


### <a name="similar_products">5.2 Similar products available in the market</a>
There have been similar attempts at making health monitors, bracelets, and infant care devices. However, SIHMON brings a fresh approach. The idea of making SIHMON as a bracelet was inspired by the Apple Smart Watch. Previous attempts at monitoring the baby's health include cameras, temperature, and sleep quality monitors. However, these focus mostly on external agents. SIHMON focuses on monitoring the baby's health itself, and not the environment the baby is in. It is tailored for infants and babies with health complications.

Some previously implemented projects include: -
#### 5.2.1 Apple SmartWatch
Link to product: https://www.bestbuy.ca/en-ca/product/apple-watch-series-9-gps-45mm-midnight-aluminium-case-with-midnight-sport-band-medium-large-160-210mm/17278985

Description: Offers mobile phone features like calling, texting, voice assistants, and time on the smartwatch. Includes added features like heart rate monitoring and calorie-burnt counting.
#### 5.2.1 Owlet Dream Duo with Camera
Link to product: https://www.bestbuy.ca/en-ca/product/owlet-dream-duo-with-cam-2-wearable-baby-monitor-ps04nmbbj-mint-green/16370778?cmp=knc-s-71700000071826053&gad_source=1&gclid=Cj0KCQiA3uGqBhDdARIsAFeJ5r1eDRFvVe-JG9XNVT66-kG2XsYuzoVu2mWZphQhz-62qWaP-wFTgZgaAtzNEALw_wcB&gclsrc=aw.ds 

Description: Monitors the baby's movements, heart rate, and sounds; streams the baby's live sleep using a camera. 

## 6.0 Conclusions   
In a nutshell, SIHMON (Smart Infant Health MONitor) is more than just a tech project; it's about making a real impact in the lives of parents worldwide. With its BioSensor bracelet and user-friendly app, SIHMON offers a simple yet powerful solution to monitor infants' health, particularly addressing the concern of Sudden Infant Death Syndrome (SIDS).

Picture this: a parent gets a friendly alert on their phone, prompting them to check on their baby as SIHMON detects any unusual health signs. It's not just about technology; it's about providing peace of mind in an unpredictable world.

Beyond individual families, SIHMON could change how we approach healthcare. It bridges the gap between parents and healthcare professionals, making infant health a shared responsibility. The goal is a world where technology isn't a barrier, but a tool that brings people together to protect the littlest lives.

Furthermore, SIHMON can be developed into many advanced solutions that can potentially save millions of lives and improve healthcare worldwide. SIHMON can be extended to be used for patients in general. Meaning that most patients who require close monitoring benefit from SIHMON, as they would not need to be admitted to the hospital to use their advanced tools for health monitoring, as it can be done easily using our product. This won't just help the users, but also free up space in the hospital so that the room can be used for other, more serious cases.  

In essence, SIHMON represents human ingenuity and care. Through SIHMON, we envision a future where parents can embrace the joys of parenthood without constant fear, and a progressive healthcare industry, accessible to all.

## 7.0 Appendix
### 7.1 Firmware code   
This is the link to the firmware, which includes individual Python test files for each of the sensors, and the final Python program. The final program is in the 'Final Python' directory and includes 4 files: 3 dependencies, and one main file.   
[Link to firmware](firmware).   
### 7.2 Mobile Application code   
This is the link to the GitHub repository of the software project for the mobile app. The app is built on Android Studio with Java and XML.   
[Link to GitHub repository of the Mobile App Project](https://github.com/ZoyebaMahbub5837/InfantHealthMonitor).   

## 8.0 References   



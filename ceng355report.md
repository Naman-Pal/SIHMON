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


## 1.0 Introduction   
### 1.1 Background   
Our vision is to provide parents/caregivers, with a convenient way to monitor their infant’s health in real-time. With the baby wearing the bracelet, parents can track their baby's critical health metrics and receive alerts if the metrics cross a certain threshold. Inspired by the increasing deaths worldwide caused by SIDS (Sudden Infant Death Syndrome), we created SIHMON (Smart Infant Health MONitor). SIHMON will revolutionize the Healthcare Industry by providing a user-friendly interface to monitor the health information of the infant, understand trends, and share information with healthcare professionals. Even non-technical caregivers can easily navigate our app. Ultimately, we aim to help parents/caregivers ensure their baby's well-being and give them peace of mind. This report dives into the development methodologies and strategies, including the software and hardware we used to bring the idea of SIHMON to reality. We have used an iterative approach to build this report.

### 1.2 Project Requirements and Specifications   
#### 1.2.1 Hardware Requirements: -
- Raspberry Pi 3 Model B Kit: SoC computer + Power Adapter + Ethernet cable + Ethernet to USB adapter
- The 4 sensors: adxl345 (accelerometer), tmp006 (temperature), max30102 (pulse and oximeter), and lm393 (sound)
- Soldered PCB (Printed Circuit Board) with resistors, transistor, and LED: designed and soldered for SIHMON by BioBytes
- 40-pin stacking header for Raspberry Pi
- Hardware Case: created for SIHMON by BioBytes
### 1.3 Project Schedule   
Final Gantt Charts: Indlude the 2 latest updates to our Mobile App 
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

The schematic circuit design was completed on Fritzing PC software and laid the foundation for our breadboard and hence the PCB circuit.   
![Schematic View](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/82e7b46b-07fc-4149-bcec-60ad6d77be41)

### 2.3 Breadboard   
The breadboard circuit was extensively used to test our circuits and sensors. We tested every sensor individually before assembling them onto our PCB.   

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
After rigorously and successfully testing all the sensors on a breadboard, we tested each circuit on the PCB. We used the Fritzing software to build our PCB design. 
###### <a name="fig10.1">Figure 10.1: PCB View in Fritzing Software</a>     
![PCB View](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/cafe0a56-8a6f-419c-8b30-12b104b90955)   
We collaborated with JLCPCB, a well-known Chinese PCB manufacturer, to produce our PCBs. We sent out the design to JLCPCB in Gerber format. 
###### <a name="fig10.2">Figure 10.2: PCB in Gerber Format on the JLCPCB website</a>     
![Gerber View](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/37bfbe9f-8e8d-4b63-90d6-997300b11087)   
###### <a name="fig10.3">Figure 10.3: Unassembled PCB from JLCPCB</a>     
![unz](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/7ad4ed43-4457-4faf-972a-4695bc36d2ff)   
We assembled one PCB per sensor by soldering resistors, transistors, LED, and a short pin header onto each PCB. We soldered short pin headers onto the PCB instead of the sensor themselves so that we could attach and remove sensors, hence making it easier to troubleshoot any potential errors. and successfully tested all 4 circuits. Hence, we combined all 4 sensors into one PCB and tested the final circuit.   
###### <a name="fig10.4">Figures 10.4.1 and 10.4.2: PCB after assembly: includes 4 sensors, resistors, transistor, short pin headers, LED, and connection with Raspberry Pi</a>     
![as2z](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/8fbb4bfd-a01d-4df6-ac9f-fafe25a3ce31)    
![as1z](https://github.com/PrototypeZone/computer-systems-project-biobytes/assets/98178255/0a773493-3250-4506-9092-09e1d2dc94bb)   

#### 2.4.1 Independent   
#### 2.4.2 Combined   
### 2.5 Enclosure   
#### 2.5.1 Laser cutting   
#### 2.5.2 3D printing   
### 2.6 Image/firmware   
### 2.7 Connectivity/testing   

## 3.0 Mobile Application Report   
### 3.1 Layout   
#### 3.1.1 Splash screen with drawable image   
#### 3.1.2 App icon   
#### 3.1.3 User sign-up/registration, Login activity, reset/lost password   
#### 3.1.4 Data Visualization Activity   
#### 3.1.5 Action Control Activity   
#### 3.1.6 About   
#### 3.1.7 Help   
#### 3.1.8 Settings   
### 3.2 Flow diagram   
#### 3.2.1 Toast message   
#### 3.2.2 Exit confirmation dialog   
### 3.3 Navigation drawer   
### 3.4 End-user Considerations   
#### 3.4.1 User interface   
### 3.5 Firebase authentication   
In our app, we use Firebase Authentication to make secure authentication easy while improving the sign-in and onboarding experience for end users. It provides endless scalability, supporting login for email and password accounts, Google, Twitter, and Facebook.
#### 3.5.1 Backend- push/pull from Firebase database   
### 3.6 Internationalization   
### 3.7 Test cases   

## 4.0 Integration   
### 4.1 Enterprise wireless connectivity   
### 4.2 Database configuration   
### 4.3 Network and Security Considerations   
### 4.4 Unit Testing   
### 4.5 Production Testing   
### 4.6 Challenges/Problems   
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
This is the link to our firmware, which includes individual Python test files for each of our sensors, and our final Python program. The final program is in the 'Final Python' directory and includes 4 files: 3 dependencies, and one main file.   
[Link to firmware](firmware).   
### 7.2 Mobile Application code   
This is the link to the GitHub repository of our software project for the mobile app. The app is built on Android Studio with Java and XML.   
[Link to GitHub repository of the Mobile App Project](https://github.com/ZoyebaMahbub5837/InfantHealthMonitor).   

## 8.0 References   



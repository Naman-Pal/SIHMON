# CENG 355: Smart Infant Health MONitor (SIHMON)
Title Page (1st odd page not numbered, X.0 sections begin on odd pages, otherwise double sided and numbered)  

## Declaration of Joint Authorship   

### Table of Contributions
You will notice from the OACETT Gudelines page 3 and 4 and from the PowerPoint presnetation Joint Declaration Directions https://learn.humber.ca/ultra/courses/_235686_1/outline/file/_17191432_1 that a table is required decribing how each team members contributed to each major section of the document. This can be done at either the Heading 1 and / or Heading 2 level. This must be on a seperate page above the joint decalaration statements. 

- Heading 1 : the major sections e.g. 1.0 Introduction, 2.0 Hardware Development Platformn Report, etc
- Heading 2 : the level 1 subsections e.g, 1.1, 1.2, 1.3, 2.1, 2.2.

### Declarations
I, Naman Pal, confirm that this breakdown of authorship represents my contribution to the work submitted for assessment and my contribution is my own work and is expressed in my own words. Any uses made within the Technology Report of the works of any other author, separate to the work group, in any form (ideas, equations, figures, texts, tables, programs), are properly acknowledged at the point of use. A list of the references used is included.

I, Zoyeba Mahbub, confirm that this breakdown of authorship represents my contribution to the work submitted for assessment and my contribution is my own work and is expressed in my own words. Any uses made within the Technology Report of the works of any other author, separate to the work group, in any form (ideas, equations, figures, texts, tables, programs), are properly acknowledged at the point of use. A list of the references used is included.

I, Satinder Kaur, confirm that this breakdown of authorship represents my contribution to the work submitted for assessment and my contribution is my own work and is expressed in my own words. Any uses made within the Technology Report of the works of any other author, separate to the work group, in any form (ideas, equations, figures, texts, tables, programs), are properly acknowledged at the point of use. A list of the references used is included.

I, Eshan Salwan, confirm that this breakdown of authorship represents my contribution to the work submitted for assessment and my contribution is my own work and is expressed in my own words. Any uses made within the Technology Report of the works of any other author, separate to the work group, in any form (ideas, equations, figures, texts, tables, programs), are properly acknowledged at the point of use. A list of the references used is included.

## Proposal/Project Specifications   
[Link to proposal](ceng355wk01proposal.md).   
## Executive Summary   
We have designed SIHMON (Smart Infant Health MONitor) for parents with babies, especially with health complications like SIDS (Sudden Infant Death Syndrome). SIHMON consists of 2 key components. 
- A BioSensor bracelet, which the baby wears.
- An Android app, which analyzes the baby’s health using the data from the bracelet.

 The bracelet monitors the infant’s health using sensors like heart rate, oxygen levels, body temperature, movement, and surrounding sound. The bracelet is connected to the Android app through Firebase (back-end). The app displays this health data, analyzes it, and provides insights into the infant’s health based on the analysis to the parent/caregiver.

## Table of Contents

[Declaration of Joint Authorship](#declaration-of-joint-authorship)   
[Proposal/Project Specifications](#proposalproject-specifications)   
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

[6.0 Conclusions](#60-conclusions)

[7.0 Appendix](#70-appendix)  
[7.1 Firmware Code](#71-firmware-code)  
[7.2 Mobile Application Code](#72-mobile-application-code)  

[8.0 References](#80-references)  

## List of Figures   
[Figure 1: Gantt Chart](#figure-1-gantt-chart)  

## 1.0 Introduction   
### 1.1 Background   
Our vision is to provide parents/caregivers, a convenient way to monitor their infant’s health in real-time. With the baby wearing the bracelet, parents can track their baby's critical health metrics and receive alerts if the metrics cross a certain threshold. Inspired by the increasing deaths worldwide caused by SIDS (Sudden Infant Death Syndrome), we created SIHMON (Smart Infant Health MONitor). SIHMON will revolutionize the Healthcare Industry by providing a user-friendly interface to monitor the health information of the infant, understand trends, and share information with healthcare professionals. Even non-technical caregivers can easily navigate our app. Ultimately, we aim to help parents/caregivers ensure their baby's well-being and give them peace of mind. This report dives into the development methodologies and strategies, including the software and hardware we used to bring the idea of SIHMON to reality. We have used an iterative approach to build this report.

### 1.2 Project Requirements and Specifications   
#### 1.2.1 Hardware Requirements: -
- Raspberry Pi
- The 4 sensors: adxl345 (accelerometer), tmp006 (temperature), max30102 (pulse and oximeter), lm393 (sound)
- PCB (created for SIHMON by BioBytes)
- Encasing for the hardware (created for SIHMON by BioBytes)
### 1.3 Project Schedule   
Insert Gantt Chart
- Milestone Level is sufficient

###### Figure 1: Gantt Chart     

## 2.0 Hardware Development Platform Report/Build instructions   
### 2.1 Parts, Components, Materials   
#### 2.1.1 Tools, Facilities, and Safety   
#### 2.1.2 Time Expenditure   
#### 2.1.3 PCB Bill of Materials   
#### 2.1.4 Overall Budget (incl. shipping, duty, taxes)   
### 2.2 Schematic   
### 2.3 Breadboard   
### 2.4 Printed Circuit Board   
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
### 3.4 End-user considerations   
#### 3.4.1 User interface   
### 3.5 Firebase authentication   
#### 3.5.1 Backend- push/pull from firebase database   
### 3.6 Internationalization   
### 3.7 Test cases   

## 4.0 Integration   
### 4.1 Enterprise wireless connectivity   
### 4.2 Database configuration   
### 4.3 Network and Security considerations   
### 4.4 Unit Testing   
### 4.5 Production Testing   
### 4.6 Challenges/Problems   
### 4.7 Solutions   

## 5.0 Results and Discussion   
### 5.1 Research on Infant-Health Worldwide
There are several 
- SIDS: Sudden Infant Death Syndrome
  SIDS is the leading cause of death in infants between one month and one year of age in the United States alone, where approximately 2500 children per year die as a result of SIDS.
- Gastrointestinal issues
  It is the second leading cause of death in infants under 5 years of age. It is very common for babies to have gastrointestinal complications for a variety of reasons including diet, physical activity, and even sleep. However, common problems like diarrhea can seriously dehydrate the infant, often leading to underdeveloped organs, malnutrition, and even death. The worst part is most parents would never realize their baby's developing these complications, as this requires continuous monitoring of the baby's health, especially after meals. These often develop into bigger digestive issues as the baby grows, if not treated early. 
- Heart Defects
  About 40,000 babies are born with Heart defects each year in the US alone. Such babies are vulnerable to more serious complications like respiratory diseases, poor brain and organ development, and malnutrition. Such babies' health has to be monitored to ensure the baby's proper development, especially during the early stages of their lives.
- Respiratory infections
  Babies commonly develop respiratory infections under the age of 5. If not diagnosed and monitored properly, they lead to lifelong respiratory complications, limiting the baby's ability for physical activities, and hence deeply affecting their futures. Not just that, respiratory infections cause 5.02 deaths per 1000 live births in the US alone. 
- Prematurely born babies
  An estimated 13.4 million babies were born pre-term in 2020, with nearly 1 million dying from preterm complications worldwide. It is not feasible for all parents to keep their children in the ICU for months. Monitoring such babies' sleep, heart rates, and oxygen levels during different times of the day can make all the difference. 

### 5.2 Similar products available in the market
There have been similar attempts at making health monitors, bracelets, and infant care devices. However, SIHMON brings a fresh approach. The idea of making SIHMON as a bracelet was inspired by the Apple Smart Watch. Previous attempts at monitoring the baby's health include cameras, temperature, and sleep quality monitors. However, these focus mostly on external agents. SIHMON focuses on monitoring the baby's health itself, and not the environment the baby is in. It is tailored for infants and babies with health complications.

Some previously implemented projects include: -
#### 5.2.1 Apple SmartWatch
Link to product: https://www.bestbuy.ca/en-ca/product/apple-watch-series-9-gps-45mm-midnight-aluminium-case-with-midnight-sport-band-medium-large-160-210mm/17278985

Description: Offers mobile phone features like calling, texting, voice assistants, and time on the smartwatch. Includes added features like heart rate monitoring and calories-burnt counting.
#### 5.2.1 Owlet Dream Duo with Camera
Link to product: https://www.bestbuy.ca/en-ca/product/owlet-dream-duo-with-cam-2-wearable-baby-monitor-ps04nmbbj-mint-green/16370778?cmp=knc-s-71700000071826053&gad_source=1&gclid=Cj0KCQiA3uGqBhDdARIsAFeJ5r1eDRFvVe-JG9XNVT66-kG2XsYuzoVu2mWZphQhz-62qWaP-wFTgZgaAtzNEALw_wcB&gclsrc=aw.ds 

Description: Monitors the baby's movements, heart rate, and sounds; streams the baby's live sleep using a camera. 

## 6.0 Conclusions   

## 7.0 Appendix
### 7.1 Firmware code   
[Link to firmware](firmware).
### 7.2 Mobile Application code   
Link to GitHub repository for app.

## 8.0 References   
= https://www.uptodate.com/contents/sudden-infant-death-syndrome-sids-beyond-the-basics/print#:~:text=SIDS%20is%20the%20leading%20cause,as%20a%20result%20of%20SIDS.
- https://www.bestbuy.ca/en-ca/product/owlet-dream-duo-with-cam-2-wearable-baby-monitor-ps04nmbbj-mint-green/16370778?cmp=knc-s-71700000071826053&gad_source=1&gclid=Cj0KCQiA3uGqBhDdARIsAFeJ5r1eDRFvVe-JG9XNVT66-kG2XsYuzoVu2mWZphQhz-62qWaP-wFTgZgaAtzNEALw_wcB&gclsrc=aw.ds
- https://www.bestbuy.ca/en-ca/product/apple-watch-series-9-gps-45mm-midnight-aluminium-case-with-midnight-sport-band-medium-large-160-210mm/17278985
- https://www.mayoclinic.org/diseases-conditions/sudden-infant-death-syndrome/symptoms-causes/syc-20352800#:~:text=Sudden%20infant%20death%20syndrome%20is,often%20die%20in%20their%20cribs.
- https://kidshealth.org/en/parents/sids.html
- https://www.childrenshospital.org/conditions/sudden-infant-death-syndrome-sids
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6325348/
- https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease
- https://www.cdc.gov/ncbddd/heartdefects/facts.html#:~:text=CHDs%20are%20present%20at%20birth,formed%20parts%20of%20the%20heart).
- https://www.marchofdimes.org/find-support/topics/planning-baby/congenital-heart-defects-and-critical-chds
- https://www.who.int/news/item/09-05-2023-152-million-babies-born-preterm-in-the-last-decade#:~:text=An%20estimated%2013.4%20million%20babies,37%20weeks%20of%20pregnancy)%20worldwide.
- 

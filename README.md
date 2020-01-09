# Introduction  
  
AidRefugee is a web application for refugees to communicate with NGO's and lost victims at the time of natural calamity. With AidRefugee portal, one can locate missing refugees, search for relatives, nearby campsites and medical services. Additionally, the portal also allows one to donate resources to the NGOs involved in providing aids to people affected by natural calamities.  
  
# Features  
  
Unique identification of refugees. A refugee is identified by **face recognition and profile matching.** This is useful in locating the refugee and connecting him/her to the poeple who are searching for the person.  
<br>
**Real time location tracking** enables one to find their way to nearby camps and also the poeple they are connected to via the website.      
<br>
**Resources available and capacity of each camp is displayed pictorially using maps**. If a camp is fails to accomodate new refugees, it can delegate these refugees to other nearby rescue camps. All this data is managed on the web app usnig which the camps can allocate refugees to other sites taking into condsideration avaliable space and resources.  
<br>
Any organisation or individual can provide help in terms of money or other resources needed via the **Donation** section in the web application. The refugees and the camps are resposible to upload their requirements and **dynamic allocation of the received donations** is done by the web app.  
<br>
Lastly, during such crisis, it is very importnat that people stay updated. Therefore,  **notifications** which include - services being provided, medical help and alerts regaring dangerous areas -   weather conditions - epedemic affected areas are sent to the users.  
<br>
<br>

**ENTER API KEY AT FOLLOWING PLACES:**
<br/>
*Google Maps API Key: src/ngo/templates/ngo/PAGE2(view).html - Line 52  
*Google Maps API Key: src/templates/base/js.html - Line 5  
*Twilio Account Details: src/ngo/views.py - Line 46 and 47  


# NewCourseNotifier
The program checks if a new course is added in the 
Computer Science section on the StudIP of the 
University of Passau and notifies via email


Due to the high demand and the limited number of spots,
 it is possible to miss the opportunity to attend some
  of the courses in the university. This project I did
   solves the problem. You can use this too if 
   you are a Masters in Computer Science student of 
   the University of Passau. Make the following 
   changes to make it work for you.
   
   On lines 35 and 36,
   
    user_name.send_keys(studip.get("user_name")) 
    password.send_keys(studip.get("password"))  
    
   provide your StudIP username and password respectively
   
   On line 112,
   
    smtp_instance = smtplib.SMTP(host="smtp.gmail.com", port=587)
   
   change the "host" and "port" to the one provided 
   by your email service provider.
   
   On line 114,
   
    smtp_instance.login(gmail.get("email"), gmail.get("password"))
   
   provide the email id and the password. This is 
   used for sending the email.
   
   On line 119,
   
    message['From'] = gmail.get("email")
   
   use the same email id used on line 114.
   
   On line 120,
   
    message['To'] = gmail.get("email_to")
   
   provide the email id to which the notification is 
   to be sent.   
   
   You can schedule the code to run repeatedly at 
   intervals of your choice using Crontab. 
   [Click here to know how](http://www.adminschoice.com/crontab-quick-reference)
   
   The project relies mainly on [Selenium](https://github.com/SeleniumHQ)
   
   
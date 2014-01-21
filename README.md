IRVING
======

Integrated Review and Visibility Interface Notification Gadget

> IRVING is a system built to integrate directly with end user systems. Users know their data and they know the conditions that are abnormal and worth monitoring. IRVING allows users and administrators to set up predefined criteria for these monitors and allows the users the ability to set up a dashboard customized to their daily work flow. 

> They can define warning and error thresholds, systems that should be monitored and groups that should appear. Administrators of an IRVING installation can define system wide events that all users should be able to monitor.

### Quick Overview

**IRVING** is designed to allow your users quick access to *their* metrics. Each of your users is responsible for data in the systems they work on in different ways. **IRVING** allows them to view data points that are important to them. With the ability to query across databases, and database types, **IRVING** can show a user exactly what they need to see to monitor the overall health of data and processes.

![Front End Overview](http://i.imgur.com/rAtbqMg.png)

The dashboard that users set up are easy to read and understand. They allow quick identification of data points that are in an alert state (known as *errors* in **IRVING**) or data points that could become errors (known as *warnings* in **IRVING**). Additionally, administrators can set up a panel for all users of **IRVING** to have on the dashboard. 

![Drag and Drop Systems](http://i.imgur.com/Ydcwhiu.png)
![Drag and Drop Data points](http://i.imgur.com/JQ0gfow.png)

**IRVING** has a simple drag and drop interface for users to reorder how their dashboard appears. Groups of data points can be arranged and data points within groups can be arrange via a simple drag and drop interface.








---

Developer Notes:

 - This is my first large-ish project using Django. As such, I expect that it does not meet all standard conventions of Django packaging. Over time, I plan on fixing this
 - IRVING has been tested against the following database types: Oracle (using `cx_oracle`), Microsoft SQL (using `django-mssql` and `PyWin32`), MySQL/Maria, and SQLite
 - I am very pleased with how the front end of the system looks. I'm not as pleased with the backend/admin panel. Again, this is something I plan on fixing in the future, but the front end was most important for my end users
 - I am more than happy to take pull requests, issue reports or comments and will do my best to integrate them into this repository

 
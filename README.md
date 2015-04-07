Welcome to Harvey
=================
-an automated suite for recruiting eligible usability participants for research purposes, coupled with a suite of data visualization tools for common UX outputs, such as eye tracking and CSV (comma separated values).

The suite is free for you to use however you see fit. Take my code and tailor it to your needs, free of charge.

These tools were developed at the Full Sail User Experience Research lab, located in Winter Park, FL for the purposes of improving currently existing recruiting techniques.

About
=====

Harvey's first client release version will have a Django backend with a MongoDB database.

It will take established criteria for a given playtest/usability test, compare it to user-submitted preferences, including intended appointment times and favorite genres. This information will be used to select the MOST viable candidates to gain valid data. It will be possible to have Harvey automatically schedule these appointments or have a human decide eligibility.

Harvey will be capable of automatically sending messages to users in the form of emails and text messages as reminders. These will be personalized with messages detailing their eligibility, along with their first name and appointment times. 

Any information that gets entered in the database will be accessible and viewable on multiple machines with less than one second latency (and it will probably be closer to 1/50th of a second). Information will be stored as JSON objects, which act as hash tables/dictionaries. Duplicate entries will intentionally be ignored.

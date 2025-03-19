# GCalUpdater  
python scripts and Google Cloud API calls to update a calendar with a given CSV  
  
## Pre-requisites:  
<pre>
o  Python and PIP  
o  Install Google Client Library  
   o  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib  
o  Creating a Google Cloud Project with Calendar API enabled to create auth credentials for the app.  
(taken directly from Google documentation and Google Gemini)
   o  Go to the Google Cloud Console: console.cloud.google.com
      o  Create a new project or select an existing one.
      o  Enable the Google Calendar API for your project.
      o  Create OAuth 2.0 credentials:
      o  Go to "APIs & Services" > "Credentials".
      o  Click "Create Credentials" > "OAuth client ID".
      o  Select "Desktop app" as the application type.
      o  Download the credentials.json file and place it in the same directory as your Python script.
</pre>
  
## Running the Script
<pre>
   o  create a CSV named "events.csv" with your event dates:  date,start_time,end_time,title,calendar_id,timezone
   o  If this is for your main/primary google calendar in your account, use "primary" for the calendar_id.
   o  If you want to use another calendar for the event, look up the Calendar ID to use:
      o  Go to Calendar Settings
      o  Find the calendar under "Settings for my calendars"
      o  the Calendar ID string is under the "Integrate Calendar" section.
o  Run the script:  python3 gcalupdater.py
   o  Upon first-run, you will recieve a popup to authenticate the application.
   o  This will create a "token.json" file for future runs of the script.

</pre>




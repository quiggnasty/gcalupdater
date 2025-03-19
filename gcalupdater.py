from __future__ import print_function

import datetime
import os.path
import csv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def create_calendar_event(date, start_time, end_time, title, calendar_id, timezone):
    """Creates an event in the specified Google Calendar.
    Args:
        date: The date of the event (YYYY-MM-DD).
        start_time: The start time of the event (HH:MM).
        end_time: The end time of the event (HH:MM).
        title: The title of the event.
        calendar_id: The ID of the calendar to create the event in.
        timezone: The timezone of the event (e.g., 'America/New_York').
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        start_datetime = datetime.datetime.strptime(f"{date}T{start_time}", "%Y-%m-%dT%H:%M")
        end_datetime = datetime.datetime.strptime(f"{date}T{end_time}", "%Y-%m-%dT%H:%M")

        event = {
            'summary': title,
            'start': {
                'dateTime': start_datetime.isoformat(),
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_datetime.isoformat(),
                'timeZone': timezone,
            },
        }

        event = service.events().insert(calendarId=calendar_id, body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')

    except HttpError as error:
        print(f'An error occurred: {error}')

def create_events_from_csv(csv_file):
    """Creates calendar events from data in a CSV file."""
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            date = row.get('date')
            start_time = row.get('start_time')
            end_time = row.get('end_time')
            title = row.get('title')
            calendar_id = row.get('calendar_id')
            timezone = row.get('timezone')

            if all([date, start_time, end_time, title, calendar_id, timezone]):
                create_calendar_event(date, start_time, end_time, title, calendar_id, timezone)
            else:
                print(f"Missing data in row: {row}")

if __name__ == '__main__':
    csv_file = 'events.csv'  # Replace with your CSV file name
    create_events_from_csv(csv_file)


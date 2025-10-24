from imap_tools import MailBox
from imap_tools import AND
import os
from pathlib import Path

MAIL_PASSWORD = "your app api password"
MAIL_USERNAME = "your email.com"
MAIL_SERVER = "imap.gmail.com"

DOWNLOADS_DIR = str(Path.home() / "Downloads")
DOWNLOAD_FOLDER = os.path.join(DOWNLOADS_DIR, "downloaded_csvs")

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)
    print(f"Created csv download folder at {DOWNLOAD_FOLDER}")

with MailBox(MAIL_SERVER).login(MAIL_USERNAME, MAIL_PASSWORD,"INBOX") as mailbox:
    print("Logged in successfully")
    for msg in mailbox.fetch(AND(subject = "WSU Track")):
        print(f"From: {msg.from_}")
        print(f"Subject: {msg.subject}")
        print(f"Date: {msg.date}")
        print(f"Body: {msg.text}")
        for att in msg.attachments:
            print(f"Attachment: {att.filename} ({len(att.payload)} bytes)")
            if att.filename.lower().endswith(".csv"):
                filepath = os.path.join(DOWNLOAD_FOLDER, att.filename)
                with open(filepath, "wb") as f:
                    f.write(att.payload)
                print(f"Saved attachment to {filepath}")


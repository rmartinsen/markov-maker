import httplib2
import os
import base64
import html

from apiclient import discovery
from apiclient.http import BatchHttpRequest
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
PRODUCT_NAME = 'robguapoawesome'
APPLICATION_NAME = 'robguapoawesome'



class GmailDownloader:

    def __init__(self, target_name, target_email):
        self.target_name = target_name
        self.target_email = target_email
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('gmail', 'v1', http=http)

    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'gmail-python-quickstart.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            print('Storing credentials to ' + credential_path)
        return credentials

    def save_emails_to_text(self):
        emails = " ".join(self.get_all_emails())
        print(emails)

    def get_all_emails(self):
        filter = "from:" + self.target_email
        results = self.service.users().messages().\
            list(userId='me', q=filter).execute()
    
        for result in results["messages"]:
            email_id = result["id"]
            full_text = self.get_email_full_text(email_id)
            snippet = self.get_email_snippet(full_text)
            yield snippet

    def get_email_full_text(self, email_id):
        result = self.service.users().messages().get(userId='me',
                                                id=email_id).execute()
        return result

    def get_email_snippet(self, full_text):
        snippet = html.unescape(full_text['snippet'])
        message_end = snippet.find(" On ")
        snippet_text = snippet[:message_end]
        last_space = snippet_text.rfind(" ")
        return snippet_text[:last_space]

gd = GmailDownloader("kate", "dylantyagi@gmail.com")
gd.save_emails_to_text()
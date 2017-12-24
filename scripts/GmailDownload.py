import httplib2
import os
import base64

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools


SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
CREDENTIAL_DIR = "/Users/tempadmin/.credentials"
APPLICATION_NAME = 'robguapoawesome'


class GmailDownloader:

    def __init__(self):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('gmail', 'v1', http=http)

    def get_credentials(self):
        if not os.path.exists(CREDENTIAL_DIR):
            os.makedirs(CREDENTIAL_DIR)
        credential_path = os.path.join(CREDENTIAL_DIR, 'gmail-download.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)

        return credentials

    def get_all_emails(self, target_email):
        filter = "from:" + target_email
        results = self.service.users().messages().list(userId='me', q=filter).execute()

        for result in results["messages"]:
            email_id = result["id"]
            full_text = self.get_email_full_text(email_id)
            yield full_text

    def get_email_full_text(self, email_id):
        result = self.service.users().messages().get(userId='me', id=email_id).execute()
        parts = result["payload"]["parts"]
        data = parts[0]["body"]["data"]
        clean_data = data.replace("-", "+").replace("_", "/")
        decoded_data = base64.b64decode(bytes(clean_data, "UTF-8"))
        return str(decoded_data)

    def remove_replies_and_forwards(self, email):
        reply_separator = "\\r\\n\\r\\nOn"

        separator_index = email.find(reply_separator)
        if separator_index > -1:
            clean_email = email[:separator_index]

        return clean_email

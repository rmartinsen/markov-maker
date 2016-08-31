import httplib2
import os

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

def get_credentials():
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

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    filter = {
    'criteria': {
        'from': 'srkirkland@gmail.com'
    	}
	}

	batch = service.new_batch_http_request()

    results = service.users().messages().\
    			list(userId='me', q='from:srkirkland@gmail.com').execute()
    
    for result in results['messages']:
      	print(result)


if __name__ == '__main__':
    main()
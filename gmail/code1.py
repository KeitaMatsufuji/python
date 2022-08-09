from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://mail.google.com/']

flow = InstalledAppFlow.from_client_secrets_file("./client_secret.json", SCOPES)

cred = flow.run_local_server(port = 0)
# トークンをJSONで取得
with open('token.json', 'w') as token :
    token.write(cred.to_json())
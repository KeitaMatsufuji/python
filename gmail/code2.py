from email import message
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import base64
import mimetypes

def message_base64_encode(message) :
    return base64.urlsafe_b64encode(message.as_bytes()).decode()

def attach_file(message, file_path, file_name) :
    content_type, encoding = mimetypes.guess_type(file_path)
    main_type, sub_type = content_type.split("/", 1)
    f = open(file_path, "rb")
    message_file = MIMEBase(main_type, sub_type)
    # データを読み込んだ値を渡す
    message_file.set_payload(f.read())
    message_file.add_header(
        "Content-Disposition", "attachment", filename=file_name
    )
    encoders.encode_base64(message_file)
    f.close()
    message.attach(message_file)
    return message

def main() :
    scopes = ['https://mail.google.com/']
    creds = Credentials.from_authorized_user_file("token.json", scopes)
    service = build("gmail", "v1", credentials = creds)

    # 文字列を送信
    # message = MIMEText("Hello Python")
    # message["To"] = "k1-matsufuji@ask-planning.co.jp"
    # message["From"] = "kale8001@gmail.com"
    # message["Subject"] = "send test"
    # raw = {"raw" : message_base64_encode(message)}

    # service.users().messages().send(
    #     userId = "me",
    #     body = raw
    # ).execute()

    message = MIMEMultipart()
    message["To"] = "kale8001@gmail.com"
    message["From"] = "kale8001@gmail.com"
    message["Subject"] = "送信テスト2"
    message.attach(MIMEText("ファイルを送信", "plain"))
    message = attach_file(message, "./test.png", "test.png")

    raw = {"raw" : message_base64_encode(message)}

    # service.users().messages().send(
    #     userId = "me",
    #     body = raw
    # ).execute()

    

    print("complete！")

if __name__ == '__main__' :
    main()
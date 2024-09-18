import os
import importlib
import importlib.util
from os.path import basename
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class EmailSender:
    def __init__(self, config_name="smtpconfig_1", config_dir=None):
        try:
            script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            config_dir = os.path.join(script_dir, "mail_lib", "smtpconfig")
            self.config_path = os.path.join(config_dir, f"{config_name}.py")
            spec = importlib.util.spec_from_file_location(config_name, self.config_path)
            config_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config_module)
            self.config = getattr(config_module, f"SMTP_CONFIG_{config_name.split('_')[-1]}").copy()
        except (ImportError, AttributeError) as e:
            print(f"Error loading configuration: {str(e)}")
        self.message = None


    def create_message(self, subject, recipient):
        self.message = MIMEMultipart()
        self.message["Subject"] = subject
        self.message["From"] = self.config["sender_email"]
        self.message["To"] = recipient

    def add_text_content(self, body):
        self.message.attach(MIMEText(body, 'plain'))

    def add_html_content(self, body):
        self.message.attach(MIMEText(body, 'html'))

    def add_attachment(self, file_path):
        with open(file_path, mode="rb") as file:
            part = MIMEApplication(file.read(), Name=basename(file_path))
        part["Content-Disposition"] = f"attachment; filename='{basename(file_path)}'"
        self.message.attach(part)

    def send(self):
        try:
            with SMTP(self.config["smtp_server"], self.config["port"]) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(self.config["sender_email"], self.config["password"])
                server.send_message(self.message)
                print("Mail Sent")
            return True
        except Exception as e:
            print(f"Mail sent error: {e}")
            return False

if __name__ == "__main__":
    email_sender = EmailSender()
    #1 メールの基本情報を設定
    subject = ""
    recipient = ""
    email_sender.create_message(subject, recipient)

    #? 2のどれか一つを選んでください。
    #2 テキスト形式の本文を追加
    text_content = """
    
    """
    email_sender.add_text_content(text_content)

    #2 HTML形式の本文を追加（オプション）
    html_content = """
    <html>
    <body>
        <h2></h2>
        <p></p>
        <p></p>
    </body>
    </html>
    """
    email_sender.add_html_content(html_content)

    #2 添付ファイルを追加
    attachment_path = "例 /path/to/project_report.pdf"
    email_sender.add_attachment(attachment_path)

    #3 メールを送信
    if email_sender.send():
        print("メールが正常に送信されました。")
    else:
        print("メールの送信に失敗しました。ログを確認してください。")


 # ? 1 email_sender = EmailSender()
 # ? 2 email_sender.create_message(subject, recipient)
 # ? 3 email_sender.add_text_content(text_content)
 # ? 4 email_sender.send()
    
       
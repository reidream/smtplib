# EmailSender

EmailSender は、Python で簡単にメールを送信するためのライブラリです。SMTP を使用してメールを送信し、テキストコンテンツ、HTML コンテンツ、添付ファイルをサポートしています。

## 特徴

- 簡単な設定と使用方法
- テキストと HTML の両方のコンテンツをサポート
- ファイル添付機能
- 柔軟な設定ファイルの使用

## インストール

このライブラリは現在、直接ソースコードとして提供されています。プロジェクトディレクトリに`email_sender.py`ファイルをコピーしてください。

## 設定

1. `smtpconfig`ディレクトリを作成し、その中に設定ファイルを作成します（例：`smtpconfig_1.py`）。
2. 設定ファイルに以下の形式で SMTP 設定を記述します：

```python
SMTP_CONFIG_1 = {
    "smtp_server": "smtp.example.com",
    "port": 587,
    "sender_email": "your_email@example.com",
    "password": "your_password"
}
```

## 使用方法

基本的な使用方法は以下の通りです：

```python
from email_sender import EmailSender

# EmailSenderのインスタンスを作成
email_sender = EmailSender()

# メッセージの作成
email_sender.create_message("件名", "recipient@example.com")

# テキスト本文の追加
email_sender.add_text_content("これはテストメールです。")

# HTMLコンテンツの追加（オプション）
email_sender.add_html_content("<html><body><h1>テストメール</h1></body></html>")

# 添付ファイルの追加（オプション）
email_sender.add_attachment("/path/to/file.pdf")

# メールの送信
if email_sender.send():
    print("メールが正常に送信されました。")
else:
    print("メールの送信に失敗しました。")
```

## 注意事項

- SMTP 設定にはセキュリティ上の機密情報が含まれるため、設定ファイルを適切に保護してください。
- 大量のメール送信を行う場合は、SMTP サーバーの制限に注意してください。
- 添付ファイルのサイズ制限に注意してください。

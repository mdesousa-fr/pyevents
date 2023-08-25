def send_email(to: str, subject: str, body: str):
    email = "\n".join(
        [
            "From: MailBot",
            f"To: {to}",
            f"Subject: {subject}",
            f"Body: {body}",
        ]
    )
    print(email)

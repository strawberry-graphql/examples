from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from typing import Optional

from reddit import settings
from reddit.tasks import celery

__all__ = ("send_mail",)


@celery.task(name="send_email")
def send_mail(
    recipient: str, subject: str, content: str, html_content: Optional[str] = None
) -> None:
    """
    Sends a multipart email to the provided recipient.
    """
    message = MIMEMultipart()
    message["From"] = settings.MAIL_SENDER
    message["To"] = recipient
    message["Subject"] = subject

    plain_text = MIMEText(content)
    message.attach(plain_text)

    if html_content is not None:
        html_text = MIMEText(html_content, "html")
        message.attach(html_text)

    server = SMTP(host=settings.MAIL_HOST, port=settings.MAIL_PORT)
    server.login(user=settings.MAIL_USERNAME, password=settings.MAIL_PASSWORD)
    server.starttls()
    server.send_message(message)
    server.quit()

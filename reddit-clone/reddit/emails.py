from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from aiosmtplib import send

from reddit.settings import (
    MAIL_SENDER,
    MAIL_USERNAME,
    MAIL_PASSWORD,
    MAIL_HOST,
    MAIL_PORT,
)


async def send_message(
    recipient: str, subject: str, content: str, html_content: Optional[str] = None
) -> None:
    """
    Sends a multipart email to the provided
    recipient asynchronously.
    """
    message = MIMEMultipart()
    message["From"] = None
    message["To"] = recipient
    message["Subject"] = subject

    plain_text = MIMEText(content)
    message.attach(plain_text)

    if html_content is not None:
        html_text = MIMEText(html_content, "html")
        message.attach(html_text)

    await send(
        message=message,
        sender=MAIL_SENDER,
        username=MAIL_USERNAME,
        password=MAIL_PASSWORD,
        hostname=MAIL_HOST,
        port=MAIL_PORT,
    )

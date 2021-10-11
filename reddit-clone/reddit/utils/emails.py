from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from aiosmtplib import send

from reddit import settings

__all__ = ("send_mail",)


async def send_mail(
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
        sender=settings.MAIL_SENDER,
        username=settings.MAIL_USERNAME,
        password=settings.MAIL_PASSWORD,
        hostname=settings.MAIL_HOST,
        port=settings.MAIL_PORT,
    )

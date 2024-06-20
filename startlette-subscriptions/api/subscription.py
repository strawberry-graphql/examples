from strawberry.tools import create_type

from .subscriptions.latest_crypto_price import latest_crypto_price
from .subscriptions.get_job_status import get_job_status

Subscription = create_type(
    "Subscription",
    [
        latest_crypto_price,
        get_job_status,
    ],
)

from strawberry.tools import create_type

from .subscriptions.latest_crypto_price import latest_crypto_price

Subscription = create_type(
    "Subscription",
    [
        latest_crypto_price,
    ],
)

# -*- coding: utf-8 -*-

from dataclasses import dataclass

from broadcaster import Broadcast
from django.db import connection

broadcast = None


async def get_broadcast():
    global broadcast

    if not broadcast:
        dbinfo = connection.settings_dict
        if dbinfo.get("ENGINE") == "django.db.backends.postgresql":
            host = (
                f"{dbinfo.get('HOST')}:{dbinfo.get('PORT')}"
                if dbinfo.get("PORT")
                else dbinfo.get("HOST")
            )
            dsnstr = f"postgresql://{dbinfo.get('USER')}:{dbinfo.get('PASSWORD')}@{host}/{dbinfo.get('NAME')}"
            broadcast = Broadcast(dsnstr)
        else:
            broadcast = Broadcast("memory://")

        await broadcast.connect()

    return broadcast


@dataclass
class Context:
    broadcast: Broadcast

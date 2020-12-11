# -*- coding: utf-8 -*-

# standard library
from datetime import datetime
from http import HTTPStatus
import logging
import pytz
import uuid
import sys

def set_timezone():
    tz = pytz.timezone('America/Mexico_City')
    ct = datetime.now(tz=tz)
    return int(datetime.timestamp(ct))

def date():
    fecha = datetime.fromtimestamp(set_timezone())
    return fecha

def generateNonceStr():
    id = uuid.uuid1()
    return id.hex
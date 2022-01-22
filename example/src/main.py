import sys
import logging
logging.basicConfig(encoding="utf-8", stream=sys.stdout, level=logging.DEBUG)

import os

from dotenv import load_dotenv
load_dotenv()

from cry_vs.client import Client

client = Client(key=os.environ["KEY"])


@Client.listen
async def on_ready():
    print("logged in")


@Client.listen
async def any_event():
    print("an event has been called")


print("Logging in...")
client.login()

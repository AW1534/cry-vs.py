import sys
import logging

logging.basicConfig(encoding="utf-8", stream=sys.stdout, level=logging.INFO)

import os

from dotenv import load_dotenv

load_dotenv()

from cry_vs.client import Client

client = Client()


@client.listen
async def on_ready():
    print("logged in")

@client.listen
async def on_token_refresh():
    print("token has been refreshed")


@client.listen
async def any_event():
    print("an event has been called")


print("Logging in...")
client.login(os.environ["KEY"])

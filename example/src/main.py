import logging
import os
import sys

logging.basicConfig(encoding="utf-8", stream=sys.stdout, level=logging.DEBUG)

from dotenv import load_dotenv

from cry_vs.client import Client

load_dotenv()
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
client.login(os.getenv("KEY"))

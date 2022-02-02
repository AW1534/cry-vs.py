import logging
import sys

logging.basicConfig(encoding="utf-8", stream=sys.stdout, level=logging.DEBUG)

from dotenv import load_dotenv

from cry_vs.client import Client

load_dotenv()
cry = Client()


@cry.listen
async def on_ready():
    print("logged in")


@cry.listen
async def on_token_refresh():
    print("token has been refreshed")


@cry.listen
async def any_event():
    print("an event has been called")


print("Logging in...")
cry.login("new_username", "new_password")

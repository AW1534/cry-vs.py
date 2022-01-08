import json

from .emitter import Emitter
from .HTTPHelper import http


class Client:
    funcs = []

    def listen(func):
        Client.funcs.append(func)

    def login(self, key, server="https://cry-vs.herokuapp.com", allowUnsecure=False):
        server = server
        if not server.lower().startswith("https://cry-vs.herokuapp.com") and not server.lower().startswith("https://beta-cry-vs.herokuapp.com"):
            print("This is not an official Crypto Versus server. Please proceed with caution")

        if server.lower().startswith("https://beta-cry-vs.herokuapp.com"):
            print(
                "This is the domain for the beta branch. Please switch to the main branch 'https://cry-vs.herokuapp.com' if you don't know what you're doing.")

        if server.lower().startswith("http://") and allowUnsecure == False:
            print(
                f"{server} could not be loaded as it is http. please change it to https or set allowUnsecure to True in the function parameters.")
            return

        r = http.sendRequest(
            method=http.methods.POST,
            url=server + "/login",
            data=json.dumps({
                "key": key
            })
        )

        emitter = Emitter(funcs=self.funcs, expire=r.headers["Expire"])
        emitter.enqueue(name="on_ready")
        emitter.queue()  # runs the event loop. this is an infinite function so anything that needs to be done should be done before this

    def end():
        exit(0)
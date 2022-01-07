import json

from .emitter import Emitter
from .HTTPHelper import http


class Client:
    server = "https://cry-vs.herokuapp.com"
    funcs = []

    def listen(func):
        Client.funcs.append(func)

    def login(self, key, allowUnsecure = False):


        server = Client.server
        if server.lower().startswith("http://") and allowUnsecure == False:
            print(f"{server} could not be loaded as it is http. please change it to https or set alowUnsecure to True in the function paramaters.")
            return

        r = http.sendRequest (
            method=http.methods.POST,
            url=server + "/login",
            data=json.dumps({
                "key": key
            })
        )


        emitter = Emitter(funcs=self.funcs, expire=r.headers["Expire"])
        emitter.enqueue(name="on_ready")
        emitter.queue()

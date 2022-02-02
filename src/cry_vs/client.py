import datetime
import logging
import secrets

import cry_vs.emitter
from . import exceptions

logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    for handler in logging.getLogger().handlers:
        logger.addHandler(handler)

import json
from .HTTPHelper import Socket


class Client:
    class _Auth:
        class _Token:
            text: str = None
            time: datetime.datetime = None

            def __init__(self, text: str, time: int):
                self.text = text
                self.time = datetime.timedelta(milliseconds=time) + datetime.datetime.now()

            def __str__(self):
                return self.text

            def _update(self, text: str, time: int):
                self.text = text
                self.time = datetime.timedelta(milliseconds=time) + datetime.datetime.now()

        token: _Token = None

    _self = None
    host: str = None
    allowUnsecure: bool = None
    keep_alive: bool = None

    auth: _Auth = _Auth()
    token: auth._Token = None

    def __init__(self, host="https://cry-vs.herokuapp.com", port=80, allow_unsecure=False, keep_alive=True):
        self.emitter = None
        self.socket = Socket(host=host, port=port, client=self)
        from .emitter import Emitter
        self.Emitter = Emitter
        self.host = host
        self.allowUnsecure = allow_unsecure
        self.keep_alive = keep_alive
        self.funcs.append(self.before_expire)
        logging.info("Client created")

    funcs = []
    this = ""

    def listen(self, func):
        self.funcs.append(func)

    def login(self, *args):
        server = self.host

        if not server.lower().startswith("https://cry-vs.herokuapp.com") and not server.lower().startswith(
                "https://beta-cry-vs.herokuapp.com"):
            logger.warning("This is not an official Crypto Versus host. Please proceed with caution")

        if server.lower().startswith("https://beta-cry-vs.herokuapp.com"):
            logger.warning(
                "This is the domain for the beta branch. Please switch to the main branch 'https://cry-vs.herokuapp.com' if you don't know what you're doing."
            )

        if server.lower().startswith("http://") and self.allowUnsecure is False:
            logger.critical(
                f"{server} could not be loaded as it is http. please change it to https or set allowUnsecure to True in the class parameters.")
            return

        def finish(r):
            logger.debug(self.funcs)
            self.auth.token = self._Auth._Token(r.text, int(r.headers["Expire"]))
            self.emitter = self.Emitter(funcs=self.funcs, client=self)
            self.emitter.enqueue(name="on_ready", args=r.headers["Expire"])

            try:    # test if the 3rd argument has been passed
                if args[2] == False:
                    logger.info(
                        "You have disabled the event loop. This means that you will not be able to use the client until you call the Client.emitter.queue() function, but the client will still work.")
                elif args[2] == True:
                    try:
                        self.emitter.queue()  # runs the event loop. this is an infinite function so anything that needs to be done should be done before this
                    except KeyboardInterrupt:
                        logger.info("KeyboardInterrupt")

            except IndexError:  # if the 3rd argument is not passed, default to True and start the event loop
                try:
                    self.emitter.queue()  # runs the event loop. this is an infinite function so anything that needs to be done should be done before this
                except KeyboardInterrupt:
                    logger.info("KeyboardInterrupt")

        if len(args) == 0:
            logger.critical("No auth data provided. please provide a username and password, or an API token")
        elif len(args) == 1:
            logger.info("using API key")
            r = self.socket.Send_Request(
                method=self.socket.Methods.POST,
                url=server + "/api/login",
                data=json.dumps({
                    "key": args[0]
                })
            )
            if r.status_code == 401:
                raise exceptions.AuthFailed("Invalid credentials. the server returned 401")
            else:
                finish(r)
        elif len(args) == 2:
            logger.info("using username and password")
            r = self.socket.Send_Request(
                method=self.socket.Methods.POST,
                url=server + "/api/login",
                data=json.dumps({
                    "username": args[0],
                    "password": args[1]
                })
            )
            if r.status_code == 401:
                raise exceptions.AuthFailed("Invalid credentials. the server returned 401")
            else:
                finish(r)

    async def before_expire(self):
        r = self.socket.Send_Request(
            method=self.socket.Methods.POST,
            url=self.host + "/api/refresh-token",
            data=json.dumps({
                "token": self.auth.token.text
            })
        )
        self.auth.token._update(r.text, int(r.headers["Expire"]))
        self.emitter.enqueue(name="on_token_refresh", args=r.headers["Expire"])
        logger.info("Token refreshed")

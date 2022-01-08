from cry_vs.client import Client


@Client.listen
def on_ready():
    print("ready")

@Client.listen
def any_event():
    print("an event has been called")

Client.login(server="https://cry-vs.herokuapp.com", self=Client, key="Gtn80t9qfA4SALYON9xSr4LChNS8JAiu")
# cry-vs
An official API wrapper for [Crypto_Versus](https://github.com/ProtagonistsWasTaken/crypto_versus)

## Installation
Installation is simple. just run `$ python -m pip install cry_vs.py` in your terminal.

## Usage
```{note} 
This package is used in a way similar to [discord.py](https://pypi.org/project/discord.py/). if you know how to use discord.py, the following steps should be a cakewalk.
```

---
### Initialization & logger setup
First set up the logging module. this is not necessary because cry_vs will try to set up the logging module for you, but is highly recommended.
```python
import logging, sys
logging.basicConfig(encoding="utf-8", stream=sys.stdout, level=logging.INFO)
```

Next, import cry_vs's client class.

```python
from cry_vs.client import Client
```

Once you have done that, you can create a client.

```python
cry = Client()
```

while there are no required arguments, you can also pass in the other arguments.

| **Name**           | **Type** | **Default value**      | **Description**                                                             |
|--------------------|----------|------------------------|-----------------------------------------------------------------------------|
| **host**           | string   | "cry-vs.herokuapp.com" | The url of the server you want to connect to.                               |
| **port**           | int      | 80                     | The port that the socket should listen to.                                  |
| **allow_unsecure** | bool     | False                  | Whether to allow unsecure connections.                                      |
| **keep_alive**     | bool     | True                   | Whether to keep the client validated by automatically refreshing the token. |


---
### events
Now that you have a client, you can start listening to events. to do so, just make a function with the `@cry.listen` decorator.

for example, if you want to listen to the `on_ready` event, you would do the following:
```python
@cry.listen
async def on_ready():
    print("on_ready has been called")
```

you can add as many events as you want, and they depend on the name. (function must be asynchronous)

| **Name**         | **Description**                                                                    |
|------------------|------------------------------------------------------------------------------------|
| any_event        | Fired when any event is called                                                     |                                                                                    |
| on_ready         | Fired when the event emitter is initialized (right after the client has logged in) |
| on_token_refresh | Fired after the token has been refreshed                                           |

---
### finalize
finally, you can call `cry.login()` to start the client.

````{tabbed} API Key
```python
cry.login("key")
```
````

````{tabbed} Username and Password
```python
cry.login("username", "password")
```
````
```{warning}
this will start the event loop, and will not return until the client is closed. any logic that needs to be done after this function should be done in the `on_ready` event.
```

<!-- footer gets added here for pypi version in setup.py-->
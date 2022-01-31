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
<details>
<summary>Other arguments that Client accepts</summary>
<ul>
    <li> <code>host: string = "cry-vs.herokuapp.com"</code> the url of the server you want to connect to. </li>
    <li> <code>port: int = 80</code> the port that the socket should listen to.</li>
    <li> <code>allow_unsecure: bool = False</code> whether to allow unsecure connections.</li>
    <li> <code>keep_alive: bool = True</code> whether to keep the client validated by automatically refreshing the token</li>
</ul>
</details>

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
<details>
<summary>All events</summary>
<ul>
    <li> <code>any_event()</code> fired when any event is called</li>
    <li> <code>on_ready()</code> fired when the event emitter is initialized (right after the client has logged in) </li>
    <li> <code>on_token_refresh()</code> fired after the token has been refreshed</li>
</ul>
</details>

---
### finalize
finally, you can call `cry.login()` to start the client. 

this will start the event loop, and will not return until the client is closed. any logic that needs to be done after the client has been started should be done in the `on_ready` event.

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

<!-- footer gets added here for pypi version in setup.py-->
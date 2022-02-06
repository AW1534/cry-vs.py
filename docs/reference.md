# API reference
*An official API wrapper for [Crypto_Versus](https://github.com/ProtagonistsWasTaken/crypto_versus)*

*this section is under construction, and isn't very good yet*

```{seealso}
If you are looking for the docs of the HTTP API, visit the [crypto-versus github page](https://github.com/ProtagonistsWasTaken/crypto_versus#readme)
```


```{note}
this guide will assume you have made a [`Client`](#Client) instance called `cry`
```

## Client

### Constructor parameters
| **Name**           | **Type** | **Default value**      | **Description**                                                             |
|--------------------|----------|------------------------|-----------------------------------------------------------------------------|
| **host**           | string   | "cry-vs.herokuapp.com" | The url of the server you want to connect to.                               |
| **port**           | int      | 80                     | The port that the socket should listen to.                                  |
| **allow_unsecure** | bool     | False                  | Whether to allow unsecure connections.                                      |
| **keep_alive**     | bool     | True                   | Whether to keep the client validated by automatically refreshing the token. |

### Exposed methods

| **Name**               | **Parameters**                          | **Returns**                 | **Login required** | **Description**                                                                                                                                  |
|------------------------|-----------------------------------------|-----------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **cry.listen**      | N/A                                     | N/A                         | No                 | Should be used as a decorator. registers the function as an [event handler](#events).                                                            |
| **cry.login**       | `username`, `password` *or* `API token` | N/A                         | No                 | Authenticates the client. this will also start the event loop so any code that needs to be done before this should be done in the on_ready event |
| **cry.game.action** | N/A                                     | JSON (HTTP response object) | Yes                | call the `/api/v0/dostuff` endpoint. that endpoint is temporary and so is this method.                                                           |

### Exposed variables
*coming soon™*



## events
to create an event handler, just use the `@cry.listen` decorator. The client will automatically call the handler based on the function name.
| **Name**             | **Description**                                                                    |
|----------------------|------------------------------------------------------------------------------------|
| **any_event**        | Fired when any event is called                                                     |                                                                                    |
| **on_ready**         | Fired when the event emitter is initialized (right after the client has logged in) |
| **on_token_refresh** | Fired after the token has been refreshed                                           |

## login parameters
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
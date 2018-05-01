# Walabot-WebSocketServer

Simple framework for Creating a Walabot application using Web Socket protocol.<br>


***Using the code***

**NewWalabotAppTemplate**

This Walabot new App template based on [Walabot API Beta](http://api.beta.walabot.com/_sample.html) Code Examples.


Create your own app based on the following explanations:

Code Sample is divided into 7 steps:
1) Connect
2) Configure
3) Start
4) Calibrate
5) Trigger
6) Get action
7) Stop/Disconnect

This template is designed to connect the app you've created to a web server

which need to meet some of the basic requirements listed below.


**Client Handler**

This class contains a asynchronous function to handle with client requirements.

This client handler is with a strong bond to NewWalabotAppTemplate.py requirements.

Basic functions that must be:
```python
start()
get_data()
stop()
```
Feel free to add your uwn function just note that you also support client-side commands.

The information is transmitted in json.

The protocol: ```{"Command": "", "Message": "", Params":[data]}```

Two examples are attached : **Breathing** and **Tracker**

Follow **TODO** to add a new Walabot project.

**Server**

The server requires  a Handler.

For example: 

```pyhton
from server import WebServer
from client_handler import WalabotHandler

handler =WalabotHandler()

s = WebServer(port=8888, handler=handler.commandsHandler)
s.start()
```


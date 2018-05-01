
'''
This is a asynchronous function to handle with client requirements.


This client handler is with a strong bond to NewWalabotAppTemplate.py requirements.

Basic functions that must be:
start()
get_data()
stop()

Feel free to add your uwn function just note that you also support client-side commands.

The information is transmitted in json.

The protocol: {"Command": "", "Message": "", Params":[data]}

Two examples are attached : Breathing and Tracker

Follow TODO to add a new project
'''

import asyncio
import websockets
import json
import socket
from imp import load_source
import WalabotBreathing as breathing
import WalabotTracker as tracker


#####################################
# TODO import WalabotMyApp as my_app
#####################################

class WalabotHandler:

    def __init__(self):
        self.initialize = False
        self.stop = False


    async def commandsHandler(self ,client,path):
        app = None
        try:
            print("Client connected..")
            print(str(self.stop))
            while not self.stop:
                data = json.loads(await client.recv())
                command = data['Command']
                if command == 'BREATHING':
                    print(command)
                    app = breathing
                elif command == "TRACKER":
                    print(command)
                    app = tracker
                ############################ ADD YOUR APP HERE  ##################################
                # TODO elif command == "MY_APP":
                #         print(command)
                #         app = my_app
                ##################################################################################

                if not self.initialize:
                    self.initialize = True
                    app.start()

                elif command == 'STOP':
                    print(command)
                    app.stop()
                    self.initialize=False
                    await client.send(json.dumps({"Command": "EXIT"}))
                elif command == 'DATA':
                    try:
                        if self.initialize:
                            data = app.get_data()
                            res = {"Command": "DATA", "Params":[data] , "Message": ""}
                            await client.send(json.dumps(res))
                        else:
                            await client.send(json.dumps({"Command": "EXIT","Message": "App not initialized"}))
                    except:
                        res = {"Command": "ERROR", "Message": "App is NOT defined"}
                        await client.send(json.dumps(res))
                else:
                    res = {"Command": "ERROR", "Message": "Unknown Command"}
                    await client.send(json.dumps(res))
        except Exception as e:
               print("Connection problem" + str(e))
               res = {"Command": "ERROR", "Message": str(e)}
               await client.send(json.dumps(res))


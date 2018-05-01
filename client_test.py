import asyncio
import websockets
import json
import time

from sys import platform
from os import system

HOST = '192.168.100.114'

async def handler():
    try:
        stop = 0
        async with websockets.connect('ws://'+HOST+':8888') as websocket:
            data ={"Command":"BREATHING", "Params":[],"Message":""}
            await websocket.send(json.dumps(data))
            print("> {}".format(data))
            time.sleep(0.3)
            while stop < 15:
                data = {"Command": "DATA", "Params": [], "Message": ""}
                await websocket.send(json.dumps(data))
                time.sleep(0.3)
                rec = json.loads(await websocket.recv())
                if rec['Command'] =='EXIT':
                    stop = True
                if rec['Command'] == 'ERROR':
                    stop = True
                    print("< {}".format(rec['Message']))
                print("< {}".format(rec))
                stop +=1
            data = {"Command": "STOP", "Params": [], "Message": ""}
            await websocket.send(json.dumps(data))
            rec = await websocket.recv()
            print("< {}".format(rec))
            # data = {"Command": "STOP", "Params": [], "Message": "Bla Bla Bla"}
            # await websocket.send(json.dumps(data))


    except Exception as e:
        print("Connection problem" + str(e))


asyncio.get_event_loop().run_until_complete(handler())

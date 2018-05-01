import asyncio
import websockets
import json
import socket
import threading

SERVER_PORT = 4455
'''
Simple Web server

If the IP is not set, then the server automatically finds and uses the current IP

'''
class WebServer:

    def __init__(self,handler,ip = None,port = None):
        self.ip = ip or self.get_ip()
        self.port = port or SERVER_PORT
        self.handler = handler


    def start(self):

        try:
            start_server = websockets.serve(self.handler, self.ip, self.port)

            print("Listening on: " + str(self.ip) + " Port: " + str(self.port))
            t = threading.Thread(target=self.run(start_server))
            t.start()
            # asyncio.get_event_loop().run_until_complete(start_server)
            asyncio.get_event_loop().run_forever()

        except ValueError:
            print("handler miss")
            
    def run(self, start_server):
        asyncio.get_event_loop().run_until_complete(start_server)
        # asyncio.get_event_loop().run_forever()
    def stop(self):
        asyncio.get_event_loop().close()
    def get_ip(selfe):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

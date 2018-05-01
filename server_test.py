from server import WebServer
from client_handler import WalabotHandler

handler =WalabotHandler()

s = WebServer(port=8888, handler=handler.commandsHandler)
s.start()
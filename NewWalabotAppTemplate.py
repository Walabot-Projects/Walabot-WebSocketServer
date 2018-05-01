'''

This Walabot new App template based on 'Walabot API Beta' Code Examples.

http://api.beta.walabot.com/_sample.html

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


'''


from __future__ import print_function  # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join

# import WalabotAPI.py
if platform == 'win32':
    modulePath = join('C:/', 'Program Files', 'Walabot', 'WalabotSDK',
                      'python', 'WalabotAPI.py')
elif platform.startswith('linux'):
    modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')
wlbt = load_source('WalabotAPI', modulePath)

wlbt.Init()

def start():
    # Initializes walabot lib

    # 1) Connect : Establish communication with walabot.

    # 2) Configure: Set scan profile and arena

    # 3) Start: Start the system in preparation for scanning.

def get_data():
    # 4) Trigger: Scan (sense) according to profile and record signals to be
    # available for processing and retrieval.

    # 5) Trigger: Scan(sense) according to profile and record signals
    # to be available for processing and retrieval.

    # 6) Get action: retrieve the last completed triggered recording

    #Return your data to client
    return

def stop():

    # 7) Stop and Disconnect.
    # wlbt.Stop()
    # wlbt.Disconnect()
    # wlbt.Clean()
    # print('Terminate successfully')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # TESTS # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    start()
    print(get_data())
    stop()
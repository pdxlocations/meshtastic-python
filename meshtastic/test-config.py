import meshtastic.serial_interface
import time


interface = meshtastic.serial_interface.SerialInterface()

interface.nodeConfigure("prefs.yaml")

while True:
    time.sleep(0.1)

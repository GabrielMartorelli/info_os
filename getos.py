import platform
import getpass
from datetime import datetime
from getmac import get_mac_address as gma

print("Computer information")
print("")
print("Computer name: ", platform.node())
print("Archetecture: ", platform.architecture())
print("Running OS:", platform.system())
print("OS version: ", platform.release())
print("Processor: ", platform.processor())
print("Username: ", getpass.getuser())
print("MAC address: ", gma())

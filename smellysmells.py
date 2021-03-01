import os
import time

while(True):
  thing = input("Enter Name (then hit enter): ")
  if (thing == ""):
    break
  else:
    print(thing, " smeels")
    print("please wait...")
    time.sleep(5)
    os.system("curl parrot.live")
    # exec("cmd curl parrot.live")
    break
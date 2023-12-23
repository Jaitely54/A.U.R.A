# System Control Script
This Python script prompts the user to decide whether to reboot or shut down the system based on user input. The script uses the os module to execute the respective system command.

## Import Statement
```python

import os
```
## User Prompt Script
```python

reboot_1 = ["reboot the system", "reboot the laptop", "reboot system", "shutdown the laptop",
             "shutdown the system", "shutdown system", "restart the laptop", "restart the system", "restart system",
             "shutdown the pc", "restart the pc", "reboot the pc"]

for promt in reboot_1:
    print("\n")
    print('Do you wish to reboot the pc or shut it down?\n')
    n = input("Press 1 for reboot, Press 2 for shutdown, press any other key for canceling the process:")
    print("\n")

    if n == "1":
        print("Restarting the pc\n")
        os.system("shutdown /r /t 1")

    elif n == "2":
        print("Shutting down the pc\n")
        os.system("shutdown /s /t 1")

    else:
        print("No rebooting/shutdown will be performed\n")
        break

print("Function will be working properly\n")
```
##  License
This project is licensed under the MIT License

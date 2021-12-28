#!/usr/bin/python3

import time
from sys import argv
from functools import partial
import configManager, IPHelper, gmail

config = configManager.loadConfig("/etc/AutoIP/config.json")

print = partial(print, flush=True)

def checkArgv():
    for a in argv:
        if a == "-t":
            config.startAfter = 0
            config.waitToCheck = 0
        elif a == "-n":
            global getNewIp
            getNewIp = True

getNewIp = False
def GetIPV4Retry():
    global getNewIp
    if getNewIp:
        ip = "refreshPls!"
        getNewIp = False
    else:
        ip = IPHelper.GetIPV4()
    while ip == "error":
        print(f"Can't get ip, retry in {config.errorRetry}.")
        time.sleep(config.errorRetry)
        ip = IPHelper.GetIPV4()
    return ip

if __name__ == "__main__":
    print("AutoIP v1.2")
    checkArgv()
    configManager.printConfig(config)
    print(f"First run script. Trying get ipv4 after {config.startAfter} seconds.")
    time.sleep(config.startAfter)
    ip = GetIPV4Retry()
    print(f"Got ipv4: {ip}. First launch script will send email to your.")
    gmail.SendGmail(config.mailSubject, f"[Script first launch]\nip: {ip}")
    print(f"Wait {config.waitToCheck} seconds to check ip status")
    time.sleep(config.waitToCheck)
    while True:
        print("Now check ip status..")
        newIp = GetIPV4Retry()
        if ip != newIp:
            print("Ip changed, now sending gmail.")
            gmail.SendGmail(config.mailSubject, f"Old ip: {ip}\nNew ip: {newIp}")
            ip = newIp
            print("Gmail sended.")
        else:
            print("Ip status normal.")
        print(f"Now wait {config.waitToCheck} seconds again..")
        time.sleep(config.waitToCheck)
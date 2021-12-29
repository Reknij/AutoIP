import os, json
from sys import stdout
from configModule.myconfig import *

CONFIG_PATH = "/etc/AutoIP/config.json"

def __jsonToConfig(d):
    return config(d['startAfter'],d['waitToCheck'],d['errorRetry'],d['mailSubject'],d['sender'],d['senderPass'],d['receiver'])

def __loadConfig()->config:
    with open(CONFIG_PATH) as f:
        return __jsonToConfig(json.load(f))

globalConfig:config = __loadConfig()

def getConfig()->config:
    return globalConfig

def printConfig(config):
    print("=========================")
    print("[Config]")
    print(f"Start after seconds: {config.startAfter}")
    print(f"Wait to check seconds: {config.waitToCheck}")
    print(f"Error retry seconds: {config.errorRetry}")
    print(f"Email subject: {config.mailSubject}")
    print(f"Email sender: {config.sender}")
    print(f"Password sender: {config.senderPass}")
    print(f"Email receiver: {config.receiver}")
    print("=========================")
    stdout.flush()
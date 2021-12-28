import os, json
from sys import stdout

globalConfig = None

class config(object):
    def __init__(self, a,b,c,d,e,f,g):
        self.startAfter = a
        self.waitToCheck = b
        self.errorRetry = c
        self.mailSubject = d
        self.sender = e
        self.senderPass = f
        self.receiver = g

def jsonToConfig(d):
    return config(d['startAfter'],d['waitToCheck'],d['errorRetry'],d['mailSubject'],d['sender'],d['senderPass'],d['receiver'])

def loadConfig(configFile)->config:
    with open(configFile) as f:
        global globalConfig
        globalConfig = json.load(f, object_hook=jsonToConfig)
        return globalConfig

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
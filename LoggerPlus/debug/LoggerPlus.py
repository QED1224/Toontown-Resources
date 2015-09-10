import inspect
import json

from direct.showbase.DirectObject import DirectObject
from panda3d.core import *

class LoggerPlus(DirectObject):
    """
    A simple logging utility for Toontown.
    """
    def __init__(self):
        self.accept("suite updated", self.getSuiteInfo)
        self.jsonFile = Filename("config", "debugging.json").toOsSpecific()
        self.suite = None
        self.modules = []
        self.methods = []
        self.getSuiteInfo()

    def getSuiteInfo(self):
        """
        Get suite information based on the data in debugging.json.
        """
        self.suite = ConfigVariableString("suite", "").getValue()
        if not self.suite:
            return

        with open(self.jsonFile) as data:
            try:
                jData = json.load(data)
                self.modules = jData[self.suite].keys()
                self.methods = sum(jData[self.suite].values(), [])
            except (KeyError, ValueError) as e:
                print("LoggerPlus Error: " + e.message)
                self.suite = None

    def log(self, msg, whisper=False, whisperOnly=False, suites=[]):
        """
        Print msg to the specified output location(s).

        Args:
            msg (str): The message to send.
            whisper (bool, optional): msg is sent as a whisper.
            whisperOnly (bool, optional): msg is only sent as a whisper.
            suites (list, optional): A list of debug suites to be used.
        """
        stack = inspect.stack()
        method = stack[1][3]

        if not self.suite:
            return
        if self.methods and method not in self.methods:
            return
        if suites and self.suite not in suites:
            return

        module = inspect.getmodule(stack[1][0]).__name__.split(".")[-1]
        if not whisperOnly:
            text = ":{0}(LP): {1}".format(module, msg)
            filename = ConfigVariableFilename("output-file", "").getValue()
            if filename:
                with open(filename.toOsSpecific(), "a") as output:
                    output.write(text + "\n")
            print(text)

        whisper = whisperOnly if whisperOnly else whisper
        if whisper and module in self.modules:
            from otp.avatar.DistributedPlayerAI import system
            system(msg)

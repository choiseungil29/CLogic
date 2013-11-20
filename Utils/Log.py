#!/usr/bin/python
# -*- coding: cp949 -*-

from Utils.Singleton import Singleton

import sys
import os
import datetime


@Singleton
class Logger(object):
    logFile = None

    def __init__(self):
        self.logFile = open("Log.txt", 'a')
        self.logFile.write(str(datetime.datetime.now()) + '\n')
        self.logFile.close()

    def Info(self, comment):
        self.writeLog('Info', comment)

    def Warn(self, comment):
        self.writeLog('Warn', comment)

    def Error(self, comment):
        self.writeLog('Error', comment)

    def writeLog(self, level, comment):
        self.logFile = open("Log.txt", 'a')
        self.logFile.write(level + ': ' + comment + '\n')
        self.logFile.close()
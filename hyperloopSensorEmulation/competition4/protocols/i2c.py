import numpy as np
import csv
import logging
import math

from lines.SerialData import SerialData
from lines.SerialClock import SerialClock

#import sys
#sys.path.append("")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class i2c:
    def __init__(self):
        self.pin = 1
        self.sda = SerialData()
        self.scl = SerialClock()
        self.clockSpeed = 100 #Bitrate
        self.address = '1100000'
        self.sda.setHigh()


    def setStartCondition(self):
        self.sda.setLow()

    def setEndCondition(self):
        self.sda.setHigh

    def setAddress(self,sevenBitAddress):
        self.address = sevenBitAddress

    def setClockSpeed(self, speed):
        self.clockSpeed = speed

    def write(self, inputMessage):
        self.message = inputMessege
        sizeOf = len(inputMessage)

    def read(self):
        self.write(self.sda.setLow())

    def beginTransmission(self):
        listOutput[2][] = 0
        return listOutput


    

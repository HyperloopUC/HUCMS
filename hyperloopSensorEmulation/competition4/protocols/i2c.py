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
        self.speed = 100 #Bitrate
        self.address = '1100000'
        

    def read(self):
        #will do in a bit

    def write(self, inputMessege):
        self.message = inputMessege

    def setStartCondition(self):
        self.sda.setLow

    def setEndCondition(self):
        self.sda.setHigh

    def setAddress(self,sevenBitAddress):
        self.address = sevenBitAddress

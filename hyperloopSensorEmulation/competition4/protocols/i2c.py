import csv
import logging
import math

from lines.SerialData import SerialData
from lines.SerialClock import SerialClock

#import sys
#sys.path.append("")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#For reference: https://en.wikipedia.org/wiki/Synchronous_Serial_Interface
class i2c:
    def __init__(self):
        self.sda = SerialClock()
        self.scl = SerialData()

    def read(self):
        #will do in a bit

    def write(self, inputMessege):
        self.message = inputMessege

    def setStartCondition(self, startCondition):
        self.startCondition = startCondition

    def setEndCondition(self, endCondition):
        self.endCondition = endCondition

    def setAddress(self,sevenBitAddress):
        self.address = sevenBitAddress
        

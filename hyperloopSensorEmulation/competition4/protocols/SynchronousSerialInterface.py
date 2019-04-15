import csv
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


#For reference: https://en.wikipedia.org/wiki/Synchronous_Serial_Interface
class SynchronousSerialInterface:
    def __init__(self,clockSignalPeriod,pauseTime,monoflopTime, mostSignificantBit, leastSignificantBit):
        self.clockSignalPeriod = clockSignalPeriod
        self.pauseTime = pauseTime
        self.monoflopTime = monoflopTime
        self.mostSignificantBit = mostSignificantBit
        self.leastSignificantBit = leastSignificantBit

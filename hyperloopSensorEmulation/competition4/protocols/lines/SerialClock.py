import csv
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import BusLine
#Find out how to get a binary file onto then FPGA
class SerialClock:
    def __init__(self):
        self.line = 1

    def setLow(self):
        self.line = 0

    def setHigh(self):
        self.line = 1

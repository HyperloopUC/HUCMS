import csv
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class SerialData:
    def __init__(self):
        self.line = 1

    def setLow(self):
        self.line = 0
        
    def setHigh(self):
        self.line = 1

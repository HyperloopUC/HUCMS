import csv
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class BusLine:
    def __init__(self,busSpeed):
        self.busSpeed = busSpeed
        

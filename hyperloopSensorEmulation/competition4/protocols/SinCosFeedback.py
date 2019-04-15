import csv
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import BusLine

#Find out how to get a binary file onto then FPGA
class SinCosFeedback:

    def __init__(self):

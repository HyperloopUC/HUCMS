import numpy as np
import csv
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

import BusLine

#Find out how to get a binary file onto then
#Resource for SinCosFeedback: http://doc.ingeniamc.com/venus/product-manual/installation-and-configuration/motor-feedback-connections/position-feedback-interfaces/analog-encoder-sin-cos-encoder

class SinCosFeedback:

    def __init__(self):

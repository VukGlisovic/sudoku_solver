"""
Run this script with the the wanted input and get your output
"""

import numpy as np
import logging

logger = logging.getLogger()
log_format = '%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s - %(funcName)s | %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)


logger.info("Hello numpy {}".format(np.float(6)))

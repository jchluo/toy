# -*- coding: utf-8 -*-

"""
XXX library
~~~~~~~~~~~~~~~~~~~~~
how to use
usage:

   >>> print "ok" 
   ok

"""

__title__ = ''
__version__ = '1.0.0'
__author__ = 'jchluo'
#__license__ = 'Apache 2.0'
#__copyright__ = ''


#import api
from .main import main 

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

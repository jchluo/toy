# -*- coding: utf-8 -*-

"""
toy.main
~~~~~~~~~~~~~~

main module

"""

import os
import sys
import logging

log = logging.getLogger(__name__)


def main():
    """main function"""
    print "main ok"
    log.info("log main ok")


if __name__ == "__main__":
    main()

#
# Created on Thu Jun 29 2023
#
# COMPANY: CEIT
#  This document is property of CEIT. Under the copyright laws, the
#  documentation may not be copied, photocopied, reproduced, translated, or
#  reduced to any electronic medium or machine-readable form, in whole or
#  in part, without the prior written consent of CEIT.
# Copyright (c) 2023, CEIT.
#
# FILENAME: run_live.py
#
# AUTHOR:   Paul Zabalegui Landa (pzabalegui@ceit.es)
#
# EDITION HISTORY:
#   Version 0.1: Thu Jun 29 2023 - Paul Zabalegui Landa (pzabalegui@ceit.es)
#       Initial creation
#


import sys
sys.path.insert(0, '..')

from osnma.receiver.receiver import OSNMAReceiver
from osnma.receiver.input_android import ANDROIDLive

import os
from os.path import dirname, join


LOCALHOST = '127.0.0.1'


def live_android_config():
    config_dict = {
        'exec_path': os.environ["HOME"],
        'pubk_name': str(dirname(__file__)) + '/OSNMA_PublicKey.xml',
        'merkle_name': str(dirname(__file__)) + '/OSNMA_MerkleTree.xml'
    }

    # input_module = ANDROIDLive(LOCALHOST, 9000)
    input_module = ANDROIDLive('0.0.0.0', 10000)
    osnma_r = OSNMAReceiver(input_module, config_dict)

    osnma_r.start()


if __name__ == "__main__":

    print("Running using ANDROID live data.")
    live_android_config()

def main():

    print("Running using ANDROID live data.")
    live_android_config()

import argparse
import sys
sys.path.insert(0, '..')
import time

from osnma.receiver.receiver import OSNMAReceiver
from osnma.receiver.input_ubx import UBXLive


VBOX = '10.63.16.38'
LOCALHOST = '127.0.0.1'

# parser = argparse.ArgumentParser(description='Choose connection [VBOX or LOCALHOST]')
# parser.add_argument("Connection", type=str, default="LOCALHOST")

# args = parser.parse_args()


def live_ubx_config(connection: str):
    config_dict = {
        'exec_path': '.',
        'pubk_name': 'OSNMA_PublicKey.xml',
        'merkle_name': 'OSNMA_MerkleTree.xml',
        # 'kroot_name': 'OSNMA_last_KROOT.txt'
    }

    if (connection == "VBOX"):
        input_module = UBXLive(VBOX, 9000)
    elif (connection == "LOCALHOST"):
        input_module = UBXLive(LOCALHOST, 9000)

    osnma_r = OSNMAReceiver(input_module, config_dict)

    osnma_r.start()


if __name__ == "__main__":

    print("Running using UBX live data.")
    hora_actual = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"El script se ha ejecutado a las {hora_actual}.")
    live_ubx_config("VBOX")

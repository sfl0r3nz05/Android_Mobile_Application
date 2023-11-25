import socket
import time
import struct
from bitstring import BitArray
import datetime



from osnma.receiver.input import DataFormat

GAL_INAV = 1537

STATUS_PARITY_PASSED = 1
STATUS_PARITY_REBUILT = 2
STATUS_UNKNOWN = 0

BYTES_IN_PAYLOAD_LONG  = 29 + 3
BYTES_IN_PAYLOAD_SHORT = 29

GAL_GNSS_ID = 2
MAX_GAL_SATS = 36

TIME_STAMP = slice(8, 14)
SVID = 14
CRC = 15
SOURCE = 17
NAV_START = 20

TOW_DNU = 4294967295
WNc_DNU = 65535

BUFFLEN = 1024

GALRawINAV_NAV_BYTES = 8
NAV_REAL_SIZE = 234

SIGNAL_MASK = 0x1F

signal_type = {
    17: "GAL_L1BC",
    19: "GAL_E6BC",
    20: "GAL_E5a",
    21: "GAL_E5b",
    22: "GAL_E4_AltBOC",
}

CRC24_XMODEM_TABLE = [
    0x000000,0x864CFB,0x8AD50D,0x0C99F6,0x93E6E1,0x15AA1A,0x1933EC,0x9F7F17,
    0xA18139,0x27CDC2,0x2B5434,0xAD18CF,0x3267D8,0xB42B23,0xB8B2D5,0x3EFE2E,
    0xC54E89,0x430272,0x4F9B84,0xC9D77F,0x56A868,0xD0E493,0xDC7D65,0x5A319E,
    0x64CFB0,0xE2834B,0xEE1ABD,0x685646,0xF72951,0x7165AA,0x7DFC5C,0xFBB0A7,
    0x0CD1E9,0x8A9D12,0x8604E4,0x00481F,0x9F3708,0x197BF3,0x15E205,0x93AEFE,
    0xAD50D0,0x2B1C2B,0x2785DD,0xA1C926,0x3EB631,0xB8FACA,0xB4633C,0x322FC7,
    0xC99F60,0x4FD39B,0x434A6D,0xC50696,0x5A7981,0xDC357A,0xD0AC8C,0x56E077,
    0x681E59,0xEE52A2,0xE2CB54,0x6487AF,0xFBF8B8,0x7DB443,0x712DB5,0xF7614E,
    0x19A3D2,0x9FEF29,0x9376DF,0x153A24,0x8A4533,0x0C09C8,0x00903E,0x86DCC5,
    0xB822EB,0x3E6E10,0x32F7E6,0xB4BB1D,0x2BC40A,0xAD88F1,0xA11107,0x275DFC,
    0xDCED5B,0x5AA1A0,0x563856,0xD074AD,0x4F0BBA,0xC94741,0xC5DEB7,0x43924C,
    0x7D6C62,0xFB2099,0xF7B96F,0x71F594,0xEE8A83,0x68C678,0x645F8E,0xE21375,
    0x15723B,0x933EC0,0x9FA736,0x19EBCD,0x8694DA,0x00D821,0x0C41D7,0x8A0D2C,
    0xB4F302,0x32BFF9,0x3E260F,0xB86AF4,0x2715E3,0xA15918,0xADC0EE,0x2B8C15,
    0xD03CB2,0x567049,0x5AE9BF,0xDCA544,0x43DA53,0xC596A8,0xC90F5E,0x4F43A5,
    0x71BD8B,0xF7F170,0xFB6886,0x7D247D,0xE25B6A,0x641791,0x688E67,0xEEC29C,
    0x3347A4,0xB50B5F,0xB992A9,0x3FDE52,0xA0A145,0x26EDBE,0x2A7448,0xAC38B3,
    0x92C69D,0x148A66,0x181390,0x9E5F6B,0x01207C,0x876C87,0x8BF571,0x0DB98A,
    0xF6092D,0x7045D6,0x7CDC20,0xFA90DB,0x65EFCC,0xE3A337,0xEF3AC1,0x69763A,
    0x578814,0xD1C4EF,0xDD5D19,0x5B11E2,0xC46EF5,0x42220E,0x4EBBF8,0xC8F703,
    0x3F964D,0xB9DAB6,0xB54340,0x330FBB,0xAC70AC,0x2A3C57,0x26A5A1,0xA0E95A,
    0x9E1774,0x185B8F,0x14C279,0x928E82,0x0DF195,0x8BBD6E,0x872498,0x016863,
    0xFAD8C4,0x7C943F,0x700DC9,0xF64132,0x693E25,0xEF72DE,0xE3EB28,0x65A7D3,
    0x5B59FD,0xDD1506,0xD18CF0,0x57C00B,0xC8BF1C,0x4EF3E7,0x426A11,0xC426EA,
    0x2AE476,0xACA88D,0xA0317B,0x267D80,0xB90297,0x3F4E6C,0x33D79A,0xB59B61,
    0x8B654F,0x0D29B4,0x01B042,0x87FCB9,0x1883AE,0x9ECF55,0x9256A3,0x141A58,
    0xEFAAFF,0x69E604,0x657FF2,0xE33309,0x7C4C1E,0xFA00E5,0xF69913,0x70D5E8,
    0x4E2BC6,0xC8673D,0xC4FECB,0x42B230,0xDDCD27,0x5B81DC,0x57182A,0xD154D1,
    0x26359F,0xA07964,0xACE092,0x2AAC69,0xB5D37E,0x339F85,0x3F0673,0xB94A88,
    0x87B4A6,0x01F85D,0x0D61AB,0x8B2D50,0x145247,0x921EBC,0x9E874A,0x18CBB1,
    0xE37B16,0x6537ED,0x69AE1B,0xEFE2E0,0x709DF7,0xF6D10C,0xFA48FA,0x7C0401,
    0x42FA2F,0xC4B6D4,0xC82F22,0x4E63D9,0xD11CCE,0x575035,0x5BC9C3,0xDD8538]

CRC16_XMODEM_TABLE = [
    0x0000,
    0x1021,
    0x2042,
    0x3063,
    0x4084,
    0x50A5,
    0x60C6,
    0x70E7,
    0x8108,
    0x9129,
    0xA14A,
    0xB16B,
    0xC18C,
    0xD1AD,
    0xE1CE,
    0xF1EF,
    0x1231,
    0x0210,
    0x3273,
    0x2252,
    0x52B5,
    0x4294,
    0x72F7,
    0x62D6,
    0x9339,
    0x8318,
    0xB37B,
    0xA35A,
    0xD3BD,
    0xC39C,
    0xF3FF,
    0xE3DE,
    0x2462,
    0x3443,
    0x0420,
    0x1401,
    0x64E6,
    0x74C7,
    0x44A4,
    0x5485,
    0xA56A,
    0xB54B,
    0x8528,
    0x9509,
    0xE5EE,
    0xF5CF,
    0xC5AC,
    0xD58D,
    0x3653,
    0x2672,
    0x1611,
    0x0630,
    0x76D7,
    0x66F6,
    0x5695,
    0x46B4,
    0xB75B,
    0xA77A,
    0x9719,
    0x8738,
    0xF7DF,
    0xE7FE,
    0xD79D,
    0xC7BC,
    0x48C4,
    0x58E5,
    0x6886,
    0x78A7,
    0x0840,
    0x1861,
    0x2802,
    0x3823,
    0xC9CC,
    0xD9ED,
    0xE98E,
    0xF9AF,
    0x8948,
    0x9969,
    0xA90A,
    0xB92B,
    0x5AF5,
    0x4AD4,
    0x7AB7,
    0x6A96,
    0x1A71,
    0x0A50,
    0x3A33,
    0x2A12,
    0xDBFD,
    0xCBDC,
    0xFBBF,
    0xEB9E,
    0x9B79,
    0x8B58,
    0xBB3B,
    0xAB1A,
    0x6CA6,
    0x7C87,
    0x4CE4,
    0x5CC5,
    0x2C22,
    0x3C03,
    0x0C60,
    0x1C41,
    0xEDAE,
    0xFD8F,
    0xCDEC,
    0xDDCD,
    0xAD2A,
    0xBD0B,
    0x8D68,
    0x9D49,
    0x7E97,
    0x6EB6,
    0x5ED5,
    0x4EF4,
    0x3E13,
    0x2E32,
    0x1E51,
    0x0E70,
    0xFF9F,
    0xEFBE,
    0xDFDD,
    0xCFFC,
    0xBF1B,
    0xAF3A,
    0x9F59,
    0x8F78,
    0x9188,
    0x81A9,
    0xB1CA,
    0xA1EB,
    0xD10C,
    0xC12D,
    0xF14E,
    0xE16F,
    0x1080,
    0x00A1,
    0x30C2,
    0x20E3,
    0x5004,
    0x4025,
    0x7046,
    0x6067,
    0x83B9,
    0x9398,
    0xA3FB,
    0xB3DA,
    0xC33D,
    0xD31C,
    0xE37F,
    0xF35E,
    0x02B1,
    0x1290,
    0x22F3,
    0x32D2,
    0x4235,
    0x5214,
    0x6277,
    0x7256,
    0xB5EA,
    0xA5CB,
    0x95A8,
    0x8589,
    0xF56E,
    0xE54F,
    0xD52C,
    0xC50D,
    0x34E2,
    0x24C3,
    0x14A0,
    0x0481,
    0x7466,
    0x6447,
    0x5424,
    0x4405,
    0xA7DB,
    0xB7FA,
    0x8799,
    0x97B8,
    0xE75F,
    0xF77E,
    0xC71D,
    0xD73C,
    0x26D3,
    0x36F2,
    0x0691,
    0x16B0,
    0x6657,
    0x7676,
    0x4615,
    0x5634,
    0xD94C,
    0xC96D,
    0xF90E,
    0xE92F,
    0x99C8,
    0x89E9,
    0xB98A,
    0xA9AB,
    0x5844,
    0x4865,
    0x7806,
    0x6827,
    0x18C0,
    0x08E1,
    0x3882,
    0x28A3,
    0xCB7D,
    0xDB5C,
    0xEB3F,
    0xFB1E,
    0x8BF9,
    0x9BD8,
    0xABBB,
    0xBB9A,
    0x4A75,
    0x5A54,
    0x6A37,
    0x7A16,
    0x0AF1,
    0x1AD0,
    0x2AB3,
    0x3A92,
    0xFD2E,
    0xED0F,
    0xDD6C,
    0xCD4D,
    0xBDAA,
    0xAD8B,
    0x9DE8,
    0x8DC9,
    0x7C26,
    0x6C07,
    0x5C64,
    0x4C45,
    0x3CA2,
    0x2C83,
    0x1CE0,
    0x0CC1,
    0xEF1F,
    0xFF3E,
    0xCF5D,
    0xDF7C,
    0xAF9B,
    0xBFBA,
    0x8FD9,
    0x9FF8,
    0x6E17,
    0x7E36,
    0x4E55,
    0x5E74,
    0x2E93,
    0x3EB2,
    0x0ED1,
    0x1EF0,
]

from bitstring import BitArray

def getbitu(buff, pos, len):
    return buff[pos:pos+len]

def setbitu(buff, pos, len, data):
    mask = 1 << (len - 1)
    if len <= 0 or 32 < len:
        return
    for i in range(pos, pos + len):
        if data & mask:
            buff[i//8] |= 1 << (7 - i % 8)
        else:
            buff[i//8] &= ~(1 << (7 - i % 8))
        mask >>= 1

def isChecksumOk(data):
    # Unpack the checksum bytes from the message
    ck_a = data[-2]
    ck_b = data[-1]

    # Initialize the checksum accumulators
    ck_a_calc = 0
    ck_b_calc = 0

    # Iterate over the bytes of the message and update the checksum accumulators
    for byte in data[2:-2]:
        ck_a_calc = ck_a_calc + byte
        ck_b_calc = ck_b_calc + ck_a_calc

        ck_a_calc = ck_a_calc & 0xFF
        ck_b_calc = ck_b_calc & 0xFF

    # print(f"Checksum {format(ck_a, '02X'), format(ck_b, '02X')} Calculated Checksum {format(ck_a_calc, '02X'), format(ck_b_calc, '02X')}\n")

    # Compare the calculated checksum to the checksum bytes in the message
    return (ck_a == ck_a_calc) and (ck_b == ck_b_calc)


def parse_header(header):
    """Parses the header into crc, id, length and id into block
    number and block revision.

    :param header: Bytes object with the 8 byte header.
    :return: Tuple with the values (bytes) messageType, (int) length

    """
    messageType = header[2:4]
    length = int.from_bytes(header[4:6], "little")

    return messageType, length


def parse_tow_wn(buffer):
    tow = int.from_bytes(buffer[:4], "little")
    wn_c = int.from_bytes(buffer[4:], "little")

    if tow == TOW_DNU:
        tow = "DNU"
    if wn_c == WNc_DNU:
        wn_c = "DNU"

    return tow, wn_c


def parse_SVID(svid):
    if svid == 0:
        svid = "DNU"
    elif 1 <= svid <= 37:
        pass
    elif 38 <= svid <= 61:
        svid = svid - 37
    elif svid == 62:
        svid = "GLONASS not known"
    elif 63 <= svid <= 68:
        svid = svid - 38
    elif 71 <= svid <= 106:
        svid = svid - 70
    elif 107 <= svid <= 119:
        pass
    elif 120 <= svid <= 140:
        pass
    elif 141 <= svid <= 180:
        svid = svid - 140
    elif 181 <= svid <= 187:
        svid = svid - 180
    elif 191 <= svid <= 197:
        svid = svid - 190
    elif 198 <= svid <= 215:
        svid = svid - 57
    elif 216 <= svid <= 222:
        svid = svid - 208
    elif 223 <= svid <= 245:
        svid = svid - 182
    else:
        svid = "Not known"

    return svid


def parse_nav_bits(nav_bits):
    return [nav_bits[i : i + 4][::-1].hex() for i in range(0, len(nav_bits), 4)]


def parse_GALRawINAV(block):
    tow, wn_c = parse_tow_wn(block[TIME_STAMP])
    svid = parse_SVID(block[SVID])
    crc_passed = bool(block[CRC])
    source = signal_type[block[SOURCE] & SIGNAL_MASK]
    nav_bits_hex = parse_nav_bits(
        block[NAV_START : NAV_START + 4 * GALRawINAV_NAV_BYTES]
    )

    # print_nav_page_block(tow, wn_c, svid, crc_passed, viterbi_errors, source, rx_channel, nav_bits_hex)
    # return csv_nav_page_block(tow, wn_c, svid, crc_passed, viterbi_errors, source, rx_channel, nav_bits_hex)
    return tow, wn_c, svid, crc_passed, source, nav_bits_hex


def parse_GALRawObsANDROID(block):
    tow = int(struct.unpack("d", block[:8])[0])+1
    wn_c = struct.unpack("H", block[8:10])[0]
    leapS = block[10]
    # numMeas = block[11]
    # recStat = block[12]
    # version = block[13]
    # reserved1 = block[14:15]

    return tow, wn_c, leapS


def parse_GALRawINAVANDROID(block):
    gnssId = block[0]
    svId = block[1]
    reserved1 = block[2]
    freqId = block[3]
    numWords = block[4]
    chn = block[5]
    version = block[6]
    reserved2 = block[7]
    dataWords = block[8:]

    return gnssId, svId, reserved1, numWords, dataWords


def ubloxPages2GalileoICD(PRN, tow, dwrds):
    # print(dwrds)
    # dwrds = list(struct.unpack("8I", dwrds))
    page_string = "{:032b}," * 8
    data_page_bits = page_string.format(*dwrds)
    # Format as list and cut extra element
    data_page_original = data_page_bits.split(",")[0:8]
    data_page_bits = data_page_bits.split(",")[0:6]
    # dword4, cut last 8 pad.
    data_page_bits[3] = data_page_bits[3][0:-8]
    # Assembly pages according to ESA ICD
    nav_msg_even = "".join(data_page_bits[0:4])
    # Replace search and rescue, checksum bits with zeros.
    nav_msg_odd = "".join((*data_page_bits[4:6], "0" * 56))

    return nav_msg_even, nav_msg_odd, data_page_original


def myAndroidPages2GalileoICD(DataBytes):

    DataBytes_length = len(DataBytes)

    if (DataBytes_length == BYTES_IN_PAYLOAD_LONG):
        # Reorder bytes
        DataBytesOrdered = [0 for _ in DataBytes]
        kk = 0
        for ii in range(1, 9):
            for jj in range(4):
                DataBytesOrdered[kk] = DataBytes[ii*4-jj-1]
                kk += 1

        DataBytes = DataBytesOrdered

        # Get binary representation of Android navigation message
        DataBytes_bin = [0 for _ in DataBytes]
        for ii in range(len(DataBytes)):
            DataBytes_bin[ii] = bin(int(DataBytes[ii]) & 0xff)[2:].zfill(8)

        # Unir elementos de cuatro en cuatro
        temp = ["".join(DataBytes_bin[i:i+4]) for i in range(0, len(DataBytes_bin), 4)]

        # Convertir cada elemento de la nueva lista en una cadena binaria de 32 bits
        data_page_bits = [bin(int(elemento, 2)).replace("0b", "").zfill(32)
                          for elemento in temp]

        data_original = "".join(data_page_bits)

        # dword4, cut last 8 pad.
        data_page_bits[3] = data_page_bits[3][0:-8]
        # dword8, cut last 8 pad.
        data_page_bits[7] = data_page_bits[7][0:-8]
        # Assembly pages according to ESA ICD
        nav_msg_even = "".join(data_page_bits[0:4])
        # Replace search and rescue, checksum bits with zeros.
        nav_msg_odd = "".join(data_page_bits[4:8])

    elif (DataBytes_length == BYTES_IN_PAYLOAD_SHORT):
        # Get binary representation of Android navigation message
        DataBytes_bin = [0 for _ in DataBytes]
        for ii in range(len(DataBytes)):
            DataBytes_bin[ii] = bin(int(DataBytes[ii]) & 0xff)[2:].zfill(8)

        temp = "".join(DataBytes_bin)[:-4]
        data_page_bits = "".join([temp[0:114], '000000', temp[114::],
                                  '000000'])

        data_original = "".join(data_page_bits)

        # Assembly pages according to ESA ICD
        nav_msg_even = "".join(data_page_bits[0:120])
        # Replace search and rescue, checksum bits with zeros.
        nav_msg_odd = "".join(data_page_bits[120::])

    return nav_msg_even, nav_msg_odd, data_original


def computeCRC(nav_msg_original):
    aui8_crc_buff = [0] * 32

    for i in range(15):
        pos = i * 8
        aui8_crc_buff[i] = int(getbitu(nav_msg_original, pos, 8), 2)

    for i in range(11):
        pos = i * 8
        aui8_crc_buff[15+i] = int(getbitu(nav_msg_original[128::], pos, 8), 2)

    # List to binary string
    output = ""
    output = ["{:08b}".format(x) for x in aui8_crc_buff]
    output = "0000" + "".join(output)
    output = output[:118] + output[124:] + "00"

    output_int = []
    for i in range(0, len(output), 8):
        output_int.append(int(output[i:i+8], 2))

    # Compute CRC
    crc = 0
    for ii in range(25):
        crc = ((crc << 8) & 0xFFFFFF) ^ CRC24_XMODEM_TABLE[((crc >> 16) ^ output_int[ii])]

    return crc


def TimestampToNOWTOW(unix_timestamp):

    # Calcular el número total de segundos en una semana
    seconds_per_week = 7 * 24 * 60 * 60

    leap_seconds = 18  # @ 31/05/2023

    # Convertir milisegundos a datetime en UTC
    dt = datetime.datetime.utcfromtimestamp(unix_timestamp // 1000).replace(tzinfo=datetime.timezone.utc)

    utc_origin = datetime.datetime(1980, 1, 6, 0, 0, 0, tzinfo=datetime.timezone.utc)

    seconds_from_origin = (dt - utc_origin).total_seconds() + leap_seconds

    now = int(seconds_from_origin // seconds_per_week)
    tow = int(seconds_from_origin - now * seconds_per_week)

    return now, tow


class ANDROID:
    def __init__(self, path):
        self.file = open(path, "r")
        self.lines = self.file.readlines()
        self.index = -1
        self.tow = 0
        self.wn_c = 0

    def __iter__(self):
        return self

    def __next__(self):
        data_format = None
        # wn_c = 0
        # tow = 0
        self.index += 1

        while self.index < len(self.lines):
            if '#' in self.lines[self.index]:
                self.index += 1
                continue

            splitLine = self.lines[self.index].splitlines()[0].split(',')
            messageType = splitLine[0]
            message = splitLine[1:]

            if (messageType == 'Fix'):
                Provider = message[0]
                Latitude = message[1]
                Longitude = message[2]
                Altitude = message[3]
                Speed = message[4]
                Accuracy = message[5]
                TimeInMsUTC = message[6]
                self.time = int(TimeInMsUTC) / 1000

                self.wn_c, self.tow = TimestampToNOWTOW(TimeInMsUTC)

                self.index += 1
                continue

            elif (messageType == 'Raw'):
                self.index += 1
                continue

            elif (messageType == 'Nav'):
                svid = int(message[0])
                Type = int(message[1])
                Status = int(message[2])
                MessageId = int(message[3])     # Gal I/NAV 1-24
                SubMessageId = int(message[4])  # Gal I/NAV 1-10+
                DataBytes = message[5:]

                if (Type != GAL_INAV):
                    self.index += 1
                    continue

                if (MessageId > 24):
                    self.index += 1
                    continue

                # if (Status != STATUS_PARITY_PASSED):
                #     self.index += 1
                #     continue

                if (len(DataBytes) != BYTES_IN_PAYLOAD_LONG):
                    self.index += 1
                    continue

                # print(f"{nav_bits[:120]} {nav_bits[120:240]}")
                # print(f"\n{len(nav_msg_even)} {nav_msg_even}")
                # print(f"{len(nav_msg_odd)} {nav_msg_odd}")

                # part1 = nav_msg_even[0]
                # page1 = nav_msg_even[1]
                # part2 = nav_msg_odd[0]
                # page2 = nav_msg_odd[1]

                # # # skip alert page
                # # if ((page1 == '1') or (page2 == '1')):
                # #     print("Alert page")

                # # # Test even-odd parts
                # # if ((part1 != '0') or (part2 != '1')):
                # #     print("Unexpected parts")

                # print(f"Checksum {parsedMessage.check_crc()}")

                nav_msg_even, nav_msg_odd, nav_msg_original = \
                    myAndroidPages2GalileoICD(DataBytes)

                # Compute CRC
                computed_crc = computeCRC(nav_msg_original)
                # Read CRC
                read_crc = hex(int(nav_msg_original[128+82:128+82+24], 2))
                # CRC
                isCRCOK = computed_crc == int(read_crc, 16)

                nav_bits = BitArray(bin="".join([nav_msg_even,
                                                nav_msg_odd]))

                wn = self.wn_c - 1024 if self.wn_c > 1024 else 0

                data_format = DataFormat(
                    svid, wn, self.tow, nav_bits, "GAL_L1BC", isCRCOK
                )
                break

            self.index += 1
            continue

        if data_format is None:
            raise StopIteration

        return self.index, data_format


class ANDROIDCeit:
    def __init__(self, path):
        self.file = open(path, "r")
        self.lines = self.file.readlines()
        self.index = -1
        self.tow = 0
        self.wn_c = 0

    def __iter__(self):
        return self

    def __next__(self):
        data_format = None
        # wn_c = 0
        # tow = 0
        self.index += 1

        while self.index < len(self.lines):
            if self.lines[self.index] == '\n':
                self.index += 1
                continue

            if '#' in self.lines[self.index]:
                self.index += 1
                continue

            splitLine = self.lines[self.index].splitlines()[0].split(',')

            svid = int(splitLine[0])
            timestamp = int(splitLine[1])
            Type = int(splitLine[2])
            Status = int(splitLine[3])
            MessageId = int(splitLine[4])     # Gal I/NAV 1-24
            SubMessageId = int(splitLine[5])  # Gal I/NAV 1-10+
            DataBytes = splitLine[6:]
            DataBytes[0] = DataBytes[0][1:] 
            DataBytes[-1] = DataBytes[-1][:-1]

            self.wn_c, self.tow = TimestampToNOWTOW(timestamp)

            if (Type != GAL_INAV):
                self.index += 1
                continue

            if (len(DataBytes) != BYTES_IN_PAYLOAD_LONG and
                    len(DataBytes) != BYTES_IN_PAYLOAD_SHORT):
                self.index += 1
                continue

            nav_msg_even, nav_msg_odd, nav_msg_original = \
                myAndroidPages2GalileoICD(DataBytes)

            # print(f"part1 {nav_msg_original[0]} page1 {nav_msg_original[1]} part2 {nav_msg_original[128]} page2 {nav_msg_original[129]}")
            # print(f"tail1 {nav_msg_even[114:120] == '000000'} tail2 {nav_msg_odd[114:120] == '000000'}")

            # Compute CRC
            computed_crc = computeCRC(nav_msg_original)
            # Read CRC
            read_crc = hex(int(nav_msg_original[128+82:128+82+24], 2))
            # CRC
            isCRCOK = computed_crc == int(read_crc, 16)
            isCRCOK = True

            nav_bits = BitArray(bin="".join([nav_msg_even,
                                            nav_msg_odd]))

            wn = self.wn_c - 1024 if self.wn_c > 1024 else 0
            tow = self.tow

            data_format = DataFormat(
                svid, wn, tow, nav_bits, "GAL_L1BC", isCRCOK
            )
            break

        if data_format is None:
            raise StopIteration

        return self.index, data_format


class ANDROIDLive:
    def __init__(self, host, port):
        self.index = -1
        _sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.s.connect((host, port))
        _sock.bind((host, port))
        _sock.listen(1)
        print(f"Servidor escuchando en {host}:{port}")
   
        # Acepta una conexión entrante
        self.s, client_address = _sock.accept()
        print(f"Conexión establecida desde {client_address}")
 
        self.wn_c = 0
        self.tow = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        data_format = None
        self.index += 1
 
        try:    
            message = []
            while buffer := self.s.recv(1).decode("utf-8"):
                message.append(buffer)
               
                if (buffer != "]" or buffer == '\n'):
                    continue
               
                message = "".join(message)
 
                if message == '\n':
                    message = []
                    continue
 
                if '#' in message:
                    message = []
                    continue
                if 'TextView' in message:
                    message = []
                    continue
 
                print(message)
                # Split received message into workable pieces
                splitLine = message.splitlines()[0].split(',')
                # Store pieces into corresponding variables
                svid = int(splitLine[0])
                timestamp = int(splitLine[1])
                Type = int(splitLine[2])
                Status = int(splitLine[3])
                MessageId = int(splitLine[4])     # Gal I/NAV 1-24
                SubMessageId = int(splitLine[5])  # Gal I/NAV 1-10+
                DataBytes = splitLine[6:]
                DataBytes[0] = DataBytes[0][1:]
                DataBytes[-1] = DataBytes[-1][:-1]
 
                # Convert UNIX timestamp to NOW and TOW
                self.wn_c, self.tow = TimestampToNOWTOW(timestamp)  
 
                # Check Galileo as data source
                if (Type != GAL_INAV):
                    self.index += 1
                    message = []
                    continue
                # Check message payload's size
                if (len(DataBytes) != BYTES_IN_PAYLOAD_LONG and
                        len(DataBytes) != BYTES_IN_PAYLOAD_SHORT):
                    self.index += 1
                    message = []
                    continue
 
                # Process received data and get required binary representation
                nav_msg_even, nav_msg_odd, nav_msg_original = \
                    myAndroidPages2GalileoICD(DataBytes)
               
                # print(f"part1 {nav_msg_original[0]} page1 {nav_msg_original[1]} part2 {nav_msg_original[128]} page2 {nav_msg_original[129]}")
                # print(f"tail1 {nav_msg_even[114:120] == '000000'} tail2 {nav_msg_odd[114:120] == '000000'}")
 
                # Compute CRC
                computed_crc = computeCRC(nav_msg_original)
                # Read CRC
                read_crc = hex(int(nav_msg_original[128+82:128+82+24], 2))
                # CRC
                isCRCOK = computed_crc == int(read_crc, 16)
                isCRCOK = True
 
                nav_bits = BitArray(bin="".join([nav_msg_even,
                                                nav_msg_odd]))
 
                wn = self.wn_c - 1024 if self.wn_c > 1024 else 0
                tow = self.tow
 
                data_format = DataFormat(
                    svid, wn, tow, nav_bits, "GAL_L1BC", isCRCOK
                )
                break
 
        except KeyboardInterrupt:
            # close the socket
            self.s.close()
            print("Connection closed")
 
        if data_format is None:
            raise StopIteration
 
        return self.index, data_format

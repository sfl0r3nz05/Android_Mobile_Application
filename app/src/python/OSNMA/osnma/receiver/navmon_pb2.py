# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: navmon.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cnavmon.proto\"\xbe\x1c\n\rNavMonMessage\x12\x10\n\x08sourceID\x18\x01 \x02(\x04\x12!\n\x04type\x18\x02 \x02(\x0e\x32\x13.NavMonMessage.Type\x12\x17\n\x0flocalUtcSeconds\x18\x03 \x02(\x04\x12\x1b\n\x13localUtcNanoseconds\x18\x04 \x02(\x04\x12&\n\x02gi\x18\x05 \x01(\x0b\x32\x1a.NavMonMessage.GalileoInav\x12(\n\x02rd\x18\x06 \x01(\x0b\x32\x1c.NavMonMessage.ReceptionData\x12\"\n\x03rfd\x18\x07 \x01(\x0b\x32\x15.NavMonMessage.RFData\x12+\n\x02op\x18\x08 \x01(\x0b\x32\x1f.NavMonMessage.ObserverPosition\x12$\n\x04gpsi\x18\t \x01(\x0b\x32\x16.NavMonMessage.GPSInav\x12)\n\x04\x62id1\x18\n \x01(\x0b\x32\x1b.NavMonMessage.BeidouInavD1\x12)\n\x04\x62id2\x18\x0b \x01(\x0b\x32\x1b.NavMonMessage.BeidouInavD2\x12(\n\x04gloi\x18\x0c \x01(\x0b\x32\x1a.NavMonMessage.GlonassInav\x12&\n\x02sr\x18\r \x01(\x0b\x32\x1a.NavMonMessage.SARResponse\x12+\n\x02\x64m\x18\x0e \x01(\x0b\x32\x1f.NavMonMessage.DebuggingMessage\x12*\n\x02od\x18\x0f \x01(\x0b\x32\x1e.NavMonMessage.ObserverDetails\x12-\n\x03ujs\x18\x10 \x01(\x0b\x32 .NavMonMessage.UbloxJammingStats\x12\'\n\x03sbm\x18\x11 \x01(\x0b\x32\x1a.NavMonMessage.SBASMessage\x12$\n\x04gpsc\x18\x12 \x01(\x0b\x32\x16.NavMonMessage.GPSCnav\x12&\n\x02rm\x18\x13 \x01(\x0b\x32\x1a.NavMonMessage.RTCMMessage\x12,\n\x02to\x18\x14 \x01(\x0b\x32 .NavMonMessage.TimeOffsetMessage\x12&\n\x02gf\x18\x15 \x01(\x0b\x32\x1a.NavMonMessage.GalileoFnav\x12&\n\x02gc\x18\x16 \x01(\x0b\x32\x1a.NavMonMessage.GalileoCnav\x1a\xcb\x01\n\x0bGalileoInav\x12\x0e\n\x06gnssWN\x18\x01 \x02(\r\x12\x0f\n\x07gnssTOW\x18\x02 \x02(\r\x12\x0e\n\x06gnssID\x18\x03 \x02(\r\x12\x0e\n\x06gnssSV\x18\x04 \x02(\r\x12\x10\n\x08\x63ontents\x18\x05 \x02(\x0c\x12\r\n\x05sigid\x18\x06 \x01(\r\x12\x11\n\treserved1\x18\x07 \x01(\x0c\x12\x11\n\treserved2\x18\x08 \x01(\x0c\x12\x0b\n\x03sar\x18\t \x01(\x0c\x12\r\n\x05spare\x18\n \x01(\x0c\x12\x0b\n\x03\x63rc\x18\x0b \x01(\x0c\x12\x0b\n\x03ssp\x18\x0c \x01(\r\x1ao\n\x0bGalileoFnav\x12\x0e\n\x06gnssWN\x18\x01 \x02(\r\x12\x0f\n\x07gnssTOW\x18\x02 \x02(\r\x12\x0e\n\x06gnssID\x18\x03 \x02(\r\x12\x0e\n\x06gnssSV\x18\x04 \x02(\r\x12\x10\n\x08\x63ontents\x18\x05 \x02(\x0c\x12\r\n\x05sigid\x18\x06 \x02(\r\x1ao\n\x0bGalileoCnav\x12\x0e\n\x06gnssWN\x18\x01 \x02(\r\x12\x0f\n\x07gnssTOW\x18\x02 \x02(\r\x12\x0e\n\x06gnssID\x18\x03 \x02(\r\x12\x0e\n\x06gnssSV\x18\x04 \x02(\r\x12\x10\n\x08\x63ontents\x18\x05 \x02(\x0c\x12\r\n\x05sigid\x18\x06 \x02(\r\x1ak\n\x07GPSInav\x12\x0e\n\x06gnssWN\x18\x01 \x02(\r\x12\x0f\n\x07gnssTOW\x18\x02 \x02(\r\x12\x0e\n\x06gnssID\x18\x03 \x02(\r\x12\x0e\n\x06gnssSV\x18\x04 \x02(\r\x12\x10\n\x08\x63ontents\x18\x05 \x02(\x0c\x12\r\n\x05sigid\x18\x06 \x01(\r\x1ap\n\x0c\x42\x65idouInavD1\x12\x0e\n\x06gnssWN\x18\x01 \x02(\r\x12\x0f\n\x07gnssTOW\x18\x02 \x02(\r\x12\x0e\n\x06gnssID\x18\x03 \x02(\r\x12\x0e\n\x06gnssSV\x18\x04 \x02(\r\x12\x10\n\x08\x63ontents\x18\x05 \x02(\x0c\x12\r\n\x05sigid\x18\x06 \x01(\r\x1ap\n\x0c\x42\x65idouInavD2\x12\x0e\n\x06gnssWN\x18\x01 \x02(\r\x12\x0f\n\x07gnssTOW\x18\x02 \x02(\r\x12\x0e\n\x06gnssID\x18\x03 \x02(\r\x12\x0e\n\x06gnssSV\x18\x04 \x02(\r\x12\x10\n\x08\x63ontents\x18\x05 \x02(\x0c\x12\r\n\x05sigid\x18\x06 \x01(\r\x1a\\\n\x0bGlonassInav\x12\x0e\n\x06gnssID\x18\x01 \x02(\r\x12\x0e\n\x06gnssSV\x18\x02 \x02(\r\x12\x0c\n\x04\x66req\x18\x03 \x02(\r\x12\x10\n\x08\x63ontents\x18\x04 \x02(\x0c\x12\r\n\x05sigid\x18\x05 \x01(\r\x1a\x8c\x01\n\rReceptionData\x12\x0e\n\x06gnssID\x18\x01 \x02(\r\x12\x0e\n\x06gnssSV\x18\x02 \x02(\r\x12\r\n\x05sigid\x18\x07 \x01(\r\x12\n\n\x02\x64\x62\x18\x03 \x02(\r\x12\n\n\x02\x65l\x18\x04 \x02(\r\x12\x0b\n\x03\x61zi\x18\x05 \x02(\r\x12\r\n\x05prRes\x18\x06 \x02(\x01\x12\n\n\x02qi\x18\x08 \x01(\r\x12\x0c\n\x04used\x18\t \x01(\x08\x1a\xbe\x02\n\x06RFData\x12\x0e\n\x06rcvTow\x18\x01 \x02(\x01\x12\r\n\x05rcvWn\x18\x02 \x02(\r\x12\x0e\n\x06gnssID\x18\x03 \x02(\r\x12\x0e\n\x06gnssSV\x18\x04 \x02(\r\x12\x0f\n\x07\x64oppler\x18\x05 \x02(\x01\x12\x14\n\x0c\x63\x61rrierphase\x18\x06 \x02(\x01\x12\x13\n\x0bpseudorange\x18\x07 \x02(\x01\x12\x12\n\nlocktimeMS\x18\x08 \x02(\x01\x12\r\n\x05\x64oStd\x18\t \x02(\x01\x12\r\n\x05\x63pStd\x18\n \x02(\x01\x12\r\n\x05prStd\x18\x0b \x02(\x01\x12\r\n\x05sigid\x18\x0c \x01(\r\x12\x0b\n\x03\x63no\x18\r \x01(\r\x12\x0f\n\x07prvalid\x18\x0e \x01(\x08\x12\x0f\n\x07\x63pvalid\x18\x0f \x01(\x08\x12\x14\n\x0chalfcycvalid\x18\x10 \x01(\x08\x12\x12\n\nsubhalfcyc\x18\x11 \x01(\x08\x12\x10\n\x08\x63lkReset\x18\x12 \x01(\x08\x1aU\n\x10ObserverPosition\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\x12\x0b\n\x03\x61\x63\x63\x18\x04 \x02(\x01\x12\x13\n\x0bgroundSpeed\x18\x05 \x01(\x01\x1a|\n\x0bSARResponse\x12\x0e\n\x06gnssID\x18\x01 \x02(\r\x12\x0e\n\x06gnssSV\x18\x02 \x02(\r\x12\r\n\x05sigid\x18\x03 \x02(\r\x12\x0c\n\x04type\x18\x04 \x02(\r\x12\x12\n\nidentifier\x18\x05 \x02(\x0c\x12\x0c\n\x04\x63ode\x18\x06 \x02(\r\x12\x0e\n\x06params\x18\x07 \x02(\x0c\x1a\x31\n\x10\x44\x65\x62uggingMessage\x12\x0c\n\x04type\x18\x01 \x02(\r\x12\x0f\n\x07payload\x18\x02 \x02(\x0c\x1a\x92\x02\n\x0fObserverDetails\x12\x0e\n\x06vendor\x18\x01 \x02(\t\x12\x11\n\thwversion\x18\x02 \x02(\t\x12\x0f\n\x07modules\x18\x03 \x02(\t\x12\x11\n\tswversion\x18\x04 \x02(\t\x12\x10\n\x08serialno\x18\x05 \x02(\t\x12\x15\n\rclockOffsetNS\x18\x06 \x01(\x01\x12\x1a\n\x12\x63lockOffsetDriftNS\x18\x07 \x01(\x01\x12\x17\n\x0f\x63lockAccuracyNS\x18\x08 \x01(\x01\x12\x16\n\x0e\x66reqAccuracyPS\x18\t \x01(\x01\x12\r\n\x05owner\x18\n \x01(\t\x12\x0e\n\x06remark\x18\x0b \x01(\t\x12\x13\n\x0brecvgithash\x18\x0c \x01(\t\x12\x0e\n\x06uptime\x18\r \x01(\r\x1aV\n\x11UbloxJammingStats\x12\x12\n\nnoisePerMS\x18\x01 \x02(\r\x12\x0e\n\x06\x61gcCnt\x18\x02 \x02(\r\x12\r\n\x05\x66lags\x18\x03 \x02(\r\x12\x0e\n\x06jamInd\x18\x04 \x02(\r\x1a?\n\x0bSBASMessage\x12\x0e\n\x06gnssID\x18\x01 \x02(\r\x12\x0e\n\x06gnssSV\x18\x02 \x02(\r\x12\x10\n\x08\x63ontents\x18\x03 \x02(\x0c\x1ak\n\x07GPSCnav\x12\x0e\n\x06gnssWN\x18\x01 \x02(\r\x12\x0f\n\x07gnssTOW\x18\x02 \x02(\r\x12\x0e\n\x06gnssID\x18\x03 \x02(\r\x12\x0e\n\x06gnssSV\x18\x04 \x02(\r\x12\x10\n\x08\x63ontents\x18\x05 \x02(\x0c\x12\r\n\x05sigid\x18\x06 \x02(\r\x1a\x1f\n\x0bRTCMMessage\x12\x10\n\x08\x63ontents\x18\x05 \x02(\x0c\x1a\x8b\x01\n\nGNSSOffset\x12\x0e\n\x06gnssid\x18\x01 \x02(\r\x12\x10\n\x08offsetNS\x18\x02 \x02(\x05\x12\x0c\n\x04tAcc\x18\x03 \x02(\r\x12\r\n\x05valid\x18\x04 \x02(\x08\x12\r\n\x05leapS\x18\x05 \x01(\x05\x12\x0b\n\x03tow\x18\x06 \x02(\r\x12\n\n\x02wn\x18\x07 \x01(\r\x12\n\n\x02nT\x18\x08 \x01(\r\x12\n\n\x02n4\x18\t \x01(\r\x1aM\n\x11TimeOffsetMessage\x12\x0c\n\x04itow\x18\x01 \x02(\r\x12*\n\x07offsets\x18\x02 \x03(\x0b\x32\x19.NavMonMessage.GNSSOffset\"\x83\x03\n\x04Type\x12\x15\n\x11ReceptionDataType\x10\x01\x12\x18\n\x14ObserverPositionType\x10\x02\x12\x13\n\x0fGalileoInavType\x10\x03\x12\x0e\n\nRFDataType\x10\x04\x12\x0f\n\x0bGPSInavType\x10\x05\x12\x14\n\x10\x42\x65idouInavTypeD1\x10\x06\x12\x13\n\x0fGlonassInavType\x10\x07\x12\x14\n\x10\x42\x65idouInavTypeD2\x10\x08\x12\x13\n\x0fSARResponseType\x10\t\x12\x11\n\rDebuggingType\x10\n\x12\x17\n\x13ObserverDetailsType\x10\x0b\x12\x19\n\x15UbloxJammingStatsType\x10\x0c\x12\x13\n\x0fSBASMessageType\x10\r\x12\x0f\n\x0bGPSCnavType\x10\x0e\x12\x13\n\x0fRTCMMessageType\x10\x0f\x12\x12\n\x0eTimeOffsetType\x10\x10\x12\x13\n\x0fGalileoFnavType\x10\x11\x12\x13\n\x0fGalileoCnavType\x10\x12')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'navmon_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NAVMONMESSAGE._serialized_start=17
  _NAVMONMESSAGE._serialized_end=3663
  _NAVMONMESSAGE_GALILEOINAV._serialized_start=892
  _NAVMONMESSAGE_GALILEOINAV._serialized_end=1095
  _NAVMONMESSAGE_GALILEOFNAV._serialized_start=1097
  _NAVMONMESSAGE_GALILEOFNAV._serialized_end=1208
  _NAVMONMESSAGE_GALILEOCNAV._serialized_start=1210
  _NAVMONMESSAGE_GALILEOCNAV._serialized_end=1321
  _NAVMONMESSAGE_GPSINAV._serialized_start=1323
  _NAVMONMESSAGE_GPSINAV._serialized_end=1430
  _NAVMONMESSAGE_BEIDOUINAVD1._serialized_start=1432
  _NAVMONMESSAGE_BEIDOUINAVD1._serialized_end=1544
  _NAVMONMESSAGE_BEIDOUINAVD2._serialized_start=1546
  _NAVMONMESSAGE_BEIDOUINAVD2._serialized_end=1658
  _NAVMONMESSAGE_GLONASSINAV._serialized_start=1660
  _NAVMONMESSAGE_GLONASSINAV._serialized_end=1752
  _NAVMONMESSAGE_RECEPTIONDATA._serialized_start=1755
  _NAVMONMESSAGE_RECEPTIONDATA._serialized_end=1895
  _NAVMONMESSAGE_RFDATA._serialized_start=1898
  _NAVMONMESSAGE_RFDATA._serialized_end=2216
  _NAVMONMESSAGE_OBSERVERPOSITION._serialized_start=2218
  _NAVMONMESSAGE_OBSERVERPOSITION._serialized_end=2303
  _NAVMONMESSAGE_SARRESPONSE._serialized_start=2305
  _NAVMONMESSAGE_SARRESPONSE._serialized_end=2429
  _NAVMONMESSAGE_DEBUGGINGMESSAGE._serialized_start=2431
  _NAVMONMESSAGE_DEBUGGINGMESSAGE._serialized_end=2480
  _NAVMONMESSAGE_OBSERVERDETAILS._serialized_start=2483
  _NAVMONMESSAGE_OBSERVERDETAILS._serialized_end=2757
  _NAVMONMESSAGE_UBLOXJAMMINGSTATS._serialized_start=2759
  _NAVMONMESSAGE_UBLOXJAMMINGSTATS._serialized_end=2845
  _NAVMONMESSAGE_SBASMESSAGE._serialized_start=2847
  _NAVMONMESSAGE_SBASMESSAGE._serialized_end=2910
  _NAVMONMESSAGE_GPSCNAV._serialized_start=2912
  _NAVMONMESSAGE_GPSCNAV._serialized_end=3019
  _NAVMONMESSAGE_RTCMMESSAGE._serialized_start=3021
  _NAVMONMESSAGE_RTCMMESSAGE._serialized_end=3052
  _NAVMONMESSAGE_GNSSOFFSET._serialized_start=3055
  _NAVMONMESSAGE_GNSSOFFSET._serialized_end=3194
  _NAVMONMESSAGE_TIMEOFFSETMESSAGE._serialized_start=3196
  _NAVMONMESSAGE_TIMEOFFSETMESSAGE._serialized_end=3273
  _NAVMONMESSAGE_TYPE._serialized_start=3276
  _NAVMONMESSAGE_TYPE._serialized_end=3663
# @@protoc_insertion_point(module_scope)

import struct
import binascii

# type and length
CMD_HDR = struct.Struct("HH")

def CMD_INIT():
    return b'0x00000500hello'


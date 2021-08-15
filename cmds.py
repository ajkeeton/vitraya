import struct
import binascii

def crc16(data: bytes):
    data = bytearray(data)
    poly = 0x8001
    crc = 0
    for b in data:
        crc ^= (0xFF & b) << 8
        for _ in range(0, 8):
            if crc & (1 << 15): 
                crc <<= 1
                crc ^= poly
            else:
                crc <<= 1

    return crc & 0xffff

# type and length
CMD_HDR = struct.Struct("HH")
PACKET_SIZE = 20

def CMD_INIT():
    return b'0x00000500hello'

def parse(i2c, addr):
    if not i2c.try_lock():
        return []

    buf = bytearray(PACKET_SIZE)
    i2c.readfrom_into(addr, buf)
    #print(addr, binascii.hexlify(buf), end='')
    i2c.unlock()

    ts, t, l, a, b, c, d, e, cs = struct.unpack('LHHHHHHHH', buf)

    # Check CRC
    if cs != crc16(buf[0:18]) and t != 0:
        # print(f"{addr}: CRC failed for address: {cs} invalid")
        return []

    if t == 0:
        print(f"{addr}: Hello message, {l} bytes:")
        print(binascii.hexlify(buf))
    elif t == 1:
        # print(ts, "State:", a, b, c, d, e)
        return [a, b, c, d, e]
    else:
        print(f"Invalid type {t} in:", binascii.hexlify(buf))

    return []

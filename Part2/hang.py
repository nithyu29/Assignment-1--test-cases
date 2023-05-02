# import struct
# import sys

# data = b''
# data += b"A"*32 # Merchant ID
# data += b"B"*32 # Customer ID
# data += struct.pack("<I", 1) # One record
# # Record of type animation
# data += struct.pack("<I", 8 + 32 + 256) # Record size (4 bytes)
# data += struct.pack("<I", 3)            # Record type (4 bytes)
# data += b"A"*31 + b'\x00'               # Note: 32 byte message
# data += b'\x08' * 256                   # Program made entirely of "end program" (256 bytes)

# f = open(sys.argv[1], 'wb')
# datalen = len(data) + 4 # Plus 4 bytes for the length itself
# f.write(struct.pack("<I", datalen))
# f.write(data)
# f.close()
import struct

data = b""
data += b"A" * 32  # Merchant ID
data += b"B" * 32  # Customer ID
data += struct.pack("<I", 1)  # One record
data += struct.pack("<I", 8 + 32 + 256)  # Record size: 4 bytes size, 4 bytes type, 32 bytes message, 256 bytes program
data += struct.pack("<I", 3)  # Record type (animated message)
data += b"x" * 31 + b"\x00"  # Null-terminated 32 byte message
program = bytearray(256)
program[0:3] = [0x09, 0xFD, 0x00]  # Infinite loop: jump -3
data += program

with open("test cases/hang.gft", "wb") as f:
    datalen = len(data) + 4  # Plus 4 bytes for the length itself
    f.write(struct.pack("<I", datalen))
    f.write(data)

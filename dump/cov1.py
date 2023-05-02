import struct

# We build the content of the file in a byte string first
# This lets us calculate the length for the header at the end
data = b''
data += b"A"*32 # Merchant ID
data += b"B"*32 # Customer ID
data += struct.pack("<I", 2) # Two records
# Record of type animation
data += struct.pack("<I", 8 + 32 + 256) # Record size (4 bytes)
data += struct.pack("<I", 3)            # Record type (4 bytes)
data += b"A"*31 + b'\x00'               # Note: 32 byte message
data += b'\x00\x00\x04'                 # Program with a single opcode 0x04, i.e., MOV B, 0
# Record of type message
data += struct.pack("<I", 8 + 32)       # Record size: 4 bytes size, 4 bytes type, 32 bytes message
data += struct.pack("<I", 2)            # Record type
data += b"x"*31 + b'\0'                 # Note: 32 byte message

with open("part3/cov1.gft", "wb") as f:
    datalen = len(data) + 4 # Plus 4 bytes for the length itself
    f.write(struct.pack("<I", datalen))
    f.write(data)

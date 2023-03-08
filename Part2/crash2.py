
import struct
import sys

# Build the content of the file in a byte string
data = b''
data += b"A"*32  # Merchant ID
data += b"B"*32  # Customer ID
data += struct.pack("<I", 1)  # One record
# Record of type animation
data += struct.pack("<I", 8 + 32 + 256)  # Record size
data += struct.pack("<I", 3)  # Record type
data += b"A"*31 + b'\x00'  # Note: 32 byte message
data += b'\x00'*256  # Empty program

# Write the gift card data to a file
f = open('test cases/crash2.gft', 'wb')
datalen = len(data) + 4  # Plus 4 bytes for the length itself
f.write(struct.pack("<I", datalen))
f.write(data)
f.close()
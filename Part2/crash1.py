import struct
import sys

# Build the content of the file in a byte string
data = b''
data += b"A"*40  # Merchant ID is longer than 32 bytes
data += b"B"*32  # Customer ID
data += struct.pack("<I", 1)  # One record
# Record of type message
data += struct.pack("<I", 8 + 32)  # Record size
data += struct.pack("<I", 2)  # Record type
data += b"x"*31 + b'\0'  # Note: 32 byte message

# Write the gift card data to a file
f = open('test cases/crash1.gft', 'wb')
datalen = len(data) + 4  # Plus 4 bytes for the length itself
f.write(struct.pack("<I", datalen))
f.write(data)
f.close() 
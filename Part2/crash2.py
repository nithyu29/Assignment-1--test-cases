import struct

data = b""
data += b"A" * 32  # Merchant ID
data += b"B" * 32  # Customer ID
data += struct.pack("<I", 1)  # One record
data += struct.pack("<I", 8 + 32)  # Record size: 4 bytes size, 4 bytes type, 32 bytes message
data += struct.pack("<I", 2)  # Record type (message)
data += b"x" * 32  # Non-null-terminated 32 byte message

with open("test cases/crash2.gft", "wb") as f:
    datalen = len(data) + 4  # Plus 4 bytes for the length itself
    f.write(struct.pack("<I", datalen))
    f.write(data)

import struct

data = b""
data += b"A" * 32  # Merchant ID
data += b"B" * 32  # Customer ID
data += struct.pack("<I", 1)  # One record
data += struct.pack("<I", 8 + 32 + 256)  # Record size: 4 bytes size, 4 bytes type, 32 bytes message, 256 bytes program
data += struct.pack("<I", 3)  # Record type (animated message)
data += b"x" * 32  # Non-null-terminated 32 byte message
data += b"\x00" * 256  # No-op program

with open("test cases/crash1.gft", "wb") as f:
    datalen = len(data) + 4  # Plus 4 bytes for the length itself
    f.write(struct.pack("<I", datalen))
    f.write(data)

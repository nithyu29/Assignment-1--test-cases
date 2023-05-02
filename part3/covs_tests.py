import struct
import sys

# Function to generate test cases
def generate_test_case(filename, record_type, message):
    data = b''
    data += b"GiftCardz.com".ljust(32, b' ')  # Merchant ID
    data += b"B" * 32  # Customer ID
    data += struct.pack("<I", 1)  # One record
    data += struct.pack("<I", 8 + 32)  # Record size: 4 bytes size, 4 bytes type, 32 bytes message
    data += struct.pack("<I", record_type)  # Record type
    data += message.ljust(32, b'\0')  # Note: 32 byte message

    with open(filename, 'wb') as f:
        datalen = len(data) + 4  # Plus 4 bytes for the length itself
        f.write(struct.pack("<I", datalen))
        f.write(data)

# Test case 1: Record type 1 (amount change)
generate_test_case("cov1.gft", 1, b"Amount change test")

# Test case 2: Record type 3 (animated message)
generate_test_case("cov2.gft", 3, b"Animated message test")

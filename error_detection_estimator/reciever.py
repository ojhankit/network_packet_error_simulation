from utils.parity import verify_parity
from utils.crc import verify_crc
from utils.checksum import verify_checksum

def receive(message: str,method: str):
    if method == 'parity':
        return verify_parity(message)
    elif method == 'crc':
        return verify_crc(message)
    elif method == 'checksum':
        return verify_checksum(message)
    else:
        raise ValueError("Unknown error detection method")
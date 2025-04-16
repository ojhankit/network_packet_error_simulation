from utils.parity import apply_parity
from utils.crc import apply_crc
from utils.checksum import apply_checksum

def transmit(message: str, method: str) -> str:
    """
    Encodes the message using the selected error detection method.

    message: The raw data (string)
    method: 'parity', 'crc', or 'checksum'
    
    Returns: Encoded message.
    """
    if method == 'parity':
        return apply_parity(message)
    elif method == 'crc':
        return apply_crc(message)
    elif method == 'checksum':
        return apply_checksum(message)
    else:
        raise ValueError("Unknown error detection method")

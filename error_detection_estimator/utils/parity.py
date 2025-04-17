
def apply_parity(message:str):
    # here even parity is used
    count_one = message.count('1')
    parity_bit = '0' if count_one % 2 == 0 else '1'
    return message + parity_bit


def verify_parity(message:str):
    count_one = message.count('1')
    if count_one % 2 == 0:
        return "Data is accepted (no error detected)"
    else:
        return "Data is rejected (error detected)"
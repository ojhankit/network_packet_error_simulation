def xor(a:str ,b:str):
    ans = ""
    for i in range(1,len(b)):
        ans += "0" if a[i] == b[i] else "1"
    return ans

def mod2div(dividend:str,divisor:str):
    pick = len(divisor)
    temp = dividend[:pick]
    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor,temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp) + dividend[pick]
        pick += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)

def apply_crc(message:str):
    divisor = "1011"
    padded_message = message + "0" * (len(divisor)-1)
    remainder = mod2div(padded_message, divisor)
    return message + remainder


def verify_crc(encoded_message:str):
    divisor = "1011"
    remainder = mod2div(encoded_message ,divisor)

    return all(bit == '0' for bit in remainder)
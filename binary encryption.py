message ="I like coding! And you?"
print("original message:", message)
encrypted = [ord(c) for c in message]

def encrypted_to_binary(numbers):
    return "".join(bin(n)[2:].zfill(8) for n in numbers)

encrypt_binaraly=encrypted_to_binary(encrypted)
print("encrypted message in binary:",encrypt_binaraly, "with a length of", len(encrypt_binaraly), "bits")


decode_str= "".join([chr(int(encrypt_binaraly[i:i+8],2)) for i in range(0, len(encrypt_binaraly),8)])
print ("decoded:",decode_str)





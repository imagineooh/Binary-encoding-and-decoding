# I put comments for better understanding of the code, hope it helps!


message ="I like coding! And you?" #This is the original message to decrypt. Can of course be changed!
print("original message:", message) #This is for the display
encrypted = [ord(c) for c in message] #Encrypts the message in Unicode using the ord function

def encrypted_to_binary(numbers): #Function to turn a series of numbers into binary
    return "".join(bin(n)[2:].zfill(8) for n in numbers) #Turns number into binary, for ex 10 become 1010 in binary, and will be put into 8 bit format, so it becomes 00001010

encrypt_binaraly=encrypted_to_binary(encrypted) #Encrypted message encypted to binary
print("encrypted message in binary:",encrypt_binaraly, "with a length of", len(encrypt_binaraly), "bits") #explicits the length of the message in bits


decode_str= "".join([chr(int(encrypt_binaraly[i:i+8],2)) for i in range(0, len(encrypt_binaraly),8)]) #Decodes from binary, then from Unicode with the same process as the encoding, like reverse engineering
print ("decoded:",decode_str) #Prints the decoded message to see if it encoded and decoded correctly!





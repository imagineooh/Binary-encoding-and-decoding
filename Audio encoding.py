message = "Please come at 10 o'clock"
print("Original message:", message)


encrypted = [ord(c) for c in message]
def encrypted_to_binary(numbers):
    return "".join(bin(n)[2:].zfill(8) for n in numbers)

binary_message = encrypted_to_binary(encrypted)
print("Encrypted in binary:", binary_message)


from pydub import AudioSegment
from pydub.generators import Sine

def binary_audio_transfer(bits, filename="message2.wav"):
    audio = AudioSegment.silent(duration=0)
    for bit in bits:
        frequency = 1000 if bit == '1' else 500
        tone = Sine(frequency).to_audio_segment(duration=50)
        audio += tone
    audio.export(filename, format="wav")
    print(f"Audio message saved as '{filename}'")


binary_audio_transfer(binary_message)


#Name this file "data_handling". Make sure you don't forget the underscore :)

def make_to_binary(message: str)->str:
    encrypted = [ord(c) for c in message]
    def encrypted_to_binary(numbers):
        return "".join(bin(n)[2:].zfill(8) for n in numbers)
    return encrypted_to_binary(encrypted)

def binary_text(binary_string: str) -> str:
    characters=[chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)]
    return "".join(characters)

from pydub import AudioSegment
from pydub.generators import Sine

def binary_audio_transfer(bits, filename="Understand.wav"):
    audio = AudioSegment.silent(duration=0)
    for bit in bits:
        frequency = 1000 if bit == '1' else 500
        tone = Sine(frequency).to_audio_segment(duration=50)
        audio += tone
    audio.export(filename, format="wav")
    print(f"Audio message saved as '{filename}'")

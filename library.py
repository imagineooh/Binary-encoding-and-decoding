from data_handling import make_to_binary, binary_text, binary_audio_transfer
binary_message = make_to_binary("Hello World")
print(f"Binary Message: {binary_message}")
decoded_message = binary_text(binary_message)
print(f"Decoded Message: {decoded_message}")
binary_audio_transfer(binary_message, filename="output_message.wav")

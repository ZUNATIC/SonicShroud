import wave

def encode_audio(input_wav, secret_key, output_wav):
    # Audio file ko read mode mein open karein
    audio = wave.open(input_wav, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    # Key ke end mein marker lagaya taake decoder ko pata chale k key kahan khatam ho rahi hai
    secret_key += '###'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in secret_key])))

    # LSB (Least Significant Bit) replacement
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    
    modified_frames = bytes(frame_bytes)
    
    # Nayi audio file save karein keys/shadow_key.wav ke naam se
    with wave.open(output_wav, 'wb') as fd:
        fd.setparams(audio.getparams())
        fd.writeframes(modified_frames)
    audio.close()

def decode_audio(stego_wav):
    # Stego audio se bits nikalna
    audio = wave.open(stego_wav, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted_bits = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    
    # Bits to characters
    chars = []
    for i in range(0, len(extracted_bits), 8):
        byte = extracted_bits[i:i+8]
        chars.append(chr(int(''.join(map(str, byte)), 2)))
        if "".join(chars).endswith('###'): 
            break
    
    audio.close()
    return "".join(chars).replace('###', '')

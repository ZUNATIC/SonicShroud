import os
import wave
import struct
from core.stego import encode_audio, decode_audio
from core.engine import encrypt_data, decrypt_data

def test_stego_logic():
    # dummy audio
    test_wav = "test_sample.wav"
    output_wav = "test_shadow.wav"
    obj = wave.open(test_wav, 'w')
    obj.setnchannels(1)
    obj.setsampwidth(2)
    obj.setframerate(44100)
    for _ in range(1000):
        obj.writeframesraw(struct.pack('<h', 0))
    obj.close()

    #test hide/extract
    original_key = "ZunaticTest123"
    encode_audio(test_wav, original_key, output_wav)
    extracted_key = decode_audio(output_wav)
    
    os.remove(test_wav)
    os.remove(output_wav)
    assert original_key == extracted_key

def test_encryption_logic():
    key = "secret_key"
    data = "Hacked123"
    encrypted = encrypt_data(data, key)
    decrypted = decrypt_data(encrypted, key)
    assert data == decrypted

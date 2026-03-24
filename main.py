import os
import sqlite3
import sys
from core.stego import encode_audio, decode_audio
from core.engine import encrypt_data, decrypt_data

BANNER = "\033[1;32m" + r"""
 ██████  ██████  ███    ██ ██  ██████      ███████ ██   ██ ██████   ██████  ██    ██ ██████  
██      ██    ██ ████   ██ ██ ██           ██      ██   ██ ██   ██ ██    ██ ██    ██ ██   ██ 
██      ██    ██ ██ ██  ██ ██ ██           ███████ ███████ ██████  ██    ██ ██    ██ ██   ██ 
██      ██    ██ ██  ██ ██ ██ ██                ██ ██   ██ ██   ██ ██    ██ ██    ██ ██   ██ 
 ██████  ██████  ██   ████ ██  ██████      ███████ ██   ██ ██   ██  ██████   ██████  ██████  
                                                                                             
                          [ V1.0 - AUDIO STEGANO VAULT ]
                          [ DEVELOPED BY: ZUNATIC      ]
                          [ STATUS: STERN ENCRYPTION   ]
""" + "\033[0m"

DB_PATH = "data/vault.db"

def init_db():
    if not os.path.exists('data'): os.makedirs('data')
    if not os.path.exists('keys'): os.makedirs('keys')
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS vault (service TEXT, secret TEXT)")
    conn.close()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    init_db()
    clear_screen()
    print(BANNER)
    
    print("\033[1;34m[1]\033[0m Generate Shadow Key (Embed Key in Audio)")
    print("\033[1;34m[2]\033[0m Inject Secret into Vault")
    print("\033[1;34m[3]\033[0m Access & Decrypt Vault")
    print("\033[1;35m[4]\033[0m Rotate Master Key (Re-encrypt All)")
    print("\033[1;31m[5]\033[0m Exit")
    
    choice = input("\n\033[1;33m[?]\033[0m Access Level Selection: ")

    if choice == '1':
        orig = input("[>] Path to clean .wav file: ")
        if not os.path.exists(orig):
            print("\033[1;31m[!] Error: File not found!\033[0m")
            return
        key = input("[>] Enter Master Key String: ")
        try:
            # Output path fixed to shadow_key.wav
            encode_audio(orig, key, "keys/shadow_key.wav")
            print("\n\033[1;32m[+] SUCCESS: Shadow Key created at keys/shadow_key.wav\033[0m")
        except Exception as e:
            print(f"\n\033[1;31m[!] ERROR: {e}\033[0m")

    elif choice == '2':
        audio_key_path = input("[>] Provide Shadow Key (.wav): ")
        if not os.path.exists(audio_key_path):
            print("\033[1;31m[!] Error: Shadow Key file not found!\033[0m")
            return
        try:
            key = decode_audio(audio_key_path)
            service = input("[>] Target Service Name: ")
            secret = input("[>] Payload/Password: ")
            
            enc_secret = encrypt_data(secret, key)
            conn = sqlite3.connect(DB_PATH)
            conn.execute("INSERT INTO vault VALUES (?, ?)", (service, enc_secret))
            conn.commit()
            conn.close()
            print("\n\033[1;32m[+] SUCCESS: Data encrypted and vaulted.\033[0m")
        except Exception:
            print("\n\033[1;31m[!] FAILED: Invalid Shadow Key or decryption error.\033[0m")

    elif choice == '3':
        audio_key_path = input("[>] Upload Shadow Key to Authenticate: ")
        if not os.path.exists(audio_key_path):
            print("\033[1;31m[!] Error: File not found!\033[0m")
            return
        try:
            key = decode_audio(audio_key_path)
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.execute("SELECT * FROM vault")
            print("\n\033[1;34m" + "="*45 + "\033[0m")
            print(f"{'SERVICE':<20} | {'DECRYPTED SECRET':<20}")
            print("\033[1;34m" + "="*45 + "\033[0m")
            for row in cursor:
                print(f"{row[0]:<20} | {decrypt_data(row[1], key)}")
            conn.close()
        except Exception:
            print("\n\033[1;31m[!] AUTHENTICATION FAILED: Invalid Key or No Data.\033[0m")

    elif choice == '4':
        old_path = input("[>] Path to CURRENT Shadow Key: ")
        new_path = input("[>] Path to NEW Shadow Key (Generate first via Opt 1): ")
        
        if not os.path.exists(old_path) or not os.path.exists(new_path):
            print("\033[1;31m[!] Error: One or both files missing!\033[0m")
            return

        try:
            old_key = decode_audio(old_path)
            new_key = decode_audio(new_path)
            
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.execute("SELECT rowid, service, secret FROM vault")
            rows = cursor.fetchall()
            
            print("\033[1;33m[*] Migrating vault data to new key...\033[0m")
            for row in rows:
                rid, service, old_enc_secret = row
                dec_secret = decrypt_data(old_enc_secret, old_key)
                new_enc_secret = encrypt_data(dec_secret, new_key)
                conn.execute("UPDATE vault SET secret = ? WHERE rowid = ?", (new_enc_secret, rid))
            
            conn.commit()
            conn.close()
            print("\n\033[1;32m[+] SUCCESS: Vault migrated to New Shadow Key!\033[0m")
        except Exception as e:
            print(f"\n\033[1;31m[!] MIGRATION FAILED: {e}\033[0m")

    elif choice == '5':
        print("\033[1;33m[!] Exiting Sonic Shroud. Stay Secure.\033[0m")
        sys.exit()

if __name__ == "__main__":
    while True:
        main()
        input("\nPress Enter to return to menu...")

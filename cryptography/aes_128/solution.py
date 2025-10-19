import base64
from Crypto.Cipher import AES

def solve_challenge():
    key = b'YELLOW SUBMARINE'
    mode = AES.MODE_ECB

    try:
        with open("7.txt", 'r') as f:
            base64_text = f.read()

        byte_text = base64.b64decode(base64_text)
        
    except FileNotFoundError:
        print("Lỗi: Chạ tìm thấy file '7.txt' ")
        return

    cipher_aes = AES.new(key, mode)
    
    plaintext_bytes = cipher_aes.decrypt(byte_text)

    print(plaintext_bytes.decode('utf-8', errors='ignore'))

if __name__ == "__main__":
    solve_challenge()
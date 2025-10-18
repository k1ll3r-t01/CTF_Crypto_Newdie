import base64
from itertools import combinations

ENGLISH_FREQ = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074, ' ': 0.13000
}
#thống kê tần suất xuất hiện của các ký tự tiếng anh

def hamming_distance(bytes1: bytes, bytes2: bytes) -> int:
    if len(bytes1) != len(bytes2):
        raise ValueError("Input strings must have the same length.")
    
    xor_result = bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))
    distance = sum(bin(byte).count('1') for byte in xor_result)
    return distance
#tính kc hammintin giữa 2 chuỗi bằng cách xor 2 chuỗi đó và đếm sl bit 1 trên chuỗi mới

def find_keysize(ciphertext: bytes, min_size: int = 2, max_size: int = 40) -> list:
    normalized_distances = []
    for keysize in range(min_size, max_size + 1):
        chunks = [ciphertext[i*keysize:(i+1)*keysize] for i in range(4)]
        distances = [hamming_distance(c1, c2) for c1, c2 in combinations(chunks, 2)]
        avg_distance = sum(distances) / len(distances)
        normalized_distance = avg_distance / keysize
        normalized_distances.append((keysize, normalized_distance))
        
    sorted_keysizes = sorted(normalized_distances, key=lambda item: item[1])
    return [keysize for keysize, dist in sorted_keysizes[:5]]
#tìm keyzize có khả năng cao nhất bằng kc chuẩn hóa hamminton nhỏ nhất

def score_text(text: bytes) -> float:
    score = 0
    text_lower = text.lower()
    for char_code in text_lower:
        char = chr(char_code)
        if char in ENGLISH_FREQ:
            score += ENGLISH_FREQ[char]
    return score
#tính điểm của text
def solve_single_byte_xor(ciphertext: bytes) -> tuple:
    best_result = (None, None, 0)
    for key_candidate in range(256):
        keystream = bytes([key_candidate]) * len(ciphertext)
        plaintext_candidate = bytes([c ^ k for c, k in zip(ciphertext, keystream)])
        try:
            decoded_text = plaintext_candidate.decode('ascii')
            current_score = score_text(plaintext_candidate)
            if current_score > best_result[2]:
                best_result = (key_candidate, plaintext_candidate, current_score)
        except UnicodeDecodeError:
            continue
    return best_result
#Phá khóa xor 1 ký tự

def break_repeating_key_xor(ciphertext: bytes) -> tuple:
    possible_keysizes = find_keysize(ciphertext)
    best_keysize = possible_keysizes[0]
    final_key = b''
    
    transposed_blocks = [b''] * best_keysize
    for i in range(len(ciphertext)):
        transposed_blocks[i % best_keysize] += bytes([ciphertext[i]])
        #Transpose
        
    for block in transposed_blocks:
        key_byte, _, _ = solve_single_byte_xor(block)
        if key_byte is not None:
            final_key += bytes([key_byte])
            #lắp ráp key

    key_stream = (final_key * (len(ciphertext) // len(final_key) + 1))[:len(ciphertext)]
    plaintext = bytes([c ^ k for c, k in zip(ciphertext, key_stream)])
    #dùng key cuối để giải mã
    return (final_key, plaintext)
# hàm điều phối

if __name__ == "__main__":
    try:
        with open("6.txt", "r") as f:
            base64_content = f.read()
            ciphertext = base64.b64decode(base64_content)
            
            key, plaintext = break_repeating_key_xor(ciphertext)
            
            print("--- Attack Results ---")
            print(f"[*] Best Keysize Found: {len(key)}")
            print(f"[*] Discovered Key: {key.decode('ascii', errors='ignore')}")
            print("\n--- Decrypted Plaintext ---")
            print(plaintext.decode('ascii', errors='ignore'))

    except FileNotFoundError:
        print("Error: File '6.txt' not found. Please create this file and paste the ciphertext into it.")
    except Exception as e:
        print(f"An error occurred: {e}")
## Writeup Single-byte XOR cipher
> Đề bài: 
Cho dãy hex: `1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736`
> Hint:
>- Đã được XOR với single character
>- Hãy code, đừng tìm thủ công
>- Bằng cách tính điểm, sự xuất hiện thường xuyên so với văn bản Tiếng anh
>- "ETAOIN SHRDLU"
---
### Solution
Ở bài này ta có thể XOR với các giá trị từ 1 -> 255 và nhìn bằng mắt để tìm ra được flag

Cách khác nhanh hơn đó là ta sẽ lần lượt tạo ra các hàm dựa theo hint.

- Hàm tính điểm
- Hàm XOR
- Hàm cập nhật điểm

```python
import binascii

EL_fre = "ETAOIN SHRDLU"

def score_text(text):
    score = 0
    for char in text.upper():
        if char in EL_fre:
            score += 1
    return score
    #hàm tính điểm

def break_single_byte_xor(hex_string):
    try:
        ciphertext = binascii.unhexlify(hex_string)
    except binascii.Error:
        return None, "Lỗi: Chuỗi hex không hợp lệ."

    best_score = 0
    best_key = None
    best_plaintext = ""
    #xác định những chuỗi hex kh hợp lệ

    for key in range(256):
        plaintext_bytes = bytes([byte ^ key for byte in ciphertext])
        decoded_text = plaintext_bytes.decode('utf-8', errors='ignore')
        current_score = score_text(decoded_text)
        #tính điểm của từng kq phép xor
        if current_score > best_score:
            best_score = current_score
            best_key = key
            best_plaintext = decoded_text
        #cập nhật điểm
    return best_key, best_plaintext

if __name__ == "__main__":
    hex_input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    
    found_key, decrypted_text = break_single_byte_xor(hex_input)
    #nhập dữ liệu vào và gọi hàm
    print(f"Khóa tìm thấy (dạng ký tự): {chr(found_key)}")
    print(f"Khóa tìm thấy (dạng số): {found_key}")
    print(f"Văn bản đã giải mã: {decrypted_text}")
    
```
Ra được kết quả:

`Khóa tìm thấy (dạng ký tự): X`

`Khóa tìm thấy (dạng số): 88`

`Văn bản đã giải mã: Cooking MC's like a pound of bacon`
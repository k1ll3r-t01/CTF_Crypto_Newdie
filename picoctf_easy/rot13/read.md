## Writeup rot13
đây là thuật toán thay thế chữ cái đơn giản, ROT13 sử dụng xoay vòng một nửa bảng chữ cái (13 chữ cái)
VD: 'c' rot13 -> 'p' rot13 -> p
> Đề bài: 
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

Solution:

Sử dụng code đơn giản để xoay vòng 13 ký tự:
```python
flag_rot13 = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'
flag = ''
offset = 13

for char in flag_rot13:
    if 'a' <= char <= 'z':
        flag += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        flag += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        flag+=char

print(flag)

```
> Ra được flag:
`picoCTF{not_too_bad_of_a_problem}`
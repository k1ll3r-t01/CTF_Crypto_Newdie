## Writeup interencdec
>Đề bài: 
Can you get the real meaning from this file.
Download the file `here`.
Hint: Engaging in various decoding processes is of utmost importance

### Solution
- Ta nhận thấy được đây là các ký tự được mã hóa base64.
`YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==`
- Ta thử decode ra và được string cũng được mã hóa base64.
`d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ==`
- Ta tiếp tục và được:
`wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}`
Code:
```python
flag=''
flagc='wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}'
for i in flagc:
    if i>= 'a' and i <= 'z':
        c=chr((ord(i)- ord('a')-7)%26+ord('a'))
        flag+=c
    elif i>= 'A' and i <= 'Z':
        d=chr((ord(i)- ord('A')-7)%26+ord('A'))
        flag+=d
    else: 
        flag+=i
print(flag)
```
Ra được flag: 
`picoCTF{caesar_d3cr9pt3d_890d2379}`
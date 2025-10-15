# s='YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg=='
# import base64
# flag=''
# decode_s=base64.b64decode(s)
# a= 'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='
# decode_a=base64.b64decode(a)
# print(decode_s, decode_a)
flag=''

flagcc='wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}'
for i in flagcc:
    if i>= 'a' and i <= 'z':
        c=chr((ord(i)- ord('a')-7)%26+ord('a'))
        flag+=c
    elif i>= 'A' and i <= 'Z':
        d=chr((ord(i)- ord('A')-7)%26+ord('A'))
        flag+=d
    else: 
        flag+=i
print(flag)
## Writeup Numbers

> Đề bài: The numbers... what do they mean?
`16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }`

Solution:

Bài này ta phân tích được là với mỗi số đầu ở hình ảnh được cho tương ứng với pico{, ta thử tính toán được mã ASCII con sô đầu và của 'p' cách nhau 96.
-> 
Code:
```python
number=[16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14, '}']
flag=''
for i in number:
    if type(i)==int:
        if i >= 1 and i <= 21:
            i+=96
        a=chr(i)
        flag+=a
    else:
        flag+=i
    
print(flag)

```

Ra được flag:
`picoctf{thenumbersmason}`
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


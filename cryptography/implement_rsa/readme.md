# Writeup Implement RSA

> ### Mục tiêu:
> Mô phỏng được mã RSA được tạo ra như thế nào.
--- 
### Cách tiếp cận:
- Biết và code được Eucid và Ex Eulclid.
- Biết được modul và nghịch đảo modul
- Kết hợp lại và hoàn thiện code.
--- 
### Modul và nghịch đảo modul
- Modul là "kích thước" của một vòng lặp số.
Trong toán tử gọi là phép chia lấy dư.

- Nghịch đảo modulo của `A` theo modul M là một số `A_inv` sao cho: 

`(A * A_inv) mod M = 1`

---
Ta sẽ viết được 2 hàm là `gcd()` (tìm UCLN) 
```python
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
```

Hàm `egcd()` (tìm tổ hợp tuyến tính của gcd(a,b) )
```python
def egcd(a,b):  
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1              
    return x0, y0, a
```

Chúng ta tiếp tục tạo khóa public và private:
```python

def egcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def invmod(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Nghịch đảo modulo không tồn tại')
    else:
        return x % m

def gen_key(p, q):
    n = p * q
    et = (p - 1) * (q - 1)
    
    e = 3
    
    #nẾU e và et không là hai số nguyên tố cùng nhau thì không tìm ra được nghịch đảo modul
    g, _, _ = egcd(e, et)
    if g != 1:
        raise Exception(f'e={e} và et={et} không phải số nguyên tố cùng nhau. '
                        f'Hãy chọn p và q khác sao cho (p-1) và (q-1) không chia hết cho 3.')

    d = invmod(e, et)
    
    # Khóa công khai là (e, n)
    # Khóa bí mật là (d, n)
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def encrypt(public_key, message_int):
    e, n = public_key
    # Công thức mã hóa: c = m^e mod n
    ciphertext = pow(message_int, e, n)
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    # Công thức giải mã: m = c^d mod n
    message_int = pow(ciphertext, d, n)
    return message_int


```

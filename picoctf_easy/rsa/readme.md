# Writeup `EVEN RSA CAN BE BROKEN`
> ### Mục tiêu:
> #### Tìm được lõ hỗng qua cách tạo khóa bí mật _privat qua cod được cho ở `encrypt.py`. Từ đó giải mã được khóa RSA.

---
### Solution
- Kết nối tới cổng được cho `nc verbal-sleep.picoctf.net 49640` ta có được các con số:

`N`: 21178413619860379831491009225079292698557074947963265016822798573634951851635913129236504885143150013099852336392671898174766355541242987936646009813685258

 `e`: 65537

`cyphertext`: 9978850374552365270318384032993234546331380016096545448898402317575638857691980129632379347784152030760169679658826919725533011560800994614583174414065935


Ta đọc được ở đoạn code để hiểu thêm về cách mà `RSA` tạo ra khóa, nhận thấy:

```python
def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)
```
Nhận thấy được `p`, `q` được tạo ra 2 số nguyên tố ngẫu nhiên lớn.
Mà `N` chẵn nên ta có 1 trong 2 số chính là số 2

- Từ đó ta có được 

```python
phi_N = (p-1)(q-1) = N/2 -1
```
Ta tiếp tục sử dụng các hàm ở file encryp.py để tìm ra khóa `d` bị ẩn dấu.
```python
from Crypto.Util.number import long_to_bytes

N = 23874943750441657209739135156032093741192494272608524974728302529891674591260893045364844822783893556804098879188439422288162313735664384378250207736243222
e = 65537

q = N // 2
phi_N = q - 1
d = pow(e, -1, phi_N)

c = 15142244487705944403311273969269898421118424973686456167719038649896630424586339225905764625665657234062822314722067381498604397117790377556382549976018883
m = pow(c, d, N)
flag = long_to_bytes(m)
print(flag)

```

>Ra được flag là: `picoCTF{tw0_1$_pr!m375129bb1`
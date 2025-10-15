## Writeup Hashcrack
> Đề bài: A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
Access the server using `nc verbal-sleep.picoctf.net 58511`

### Solution:

Ở bài này chúng ta sẽ giải quyết các hàm băm, SHA256, MD5sum,... để có thể kết nối tới server và lấy mật khẩu.

- `482c811da5d5b4bc6d497ffa98491e38`
Giải mã ra được mk: `password123`

- `b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3`
Tiếp tục được mk: `letmein`

- `916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745`

Cuối cùng mk:   `qwerty098`

Sau khi nhập hết ta có được flag:
` picoCTF{UseStr0nG_h@shEs_&PaSswDs!_6965e43b}`

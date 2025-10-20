# Writeup Detect AES in ECB mode
> #### Mục tiêu:
 > Tìm ra được văn bản nghi ngờ nhất bằng cách hiểu được cách mà mode ECB hoạt động



 Hãy dễ hình dung thì mode ECB giống kiểu mật mã đã được định sẵn. 

 VD:
  a sẽ được chuyển thành c

  b thành d

  Khi mã háo a b a thì sẽ được c d c 

 và ta sẽ dễ dàng thấy được điểm yếu của nó là chính là sự lặp lại

 >-> Bằng cách đếm số lượng lặp lịa cái nào nhiều nhất thì dòng đó có khả năng cao đó chính là dữ liệu AES (Bởi vì Tiếng anh tần suất xuất hiện nó lớn)
---
## Solution
Như thế chúng ta sẽ tạo ra các đoạn code như sau
```python
def solve_challenge_8():
    with open('8.txt', "r") as file:
        lines = file.read().splitlines()
#đọc từng dòng của file
   
    max_score = 0
    ecb_line = ""
    line_number = 0
#các giá trị lưu kết quả

    for i, hex_line in enumerate(lines): #vòng lặp duyệt qua từng dòng (chỉ số, giá trị)
        ciphertext_byte = bytes.fromhex(hex_line)

        blocksize = 16#số bytes xử lý của mode ECB
        blocks = []
        for j in range(0, len(ciphertext_byte), blocksize):
            blocks.append(ciphertext_byte[j:j+blocksize])#tách ra từng khối 16bytes trên từng hàng
        
        total_blocks = len(blocks)
        s_block = set(blocks)
        score = total_blocks - len(s_block)
        #so sánh để xem có bao nhiêu sự trùng lặp

        if score > max_score:
            max_score = score
            ecb_line = hex_line
            line_number = i + 1 
        #tìm ra khối có sự trùng lặp lớn nhất

    # In kết quả cuối cùng
    print(f"Dòng có khả năng mã hóa ECB nhất là dòng số: {line_number}")
    print(f"Số khối bị lặp lại (điểm số): {max_score}")
    print(f"Nội dung dòng đó:\n{ecb_line}")

# Chạy chương trình
solve_challenge_8()
```
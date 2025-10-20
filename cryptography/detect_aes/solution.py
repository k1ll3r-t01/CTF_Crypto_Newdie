def solve_challenge_8():
    with open('8.txt', "r") as file:
        lines = file.read().splitlines()

    # Biến để lưu lại kết quả tốt nhất
    max_score = 0
    ecb_line = ""
    line_number = 0

    for i, hex_line in enumerate(lines): #vòng lặp duyệt qua từng dòng (chỉ số, giá trị)
        ciphertext_byte = bytes.fromhex(hex_line)

        blocksize = 16
        blocks = []
        for j in range(0, len(ciphertext_byte), blocksize):
            blocks.append(ciphertext_byte[j:j+blocksize])
        
        total_blocks = len(blocks)
        s_block = set(blocks)
        score = total_blocks - len(s_block)

        if score > max_score:
            max_score = score
            ecb_line = hex_line
            line_number = i + 1 

    # In kết quả cuối cùng
    print(f"Dòng có khả năng mã hóa ECB nhất là dòng số: {line_number}")
    print(f"Số khối bị lặp lại (điểm số): {max_score}")
    print(f"Nội dung dòng đó:\n{ecb_line}")

# Chạy chương trình
solve_challenge_8()
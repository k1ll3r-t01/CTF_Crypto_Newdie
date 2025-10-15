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
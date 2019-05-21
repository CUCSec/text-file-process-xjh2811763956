with open('lenna.bmp', 'r+b') as f:
    a = [2, 10, 1, 8, 1, 1, 1, 2, 3, 10, 10, 9]
    offset = 54

    for i in a:
        offset += i * 3
        f.seek(offset)
        f.write(b'\x00\x00\x00')
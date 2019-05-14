with open('lenna.bmp', 'r+b') as f:
    a = [10, 1, 8, 1, 1, 1, 2, 3, 10, 10, 9]
    f.seek(54 + 2)
    f.write(b'\x00\x00\x00')
    for i in a:
        f.seek(i, 1)
        f.write(b'\x00\x00\x00')

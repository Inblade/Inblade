from PIL import Image, ImageEnhance, ImageOps

W = 46          # columns
ramp = " .:;irsXA253hMHGS#9B&@"  # light -> dark (for light bg); invert for dark bg

im = Image.open('avatar.png').convert('L')
im = ImageOps.autocontrast(im, cutoff=2)
im = ImageEnhance.Contrast(im).enhance(1.25)
H = int(W * im.height / im.width * 0.5)
im = im.resize((W, H))

rows = []
for y in range(H):
    row = ''
    for x in range(W):
        v = im.getpixel((x, y)) / 255
        # dark pixel -> dense char
        idx = int((1 - v) * (len(ramp) - 1))
        row += ramp[idx]
    rows.append(row.rstrip())

open('ascii.txt', 'w').write('\n'.join(rows))
print('\n'.join(rows))

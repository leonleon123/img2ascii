from PIL import Image, ImageEnhance, ImageOps
import sys

def main():
    if sys.argv[1] == '--help' or len(sys.argv) < 7 or len(sys.argv) > 7:
        print("Usage: python3 imageProc.py <image> <width in px> [invert] [contrast] [sharpness] [brightness]",
            " <image>         .... path to the source image",
            " <width>         .... number of characters in a line",
            " [invert]        .... 0 for original, 1 for inverted",
            " [contrast]      .... 1 for original, 0-1 for less, >1 for more",
            " [sharpness]     .... 1 for original, 0-1 for less, >1 for more",
            " [brightness]    .... 1 for original, 0-1 for less, >1 for more",
            sep="\n")
        exit()
    else:
        imageName = sys.argv[1]

    ASCII = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    RES = int(sys.argv[2])
    adjust = [float(x) for x in sys.argv[3:]]
    im = Image.open(imageName).convert("RGB")
    enhancments = [ImageEnhance.Contrast(im), ImageEnhance.Sharpness(im), ImageEnhance.Brightness(im)]

    for i in range(3):
        enhancer = enhancments[i]
        im = enhancer.enhance(adjust[i+1])

    im = ImageOps.invert(im) if adjust[0] == 1 else im
    RES = im.size[0] if RES >= im.size[0] else RES
    size = (RES, im.size[1]*(RES/im.size[0]))
    im.thumbnail(size, Image.ANTIALIAS)

    for j in range(0, int(size[1])):
        for i in range(0, int(size[0])):
            val = int( (im.getpixel((i,j))[0] + im.getpixel((i,j))[1] + im.getpixel((i,j))[2]) /3)
            print(ASCII[int((val/255)*len(ASCII))-1], end=" ")
        print()

if __name__ == "__main__":
    main()
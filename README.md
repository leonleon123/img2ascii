# img2ascii
Short python script that transforms image to ASCII characters

Run in the directory with the image you want to transform. Width in px (second command
line argument) is how many characters wide the ASCII picture is going to be. Following options 
(invert, contrast, sharpness and brightness) are there to tinker with them in order to get
best results possible. Invert usually helps when picture is colorful and with higher level
of detail. For logos or simple shapes it usually doesn't make that much of a difference.

Usage: 

            python imageProc.py <image> <width in px> [invert] [contrast] [sharpness] [brightness]
            
            <image>         .... path to the source image
            
            <width>         .... number of characters in a line
            
            [invert]        .... 0 for original, 1 for inverted
            
            [contrast]      .... 1 for original, 0-1 for less, >1 for more
            
            [sharpness]     .... 1 for original, 0-1 for less, >1 for more
            
            [brightness]    .... 1 for original, 0-1 for less, >1 for more
            

Made with python 3.7.1

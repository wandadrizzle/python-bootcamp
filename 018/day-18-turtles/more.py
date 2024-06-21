# Challenge 6 - MILLION DOLLAR PAINTING, The Hirst Painting Project
import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

# https://chocolatey.org/install#individual - this didn't work
# pillow-10.3.0-cp311-cp311-win_amd64.whl from https://www.wheelodex.org/projects/pillow/
# pip install "LOCATION OF DOWNLOAD" --force-reinstall

#  ERROR: Failed building wheel for Pillow
# ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (Pillow)

# PS C:\Windows\system32> pip --version
# pip 24.1 from C:\Python311\Lib\site-packages\pip (python 3.11)

# What's going on? https://sourceforge.net/projects/zlib/, [THIS ONE!!] https://zlib.net/

'''
1. I downloaded the permalink
2. Extracted the zip
3. Opened the cmd [Press Win + R, type cmd, and press Enter.]
4. cd path-to-extracted-directory
5. .\configure
6. nmake -f win32\Makefile.msc

---DEAD END

Okay, so turns out I need to install CMAKE then do what they say I should do here: https://github.com/horta/zlib.install
This might also be helpful: https://eclipsebook.in/appendix/setting-up-zlib/
This came up from time to time: http://www.libpng.org/pub/png/libpng.html

15:38 ANGISAZI KE MANJE - https://pillow.readthedocs.io/en/latest/installation/building-from-source.html#building-from-source


'''

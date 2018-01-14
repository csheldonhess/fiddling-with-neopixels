import board
import neopixel
import time
import random
 
pixpin = board.D1
numpix = 10
 
# brightness goes from 0 (no light) to 1.0 (full brightness)
# auto_write=True makes it so you don't have to call strip.write()
#   to change a value, but it makes thing slower(?) 
strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.5, auto_write=False)

# this will be used as in incrementor, to keep track of which neopixel
#   we are currently looking at
i = 0

# this just turns off all of the neopixels to start
# it is nice for making sure the code updated :)
strip.fill((0, 0, 0))

while True:
    # set the current LED to a random color of purple
    # red is a random value between 120 and 255
    # green is zero
    # blue is a random value between 120 and 255
    strip[i] = (random.randrange(120, 255, 1), 0, random.randrange(120, 255, 1))
    strip.write()
    # wait a second 
    time.sleep(1)
    # move on to the next neopixel in the strip
    i = i + 1
    # if incrementing i took us past the end of the strip, go back to start
    if i >= numpix:
        i = 0

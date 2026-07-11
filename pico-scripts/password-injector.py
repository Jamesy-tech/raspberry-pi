# Made for Raspberry Pi Pico 2 W using CircutPython
# code.py

import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(0)

layout.write("password")
kbd.send(Keycode.ENTER)

time.sleep(100000000)

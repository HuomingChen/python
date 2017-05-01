#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PIL import Image


im = Image.open(r'd:\test.png')
print(im.format, im.size, im.mode)
print(im)

print(sys.path)

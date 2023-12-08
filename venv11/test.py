#!/usr/bin/env python3
import os

## basic path setup
path = os.path.abspath(__file__)

path = os.path.dirname(path)


os.chdir(path)

print("os.path.dirname(os.path.abspath(__file__)) :  "
       + path)
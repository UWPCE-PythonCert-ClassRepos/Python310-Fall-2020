#!/usr/bin/env python

"""
A really simple script just to demonstrate packaging
"""

import sys, os
from capitalize import capital_mod
from capitalize import main

import sys
for p in sys.path:
    print(p)

if __name__ == "__main__":
    main.main()    

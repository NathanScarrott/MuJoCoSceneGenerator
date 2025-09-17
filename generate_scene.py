#!/usr/bin/env python3
"""
MuJoCo Scene Generator Launcher
Simple launcher script to run the scene generator from the project root.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

os.chdir(os.path.join(os.path.dirname(__file__), 'src'))
from mujo_generator import main

if __name__ == "__main__":
    main()

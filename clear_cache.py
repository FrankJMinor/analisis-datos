# -*- coding: utf-8 -*-

# standar library
import os

CLEAR_CACHE = f"""find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf"""
os.system(CLEAR_CACHE)
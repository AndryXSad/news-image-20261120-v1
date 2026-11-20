#!/usr/bin/env python3
"""Copy the pre-rendered entry image to the output directory.

Standard library only. No network access. Writes exactly one file,
entry.png, to MAKEFUN_OUTPUT_DIR (or /output when unset).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))

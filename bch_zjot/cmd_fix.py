#!/usr/bin/env python3

import bch_zjot.util as UU

def cmd_fix():
    for pth in UU.fresh():
         for line in lines4pth(pth):
             fix_line(line)
         UU.stow_path(pth)

def fix_line(line):
    UU.append4pth4line(UU.fixed4line(line), line)

def lines4pth(pth):
    yield from pth.read_text().split('\n')


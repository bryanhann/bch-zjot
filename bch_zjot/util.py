import os
import string
import datetime
from pathlib import Path

SPACE=' '
ACC=Path(os.environ.get("ZJOT_ACC") or Path.home()/"ZJOT")
SEEN  = ACC/'seen'
FIXED = ACC/'fixed'

ACC.is_dir() or ACC.mkdir()
SEEN.is_dir() or SEEN.mkdir()
FIXED.is_dir() or FIXED.mkdir()

def fresh():
    yield from sorted(ACC.glob('*.zjot'))

def fixed():
    yield from sorted(FIXED.glob('*'))

def fixed4line(line):
    assert line[8] == 'T'
    fixed = FIXED/f"{line[:9]}.jots"
    fixed.touch()
    return fixed

def append4pth4line(pth,line):
    pth.touch()
    pth.write_text( pth.read_text() + line + '\n' )

def NOW():
    return datetime.datetime.now().strftime("%Y%m%dT%H%M%S")

def stow_path(pth):
    pth.rename(SEEN/pth.name)

def dump_all_jots():
    for pth in fixed():
        print(pth)
        print(pth.read_text())
    print('fresh')
    for pth in fresh():
        print(pth.read_text())


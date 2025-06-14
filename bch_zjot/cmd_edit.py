import os

import bch_zjot.util as UU

EDITOR=os.environ.get("EDITOR")

def cmd_edit():
    if EDITOR:
        os.system( f" {EDITOR} {UU.fixed4line(UU.NOW())}")
    else:
        print('Environment variable $EDITOR is not set')


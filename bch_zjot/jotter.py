import os
import datetime
import string
from pathlib import Path
from typing import List

import typer

ZJOT_ACC=os.environ.get("ZJOT_ACC") or Path.home()/"ZJOT"
ZJOT_ACC=Path(ZJOT_ACC)

app = typer.Typer()

@app.command()
def show ( acc: str=ZJOT_ACC ):
    STORE=Path(acc)
    for file in sorted(STORE.glob('*.zjot.acc')):
        print( f"""---------------------- {file.name}""")
        print( file.read_text() )
    print( f"""---------------------- {ZJOT_ACC}""")
    for file in sorted(STORE.glob('*.zjot')):
        line = file.read_text().strip()
        print( line )

def is_tag(x):
    return x.startswith('{') and x.endswith('}')

@app.command()
def new (
    args: List[str]=typer.Argument(None),
    short: bool=typer.Option(
        False,
        is_flag=True,
        help="Short jot (don't prompt for extra lines)")
    ):
    ZJOT_ACC.is_dir() or ZJOT_ACC.mkdir()
    args = args or []
    tags = ['{zjot}']
    while args and is_tag(args[0]):
        tags.append(args.pop(0))
    tags = ' '.join(tags)
    prefix = ' '.join(args)
    left = f"{tags} | {prefix}"

    now = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    acc = []
    if not short:
        show()
        print (f">>>>>>>>>>>>>>>>>>>>>> {tags} | {prefix} |" )
        while extra := input().strip():
            acc.append( extra )
    right = ' | '.join(acc)
    line=f"{now} {tags} | {prefix} | {right}"
    if False in [ ch in string.printable for ch in line ]:
        exit( 'cannot jot line with unprintable characters:' )
    (ZJOT_ACC/f"{now}.zjot").write_text(line)
    print(line)

@app.command()
def join ():
    if not ZJOT_ACC.is_dir():
        return
    def text4zjot(zjot):
        assert zjot.name.endswith('.zjot')
        return zjot.read_text().strip()+'\n'
    files = list(sorted(ZJOT_ACC.glob('*.zjot')))
    if not files:
        # nothing to join
        return
    lines = list(map(text4zjot, files))
    block = ''.join(lines)
    first = files[0]
    join_file = Path(f"{first}.acc")
    join_file.write_text(block)
    for file in files:
        os.remove(file)


if __name__=='__main__':
    main()

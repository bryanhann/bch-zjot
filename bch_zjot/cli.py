from typing import List

import typer

import bch_zjot.cmd_edit as cmd_edit
import bch_zjot.cmd_show as cmd_show
import bch_zjot.cmd_new as cmd_new
import bch_zjot.cmd_fix as cmd_fix

cli = typer.Typer()

@cli.command()
def show():
    cmd_show.cmd_show()

@cli.command()
def edit():
    cmd_edit.cmd_edit()

@cli.command()
def new (
    args: List[str]=typer.Argument(None),
    short: bool=typer.Option( False, is_flag=True,
        help="Short jot (don't prompt for extra lines)")
    ):
    args = args or []
    cmd_new.cmd_new(args, short)

@cli.command()
def fix():
    cmd_fix.cmd_fix()

if __name__=='__main__':
    main()

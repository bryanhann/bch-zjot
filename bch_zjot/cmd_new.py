#!/usr/bin/env python3

def cmd_new(args,short):
    import bch_zjot.util as UU
    now = UU.NOW()
    pth = UU.ACC/f"{now}.zjot"
    line = line4args(args)
    if not short:
        UU.dump_all_jots()
        print(line)
        line = line + get_extra()
    line = line.strip()
    line = f"{now} {line}"
    pth.write_text(line)
    UU.dump_all_jots()


def line4args(args):
        SPACE=' '
        def is_tag(x): return x.startswith('{') and x.endswith('}')
        args = [ '{zjot}' ] + args + ['']
        tags = []
        while is_tag(args[0]):
            tags.append(args.pop(0))
        return "%s | %s" % (SPACE.join(tags), SPACE.join(args))

def get_extra():
        import string
        def good(ch): return ch in string.printable
        acc = []
        while True:
            while not all(map(good, line:=input('-->'))):
                print( '<unprintable characters>' )
            acc.append(line)
            if acc[-2:] == ['','']:
                return " | ".join(acc[:-2])


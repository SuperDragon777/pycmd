import sys
import os
import tooly
import cmd

version = "0.1"
tooly.triangle()
colors = tooly.ColorSystem()

class PYCMD(cmd.Cmd):
    intro = f"PYCMD [Version {version}]\n(c) SuperDragon777. All rights reserved.\n"
    prompt = f"{os.getcwd()}>"
    def do_exit(self, args):
        sys.exit(0)
    def default(self, line):
        print(colors.warning(f"Проверьте написание команды: {line}"))

if __name__ == '__main__':
    try:
        PYCMD().cmdloop()
    except KeyboardInterrupt:
        sys.exit(0)
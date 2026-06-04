import sys
import os
import tooly
import cmd

version = "0.2"
tooly.triangle()
colors = tooly.ColorSystem()

class PYCMD(cmd.Cmd):
    intro = f"PYCMD [Version {version}]\n(c) SuperDragon777. All rights reserved.\n"
    prompt = f"{os.getcwd()}>"
    def do_exit(self, args):
        sys.exit(0)
    def do_cd(self, args):
        if not args:
            print(os.getcwd())
            return
        try:
            os.chdir(args)
            self.prompt = f"{os.getcwd()}>"
        except FileNotFoundError:
            print(colors.warning(f"Директория не найдена: {args}"))
        except NotADirectoryError:
            print(colors.warning(f"Это не директория: {args}"))
        except PermissionError:
            print(colors.warning(f"Нет доступа: {args}"))

    def do_ls(self, args):
        path = args.strip() or os.getcwd()
        try:
            entries = os.listdir(path)
            for entry in sorted(entries):
                full = os.path.join(path, entry)
                if os.path.isdir(full):
                    print(f"[DIR]  {entry}")
                else:
                    print(f"       {entry}")
        except FileNotFoundError:
            print(colors.warning(f"Директория не найдена: {path}"))
        except PermissionError:
            print(colors.warning(f"Нет доступа: {path}"))

    def default(self, line):
        print(colors.warning(f"Проверьте написание команды: {line}"))

if __name__ == '__main__':
    try:
        PYCMD().cmdloop()
    except KeyboardInterrupt:
        sys.exit(0)
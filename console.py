#!/usr/bin/python3
"""
Entry point module for Console program
"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """The Console Program"""
    prompt="(hbnb) "
    def do_quit(self, _):
        """quit"""
        sys.exit()

    def do_EOF(self, _):
        """EOF"""
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()

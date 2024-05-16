#!/usr/bin/python3

import cmd
import fileinput
"""PYTHON COMMAND INTERPRETER"""


class HBNBcommand(cmd.Cmd):
    """command process"""
    prompt = "(hbnb) "


    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """command to handel the end of the file"""
        return True

    def run_command(self, command):
        """execute a single command"""
        self.onecmd(command)

    def postcmd(self, stop, line):
        """call after each execution"""
        self.prompt = '(hbnb) '
        return super().postcmd(stop, line)

    def run_command_from_file(self, filepath):
        """execute command from file"""
        while True:
            user_input = input("(hbnb) ").strip()
            if user_input == "quit":
                break
            elif user_input == "help":
                pass
            else:
                return


if __name__ == '__main__':
    HBNBcommand().cmdloop()

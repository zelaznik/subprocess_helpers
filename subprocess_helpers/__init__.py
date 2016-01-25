
""" Used for consolidating GitHub repos in bulk. """
from subprocess import CalledProcessError, check_output, STDOUT
from os import mkdir, walk, rename, getcwd, chdir
from os.path import split, join, exists, isdir
from shutil import rmtree
import sys
__all__ = ['InvalidCommand','do','attempt']

class InvalidCommand(RuntimeError):
    """ Used only when a subprocess has a return code > 0. """
    def __init__(self, cmd, exc):
        args = (cmd, exc.returncode, exc.output)
        msg = """Command: %s\nStatus(%d): %s""" % args
        RuntimeError.__init__(self, msg)
        self.cmd = cmd
        self.exc = exc

def do(cmd):
    """ Wrapper to run command line scripts in Python.
        Re-raises errors if exit code > 0.
    """
    print(cmd)
    try:
        cmnd_output = check_output(cmd, stderr=STDOUT, shell=True)
        if cmnd_output:
            print(cmnd_output)
        return True
    except CalledProcessError as exc:
        e = exc
    raise InvalidCommand(cmd, e)

def attempt(cmd, silent=False):
    """ Just like 'do' but it ignores the errors.
        'silent' decides whether to print the error messages.
    """
    try:
        do(cmd)
        return
    except InvalidCommand as exc:
        e = exc

    if not silent:
        print(str(e))

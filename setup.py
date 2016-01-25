from distutils.core import setup

def test():
  import unittest
  import tests
  unittest.main()

setup(
    name     = 'subprocess_helpers',
    version  = '1.0',
    url      = 'https://github.com/zelaznik/subprocess_helpers',
    author       = 'Steve Zelaznik',
    author_email = 'steve.zelaznik@gmail.com',

    description = """ A set of helper functions to make it easier to run subprocesses in Python. """,

    packages = ['subprocess_helpers'],
    license  = 'MIT License',
    test_suite = 'tests',
    cmds = {
      'test': test
    }
)

# -*- coding: utf-8 -*-
"""
.. module:: ptreader
    :platform: Unix, Windows
    :synopsis: Reader for binary blob print-files for HP P-Touch series
    printers.

.. moduleauthor:: Terje Elde <terje@elde.net>

"""

from __future__ import print_function

import io
from binascii import unhexlify

cmds = {}


# Keeping a dictionary, where we map command-bytes to command-handlers.
# Decorators on the handlers map their command-bytes to them, so we keep
# everything for the handler together with it's definition.
def cmd(byte):
    def cmd_sub(c):
        cmds[unhexlify(byte)] = c
    return cmd_sub


class PTReader(object):
    """Reader-class for reading binary blob printer-files for HP P-Touch
    series of label-printers.
    """

    def __init__(self, input=None):
        """Initialize reader.

        Args:
            input (str or file): Path of file, or file-like object, that we'll
            be reading our input-data from.
        """

        if input:
            if type(input) in [str, unicode]:
                self._input = io.open(input)
            else:
                self._input = input

    def read(self, input=None):

        self._input.seek(0)

    @cmd('1B')  # 1B40 == initialize, 1B69 == other command
    def cmd_(self):
        print("--> cmd_")

    @cmd('4D')
    def cmd_compression(self):
        print("--> cmd_compression")

    @cmd('67')
    def cmd_raster(self):
        print("--> cmd_raster")

    @cmd('1A')
    def cmd_print_eject(self):
        print("--> cmd_print_eject")

    @cmd('FF')
    def cmd_print_no_eject(self):
        print("--> cmd_print_no_eject")


if __name__ == '__main__':
    ptr = PTReader()
    print("cmds: %r" % cmds)

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

subs = {}  # Dictionary containing subscriptions to tags.

cmds = {}  # Dictionary containing subscriptions to commands.


def sub(byte):
    """Decorator allowing for easy subscription to tags in the stream.

    Args:
        byte (str): Byte to subscribe the decorated callback to.
    """
    def sub_dec(c):
        subs[unhexlify(byte)] = c
    return sub_dec


def cmd(byte):
    """Decorator allowing for easy subscription of command-tags in stream."

    Args:
        byte (str): Byte to subscribe the decorated callback to."
    """
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

    @sub('1B')  # 1B40 == initialize, 1B69 == other command
    def sub_cmd(self):
        print("--> sub_cmd")

    @sub('4D')
    def sub_compression(self):
        print("--> sub_compression")

    @sub('67')
    def sub_raster(self):
        print("--> sub_raster")

    @sub('1A')
    def sub_print_eject(self):
        print("--> sub_print_eject")

    @sub('FF')
    def sub_print_no_eject(self):
        print("--> sub_print_no_eject")

    @cmd('40')
    def cmd_initialize(self):
        """Callback handling initialization of printer."""
        print("--> cmd_initialize")

    @cmd('6961')
    def cmd_mode(self):
        """Callback handling mode-setting of printer."""
        print("--> cmd_mode")

    @cmd('697A')
    def cmd_set_media_and_quality(self):
        """Callback for setting print-media and -quality."""
        print("--> cmd_set_media_and_quality")

    @cmd('694D')
    def cmd_set_mode(self):
        """Callback handling set mode."""
        print("--> cmd_set_mode")

    @cmd('6941')
    def cmd_cut_every(self):
        """Callback handling cut-settings."""
        print("--> cmd_cut_every")

    @cmd('694B')
    def cmd_cut_type(self):
        """Callback handling cut-type."""
        print("--> cmd_cut_type")

    @cmd('6964')
    def cmd_set_margins(self):
        """Callback handling setting of margins."""
        print("--> cmd_set_margins")


if __name__ == '__main__':
    ptr = PTReader()
    print("subs: %r" % subs)

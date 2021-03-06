# -*- coding: utf-8 -*-
"""
.. module:: ptreader
    :platform: Unix, Windows
    :synopsis: Reader for binary blob print-files for HP P-Touch series
    printers.

.. moduleauthor:: Terje Elde <terje@elde.net>

"""

import io
from binascii import hexlify, unhexlify

from .logger import logger

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

        self.preamble = 0
        self.init = 0

        if input:
            self.__init_input(input)

    def __init_input(self, input):
        """Initialize a new input-stream, called from __init__ and read().

        Args:
            input (str or file): Path of file, or file-like object, that
            reader will be initialized to read from.
        """

        if type(input) in [str]:  # unicode?
            self._input = io.open(input, 'rb')
        else:
            self._input = input
        self._input.seek(0)

    def read(self, input=None):
        """Read file, dispatch handlers based on how things are set up.

        Args:
            input (str or file): Optionally provide a file (path or object)
            that gets read from.
        """
        if input:
            self.__init_input(input)

        while True:
            op = self._input.read(1)
            if not op:  # EOF
                break
            logger.debug('--> op: %r' % op)
            if op in subs:
                logger.debug('  --> found!')
                subs[op](self)
            else:
                logger.debug(" --> op not found: %r" % op)

    @sub('00')  # preamble
    def sub_pre(self):
        """Preamble, can be safely ignored.  It's just a burst of zeros, to
        clear comamnd-buffer on serial-printers."""
        logger.debug("--> sub_pre")
        self.preamble += 1

    @sub('1B')
    def sub_cmd(self):
        logger.debug("--> sub_cmd")
        cmd = self._input.read(2)
        if cmd in cmds:
            logger.debug("  --> found 2-byte cmd: %r" % hexlify(cmd))
            cmds[cmd](self)
        else:
            if cmd[0] in cmds:
                # one-byte command, but read two, so seek one back.
                self._input.seek(-1, io.SEEK_CUR)
                logger.debug(" --> found 1-byte cmd: %r" % hexlify(cmd[0]))
                cmds[cmd[0]](self)
            else:
                logger.debug("  --> UNKNOWN cmd: %r" % hexlify(cmd))

    @sub('4D')
    def sub_compression(self):
        logger.debug("--> sub_compression")

    @sub('67')
    def sub_raster(self):
        logger.debug("--> sub_raster")

    @sub('1A')
    def sub_print_eject(self):
        logger.debug("--> sub_print_eject")

    @sub('FF')
    def sub_print_no_eject(self):
        logger.debug("--> sub_print_no_eject")

    @cmd('40')
    def cmd_initialize(self):
        """Callback handling initialization of printer."""
        if self.preamble:
            logger.debug("--> cmd_initialize (%r bytes of preamble)" % self.preamble)
        else:
            logger.debug("--> cmd_initialize (no preamble)")
        self.init += 1

    @cmd('6961')
    def cmd_mode(self):
        """Callback handling mode-setting of printer."""
        logger.debug("--> cmd_mode")

    @cmd('697A')
    def cmd_set_media_and_quality(self):
        """Callback for setting print-media and -quality."""
        logger.debug("--> cmd_set_media_and_quality")

    @cmd('694D')
    def cmd_set_mode(self):
        """Callback handling set mode."""
        logger.debug("--> cmd_set_mode")

    @cmd('6941')
    def cmd_cut_every(self):
        """Callback handling cut-settings."""
        logger.debug("--> cmd_cut_every")

    @cmd('694B')
    def cmd_cut_type(self):
        """Callback handling cut-type."""
        logger.debug("--> cmd_cut_type")

    @cmd('6964')
    def cmd_set_margins(self):
        """Callback handling setting of margins."""
        logger.debug("--> cmd_set_margins")


if __name__ == '__main__':
    ptr = PTReader()
    import os
    ptr.read(os.path.join(os.path.dirname(__file__),
                          'test',
                          'python.ptouch'))
    logger.debug("subs: %r" % subs)

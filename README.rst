========
pyptouch
========

.. image:: https://img.shields.io/travis/tld/pyptouch.svg
        :target: https://travis-ci.org/tld/pyptouch

.. image:: https://img.shields.io/pypi/v/pyptouch.svg
        :target: https://pypi.python.org/pypi/pyptouch

=======================================================================================
Code is written, but in the process of cleaning it up while adding it to this repo.
=======================================================================================

================================
Please come back in a few weeks.
================================

"Driver" for Brothers Q-Touch series of label printers, providing PDF/PS/PNG to
native files for the printers, that can be fed directly to the printers on
JetDirect port (TCP 9100).

Documentation: https://pyptouch.readthedocs.org

The good:
 * Free software: BSD license
 * Can be used directly from command line
 * Or as a Python-module
 * Can also inspect ptouch-blobs, and decode to PNG

The bad:
 * Only tested with Brother QL-1060N
 * Only tested with JetDirect
 * No USB-specific code

The (optional) dependancies:
 * Pillow (PNG-support)
 * Ghostscript (PS/PDF-support)

Usage - CLI
-----------

Simply convert a PNG to a .ptouch-file, that can be given directly to printer:

    png2ptouch -o foo.ptouch foo.png

Give it directly to the printer:

    nc 10.10.10.10 9100 < foo.ptouch

Usage - module
--------------




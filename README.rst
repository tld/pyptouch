========
pyptouch
========

"Driver" for Brothers Q-Touch series of label printers, providing PDF/PS/PNG to
native files for the printers, that can be fed directly to the printers on
JetDirect port (TCP 9100).

The good:
 * Free software: BSD license
 * Usable as a Python-module
 * Can be used directly from command line
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




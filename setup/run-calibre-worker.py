#!/usr/bin/env python2
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2016, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import (unicode_literals, division, absolute_import,
                        print_function)
import sys, os
sys.setup_dir = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(os.path.dirname(sys.setup_dir), 'src'))
sys.path.insert(0, SRC)
sys.resources_location = os.path.join(os.path.dirname(SRC), 'resources')
sys.extensions_location = os.path.join(SRC, 'calibre', 'plugins')
sys.running_from_setup = True

from calibre.utils.ipc.worker import main
print(111111111111)
sys.exit(main())

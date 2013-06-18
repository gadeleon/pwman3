""""
#============================================================================
# This file is part of Pwman3.
#
# Pwman3 is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2
# as published by the Free Software Foundation;
#
# Pwman3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pwman3; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#============================================================================
# Copyright (C) 2012 Oz Nahum <nahumoz@gmail.com>
#============================================================================
# Copyright (C) 2006 Ivan Kelly <ivan@ivankelly.net>
#============================================================================
"""


from pwman.ui.cli import PwmanCliNew
from pwman.ui import tools
import time
import msvcrt
import pwman.util.config as config


class PwmanCliWinNew(PwmanCliNew):

    def print_node(self, node):
        width = str(tools._defaultwidth)
        print "Node %d." % (node.get_id())
        print ("%"+width+"s %s") % (tools.typeset("Username:", tools.ANSI.Red),
                                    node.get_username())
        print ("%"+width+"s %s") % (tools.typeset("Password:", tools.ANSI.Red),
                                    node.get_password())
        print ("%"+width+"s %s") % (tools.typeset("Url:", tools.ANSI.Red),
                                    node.get_url())
        print ("%"+width+"s %s") % (tools.typeset("Notes:", tools.ANSI.Red),
                                    node.get_notes())
        print tools.typeset("Tags: ", tools.ANSI.Red),
        for t in node.get_tags():
            print " %s \n" % t.get_name(),

        def heardEnterWin():
            c = msvcrt.kbhit()
            if c == 1:
                ret = msvcrt.getch()
                if ret is not None:
                    return True
            return False

        def waituntil_enter(somepredicate, timeout, period=0.25):
            mustend = time.time() + timeout
            while time.time() < mustend:
                cond = somepredicate()
                if cond:
                    break
                time.sleep(period)
            self.do_cls('')

        flushtimeout = int(config.get_value("Global", "cls_timeout"))
        if flushtimeout > 0:
            print "Press any key to flush screen (autoflash "\
                + "in %d sec.)" % flushtimeout
            waituntil_enter(heardEnterWin, flushtimeout)
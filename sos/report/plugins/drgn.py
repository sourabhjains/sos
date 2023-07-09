# This file is part of the sos project: https://github.com/sosreport/sos

# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from collections import OrderedDict
from sos.report.plugins import Plugin, IndependentPlugin


class drgn(Plugin, IndependentPlugin):

    short_desc = 'IBM Power systems'

    plugin_name = 'drgn'
    profiles = ('system', 'hardware')
    architectures = ('ppc.*',)

    def setup(self):
        drgn_script_loc = "/usr/share/drgn/scripts/"
        self.add_cmd_output("drgn --version")
        scripts_opt_dic = OrderedDict([
            ("bpf_inspect.py", ["prog", 'map']),
            ("cgroup.py", None),
            ("fs_inodes.py", None),
            ("kcore_list.py", None),
            ("kernel_sys.py", None),
            ("lsmod.py", None),
            ("mount.py", None),
            ("ps.py", ["-u", "-k", "-a"]),
            ("tcp_sock.py", None),
            ("vmmap.py", ["1"]),
            ("vmstat.py", None),
        ])

        for script in scripts_opt_dic.keys():
            if scripts_opt_dic[script]:
                for opt in scripts_opt_dic[script]:
                    self.add_cmd_output(drgn_script_loc + script + " " + opt)
                continue
            self.add_cmd_output(drgn_script_loc + script)

# vim: set et ts=4 sw=4 :


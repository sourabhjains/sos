# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.


# This sosreport plugin is meant for sas adapters.
# This plugin logs inforamtion on each adapter it finds.

from sos.report.plugins import Plugin, IndependentPlugin


class arcconf(Plugin, IndependentPlugin):

    short_desc = 'arcconf Integrated RAID adapter information'

    plugin_name = "arcconf"
    commands = ("arcconf",)

    def setup(self):

    # get list of adapters
    self.add_cmd_output([
        "arcconf list"
    ])

    # Get the list of available controller
    listarcconf = self.collect_cmd_output("arcconf list")

    # Parse the 'arcconf list' output and extract controller IDs
    # For each Controller ID found in 'arcconf list', add commands
    # to getconfig and GETLOGS
    if listarcconf['status'] == 0:
        for line in listarcconf['output'].splitlines():
            words = line.split()

            # Skip line has less than two words
            if (len(words) < 2)
                continue
            # Line with "Controller XX: *" has Controller ID
            if words[0] != "Controller" or not words[1].endswith(":"):
                continue

            # Controller ID ends with :, so remove it
            controller_id = words[1][:-1]

            # Add new command with Controller ID
            self.add_cmd_output([
                "arcconf getconfig %s" % controller_id,
                "arcconf GETLOGS %s UART" % controller_id
            ])
# vim: et ts=4 sw=4

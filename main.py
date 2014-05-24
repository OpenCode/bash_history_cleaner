#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
##############################################################################
#
#    BASH HISTORY CLEANER
#    Copyright (c) 2014 Francesco OpenCode Apruzzese All Rights Reserved.
#                       www.e-ware.org
#                       opencode@e-ware.org
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from os.path import expanduser
import argparse


# ----- List of commands to delete from bash history file
#       Keep the commands separated for alphabetical order
command_list = [
    'cd', 'clear',
    'exit',
    'ifconfig',
    'ls', 'lshd',
    'ping', 'pwd',
    'top', 'reset',
    ]


# ----- Return True if the line is a valide line for new history
def valide_line(line):

    valide = True
    line = line.replace('\n', '')
    for command in command_list:
        # ----- Command with arguments or stand-alone command
        if line.startswith('%s ' % command) or line == command:
            valide = False
    return valide


def main(args):

    # ---- Use standard file or passed path
    if not args.history_file:
        home_path = expanduser("~")
        history_file_path = '%s/.bash_history' % (home_path)
        if args.verbose:
            print 'Will be used standard bash history file %s' % (
                history_file_path)
    else:
        history_file_path = args.history_file
        if args.verbose:
            print 'Will be used defined bash history file %s' % (
                history_file_path)

    # ----- Open the file and read line per line
    history_file = open(history_file_path, 'r')
    new_history = ''
    for line in history_file.readlines():
        if valide_line(line):
            new_history = '%s%s' % (new_history, line)
    history_file.close()

    # ----- Update file
    if args.verbose:
        print 'Update history file'
    history_file = open(history_file_path, 'w')
    history_file.write(new_history)
    history_file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='history_file',
                        help='Set an alternative bash history file')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    main(args)

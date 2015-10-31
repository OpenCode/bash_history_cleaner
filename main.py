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


from os import listdir
from os.path import expanduser
from shutil import copyfile
import argparse
import importlib
import re
from extras import *

# ----- Read extra module to extend functionality
extra_modules = [f.replace('.py', '') for f in listdir('extras')
                 if not (f.endswith('.pyc') or f == '__init__.py')]

# ----- List of commands filled from extended file
command_list = []

# ----- Extend the command list with extra module command list
if extra_modules:
    for extra_module in extra_modules:
        print 'Load module "%s" from extras' % (extra_module)
        module = importlib.import_module('extras.%s' % (extra_module))
        command_list = command_list + module.command_list


# ----- Return True if the line is a valide line for new history
def valide_line(line, sudo):

    valide = True
    line = line.replace('\n', '')
    for command in command_list:
        # ----- Command with arguments or stand-alone command
        if line == '' or re.match(command, line):
            valide = False
        if sudo:
            # ----- Check sudo command, too
            if re.match('sudo {cmd}'.format(cmd=command), line):
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

    # ----- Backup if required
    if args.backup:
        copyfile(history_file_path, '%s_bck' % (history_file_path))
        if args.verbose:
            print 'Backup created in %s_bck' % (history_file_path)

    # ----- Open the file and read line per line
    history_file = open(history_file_path, 'r')
    new_history = ''
    lines = history_file.readlines()
    new_lines_count = 0
    if args.verbose:
        print 'History lines: %s' % (len(lines))
    for line in lines:
        if valide_line(line, args.sudo):
            new_history = '%s%s' % (new_history, line)
            new_lines_count += 1
    history_file.close()

    # ----- Update file
    if args.verbose:
        print 'Update history file'
        print 'History lines: %s' % (new_lines_count)
        print '%s lines cleaned' % (len(lines)-new_lines_count)
    history_file = open(history_file_path, 'w')
    history_file.write(new_history)
    history_file.close()


if __name__ == "__main__":

    # ----- Parse terminal arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='history_file',
                        help='Set an alternative bash history file')
    parser.add_argument('-s', '--sudo', dest='sudo', action='store_true',
                        help='Include sudo command in cleaning, too')
    parser.add_argument('-b', '--backup', dest='backup', action='store_true',
                        help='Create a bash history file backup before use it')
    parser.add_argument('-v', dest='verbose', action='store_true',
                        help='Verbose mode')
    args = parser.parse_args()
    main(args)

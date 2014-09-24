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

# ----- List of commands to delete from bash history file
#       Keep the commands separated for alphabetical order
command_list = [
    '!!', '!pattern',
    'cat', 'cd', 'clear', 'cp',
    'date',
    'exit',
    'ifconfig',
    'kill', 'killall',
    'less', 'locate', 'ls', 'lshd',
    'man', 'more', 'mkdir', 'mv',
    'ping', 'pwd',
    'reset',
    'su',
    'top', 'touch',
    'xkill',
    ]

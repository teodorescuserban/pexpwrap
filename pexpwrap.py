#!/usr/bin/python

import sys
import os
import re
import pexpect
import getpass
########################################################
#### do not modify anything below this line


# other vars
ini_file = ""
cmd_file = ""
ssh_exec = "ssh"
base_dir = ""
script_name = ""
commands = {}
# s = pxssh.pxssh()
HOST, USER, PASS, PROMPT = ("", "", "", "")
COMMANDS = []


def terminate_session(p):
    endmode = raw_input('terminate the session or enter intercative mode? (T/i): ')
    p.before
    if endmode == 'i':
        # p.sendline('\n')
        print "The keyboard is all yours :)"
        p.sendline('\n')
        p.interact()
    print "Closing pipe..."
    p.terminate()
    print "Done!"


def execute_pexpect_commands(p):
    global PROMPT
    for command in COMMANDS:
        print "++++++ Sending command: " + command
        p.sendline (command)
        print p.before
        p.expect(PROMPT)        
        print p.before
    return p


def make_pexpect_connection():
    global HOST, USER, PASS, PROMPT
    mode = raw_input('read ini file or enter details manually? (I/m): ')
    if mode == 'm':
        HOST = raw_input('hostname: ')
        USER = raw_input('username: ')
        PASS = getpass.getpass('password: ')
        PROMPT = raw_input('server prompt: ')
        if len(PROMPT) < 1:
            PROMPT = "\$"
    else:
        read_ini_file()
    print "Logging in. Please wait..."
    p = pexpect.spawn('ssh -l ' + USER + ' ' + HOST)
    p.expect('assword:')
    p.sendline(PASS)
    p.expect(PROMPT)
    print "Connected!"
    return p


def read_ini_file():
    global ini_file
    if not os.path.isfile(ini_file):
        print "\n\tError: ini file does not exist."
        dev_null()
    with open(ini_file, 'r') as f:
        for line in f:
            # ignore commented lines
            if re.search(r'^\s*#\s*',line):
                continue
            # ignore empty lines
            if re.search(r'^\s*$',line):
                continue
            # chop the newline at the end
            line = line.rstrip()
            # chop the inline comments
            line = re.sub(r'#.*', '', line)
            # print "uhu" + line
            (var, val) = line.split('=')
            globals()[var] = val


def read_cmd_file():
    global cmd_file
    if not os.path.isfile(cmd_file):
        print "\n\tError: command file given does not exist."
        dev_null()
    with open(cmd_file, 'r') as f:
        for line in f:
            # ignore commented lines
            if re.search(r'^\s*#\s*',line):
                continue
            # chop the newline at the end
            line = line.rstrip()
            # chop the inline comments
            line = re.sub(r'#.*', '', line)
            COMMANDS.append(line)
            # print "cmd: " + line


def parse_args():
    global ini_file, cmd_file, base_dir, script_name
    abs_path = os.path.abspath(sys.argv.pop(0))
    base_dir =os.path.dirname(abs_path)
    script_name = os.path.basename(abs_path)
    # print abs_path
    # print base_dir
    # print script_name
    def_ini_file = re.sub(r'.py$', r'.ini', script_name)
    def_cmd_file = re.sub(r'.py$', r'.cmd', script_name)
    if '-h' in sys.argv or '--help' in sys.argv:
        dev_null()
    elif len(sys.argv) == 1:
        cmd_file = sys.argv.pop(0)
        ini_file = def_ini_file
    elif len(sys.argv) > 1:
        cmd_file = sys.argv.pop(0)
        ini_file = sys.argv.pop(0)
    else:
        ini_file = def_ini_file
        cmd_file = def_cmd_file
    ini_file = os.path.join(base_dir, ini_file)
    cmd_file = os.path.join(base_dir, cmd_file)


def dev_null():
    global script_name
    def_ini_file = re.sub(r'.py$', r'.ini', script_name)
    def_cmd_file = re.sub(r'.py$', r'.cmd', script_name)
    print "\n\tUsage: " + script_name + " cmd_file_name [ini_file_name]"
    print "\tThe default ini file name is " + def_ini_file + "\n"
    print "\tThe default cmd file name is " + def_cmd_file + "\n"
    sys.exit()


def main():
    parse_args()
    read_cmd_file()
    print "\nusing " + ini_file + " as init file and"
    print cmd_file + " as command file...\n"
    p = make_pexpect_connection()
    execute_pexpect_commands(p)
    terminate_session(p)

if __name__ == "__main__":
    main()

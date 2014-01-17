pexpwrap
========

Wrapper for pexpect

pexpect is a pure python module alternative to expect (please see http://pexpect.sourceforge.net/pxssh.html)

pyssh is a wrapper for this one, made by the same author; unfortunately there is not quite mature yet to be used.

pexpwrap is using pexpect attempting to make the life easier for some sysadmins and field engineers.

It is based on the assumption that you need to run alot of [configuration] commands on a device.

Parameters in .ini file
-----------------------
HOST - ip or hostname of the device
USER - user used
PASS - password for the user above
PROMPT - prompt is very important, because pexpect will expect that char sequence to run the next command.
If no prompt is given, it will default to the most common linux prompt: $

Note: At this time, the script does not have a way to handle a new ssh key dialog. Please connect from your computer with a normal ssh first. You only need to respond "yes" to the new ssh dialog.


Usage and examples
------------------

Let's say you need to replace an old Brocade FC switch with a new one; licenses are different, maybe the IP is different and you just can't afford to stay in site to replicate the config in the web interface.

You can just ask the customer to send you by e-mail the old config, downloaded from the switch. Using grep, sed and whatever you like, you create a file that contains the text-mode commands needed for the new switch to work.

You also ask the customer what should be the ip, user, password and switch name.

Now you have all that is required to stay in site less than 15 minutes.

Downtime will be lower, customers will be happier.

pexpwrap have 3 files - you only really need one, pexpwrap.py
The ini file is used in automatic connection mode (if you don't have all details, just let the customer to input them by hand in manual mode)
The cmd file is the file in which you have all commands required to be run on the switch. You can always choose a different name from command line.

Examples of use:

./pexprap.py
default ini file, default command file
default command file is used.

./pexpwrap.py my_command_file
tries to run commands from the file you specified

./pexpwrap.py my_command_file my_ini_file
another ini file, another command file

Good luck! :)

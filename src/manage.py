#!/usr/bin/env python
import os
import sys
import shlex

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TheDragonDashboard.settings")

    from django.core.management import execute_from_command_line

    if len(sys.argv)>1:
        execute_from_command_line(sys.argv)
    else:
        print("enter command: ")
        sys.argv.extend(shlex.split(input()))
        execute_from_command_line(sys.argv)

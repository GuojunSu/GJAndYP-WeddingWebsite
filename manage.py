#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    import os

    os.environ['DJANGO_SETTINGS_MODULE'] = 'bigday.settings'
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigday.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

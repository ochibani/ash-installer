#!/usr/bin/env python3

import os
import time
import subprocess as sp

snapshot = sp.check_output("/usr/sbin/ash c", shell=True)
while True:
    if os.path.exists(f"/.snapshots/rootfs/snapshot-chr{snapshot}"):
        time.sleep(20)
    else:
        os.system("/usr/sbin/ash clone $(/usr/sbin/ash c)")
        os.system("/usr/sbin/ash auto-upgrade")
        os.system("/usr/sbin/ash base-update")
        break

upstate = open("/.snapshots/ash/upstate")
line = upstate.readline()
upstate.close()
if "1" not in line:
    os.system("/usr/sbin/ash deploy $(/usr/sbin/ash c)")

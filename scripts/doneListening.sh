#!/bin/sh
sh_pid=`pgrep -f listening.sh`
py_pid=`pgrep -f listening.py`

kill -9 $sh_pid
kill -9 $py_pid

python3 /home/pi/Jerry/scripts/doneListening.py

#!/bin/sh
irsend SEND_START "$1" "$2" &
sleep 1
irsend SEND_STOP "$1" "$2"

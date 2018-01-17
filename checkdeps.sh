#!/bin/sh

if ! [ -e /usr/bin/unix2dos ]; then
    echo "Can't find /usr/bin/unix2dos. Please install it on your system."
    exit 1
fi

if ! [ -e /usr/bin/wget ]; then
    echo "Can't find /usr/bin/wget. Please install wget on your system"
    exit 1
fi

#!/bin/sh

if ! [ -e /usr/bin/unix2dos ]; then
    echo "Can't find /usr/bin/unix2dos. Please install it on your system."
    exit 1
fi

memdisk_done=0
if ! [ -e /boot/memdisk ]; then
    for i in /usr/lib/syslinux/memdisk /usr/share/syslinux/memdisk
    do
        if [ -e $i ]; then
            cp -f $i /boot
            memdisk_done=1
        fi
    done
else
    memdisk_done=1
fi

if [ $memdisk_done -eq 0 ]; then
    echo "Can't find memdisk. Please install syslinux and copy memdisk to /boot"
    exit 1
fi

if ! [ -e /usr/bin/python ]; then
    echo "Can't find /usr/bin/python. Please install python on your system"
    exit 1
fi

if ! [ -e /usr/bin/wget ]; then
    echo "Can't find /usr/bin/wget. Please install wget on your system"
    exit 1
fi

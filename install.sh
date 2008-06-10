#!/bin/sh
## Simple Install script for biosdisk
## John Hull <john_hull@dell.com>

mkdir -p /var/lib/biosdisk
mkdir -p /etc/biosdisk

install -m 755 biosdisk /usr/sbin
install -m 644 dosdisk.img /var/lib/biosdisk
install -m 644 biosdisk.conf /etc/biosdisk
install -m 644 biosdisk-mkrpm-template.spec /etc/biosdisk
install -m 644 biosdisk.8.gz /usr/share/man/man8

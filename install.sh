#!/bin/bash
## Simple Install script for biosdisk
## John Hull <john_hull@dell.com>

sh checkdeps.sh

mkdir -p /var/lib/biosdisk
mkdir -p /usr/share/biosdisk

install -m 755 biosdisk /usr/sbin
install -m 755 blconf /usr/sbin
#install -m 755 geturl /usr/sbin
install -m 644 dosdisk.img /usr/share/biosdisk
install -m 644 dosdisk288.img /usr/share/biosdisk
install -m 644 dosdisk8192.img /usr/share/biosdisk
install -m 644 dosdisk20480.img /usr/share/biosdisk
install -m 644 biosdisk.conf /etc/
install -m 644 biosdisk.8.gz /usr/share/man/man8

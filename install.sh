#!/bin/bash
## Simple Install script for biosdisk
## John Hull <john_hull@dell.com>

sh checkdeps.sh

mkdir -p /var/lib/biosdisk
mkdir -p /usr/share/biosdisk

install -m 755 biosdisk /usr/sbin
install -m 644 biosdisk.conf /etc/
install -m 644 biosdisk.8.gz /usr/share/man/man8
install -m 644 42_biosdisk /usr/share/biosdisk
cp -R freedos-iso /usr/share/biosdisk

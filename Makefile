#!/usr/bin/make

prefix ?= /usr/
confdir ?= /etc/
sbindir ?= $(prefix)sbin
datadir ?= $(prefix)share/biosdisk
mandir ?= $(prefix)/share/man/man8
sharedstatedir ?= /var/lib/biosdisk

all:
	gzip -c biosdisk.8 > biosdisk.8.gz

install: all
	mkdir -p $(sharedstatedir)
	mkdir -p $(datadir)
	mkdir -p $(sbindir)
	mkdir -p $(mandir)
	mkdir -p $(confdir)
	install -m 755 biosdisk $(sbindir)
	install -m 644 biosdisk.conf $(confdir)
	install -m 644 biosdisk.8.gz $(mandir)
	install -m 755 42_biosdisk $(datadir)
	cp -R freedos-iso $(datadir)

clean:
	rm -f biosdisk.8.gz

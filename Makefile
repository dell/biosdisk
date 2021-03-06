#!/usr/bin/make

DESTDIR =
prefix ?= /usr/
confdir ?= /etc/
sbindir ?= $(prefix)sbin
datadir ?= $(prefix)share/biosdisk
mandir ?= $(prefix)/share/man/man8
sharedstatedir ?= /var/lib/biosdisk

VERSION=$(shell git describe --abbrev=0 | sed "s,v,,")
DESCRIBE=$(shell git describe)

all:
	gzip -c biosdisk.8 > biosdisk.8.gz

packages: clean-packages rpm deb

rpm:
	#put spec in common build area
	mkdir -p tmp/SPECS
	sed "s,##VERSION##,$(VERSION)," biosdisk.spec.in > tmp/SPECS/biosdisk.spec
	rpmbuild --define "_topdir `pwd`/tmp" -ba tmp/SPECS/biosdisk.spec

deb:
	#copy to the common area to build RPM/deb
	mkdir -p tmp/BUILD
	rsync -av --exclude='tmp' . tmp/BUILD
	cd tmp/BUILD
	pwd
	sed "s,##VERSION##,$(VERSION),; \
	     s,##DESCRIBE##,$(DESCRIBE),;" tmp/BUILD/debian/changelog.in > \
					   tmp/BUILD/debian/changelog
	cd tmp/BUILD && fakeroot dpkg-buildpackage
	cd tmp/BUILD && debian/rules clean

clean-packages:
	rm -fr tmp

install: all
	mkdir -p $(DESTDIR)$(sharedstatedir)
	mkdir -p $(DESTDIR)$(datadir)
	mkdir -p $(DESTDIR)$(sbindir)
	mkdir -p $(DESTDIR)$(mandir)
	mkdir -p $(DESTDIR)$(confdir)
	install -m 755 biosdisk $(DESTDIR)$(sbindir)
	install -m 644 biosdisk.conf $(DESTDIR)$(confdir)
	install -m 644 biosdisk.8.gz $(DESTDIR)$(mandir)
	install -m 755 42_biosdisk $(DESTDIR)$(datadir)
	cp -R freedos-iso $(DESTDIR)$(datadir)

clean:
	rm -f biosdisk.8.gz

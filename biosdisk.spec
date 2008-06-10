%define name biosdisk
%define version 0.75
%define release 1

Summary: biosdisk package for creating BIOS flash floppy images
Name: %{name}
Version: %{version}
Release: %{release}
Vendor: Dell Computer Corp
License: GPL
Group:    Applications/File
Packager: Dell Computer Corporation - John Hull (john_hull@dell.com)
Source0:  %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}
BuildArch: noarch
Requires: python >= 2.2, unix2dos, syslinux, wget

%description
Provides biosdisk utility for creating BIOS disk images in Linux

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/var/lib/%{name}
mkdir -p %{buildroot}/usr/share/biosdisk
mkdir -p %{buildroot}/usr/share/man/man8
mkdir -p %{buildroot}/etc


#place files
install -m 755 biosdisk %{buildroot}/usr/sbin
install -m 755 blconf %{buildroot}/usr/sbin
#install -m 755 geturl %{buildroot}/usr/sbin
install -m 644 dosdisk.img %{buildroot}/usr/share/%{name}
install -m 644 biosdisk.conf %{buildroot}/etc
install -m 644 biosdisk-mkrpm-redhat-template.spec %{buildroot}/usr/share/biosdisk
install -m 644 biosdisk-mkrpm-generic-template.spec %{buildroot}/usr/share/biosdisk
install -m 644 biosdisk.8.gz %{buildroot}/usr/share/man/man8

%clean
rm -rf %{buildroot}

%pre

%files
%defattr(-,root,root,-)
%attr(0755,root,root) /usr/sbin/biosdisk
%attr(0755,root,root) /usr/sbin/blconf
#%attr(0755,root,root) /usr/sbin/geturl
/var/lib
/usr/share/biosdisk/
%config /etc/biosdisk.conf
%doc /usr/share/man/man8/biosdisk.8.gz
%doc COPYING ChangeLog AUTHORS README INSTALL TODO README.dosdisk VERSION

%post
#copy memdisk to /boot
if ! [ -e /boot/memdisk ]; then
    for i in /usr/lib/syslinux/memdisk /usr/share/syslinux/memdisk
    do
        if [ -e $i ]; then
            cp -f $i /boot
        fi
    done
fi

%preun

%postun

%changelog
* Tue Dec 18 2007 - John Hull <john_hull@dell.com>
- Changed dos2unix requirement to unix2dos
* Fri Nov 12 2004 - John Hull <john_hull@dell.com>
- updated paths for spec files and biosdisk.conf
* Wed Sep 15 2004 - John Hull <john_hull@dell.com>
- Added python and dos2unix requirements. Added blconf install
* Thu Jul 15 2004 - John Hull <john_hull@dell.com>
- Updated to version 0.45. Added architecture change to support different actions
* Mon May 24 2004 - John Hull <john_hull@dell.com>
- Initial release

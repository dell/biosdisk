%define name biosdisk
%define version 0.75
%define release 1

Summary: Creates BIOS flash floppy images from Dell BIOS executables
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://linux.dell.com/biosdisk/
License: GPLv2+
Group:    Applications/File
Source0:  %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires(post): syslinux
Requires: unix2dos, wget, /usr/bin/rpmbuild

%description
Provides biosdisk utility for creating BIOS disk images in Linux

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}/%{_sysconfdir}


#place files
install -m 755 biosdisk %{buildroot}%{_sbindir}
install -m 644 dosdisk.img %{buildroot}%{_datadir}/%{name}
install -m 644 dosdisk288.img %{buildroot}%{_datadir}/%{name}
install -m 644 dosdisk8192.img %{buildroot}%{_datadir}/%{name}
install -m 644 dosdisk20480.img %{buildroot}%{_datadir}/%{name}
install -m 644 biosdisk.conf %{buildroot}/%{_sysconfdir}
install -m 644 biosdisk.8.gz %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/biosdisk
%{_localstatedir}/lib/%{name}/
%{_datadir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man8/%{name}.8.gz
%doc COPYING ChangeLog AUTHORS README INSTALL TODO README.dosdisk

%post
# copy memdisk to /boot
# yes rpmlint throws warnings about hardcoded paths and unsafe use of cp
if ! [ -e /boot/memdisk ]; then
    for i in /usr/lib/syslinux/memdisk %{_datadir}/syslinux/memdisk
    do
        if [ -e $i ]; then
            cp -f $i /boot
        fi
    done
fi

%changelog
* Tue Jun 10 2008 - Matt Domsch <Matt_Domsch@dell.com>
- spec cleanups

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

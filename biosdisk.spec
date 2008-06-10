%define name biosdisk
%define version 0.50
%define release 1

Summary: biosdisk package for creating BIOS flash floppy images
Name: %{name}
Version: %{version}
Release: %{release}
Vendor: Dell Computer Corp
Copyright: GPL
Group:    Applications/File
Packager: Dell Computer Corporation - John Hull (john_hull@dell.com)
Source0:  %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}
BuildArch: noarch

%description
Provides biosdisk utility for creating Dell BIOS disk images in Linux

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/var/lib/%{name}
mkdir -p %{buildroot}/etc/biosdisk
mkdir -p %{buildroot}/usr/share/man/man8

#place files
install -m 755 biosdisk %{buildroot}/usr/sbin
install -m 644 dosdisk.img %{buildroot}/var/lib/%{name}
install -m 644 biosdisk.conf %{buildroot}/etc/biosdisk
install -m 644 biosdisk-mkrpm-template.spec %{buildroot}/etc/biosdisk
install -m 644 biosdisk.8.gz %{buildroot}/usr/share/man/man8

%clean
rm -rf %{buildroot}

%pre

%files
%defattr(-,root,root,-)
%attr(0755,root,root) /usr/sbin/biosdisk
/var/lib
/etc/biosdisk/biosdisk-mkrpm-template.spec
%config /etc/biosdisk/biosdisk.conf
%doc /usr/share/man/man8/biosdisk.8.gz
%doc COPYING CHANGELOG AUTHORS README INSTALL TODO README.dosdisk VERSION

%post
      
%preun

%postun

%changelog
* Thu Jul 15 2004 - John Hull <john_hull@dell.com>
- Updated to version 0.45. Added architecture change to support different actions
* Mon May 24 2004 - John Hull <john_hull@dell.com>
- Initial release

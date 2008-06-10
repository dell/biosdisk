
Summary: biosdisk RPM for installing BIOS flash images
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group:    Applications/File
Packager: biosdisk
Source0: %{destination}
BuildRoot: %{_tmppath}/%{name}
BuildArch: noarch
Requires: mkinitrd, syslinux, biosdisk >= 0.55, /usr/sbin/blconf

%description
biosdisk RPM to install %{name} %{version}

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/boot

#place files
install -m 755 %{SOURCE0} %{buildroot}/boot

%clean
rm -rf %{buildroot}

%pre

%files
%defattr(-,root,root,-)
/boot

%post
#set up bootloader with BIOS image flash entry
if [ %{release} == "1" ]; then
    title=%{version}
else
    title=%{version}-%{release}
fi

if ! [ -e /boot/memdisk ]; then
    if [ -e /usr/lib/syslinux/memdisk ]; then
        cp -f /usr/lib/syslinux/memdisk /boot
    elif [ -e /usr/share/syslinux/memdisk ]; then
        cp -f /usr/share/syslinux/memdisk /boot
    fi
fi    

/usr/sbin/blconf --add-kernel=/boot/memdisk --add-initrd=/boot/`basename %{SOURCE0}` --title="BIOS $title"

      
%preun
/usr/sbin/blconf --remove-image=`basename %{SOURCE0}`

%postun

%changelog

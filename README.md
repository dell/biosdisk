biosdisk
--------
FreeDOS based BIOS updating utility for Dell machines.

This utility can be used to update the BIOS on a Dell machine running in
legacy mode.
If your machine is running in UEFI mode, it's recommended that you instead
update using UEFI capsule as described at https://www.dell.com/support/article/us/en/19/sln171755/updating-the-dell-bios-in-linux-and-ubuntu-environments?lang=en

## Installation
1. Install syslinux on your system
2. Install the package
```
# make install
```

Optimally if running on a Debian based distribution you can also generate
packages using `dpkg-buildpackage`.

# Usage
To find what options are available to use when executing the biosdisk script,
```
#biosdisk --help
```

Generating an ISO image
```
# biosdisk mkimage /path/to/exe
```

Installing an EXE update
```
# biosdisk install /path/to/exe
```
This will:
 * load the EXE file into an image
 * configure GRUB2 boot entry
 * Set next boot flag to run the image
 * Prompt for installation

Automatically installing without prompting
```
# biosdisk install -o "/nopause" /path/to/exe
```

Removing boot entries and old image
```
# biosdisk uninstall /path/to/exe
```

## pxelinux
Booting the biosdisk-created BIOS flash image with PXELINUX

To set up GRUB to allow a user to boot the BIOS flash image via a PXELINUX PXE
server, complete the following steps:

    a. Copy the biosdisk-created BIOS flash image and the SYSLINUX memdisk
       file (usually found in /usr/lib/syslinux) to your PXELINUX PXE server
       directory (usually /tftpboot/pxelinux.cfg). 
    b. Edit the "default" file (usually /tftpboot/pxelinux.cfg/default) to 
       add the following:

	label BIOS Flash <version>
		kernel /pxelinux.cfg/memdisk iso
		append initrd=/pxelinux.cfg/<imagename>.iso

4. In order to restart the computer after the Bios upgrade, press Crtl-Alt-Del


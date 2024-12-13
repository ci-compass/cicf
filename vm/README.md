Virtual Machine
---------------

A few of the tutorials use a virtual machine (VM) image that you run locally on
your computer. This lets us provide a consistent environment for everyone
regardless of the operating system on their computer or laptop. It also
provides a way for each fellow to go through the tutorials on their own time
and explore topics they find interesting.

A big goal of the CICF technical program is to provide experience with using
the command line. Many previous fellows have commented that more familiarity
with the command line would be helpful. We want every fellow to be comfortable
with using the command line—especially those who do the summer internship

We chose a Linux distribution for the VM since Linux has become ubiquitous in
scientific computing, and you will certainly encounter it if you continue
working with scientific cyberinfrastructure. There are many Linux
_distributions_, and we have chosen Debian just because the choice had to be
made. All of them are similar enough that experience with one will transfer to
others.

## Getting Started

Download the pre-made image from the CICF shared drive.
(See below if you want to make your own image from scratch).
Then choose the appropriate section below depending on the operating system on your computer. 

### OS X

You need to install a virtual machine emulator.
There are many out there; we have chosen to use [UTM](https://mac.getutm.app/).
There are many ways to get and install it:

1. You can install it using the [Mac App Store](https://apps.apple.com/us/app/utm-virtual-machines/id1538878817). This method costs $9.99.
1. You can [download a disk image](https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg) and install it from there.
1. If you have [Homebrew](https://brew.sh/) installed already, you can use that: `brew install utm`

Once UTM is installed, either download the UTM machine image from the CICF shared drive (easy) or make your image using the instructions below (hard).
Then start UTM





----

Pre-made images will be available for student fellows to download.
You can also build one yourself using the instructions given here.


## Creating the VM Image

The virtualizer/emulator used depends on the host computer. For OSX we use UTM.

### OSX Steps for UTM

Got a another method that uses a pre-made Debian 12 image.

---

1. Download [ARM version of Ubuntu server 24.04.1 LTS](https://ubuntu.com/download/server/arm)
1. Now in UTM choose "new image". (I think it is a plus sign).
1. New image.
1. Choose "Virtualize"
1. Choose "Linux"
1. Choose the "ubuntu-24.04.1-live-server-arm64.iso" as the boot ISO image
1. Choose 4096 MiB as the memory
1. Choose 64 GiB as the storage size
1. Name the image CICF Y4
1. run VM.
1. "Try or Install Ubuntu Server"
1. Install with defaults
```
       name: CICF
       server name: cicf-vm
       username: cicf
       password: cicf
```
1. install openssh server
1. After the installation script finishes, remove the CD/DVD ISO image from the virtual machine and then reboot.
1. Log in using the cicf/cicf user
1. Update and install the graphic desktop [(see link)](https://docs.getutm.app/guides/ubuntu/)
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install ubuntu-desktop
$ sudo reboot
```

At this point the VM doesn't boot. So something is wrong and I haven't figured it out yet.



## Using the VM Image


* On Linux
* On MacOS
* On Windows

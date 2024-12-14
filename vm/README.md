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
We have chosen to use [UTM](https://mac.getutm.app/).
There are a few ways to install it:

1. You can install it using the [Mac App Store](https://apps.apple.com/us/app/utm-virtual-machines/id1538878817). This method costs $9.99.
1. You can [download a disk image](https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg) and install it from there.
1. If you have [Homebrew](https://brew.sh/) installed already, you can use that. Run `brew install utm`

Once UTM is installed, either download the UTM machine image from the CICF shared drive (easy) or make your image using the instructions below (hard).
Then start UTM.
Under the "File" menu choose "Open", and then select the UTM image file you downloaded.
This will add the image as an option in the main window.
Now press the play button next to the name to start image.
The VM "screen" will be displayed in a new window.
Your mouse should just work.
If your mouse is _captured_, meaning it cannot escape the virtual image to select other things on your computer, press Command-Option to release it.

### Windows






## Creating a VM Image

This section is for reference.
If you are a fellow, download a pre-made image and follow the instructions above in the Getting Started section.


### OS X Steps for UTM

We start with the pre-built Debian 12 image for ARM.
(select new virtualized image with a pre-built image).
The default log-in is `debian / debian`.
Once there open a terminal.

```
$ sudo apt update
$ sudo apt upgrade
$ sudo reboot
```
Once the system restarts, open a terminal again and then
```
$ sudo adduser cicf
# give user password: cicf
$ sudo apt install git
$ git clone https://github.com/ci-compass/cicf
```

rename image to "CICF-Y4-MACOS-ARM"



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

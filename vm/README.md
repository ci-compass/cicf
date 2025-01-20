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

We first need to install the VM host program, which will depend on the type of
operating system on your computer. Once that is done, we will all have the same
image and your computer's operating system won't matter.

### OS X

You need to install a virtual machine emulator.
We have chosen to use [UTM](https://mac.getutm.app/).
There are a few ways to install it:

1. You can install it using the [Mac App Store](https://apps.apple.com/us/app/utm-virtual-machines/id1538878817). This method costs $9.99.
1. You can [download a disk image](https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg) and install it from there.
1. If you have [Homebrew](https://brew.sh/) installed already, you can use that. Run `brew install utm`

Once UTM is installed, download the `cicf-y4.utm` file from the CICF shared drive.

When the image is downloaded, start UTM.
Under the "File" menu choose "Open", and then select the UTM image file you downloaded.
This will add the image as an option in the main window.
Now press the play button next to the name to start image.
The VM "screen" will be displayed in a new window.
Your mouse should just work.
If your mouse is _captured_, meaning it cannot escape the virtual image to
select other things on your computer, press Command-Option to release it.
Skip to the section [Using the VM Image](#using-the-vm-image).

### Windows

We use VirtualBox to run the VMs on Windows.
Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) for Windows hosts.
Once VirtualBox is installed, download the the `cicf-y4.ova` file from the CICF shared drive.
Choose the "File > Import Appliance..." menu option, and then select the file you just downloaded.
The import will take a few minutes.
Once done, choose the "Start" button to boot the image.
Continue with the next section, [Using the VM Image](#using-the-vm-image).

## Using the VM Image

At this point it doesn't matter whether your host machine is a Mac or Windows.
Using the VM manager you installed, boot the image if you haven't already.
You will eventually see a sign-in screen.
Log in using the username `cicf` and password `cicf`.
After signing in you should see a desktop envrionment.
The first time you sign in it is worthwhile to update the packages on your machine by doing this:

1. Open a terminal window (the black box with a ">" on the bottom bar).
1. Type `sudo apt update` and press return. It will ask for your password. Type it (`cicf`) and press return. Many lines of text will scroll by.
1. When the `$` prompt appears again type `sudo apt upgrade` and press return.
1. Reboot the machine by typing `sudo reboot` and pressing return.

If you ever mess up your VM image, say by running an ill-advised command, you can always download a copy of the original VM image
and re-install it by following these steps again (minus needing to download install UTM or VirtualBox).

## Creating a VM Image

This section is for reference, and student fellows can ignore it when installing and setting up a VM on their computer.
If you are a fellow, download a pre-made image and follow the instructions above in the [Getting Started](#getting-started) section.

### OS X Steps for UTM

These are the steps used to create the downloadable VM image for UTM.

1. Download the [ARM64 Debian 12 installer](https://cdimage.debian.org/debian-cd/current/arm64/iso-cd/)
1. Using UTM, make a new virtual machine and set up the CD drive to point to the downloaded ISO image.
1. Boot and install OS.
```
       name: CICF
       server name: cicf-vm
       username: cicf
       password: cicf
```
1. Of the optional packages, install the XFCE envrionment.
1. After installation is complete, eject the CD image and reboot.
1. Verify machine boots correctly. Then turn off the VM.
1. Edit the UTM settings for the machine, choose the option to compact the disk image.
1. Rename the VM image to `cicf-y4`


### Windows Steps for VirtualBox

For Windows, we use VirtualBox to create the VM.

1. Download the [ARM64 Debian 12 installer](https://cdimage.debian.org/debian-cd/current/arm64/iso-cd/) debian-12.9.0-amd64-netinst.iso
1. Create a new VM image in Virtual Box. Make sure "skip unattended installiation" is checked. Memory: 6 GB. Disk: 8 GB.
1. Boot and install OS.
```
       name: CICF
       server name: cicf-vm
       username: cicf
       password: cicf
```
1. Of the optional packages, install the XFCE envrionment.
1. After installation is complete, eject the CD image and reboot.
1. Verify machine boots correctly. Then turn off the VM.
1. 




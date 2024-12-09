Virtual Machine
---------------

A few of the tutorials use a virtual machine (VM) image that you run locally on your computer.
While it can take some effort to set up the virtual machine, it does let us do three things:

1. You can run an experiment with the lesson topics on your own. Especially since we try to no require any third-party services.
2. You can get familar with the command line and with Unix/Linux like environments.
3. We can provide common lessons regardless of what brand or kind of computer you are using.

Additionally, exploring the virtual machine on your own computer will be help you become more comfortable using the command line.
Especially those who do the summer internship, many have commented that more familiarity with the command line would be helpful.

Linux has become ubiquitious in scientific computing, and for this reason we have chosen a Linux distribution for the VM.
There are many Linux _distributions_, and we have chosen Debian just because the choice had to be made.

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

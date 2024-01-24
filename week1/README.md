# CICF Week 1

The goals for the week 1 lab are to:

1. Install and use the provided Linux virtual machine (VM)
1. Use the terminal emulator and execute commands from the command line
1. Generate an SSH keypair for your VM and submit the public key to us
1. Use git to clone this repo to your VM

## Tutorial

To begin, follow the VM instal and setup guide to get the VM running on your laptop.

Once the VM is running, open up the terminal.

`sudo apt install git`

Lets explore.
Every shell starts in your home directory.
Run `pwd`.
This gives an absolute path telling you where the current working directory is.
Run `ls` to list the files in the current directory.
There are a lot of options to `ls`.
Try `'ls -l` and `ls -t`.

echo $SHELL


Run `ls -a`. These extra files have names that start with a dot and are called "dotfiles".
The `ls` command does not display this files by default.
The files are hidden for convinence, since they are still there.
Dotfiles are used for configuration files and directories.

Lets make an SSH key for your VM.

`ssh-keygen ...`


Now lets make a copy of git repo.
Git is an extremely useful tool that we will cover in more detail in the week 4 lesson.

`git clone ....`

cd cicf

PATH?

make directory
make script
use nano




-- See [week1.md][].

## Resources

There are a lot of other tutorials on the command line.
Especially recommended is The Software Carpentry course.
- Software Carpentry [course on the unix shell](https://swcarpentry.github.io/shell-novice/).
- [Introduction to the Unix Command Line](https://codethechange.stanford.edu/guides/guide_unix_commands.html#)
- [The Command Line: a comprehensive Guide](https://hackernoon.com/the-command-line-a-comprehensive-guide)

For SSH

- GitHub [How to make an SSH keypair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Some lists of unix commands.
- [List of POSIX commands](https://en.wikipedia.org/wiki/List_of_POSIX_commands) (The standardization effort in the 1980s was called POSIX).
- [List of GNU Core Utilities](https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands)



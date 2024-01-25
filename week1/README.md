# CICF Week 1

The goals for the week 1 lab are to:

1. Install and use the provided Linux virtual machine (VM)
1. Use the terminal emulator and execute commands from the command line
1. Generate an SSH keypair for your VM and submit the public key to us
1. Use git to clone this repo to your VM

## Tutorial

To begin, follow the VM instal and setup guide to get the VM running on your laptop.

Once the VM is running, open up the terminal.

`sudo apt install git xclip firefox-esr`

And type in the password.
This will install some programs we will need.
THe `sudo` takes its arguments and runs them as `root`, which is the admistrator
account on unix systems.
The command we are running as root is `apt`, which handles the software packages
on this distribution of Linux.

Every shell starts in your home directory.
Run `pwd`.
This gives an absolute path telling you where the current working directory is.
We signed with the username "debian".
Run `ls` to list the files in the current directory.
Try `'ls -l`.
Run `ls -a`. These extra files have names that start with a dot and are called "dotfiles".
The `ls` command does not display this files by default.
The files are hidden for convinence, since they are still there.
Dotfiles are used for configuration files and directories.

What happens if we mistype a command? We get an error of some kind:

```bash
debian@debian:~$ abcdef
bash: abcdef: command not found
```

There is a command that asks the shell which program it will run for a given
command `which cat`.

Try up arrow and down arrow. Try tab completion. `cd Doc` and then press tab. Then `cd ../D`.

We can list the envrionment variables using `env`.
There are a lot of them.
Try `env | less`.
This will leave you in a pager program called "less".
A pager takes everything on its input (STDIN) and presents it interactivally so
that you can read it at a human speed (as opposed to machine speed).
It has quirky keyboard controls:

* Press space to go to the next page.
* Up arrow and down arrow also scroll.
* Use forward slash `/` to search.
* Press `q` to exit back to the shell.

We can access envrionment variables in the shell, e.g. `echo $SHELL`.

### Git

Git is an extremely useful tool in programming and scientific computing.
A git _repository_ is used to track and share changes to a set of files, such as
source code or documentation.
We interact with a git repo by making a copy to our computer. This is called
"cloning" the repository.
Then if we make changes we can update our local repository (a _commit_) and
share by moving these changes to other repositories (a _push_).

Lets clone the CICF repository:

`git clone https://github.com/ci-compass/cicf`

The clone will be in the directory `cicf`.

```
cd cicf/week1
cat README.md
cat README.md | grep google
```

We will talk more about git in week 4.


### SSH

Lets make an SSH key for your VM.

`ssh-keygen -t ed25519 -C "your_email@example.com cicf"`
Choose to save in the default location.
Do not enter a passphrase, just press enter.

Lets look at the key pair. `cd ~/.ssh` and then `ls`
There are two files for the pair: the private file and the public file. Never
share the private file. Good practice is to never remove it from this machine.
`cat id_ed25519.pub`

In fact, I want everyone to share your public key with us, so that we can set up
some cloud computing resources for week 6.

First copy your public key to the clipboard `cat id_ed25519.pub | xclip -sel
clip`

Visit this form:

https://docs.google.com/forms/d/e/1FAIpQLSdBcZHtKcztx87IjojT7mlbqST7bSawnwNCJNxilm9oAyDgLw/viewform

Enter your name, email address, and paste the public key into the last field.


### More

A useful tool to edit text files is called a ... text editor.
There are many. For this class we will use one called `nano`.

`nano README.md`

Shell is a tool. It use is to make it easy to do things by hand. It can also be
used to glue programs and commands together.

`alias xclip='xclip -sel clip'`

`nano make-files.sh`

shell is _almost_ a programming language, but really clunky and error-prone.
best to use it to do the bare minimum to manulipluate files and glue other
programs together.

Many more topics that you can read about if interested:

* [the PATH](https://www.cs.purdue.edu/homes/bb/cs348/www-S08/unix_path.html)
* [Exit Codes](https://www.redhat.com/sysadmin/linux-shell-command-exit-codes)
* [Quoting](https://rg1-teaching.mpi-inf.mpg.de/unixffb-ss98/quoting-guide.html) and [here](https://teaching.idallen.com/cst8207/13w/notes/440_quotes.html)
* Shell scripting


## Resources

There are a lot of other tutorials on the command line.
Especially recommended is The Software Carpentry course.
- Software Carpentry [course on the unix shell](https://swcarpentry.github.io/shell-novice/).
- [Introduction to the Unix Command Line](https://codethechange.stanford.edu/guides/guide_unix_commands.html#)
- [The Command Line: a comprehensive Guide](https://hackernoon.com/the-command-line-a-comprehensive-guide)
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/html_node/index.html) exhaustive reference manual. Extremely detailed list of everything the Bash shell can do.

For SSH

- GitHub [How to make an SSH keypair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Some lists of unix commands.
- [List of POSIX commands](https://en.wikipedia.org/wiki/List_of_POSIX_commands) (The standardization effort in the 1980s was called POSIX).
- [List of GNU Core Utilities](https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands)



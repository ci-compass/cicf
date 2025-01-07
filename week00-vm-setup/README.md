# CICF Week 1

The goals for the week 1 lab are to:

1. Install and use the provided Linux virtual machine (VM)
1. Use the terminal emulator and execute commands from the command line
1. Generate an SSH keypair for your VM and submit the public key to us
1. Use git to clone this repo to your VM

## Tutorial

Begin by downloading the approprate VM software and VM image (see the [VM README](../vm/README.md)).
Sign in on the account:

    username: cicf
    password: cicf

Once the VM is running and you have logged in, open up the terminal.
This will make a window with a prompt:

```
adfadfadf
```

This is the command line, or shell.
Every shell starts in your home directory.
The `$` is the prompt, and tells us that the shell is ready for us to type a command to run.
The text in the window keeps getting added to and the most recent line and/or prompt is always at the bottom.
The oldest line is at the top of the window.

Type `pwd` and press "return".
You should see `/home/cicf/` appear.
We have just run the command `pwd`.
This command prints the current working directory to the command line.
The shell then prints a new prompt.

Run `ls` to list the files in the current directory.
Try `'ls -l`.
Run `ls -a`.
We can pass _options_ after the command name.
Each command can take different options.
For the `ls` command, the option `-a` tells it to list _every_ file, including those
whose names start with a period (aka "dot").
These files whose names that start with a dot and are called "dotfiles",
and `ls` does not list them by default.
This is for convinence, since these files are usually used for configuration files and directories.

What happens if we mistype a command? We get an error message:

```bash
debian@debian:~$ abcdef
bash: abcdef: command not found
```

This is the shell telling us that it has no idea how to execute the command `abcdef`.
It could be that we mistyped the command.
Or maybe the program is not installed.
Or the program is not in any location that the shell goes to look for commands to run.

There is a command `which` that asks the shell to tell us where the program for a given command is.

```bash
$ which abcdef
$ which cat
/bin/cat
```

The first command did not display anything, so there is no program named `abcdef`.
The second command displayed `/bin/cat` which is telling is where the program is in the filesystem.

**History** To make typing easier, the shell keeps a history of commands you have typed.
Use the up arrow to go backward in history to previous commands.
Use the down arrow to go forward in history toward the more recent commands.

**Tab Compleation** The shell will also try to complete commands and files that it knows about.
Press the tab key to ask the shell to try completaing what you have typed.
It will fill in as much as it can.
Type `cd Doc` (don't press return) and then press tab.
Then `cd ../D`.

**Envrionment variables** We can list the envrionment variables using `env`.
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

**Return codes** Each command has a return code.
It is not usually displayed, but it can sometimes be helpful.
The return code is a number between 0 and 255.
The code 0 means everything was successful.
Non-zero codes indicate errors, the exact meaning depends on the command being run.
The shell sets the variable `$?` to be equal to the return code of the previous command.

```
$ cat abcdefg
cat: abcdefg: No such file or directory
$ echo $?
1
```


### Git

Git is an extremely useful tool for programming and scientific computing.
A git _repository_ is used to track and share changes to a set of files, such as
source code project, our analysis scripts, or documentation.
We interact with a git repo by first making a copy to our computer.
This is called "cloning" the repository.
When we make changes to these files we can update our local repository (via a _commit_) and
share the changes by moving these changes to other repositories (a _push_).

Lets clone the CICF repository:

`git clone https://github.com/ci-compass/cicf`

This tells Git to copy the repository at the given URL onto our VM.
By default Git will make a directory named `cicf` and put everything inside there.

```
cd cicf
ls
ls -a
```

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

A _text editor_ useful tool to edit text files.
There are many.
For this class we will use one called `nano`.

`nano README.md`

Shell is a tool. It use is to make it easy to do things by hand. It can also be
used to glue programs and commands together.

`alias xclip='xclip -sel clip'`

`nano make-files.sh`

The shell provides some primitives to make scripts and is _almost_ a programming language, but really clunky and error-prone.

Many more topics that you can read about if interested:

* [the PATH](https://www.cs.purdue.edu/homes/bb/cs348/www-S08/unix_path.html)
* [Exit Codes](https://www.redhat.com/sysadmin/linux-shell-command-exit-codes)
* [Quoting](https://rg1-teaching.mpi-inf.mpg.de/unixffb-ss98/quoting-guide.html) and [here](https://teaching.idallen.com/cst8207/13w/notes/440_quotes.html)
* Shell scripting


## Resources

There are a lot of other tutorials on the command line.
Especially recommended is The Software Carpentry course.
- Software Carpentry [course on the unix shell](https://swcarpentry.github.io/shell-novice/).
- [The Shell Scripting Tutorial](https://www.shellscript.sh/)
- [Introduction to the Unix Command Line](https://codethechange.stanford.edu/guides/guide_unix_commands.html#)
- [The Command Line: a comprehensive Guide](https://hackernoon.com/the-command-line-a-comprehensive-guide)
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/html_node/index.html) exhaustive reference manual. Extremely detailed list of everything the Bash shell can do.

For SSH

- GitHub [How to make an SSH keypair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Some lists of unix commands.
- [List of POSIX commands](https://en.wikipedia.org/wiki/List_of_POSIX_commands) (The standardization effort in the 1980s was called POSIX).
- [List of GNU Core Utilities](https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands)



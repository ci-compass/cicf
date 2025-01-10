# CICF Week 1

The goals for the week 1 lab are to:

1. Install and use the provided Linux virtual machine (VM)
1. Use the terminal emulator and execute commands from the command line
1. Use git to clone this repo to your VM

## Tutorial

Begin by downloading the appropriate VM software and VM image (see the [VM README](../vm/README.md#getting-started)).
Start the VM if you haven't already.
At the sign-in screen log in using the credentials:

    username: cicf
    password: cicf

Once the VM is running and you have logged in, you will see a desktop environment.
Open up the terminal, which is a black icon with a caret `>_` on it at the bottom of the screen.
This will open a window with a prompt:

    cicf@cicf-vm:~$ 

This is the prompt for the command line, or shell.
Every shell starts in your home directory.
The `$` is the prompt, and tells us that the shell is ready for us to type a command to run.
The tilde `~` in the prompt indicates we are currently in the home directory.

Type `pwd` and press "return".
You should see `/home/cicf/` appear.
We have just run the command `pwd`.
This command prints the current working directory to the command line.
("pwd" stands for "present working directory". Most commands are abbreviations).
After the shell prints the directory it will then print a new prompt.

The text in the window will grow and the most recent line and/or prompt is always at the bottom of the window.
Conversely, the oldest line is at the top of the window.

Run `ls` to list the files in the current directory.
Try `'ls -l`.
Run `ls -a`.
The `-l` and `-a` are _options_ for the command.
They appear after the command name, and are separated from the command name by a space.
Each command can take different options, and will interpret the options differently.
For the `ls` command, the option `-a` tells it to list _every_ file, including those
whose names start with a period (aka "dot").
These files whose names that start with a dot and are called "dotfiles",
and `ls` does not display them by default.
(This is for convenience, since these files are usually used for configuration files and directories.)

What happens if we mistype a command? We get an error message:

    cicf@cicf-vm:~$ abcdef
    bash: abcdef: command not found

This is the shell telling us that it has no idea how to execute the command `abcdef`.
It could be that we mistyped the command.
Or maybe the program is not installed.
Or maybe the program is not where the shell goes to look for commands to run.

There is a command `which` that asks the shell to tell us where the program for a given command is.

    $ which abcdef
    $ which cat
    /usr/bin/cat

The first command did not display anything, so a program named `abcdef` was not found.
The second command displayed `/usr/bin/cat` which a path to the program "cat",
i.e. it is telling is where the program is in the file system.

**History** To make typing easier, the shell keeps a history of commands you have typed.
Use the up arrow to go backward in history to previous commands.
Use the down arrow to go forward in history toward the more recent commands.

**Tab Completion** The shell will also try to complete commands and files that it knows about.
Press the tab key to ask the shell to try completing what you have typed.
It will fill in as much as it can and then stop.
Type `cd Doc` (don't press return) and then press tab.
If you press tab twice then the shell will display all the possibilities:
type `cd Do` and then press tab. There is no completion. Press tab a second time: you will see
`Documents/ Downloads/` which are the two possibilities.

**Environment Variables** There are settings that we can change for each shell window we have open.
These are stored in _environment variables_.
These variables are hanging around in the background and programs can look at them when they are running.
We can list the environment variables using `env`.
There are a lot of them.
Try `env | less`.
This will leave you in a pager program called "less".
A pager takes everything on its input (STDIN) and presents it interactively so
that you can read it at a human speed (as opposed to machine speed).
It has quirky keyboard controls:

* Press space to go to the next page.
* Up arrow and down arrow also scroll.
* Use forward slash `/` to search.
* Press `q` to exit back to the shell.

We can access environment variables in the shell, e.g. `echo $SHELL`.

**Pipes** In the example above we did something that was a revolutionary concept when UNIX was first created.
We chained two command together: first we ran the command `env` and then we took its output and instead of displaying
it in the shell, we gave it to the command `less` as input. Then the command `less` displayed the output in a nicer way
to the terminal window.
Try `env | wc`. The `wc` (or word count) program counts the number of words in its input and outputs three numbers: the number of lines, the number of words and the number of characters.

**Return codes** Each command has a return code.
It is not usually displayed, but it can sometimes be helpful.
The return code is a number between 0 and 255.
The code 0 means everything was successful.
Non-zero codes indicate errors, the exact meaning depends on the command being run.
The shell sets the variable `$?` to be equal to the return code of the previous command.

    $ cat abcdefg
    cat: abcdefg: No such file or directory
    $ echo $?
    1


### Git

Git is an extremely useful tool for programming and scientific computing.
A git _repository_ is used to track and share changes to a set of files, such as
source code project, analysis scripts, or documentation.
We interact with a git repo by first making a copy to our computer.
This is called "cloning" the repository.
When we make changes to these files we can update our local repository (via a _commit_) and
share the changes by moving these changes to other repositories (a _push_).

Lets first install Git:

    sudo apt install git

Enter the password, and then press 'y' to agree to the installation. 
Now that Git is installed, lets clone the CICF repository:

    git clone https://github.com/ci-compass/cicf

This tells Git to copy the repository at the given URL onto our VM.
By default Git will make a directory named `cicf` and put everything inside there.

    cd cicf
    ls
    cd week01-commandline
    cat README.md

We will talk more about Git in week 4.


### More

A _text editor_ useful tool to edit text files.
There are many.
For this class we will use one called `nano`.

    nano README.md

The shell (the program that prints the prompt and executes the commands you type) is a tool that can make some jobs very easy.
Not only does it provide a powerful and concise way to do things with your computer,
it can also be used to glue programs and commands together in a shareable, repeatable way.
Since all the commands you type are text, we can also save these commands into a text file and have the shell
run many commands in a sequence.
These command files can be shared with others and run as if they were a command themselves!
The command files are called "shell scripts", and there is a sample one in this directory.

    nano make-files.sh

This script shows how we can enter comment text (the lines that start with a hash sign `#`).
Comment text is very important even though the shell ignores it.
Comments let us remember and tell others what these commands do and any strange bugs or workarounds we needed to do.
The shell also provides primitives such as conditional statements and loops, making shell scripting a programming language.



The shell and the command line bring together many more topics that you can read about if interested:

* [the PATH](https://www.cs.purdue.edu/homes/bb/cs348/www-S08/unix_path.html)
* [Exit Codes](https://www.redhat.com/sysadmin/linux-shell-command-exit-codes)
* [Quoting](https://rg1-teaching.mpi-inf.mpg.de/unixffb-ss98/quoting-guide.html) and [here](https://teaching.idallen.com/cst8207/13w/notes/440_quotes.html)
* Shell scripting. The shell we have been using is called _Bash_. There is a nice [Bash Scripting Tutorial](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/). There is also a comprehensive [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html).



## Resources

There are a lot of other tutorials on the command line.
Especially recommended is The Software Carpentry course.
- Software Carpentry [course on the Unix shell](https://swcarpentry.github.io/shell-novice/).
- [The Shell Scripting Tutorial](https://www.shellscript.sh/)
- [Introduction to the Unix Command Line](https://codethechange.stanford.edu/guides/guide_unix_commands.html#)
- [The Command Line: a comprehensive Guide](https://hackernoon.com/the-command-line-a-comprehensive-guide)
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/html_node/index.html) exhaustive reference manual. Extremely detailed list of everything the Bash shell can do.

For SSH

- GitHub [How to make an SSH keypair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Some lists of Unix commands.
- [List of POSIX commands](https://en.wikipedia.org/wiki/List_of_POSIX_commands) (The standardization effort in the 1980s was called POSIX).
- [List of GNU Core Utilities](https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands)



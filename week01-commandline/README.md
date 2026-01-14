# CICF Week 1 - The Command Line

The goals for Week 1 are:

1. Be able to run commands on the command line
1. Navigate the filesystem, read, and create files using the command line
1. Create simple shell scripts

Note: these tutorials assume you are working in a Linux/Unix environment.
You should be if you are using the Github codespace. These commands will
probably not work in a Windows command line.

## Tutorial

The command line is probably the fundamental technology for working with cyberinfrastructure.
It provides precision, and it is easy to extend by adding commands and by making scripts.
The text interface is easy to export across a network,
and they allow us to repeat commands in a reproducible way.
You will almost certainly have to work with one as you continue working on computing systems.
In exit surveys, many previous fellows have commented that having more familiarity with the command line would be helpful.

To make sure we all have a common experience, we will use the command line prompt that is in GitHub Codespaces for this course.
This command line is a Linux based container, and it will very similar to other Linux and Unix-like systems you will encounter.

This tutorial assumes you have done the steps in the [Getting Started](../getting-started/README.md) document,
and that you have a working Codespace.

<!-- revise below for code spaces -->

Open up the codespace and the terminal will be in the bottom window pane.bring up the terminal.
Make the terminal full screen by choosing the four corner box in that pane's title bar.

Your terminal window will have a prompt similar to the following:

	@dbrower ➜ /workspaces/cicf (main) $

This is a shell prompt, and it is waiting for you to type in a command.
The shell is expecting a certain structure of input, and you do not interact with it by just typing in a sentence.
(Command lines and shells go back 50 years. Computers at that time did not do natural language processing!)

As discussed in the lecture, commands start with a program name, and then have optional text that will be passed to the command.
Lets run some commands to get used to it.

Type `pwd` and press "return".
Underneath the prompt you should see the words `/workspaces/cicf` appear.
The command `pwd` prints the current working directory.
("pwd" stands for "present working directory". Most commands are abbreviations).
After the shell prints the directory it will then print a new prompt at the bottom of the window.

The text in the window will grow and the most recent line and/or prompt is always at the bottom of the window.
Conversely, the oldest line is at the top of the window.

Run `ls` to list the files in the current directory.
Try `'ls -l`.
Run `ls -a`.
The `-l` and `-a` are _options_ for `ls`.
They appear after the command name, and are separated from the command name by a space.
Each command can take different options, and will interpret the options differently.
For the `ls` command, the `-l` option will list more details for each file, such as modification dates and permissions.
The option `-a` tells it to list _every_ file, including those whose names start with a period (aka "dot").
There are files whose names start with a dot and are collectively called "dotfiles".
By default `ls` does not display them, so they are useful for configuration files, caches, and other files and directories that would otherwise clutter up the directory listing.
(This was also from a bug in 1972 and people decided they liked the behavior and kept it.)

What happens if we mistype a command? We get an error message:

    @dbrower ➜ /workspaces/cicf (main) $ asdf
    bash: asdf: command not found

This is the shell telling us that it has no idea how to execute the command `asdf`.
It could be that we mis-typed the command.
Or maybe the program is not installed.
Or maybe the program is not where the shell looks for commands to run.

There is a command `which` that asks the shell to tell us the program it found for a command.

    $ which asdf
    $ which ls
    /usr/bin/ls

The first command did not display anything, so a program named `asdf` was not found.
The second command displayed `/usr/bin/ls` which is the path to the program "ls",
i.e. it is telling is where the program is in the file system.

Typing commands gets old, so the shell provides some features to help you,
such as **cursor control**, **tab completion**, and **history**.

**Cursor Control** You can move the cursor around without using the mouse.
Control-A (so pressing the Control key and the A key without pressing the shift key)
will move the cursor to the beginning of the line.
Control-E will move the cursor to the end of the line.
Control-W will delete the previous word (so everything back to the previous space).
Control-K will delete everything from the cursor to the end of the line.
These are the ones I use everyday, but there are [many, many more](https://www.linux.org/threads/popular-keyboard-shortcuts-for-the-gnu-bash-shell.44645/),
and maybe others will be helpful to you.

**Tab Completion** To make it easier to type long file names,
you can ask the shell try to complete commands and files that it knows about.
Do this by starting to type a name and then press the tab key.
The shell will fill in as much as it can and then stop.
Type `cd we` (don't press return) and then press tab.
It will complete to `cd week` and then stop, since at this point there is not a unique extension.
Press tab twice, and the shell will display all the possibilities.

**History** To make typing easier, the shell keeps a history of commands you have typed.
This makes it easy to rerun or fix previous commands.
Use the **up arrow** to go backward in history to previous commands.
Use the **down arrow** to go forward in history toward the more recent commands.
So to rerun a previous command, just press the up arrow and then press enter to rerun.
The fix, press up arrow and then you can navigate around the command line, adjust, and then press enter to run.

**Wildcards** If you are working with a bunch of files and list all of their names on the command line,
you can use a wildcard to match all file names matching a pattern.
You type a wildcard pattern in the command line where you want a list of files to appear, and then before
running the command, the shell will replace the pattern with all of the matching file names, with each name separated by a space.
The most used wildcard is the asterisk `*`, which matches any number of non-slash characters.
For example, to list all files that end in `.txt` you can use the wildcard pattern `*.txt`.

	ls *.txt

The above will list only the files that end in `.txt`.

    mkdir my-files
    cp e*.sh my-files

This will make a new directory and copy all files that start with `e` and end with `.sh` into the new directory.

This simple pattern matching with asterisks is historically called "globbing" and you will see it used is many other places
besides the command line.

### Moving around the filesystem

The command line prompt always has a "Current Directory", which is the location in the filesystem that commands will executed in.
You can change the current directory with the `cd` (**c**hange **d**irectory) command.
The `cd` command takes a single, optional argument, which is the path to the directory you want to change to.
If you don't enter a directory you will go to your _home directory_.

	cd week01-commandline/

You can use the `.` and `..` relative paths to give locations.
For example, go up a level by using `..` as the path

	cd ..

Sometimes it is tedious to type the entire directory path, this is a good opportunity to use the tab completion.
You can see which directory you are in with the `pwd` command.

	pwd

There are many ways to make new files. One way is to redirect output into it.

	seq 100 > numbers.txt

Another way is to `touch` it.

	touch numbers.txt

You can rename files by "moving" them.
The first argument is the starting name and the second argument is the ending name.
The following renames `numbers.txt` to `numbers-orig.txt`.

	mv numbers.txt numbers-orig.txt

You can delete files with the `rm` command.
This will delete the file `numbers.txt`.

	rm numbers.txt


<!-- move following to another section.... -->

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


<!-- END -->

### Scripts

An important aspect of the command line for science is that it provides a clear way to share the commands you ran to do an analysis or to calculate a result.
Since all the commands you type are text, we can also save these commands into a text file and have the shell
run many commands in a sequence.
Moreover these commands can be recorded as scripts that are shareable and repeatable.
The shell also has basic control commands implementing conditionals and loops.

**Comments** Shell scripts can have comments, which are text and notes that are skipped and not executed.
Comments are started by a hash sign `#` and continue until the end of the line.
Comments allow us to make notes reminding us of what we were trying to do, what we need to do, or
any strange bugs we had to work around.

**Loops** There are both "for" loops and "while" loops. A "for" loop will iterate over words in a list.
The list can either be provided or can be generated by a command:

	for name in 1 2 3 4 5; do
		touch x-$name
	done

and

	for name in $(seq 5); do
		touch x-$name
	done

Both of the above loops do the same thing: they make 5 empty files named `x-1`, `x-2`, `x-3`, `x-4`, and `x-5`.
Lets delete all these files. Here are three ways of doing the same thing:

	rm x-1 x-2 x-3 x-4 x-5

	rm x-*

	for name in $(seq 5); do
		rm x-$name
	done

**Conditional Statements** There is an if/then/else statement.

	if [ -e x-1 ]; then
		echo "File x-1 exists"
	fi

The `if` statement is really just checking the exit status of the commands, and the bracket `[` is actually a command!
The `[` command is also known as `test`. The following is equivalent to the above:

	if test -e x-1; then
		echo "File x-1 exists"
	fi

**Exit Status** Each command returns an exit status when it stops running.
The exit status is a number between 0 and 255.
It is not usually displayed, but it can sometimes be helpful.
The code 0 means everything was successful.
Non-zero codes indicate errors, the exact meaning depends on the command being run.
The shell sets the variable `$?` to be equal to the exit status of the previous command.

    $ cat abcdefg
    cat: abcdefg: No such file or directory
    $ echo $?
    1

### CSV Files

Lets download some data.

    curl -O https://data.nasa.gov/docs/legacy/meteorite_landings/Meteorite_Landings.csv

    https://data.nasa.gov/docs/legacy/meteorite_landings/Meteorite_Landings.csv


    curl -L -O https://dataverse.harvard.edu/api/access/datafile/11646850

    # is an ICE cube dataset
    from here: https://icecube.wisc.edu/data-releases/2025/07/measurement-of-atmospheric-neutrino-mixing-with-improved-icecube-deepcore-calibration-and-data-processing/
    https://dataverse.harvard.edu/file.xhtml?fileId=11646850&version=1.0&toolType=PREVIEW


This is a CSV file. We can look at it in the editor.

    open Meteorite_Landings.csv

CSV stands for _Comma Separated Values_, and it is a common format for storing tabular data.
It is a text-based format that separates values with commas, with each line containing one record of data
and each column representing a different attribute of the data.

    cat Meteorite_Landings.csv | head -n 5


## Resources

The shell and the command line bring together many more topics that you can read about if interested:

* [the PATH](https://www.cs.purdue.edu/homes/bb/cs348/www-S08/unix_path.html)
* [Exit Codes](https://www.redhat.com/sysadmin/linux-shell-command-exit-codes)
* [Quoting](https://rg1-teaching.mpi-inf.mpg.de/unixffb-ss98/quoting-guide.html) and [here](https://teaching.idallen.com/cst8207/13w/notes/440_quotes.html)
* Shell scripting. The shell we have been using is called _Bash_. A nice [Bash Scripting Tutorial](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/), and a a comprehensive [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html).

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

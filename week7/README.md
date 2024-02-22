# Week 7: More on Cloud Computing, with Databases

## Goals

This weeks activity will expose you the following:

1. Logging in to cloud computing instances, including security topics.
2. Using Relational Databases - a highly structured way to store and retrieve data
3. Taking a look at a "Document Store" database.


# Tutorial

## Part 1: Logging in to the newly-created instance.

### Secure Shell

The `ssh` command is used to run commands remotely and to encrypt the
communications going both ways. Encrypting the communication is
important - you don't really know where the network traffic is going
to be routed through and there are people who will intercept it along
the way. It has happened to me.

The `ssh` command can be used to run a single command remotely. For
instance,
```ssh username@18.222.52.104 uptime
```
will run the `uptime` command on the EC2 cloud instance we created for
you, and it will report how long it has been since the Linux
installation on there was rebooted (or installed in the first place).

If you don't tell `ssh` what command to run, it will start an
interactive session. At that point, it's like your terminal window was
connected to the remote instance. It will stay that way until you log
out of the remote machine.

The command is:
```
ssh username@18.222.52.104
```

You should replace "username" with the actual username we emailed to you.
For instance, I would type `ssh escott@18.222.52.104`


### Exploring the remote cloud instance

At this point, we're logged in to the remote EC2 instance. We can
execute commands on there just like we would our own VMs or our own
local computers (our laptops). Let's take a look around.

Start by seeing what directory we're in.
```
pwd
```

Look at what files and directories are there.
```
ls -l
```
(those are "ell" characters, and there is a space before the dash)

It turns out, there are more directories there than it looks like. By
convention, `ls` doesn't show us and file or directory names that
start with a period (pronounced "dot"). Of course there is a way to
solve that...

```
ls -la
```

Notice there is a ".ssh" directory (how can we tell it's a
directory?). The dot is there to hide the directory - we rarely care
about it, so it's hidden from us. Less visual noise.

Sometimes, though, we do care about it. :-)

Let's set our current working directory to that .ssh directory and see
if there is anything interesting in there. (Of course there is!)

```
cd .ssh
ls -l
```

### Basic Linux Security topics

The file "authorized keys" is interesting. Take a look at the
contents.
```
more authorized_keys
```

No one would expect you to recognize that, but the contents of that
file is the public key you generated a few weeks ago.

Here's how this works: ssh and many other network tools rely on
"Public Key Cryptography". Public key methods rely on two keys,
actually: a public one and a private one. Neither key is adequate by
itself - they're only effective as a pair. That's why it's perfectly
safe to share your public key. Your private key, on the other hand,
needs to be closely guarded.


Let's go back to your home directory.
```
cd
pwd
ls -l
```

### It's a Multiuser System

The `cd` command by itself, with no argument, sends you back to your
home directory.


The `cd` command with two dots as its argument moves up one level.
```
cd ..
pwd
ls -l
```

Notice all the directories at that level (you're in "/home" now). Each
of these is the home directory for each of the users. There are many
people logged into this one instance right now. To see a list of
everyone logged in to a given machine, use the `w` command.

```
w
```



## Part 2: Playing with the relational database service (RDS)

Amazon (and practically all other cloud providers) create their
competitive advantage not through merely renting hardware but also by
offering "Software as a Service" (SaaS).  What this means is that they
run software packages that can be accessed remotely. "GMail" is an
example. Google runs the many thousands of servers that keep GMail
running, but all the user knows is that they connect to it with a web
browser and use it.

Almost all the cloud providers offer some kind of database under a
SaaS model. Amazon is no exception.

At this point, we need to take a look at a few slides and see what
databases are and, in particular, what makes a relational database
management system (RDBMS) special.


### Connecting to the Database

A few minutes ago I went through the steps to create a RDBMS using
Amazon's RDS (Relational Database Service). I can take upwards of 20
minutes for an RDS instance to come up, so rather than waiting we'll
just use an instance I already have running.

The instance we're going to use is running an RDBMS called
"Postgres".  Postgres has a long and storied history, being the second
Open Source, totally free database "Ingres" was the first, from the
same research group headed by Michael Stonebreaker. For his work on
Ingres, Postgres, and many subsequent RDBMSes, and his foundational
work on new technologies in databases, he won a Turing Award.

Let's connect to this running database.
```
psql --host=$DBHOST --user=cicf experiments
```

The password is "cicfsummer". The `psql` (it stands for "PostgresQL")
command connects to the database server and lets you enter
commands. These commands consist of a mixture of Structured Query
Language (SQL) and some built-in commands for monitoring and
controlling the RDBMS. SQL is pretty standardized - once you learn it
on one database, it's 99+% identical across all the other relational
databases. On the other hand, the monitoring and control commands are
unique to each one.

Anyway. Once `psql` connects, it will print a little information and
then a prompt. The "experiments" part at the end says "once you've
connected to the database server, set up everything so my commands
refer to the actual database called "experiments".

At this point, `psql` has connected and will be showing this prompt:

experiments=>

Let's play with some commands. The
semicolons at the ends of the lines are important.

```
\d
```
(Ok, no semicolon after that one, but all the others will need
one. There's no semicolon because this is not a SQL command, but
rather one of those non-standard command and control statements.)

Now let's see what is contained in the "devices" and "results" tables.
```
SELECT * FROM devices;

SELECT * FROM results;
```
The uppercase words don't have to be uppercase, that's just a
convention adopted ages ago to make queries more readable.

We don't have to select every row in table.
```
SELECT * FROM results WHERE volts > 1.6;
```

We can specify a "cartesian product" of the two tables (though to be
fair, I've only had a legitimate reason to do this twice in my entire
career)
```
SELECT * FROM results, devices;
```

If we add some "filter criteria" via the WHERE clause
then we can turn that cartesian product into a "join":
```
SELECT * FROM devices, results where results.instrument = devices.instrument;
```
Notice that instead of producing an explosive number of rows, this
gives a much more reasonable result set. What we end up with is a
report of all the experiments and we manage to include information
about the instrument itself on the relevant lines. Where a cartesian product
combines every row of one table with every row of another table, a
join only matches the rows that meet the filter criteria in the WHERE
clause.

Finally, we don't have to select every column. We can specify which
ones we want.
```
SELECT results.reading, results.volts, devices.description
FROM devices, results
WHERE results.instrument = devices.instrument;
```
Notice something else interesting? Long SQL commands can span multiple
lines. The database server will keep reading lines and adding them
onto the current query until it finally comes to a semicolon. And
that's why you have to end queries with a semicolon. :-)








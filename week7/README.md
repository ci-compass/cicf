# Week 7: More on Cloud Computing, with Databases

## Goals

This weeks activity will expose you the following:

1. Logging in to cloud computing instances, including security topics.
2. Using Relational Databases - a highly structured way to store and retrieve data
3. Taking a look at a "Document Store" database.


# Tutorial

##Part 1: Logging in to the newly-created instance.

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

### Basic Linux Security Topics

The file "authorized keys" is interesting. Take a look at the
contents.
```
more authorized_keys
```


cd
pwd
ls -l
cd ..
pwd
ls -l

w




Step 2: Playing with the relational database service (RDS)

psql --host=$DBHOST --user=cicf experiments

The password is "cicfsummer". The psql (it stands for "PostgresQL")
command connects to the database server and lets you enter commands.
The "experiments" part at the end says "once you've connected to the
database server, set up everything so my commands refer to the
actual database called "experiments".

At this point, psql has connected and will be showing this prompt:

experiments=>

Let's play with some SQL ("Structured Query Language") commands. The
semicolons at the ends of the lines are important.

\d
(Ok, no semicolon after that one, but all the others will need one)

select * from devices;

select * from results;

select * from results where volts > 1.6;

select * from results, devices;

select * from devices, results where results.instrument = devices.instrument;





# Week 6: Intro to Cloud Computing

Bad news - the semester is half gone already. Where did the time go?  Anyway.



Step 1: Logging in to the newly-created instance.

The command is:
ssh username@18.222.52.104

You should replace "username" with the actual username we emailed to you.
For instance, I would type "ssh escott@18.222.52.104".



Let's take a look around.

pwd
cd .ssh
ls -l

more authorized_keys

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





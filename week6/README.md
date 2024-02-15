# Week 6: Intro to Cloud Computing

Bad news - the semester is half gone already. Where did the time go?  Anyway.


The first thing I did when we started this lab activity was that I started
up a Virtual Machine running in Amazon's "AWS" cloud. This VM is more or less
just like the ones we've been using on our laptops, except this new one
is *very* bare-bones. It doesn't even have a GUI installed - it's all command
line all the time. This is normal in the HPC world.

Remember how we've been hounding^Wreminding everyone "We need your public
keys!"? Today we're going to be using them. I could have started up the
instance (in the cloud world, a VM is called an "instance") with a completely
generic Linux installation and then gone in and configured everything.
Instead,, well, I did do that, a week ago, and I saved a snapshot of
the instance. Today when I went to start up our instance, I selected the
option to create the instance by using the snapshot I prepared beforehand.
Amazon calls those images "AMI"s, standing for Amazon Machine Instance.

I mention this because I went ahead a few days ago and I created user accounts
for each of you. I saved your public key with your account. That means you can
log in using your private key on your laptop's VM and it will match up with
the public key installed in that AMI. Let's do that now:

ssh Username@XXX.XXX.XXX.XXX

Obviously, don't literally put "Username" there, but instead put your
username created for this lab. In my case, I would use "escott". The
XXX.XXX.XXX.XXX part is the IP address of the instance we just created.
It's in the form of four numbers separated by periods. My command a few
days ago looked like "ssh escott@18.222.52.104", but I can guarantee you
the address will be different today.


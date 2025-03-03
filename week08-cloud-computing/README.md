# CICF Week 8

The goals for week 5 lab are:

- Familiarize yourself with a virtual machine running in a cloud
  environment.

This week we will:

- Log into a cloud virtual machine (VM) using `ssh`,
- Copy some files to the VM using `scp`,
- Run JupyterLab in the VM, and
- Learn how to secure the VM.

## Tutorial

### Update your CICF repository clone

Start a terminal in the CICF VM running on your desktop, and run these
commands:

```
$ cd ~/cicf/week08-cloud-computing
$ git pull origin master
```

### Connect to your cloud VM

Each of you will get your own VM. The virtual machines are deployed
for you on Digital Ocean (DO), a cloud provider.  (DO calls VMs
"droplets".)

You can access your VM using [`ssh`][ssh], the OpenSSH remote login
client.  We will not use a password to log on to the VM, but rather,
we would use public key authentication.  (In fact, password
authentication with `ssh` is disabled on these VMs, because it is
considered insecure.  Remember that our little VM is out there on the
hostile territory of the public internet, and bad people can guess or
brute-force passwords.  Using public key cryptography is more secure.)

[ssh]: https://www.openssh.com/

```
$ ssh -o PasswordAuthentication=no -o PubkeyAuthentication=yes -i ~/.ssh/id_ed25519 cicf@YOUR-FIRST-NAME.cicf.cloud
```

Replace `YOUR-FIRST-NAME` with, well, your first name.  For reference,
these are the virtual machines:

* `aidan.cicf.cloud`
* `anshuraj.cicf.cloud`
* `baydan.cicf.cloud`
* `catherine.cicf.cloud`
* `dylan.cicf.cloud`
* `ejay17.cicf.cloud`
* `elikem.cicf.cloud`
* `emma.cicf.cloud`
* `jasmine.cicf.cloud`
* `joanna.cicf.cloud`
* `macy.cicf.cloud`
* `naomi.cicf.cloud`
* `noe.cicf.cloud`
* `priscilla.cicf.cloud`
* `rishi.cicf.cloud`
* `spoorthi.cicf.cloud`
* `tamara.cicf.cloud`
* `xiuweb.cicf.cloud`

Since that `ssh` command is long and annoying to type every time we
need to use `ssh` (and its sibling `scp`, which we will use next), we
can save those `ssh` options in `~/.ssh/config`:

```
Host *.cicf.cloud
    User cicf
    PubkeyAuthentication yes
    PasswordAuthentication no
    IdentityFile ~/.ssh/id_ed25519     
```

With that configuration, you should be able to simply do `ssh
YOUR-FIRST-NAME.cicf.cloud`.

### Copy some files to your cloud VM

We have three files in [`data`](./data) directory:

- [`install-docker.sh`](./data/install-docker.sh), our old friend from
  week 5. We will use this script to install Docker on the VM.
- [`compose.yml`](./data/compose.yml), a Docker compose file that we
  will use to deploy JupyterLab and [Caddy], a [reverse proxy] server.
- [`Caddyfile`](./data/Caddyfile), which contains necessary
  configuration for Caddy.

 [Caddy]: https://caddyserver.com/
 [reverse proxy]: https://en.wikipedia.org/wiki/Reverse_proxy

 We will use [`scp`] to copy the `data` directory from your local VM
 to the cloud VM:

 ```
  $ scp -r data YOUR-FIRST-NAME.cicf.cloud:
 ```

Note that the above is a short-cut for the longer command below:

 ```
 $ scp -o PasswordAuthentication=no -o PubkeyAuthentication=yes -i ~/.ssh/id_ed25519  -r data cicf@YOUR-FIRST-NAME.cicf.cloud:/home/cicf/
 ```

We could save some typing since we have some configuration in
`~/.ssh/config`, and since the home directory is the default
destination when you invoke `scp`.


### Install Docker on the cloud VM

In the cloud VM, run

```
$ cd ~/data
$ ./install-docker.sh
```

Press `y` when prompted.

Once Docker has been installed, add yourself to `docker` group:

```
$ sudo usermod -a -G docker $USER
```

Log out of the VM using `Control-D`, `exit`, or `logout`, and log back
in with `ssh`:

```
$ ssh YOUR-FIRST-NAME.cicf.cloud
```

Make sure that you are now indeed in `docker` group:

```
$ groups
cicf sudo docker
```

# Run JupyterLab and Caddy with Docker Compose

Docker Compse is a tool for running applications running in more than
one container together.  You would run Docker Compose in the format
`docker compose COMMAND`.  Take a look at the output of `docker
compose help` to get an idea of what you can do.

You specify the applications you need to run with Compose and their
configuration in a file named `compose.yml` or `docker-compose.yml`.
Our `compose.yml` is in `~/data` directory:

```
$ cd data
```

We already have the configuration to run JupyterLab and Caddy in this
`compose.yml`.  It needs a change in one line.  Open the file in an
editor (`nano` perhaps) and find the line that says:

```
      - DOMAIN=YOUR-FIRST-NAME.cicf.cloud # Replace with your actual domain
```

Replace `YOUR-FIRST-NAME` with the right thing, so that domain is the
correct one.

Now we can run Docker Compse in detached mode (as in, not attached to
a terminal), with:

```
$ docker compose up -d
```

This will run JupyterLab and Caddy. JupyterLab will run on port 8888,
but we will not expose that port to the internet.  We will expose
ports 80 and 443 of Caddy to the internet.  Port 80 is for HTTP
(un-encrypted web traffic) and 443 is for HTTPS (encrypted web
traffic).  All port 80 traffic will be re-routed to
port 443.

For HTTPS to work correctly, Caddy will need a TLS certificate that
basically assert that the domain is what it claims it is, and provide
the information necessary for encryption and data integrity. 

Caddy can seamlessly get a TLS certificate from [Lets Encrypt][le], a
non-profit certificate authority.

[le]: https://letsencrypt.org/

Getting a TLS certificate used to be quite an involved process. You
had to pay for your certificates, and go through some manual processes
to prove your identity.  Lets Encrypt is a wonderful project that
removed this friction and made encrypted communication accessible to
everyone.

Anyway, end of speech.  We can now test things by visiting our new
site at `https://YOUR-FIRST-NAME.cicf.cloud` with a web browser.

Watch the logs that `docker compose` prints on the console when you
started things up and when you visited the site:

```
$ docker compose logs --follow
```

Use `Control-C` to stop following the log.

You can shut down things with:

```
$ docker compose down
```

### Install a service

The `docker compose` service you ran will quit when you log out of
your `ssh` session, because that is how processes work.  

To make things continue running even when you are logged out of the
cloud VM, we can install a [systemd] service.

[systemd]: https://systemd.io/


### References

<!-- TODO -->

- [Docker Compose](https://docs.docker.com/compose/) documentation.
- [Caddyfile](https://caddyserver.com/docs/caddyfile) reference.


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


### Install and run some software

<!-- TODO -->

<!-- - JupyterLab + Caddy using docker compose perhaps? -->

### References

<!-- TODO -->

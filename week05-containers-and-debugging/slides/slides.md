---
title: "CICF Week 5: Containers and Debugging"
format:
  # pptx:
  #   reference-doc: cicf-template.pptx
  #   fig-width: 300
  revealjs:
    theme: default
#  beamer:
#    theme: default
---

# Welcome to week five of CICF!

## The plan this week

We will go over two different topics: containers and debugging

::: {.notes}

They are different topics. There could be some unifying thing there,
such as debugging containers or debugging inside containers, but we
are not there yet.  We are discussing them together only because we
could not dedicate more time to each of them. They are both important
topics.

By necessity, we will keep things short and simple, and gloss over
some things.  You should explore things on your own, and go after
things that really interest you.

:::

# Containers

## What are containers?

Containers are lightweight and portable environments that package an
application and its dependencies.

- Docker is the most popular implementation.
- Others exist too, such as:
  - Podman
  - Apptainer (formerly Singularity)
  - LXC/LXD
  - CoreOS rkt (or "Rocket")
  - Kubernetes cri-o

Let us just stay with Docker here.

::: {.notes}

Containers enable consistent deployment across different computing
platforms.  If your application was built and tested on some old
Debian stable version, you would be able to "containerize" it, and run
it on a new Ubuntu machine, or even macOS or Windows hosts -- as long
as you have a working container runtime on the target machine.

We will look at docker here, but the fundamentals are the same.

:::


## Why would you use containers?

- Building software can be a brittle process.
- So can be deploying software.

Problem is having the correct versions of all the dependencies.

So we _package_ software and dependencies into _containers_.

::: {.notes}

Building and deploying software can be a brittle process.

You have some software x that is at version 1, and it needs version 1
of library y.  But your computer has only version 0.9.8 of library y.
If you try to upgrade library y, another application z which depends
on y 0.9.8 might break.

This gets even more complicated when you are deploying software on a
fleet of computers.  Sometimes multiple people or teams ("developers"
who write the software on their machines and "operations" who run the
software on "production" machines) are involved, and there may be a
mismatch between developer environment and production environment.

When operations team complain to the developer when something does not
work, the developer would say: "it works on my machine!"

We solve this problem by "containerizing" x and its dependencies.

Containers allow us to package our applications, the runtime required
to run the application, configuration files, and any dependencies the
application needs into one artifact.

As long as there is a container runtime in the target machine, the
application works.

The host OS on the target machine could be Ubuntu 25.04, and the
container could be made using some old version of Debian stable.
Since we have "containerized the application", it will seamlessly
work.

:::

## Container images


```
+------------------------------------+
| app code                           |
+------------------------------------+
| Python libraries                   |
+------------------------------------+
| Python interpreter                 |
+------------------------------------+
| libc and other system libraries    |
+------------------------------------+
| base OS                            |     
+------------------------------------+
```

::: {.notes}

Container images are "tarballs", or compressed archives of a
filesystem tree.

TODO: add notes about layers and overlayfs.

Look around `/var/lib/docker` maybe.

:::


## A quick look at `docker` commands

```
$ docker help

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers
  build       Build an image from a Dockerfile
  pull        Download an image from a registry
  push        Upload an image to a registry
  images      List images
  login       Authenticate to a registry
  logout      Log out from a registry
  search      Search Docker Hub for images
  version     Show the Docker version information
  info        Display system-wide information

[...]
```

::: {.notes}

If you run `docker help`, it will print a longish message, with some
hints about subcommands.  We will look at some of the commonly used
subcommands.

This might look confusing at first.  It was confusing to me at first
when I was trying to figure out containers!  

Together let us try to demystify this.

:::

## What is a `Dockerfile`?

```Dockerfile
# Base image with Python 3.12
FROM python:3.12

# Set working directory in container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all project files to container
COPY . .

# Container listens on port 5000
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
```

::: {.notes}

:::


## What do you do with a `Dockerfile`?

You can build container images! You can run them!

```
docker build --tag "app:latest" .
docker images
docker run app:latest
```

In the tutorial we will use a simpler `Dockerfile` and slightly
different options with `docker build`, but you get the idea.


## Containers under the hood

They use some Linux specific techniques:

- _cgroups_ (or "control groups") to set resource limits (such as
  memory and CPU).
- _pivot_root_ to change the root filesystem.
- _namespaces_ to allow processes to have their own network, process
  IDs, hostname, mounts, users, etc.
- _capabilities_ to give specific permissions.
- _seccomp-bpf_ to prevent dangerous system calls.
- _overlay filesystems_ to make container image layers work.

## Container registries

What happens when you do a `docker pull`?

## A word about versioning

You could use:

- a number
- a date or a timestamp
- a commit hash
- a version string like `major.minor.patch`

See <https://semver.org/> and [Python version
specifiers](https://packaging.python.org/en/latest/specifications/version-specifiers/).

::: {.notes}

You work and work and work on your software project. From time to
time, you will release your project.  The releases will have some
version number.  Versions indicate what features and bugs are present
in a release.

There are several ways of versioning software projects.

When working alone on a project that only you use, versioning scheme
does not matter too much.

When working in a team, or when working on a project that has public
releases, it is a good idea to use a more formal scheme such as
semantic versioning.

:::


## Containers and virtual machines

You can run a container inside a virtual machine but can you run a
virtual machine inside a container?


# Debugging

## What is a bug?

<!-- TODO: Grace hopper and the bug -->

## Debugging strategies

## Using print statements

## Using logging

## Using Python `pdb` module

## Using Python `trace` module

## Using unit tests

## Talking to a friend

# FIN

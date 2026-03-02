# CICF Week 5

The goals for week 5 tutorial are:

1. Make and run a simple Docker image.
1. Run a service packaged in an external Docker image.
1. Use the Python debugger (pdb).

## Tutorial

Surprise! You have already been using containers since Codespaces are
implemented as a container.
Try

    $ docker ps

This lists all the containers that are currently running.
There should be no containers running, but the important thing is
that there are no errors.

> [!NOTE]
> If the `docker` command does not work we need to update the codespace container.
>
>     $ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /etc/apt/keyrings/yarn-archive-keyring.gpg > /dev/null
>     $ git pull	# inside /workspaces/cicf
>
> At this point you will be asked to rebuild your container. Say yes.
> If you accedentially chose "no" you can rebuild your container
> by chosing the command bar and start typing ">rebuild"; an option to rebuild the
> container will appear below and select it.
> (Why did it ask to rebuild? because the `.devcontainer/devcontainer.json` file
> was updated during the "git pull".)

<!-- NOTE: the above note won't be necessary after Spring 2026
The pubkey update is from https://github.com/yarnpkg/yarn/issues/6885
-->

### Build an image

Our first task is to create a container image.
The `Dockerfile-hello` contains the instructions on how to build the
image.

    $ cat Dockerfile-hello
    FROM python:3.12-slim
    COPY hello.py /hello.py
    CMD ["python", "hello.py"]

We start with an official base python image, we copy in our script,
and then we specify the command to run when the container is started.
The `docker build` will follow this receipe to make an container image:
(n.b. don't forget the "." at the end)

    $ docker build -t hello -f Dockerfile-hello .

This is making an image from that instruction file and names the image "hello".

    $ docker images
    IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
    hello:latest   05bf3d415042        177MB         43.3MB

And then to run the image:

    $ docker run hello
    Hello World

We can see the layers (i.e. sequence of commands to make the image)
with the "history" command:

    $ docker history hello
    IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
    05bf3d415042   3 minutes ago   CMD ["python" "hello.py"]                       0B        buildkit.dockerfile.v0
    <missing>      3 minutes ago   COPY hello.py /hello.py # buildkit              8.19kB    buildkit.dockerfile.v0
    <missing>      3 days ago      CMD ["python3"]                                 0B        buildkit.dockerfile.v0
    <missing>      3 days ago      RUN /bin/sh -c set -eux;  for src in idle3 p…   16.4kB    buildkit.dockerfile.v0
    <missing>      3 days ago      RUN /bin/sh -c set -eux;   savedAptMark="$(a…   41.5MB    buildkit.dockerfile.v0
    <missing>      3 days ago      ENV PYTHON_SHA256=a97d5549e9ad81fe17159ed02c…   0B        buildkit.dockerfile.v0
    <missing>      3 days ago      ENV PYTHON_VERSION=3.14.3                       0B        buildkit.dockerfile.v0
    <missing>      3 days ago      RUN /bin/sh -c set -eux;  apt-get update;  a…   4.94MB    buildkit.dockerfile.v0
    <missing>      3 days ago      ENV PATH=/usr/local/bin:/usr/local/sbin:/usr…   0B        buildkit.dockerfile.v0
    <missing>      6 days ago      # debian.sh --arch 'amd64' out/ 'trixie' '@1…   87.4MB    debuerreotype 0.17

The most recent change is at the top and the oldest change is at the bottom.

We can see the all containers (whether running or not) with the
`-a` option on the `ps` command:

    $ docker ps -a

Okay, let's see if the execution environment is really restricted:

    $ docker run -it hello bash

This has less of everything:

    env
    ping
    python3

Also, by default, containers have no network access.

We can make a second version of hello.
Edit `hello.py` to read:

>    #!/usr/bin/env python3
>
>    print("Hello World Again!!!!")

When we rebuild the container we have a choice: we can keep the same name (`hello:latest`) or we can give it a version tag.
Lets tag it as version 2.
(There is nothing special about "2", you can use any string as a label.)

    $ docker build -t hello:2 -f Dockerfile-hello .

And then we use the tag to refer to it.

    $ docker run hello:2
    Hello World Again!!!!
    $ docker run hello
    Hello World

<!-- current edit point -->
### Network Store

We are going to run a service using docker.

    $ docker run -d -p 6379:6379 redis

The container should have started and be running in the background.

    $ docker ps
    CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS          PORTS                                         NAMES
    c9b559f30c43   redis                       "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes    0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp   brave_cohen
    $ docker logs {id} | tail
    1:M 13 Feb 2026 15:56:59.145 * <ReJSON> Exported RedisJSON_V3 API
    1:M 13 Feb 2026 15:56:59.145 * <ReJSON> Exported RedisJSON_V4 API
    1:M 13 Feb 2026 15:56:59.145 * <ReJSON> Exported RedisJSON_V5 API
    1:M 13 Feb 2026 15:56:59.145 * <ReJSON> Exported RedisJSON_V6 API
    1:M 13 Feb 2026 15:56:59.145 * <ReJSON> Enabled diskless replication
    1:M 13 Feb 2026 15:56:59.145 * <ReJSON> Initialized shared string cache, thread safe: true.
    1:M 13 Feb 2026 15:56:59.145 * Module 'ReJSON' loaded from /usr/local/lib/redis/modules//rejson.so
    1:M 13 Feb 2026 15:56:59.145 * <search> Acquired RedisJSON_V6 API
    1:M 13 Feb 2026 15:56:59.145 * Server initialized
    1:M 13 Feb 2026 15:56:59.145 * Ready to accept connections tcp

This is running a network cache store called "Redis".
It provides a server (not web based, though) to store and cache values between server computers.
This is very common service to have running to support a web portal.
We can interact with it via python.

    pip install redis

<!-- TODO: update requirements.txt to include redis module -->

And now:

    $ python
    >>> import redis
    >>> r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    >>> r.get("qwerty")
    >>> r.set("qwerty", "this key is the first")
    True
    >>> r.get("qwerty")
    'this key is the first'

Redis can do a lot more than just act as a network-attached hash map.
For one thing, keys can expire after a set amount of time.

    >>> r.set("test", "this will be gone in 30 seconds", ex=30)
    >>> r.get("test")
    'this will be gone in 30 seconds'
    >>> # wait 20 seconds
    >>> r.get("test")
    >>>

We can load a web UI for redis

    $ docker run -d --name redisinsight -p 5540:5540 redis/redisinsight:latest
    $ docker ps
    CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS          PORTS                                         NAMES
    d1932500487f   redis/redisinsight:latest   "./docker-entry.sh n…"   1 minute ago     Up 1 minute     0.0.0.0:5540->5540/tcp, [::]:5540->5540/tcp   redisinsight
    c9b559f30c43   redis                       "docker-entrypoint.s…"   58 minutes ago   Up 58 minutes   0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp   brave_cohen
    $ docker inspect brave_cohen | grep IPAddress
    172.17.0.2

In place of "brave_cohen" above, use the identifier for your redis container.
Copy the IP Address and then click the button to view the 5540 port in a new browser window.
(If the pop-up dialog disappeared, you can do it by chosing the "PORT" tab and then clicking on the globe icon for port 5540).

Agree to the EULA, and then add a new database.
Replace the `127.0.0.1` address with the one we copied.
You will see keys we have added to our redis instance.
Add a key named `fib-45` with the type "string" and the value '' (the empty string).

On the command line run our `store.py` script.

Switch back to the redis viewer. The value for key `fib-45` should be 1134903170.


<!-- TODO: do pdb example -->

## Other Debugging tools

To find a bug you need information to understand what is happening.
If print statements or pdb doesn't help find a bug, sometimes it helps
to trace the execution with more detailed tools.
One is called "strace", for "system trace".
This command will run the program and log every system call to STDERR.

    $ strace python hello.py
    execve("/usr/local/bin/python", ["python", "hello.py"], 0x7ffd179a6d88 /* 58 vars */) = 0
    brk(NULL)                               = 0x57b513b24000
    mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x763891923000
    readlinkat(AT_FDCWD, "/proc/self/exe", "/usr/local/bin/python3.13", 4096) = 25
    access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/local/bin/../lib/glibc-hwcaps/x86-64-v3/libpython3.13.so.1.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
    newfstatat(AT_FDCWD, "/usr/local/bin/../lib/glibc-hwcaps/x86-64-v3/", 0x7fff44c7e1f0, 0) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/local/bin/../lib/glibc-hwcaps/x86-64-v2/libpython3.13.so.1.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
    newfstatat(AT_FDCWD, "/usr/local/bin/../lib/glibc-hwcaps/x86-64-v2/", 0x7fff44c7e1f0, 0) = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/local/bin/../lib/libpython3.13.so.1.0", O_RDONLY|O_CLOEXEC) = 3
    [...385 more lines]

Python also has a tracing module which will print every line as it is executed

    $ python -m trace -t hello.py
     --- modulename: hello, funcname: <module>
    hello.py(3):  print("Hello World")
    Hello World

## Resources

- [Python pdb debugger](https://docs.python.org/3/library/pdb.html)
- [Reprozip](https://www.reprozip.org/) is a cool tool that will watch
  a program run (using the strace mechanism) and then save all the
  files opened and their contents into a zip file. It then has the
  ability to create a container from the zip file.
- [Apptainer](https://apptainer.org/)
  ([docs](https://apptainer.org/docs/user/latest/)) is a container
  system, like Docker, that is more common in High Performance
  Computing environments.
- [List of Docker images for the IceCube Neutrino Observatory](https://hub.docker.com/u/icecube)
  and their [instructions](https://docs.icecube.aq/icetray/main/index.html)
  for using the software.
- [Minio docs](https://min.io/docs/minio/container/index.html) (The
  object store we used in the tutorial).
- [jq](https://jqlang.github.io/jq/) is a great command line tool for
  working with JSON files. And there is a
  [playground](https://jqplay.org/) for messing around.
- [misadventures in process containment](https://apenwarr.ca/log/?m=201901)
- [Fibonacci Sequence](https://oeis.org/A000045) on the OEIS.
- Minio Python client [reference
  documentation](https://min.io/docs/minio/linux/developers/python/API.html#put_object)
- A [tutorial on using GNSS reflection data](https://gnssrefl.readthedocs.io/en/latest/pages/docker_cl_instructions.html)
  to measure snow and water height that uses a docker image.

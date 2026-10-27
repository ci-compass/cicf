# CICF Week 5

The goals for the week 5 tutorial are:

1. Build and run a container image using Apptainer.
1. Run a service packaged in an external container image using Apptainer instances.
1. Use the Python debugger (`pdb`) to troubleshoot and fix a script.

## Tutorial

In previous weeks, you have been working inside a containerized environment. This week, we explore how containers work, why they are essential to cyberinfrastructure, and how to create and manage them yourself using **Apptainer**.

### Containers in Scientific Cyberinfrastructure: Why Apptainer?

Containers are lightweight, portable environments that package an application together with its runtime, system libraries, configuration files, and dependencies.

While **Docker** is widespread on personal workstations and commercial clouds, it is rarely deployed in High Performance Computing (HPC), National Science Foundation (NSF) cyberinfrastructure facilities, or shared research platforms (like the National Research Platform / National Data Platform).
Instead, **Apptainer** (formally Singularity) is usually used.
There are several reasons for this:

1. **Rootless & Security**: Docker requires a background daemon (`dockerd`) running with root privileges. Granting a user access to Docker on a multi-user cluster is effectively equivalent to giving them root access to the entire host. In contrast, Apptainer runs unprivileged in user space without any background root daemon. You are the same user inside the container as you are outside.
2. **Single-File Images (SIF)**: Apptainer packages containers into a single, immutable **Singularity Image Format (`.sif`)** file. A `.sif` file is a complete filesystem image that can be copied, moved, archived alongside research data, or shared with collaborators just like any other file.
3. **Seamless Filesystem Integration**: By default, Apptainer automatically mounts your home directory (`$HOME`), the current working directory (`$PWD`), and temporary directories (`/tmp`), making it trivial to read and write data files on the host without complicated volume mount syntax.
4. **Docker Interoperability**: Apptainer can directly pull, convert, and run container images from Docker Hub and other OCI registries using the `docker://` prefix.

Check that Apptainer is installed and available:

    $ apptainer --version
    apptainer version 1.3.6


### Build an Image

In Docker, container recipes are written in a `Dockerfile`. In Apptainer, recipes are written in an **Apptainer Definition File** (conventionally ending in `.def`).

Inspect the definition file `hello.def` in this directory:

    $ cat hello.def
    Bootstrap: docker
    From: python:3-slim

    %files
        hello.py /hello.py

    %runscript
        python /hello.py "$@"

    %labels
        Author CICF
        Version v1.0

This definition file has three main sections:
* **`Bootstrap: docker` / `From: python:3-slim`**: Specifies the base image to build upon. Apptainer will pull the official Python 3 slim base image from Docker Hub.
* **`%files`**: Copies files from the host into the container filesystem during build time. Here, `hello.py` from the current directory is copied to `/hello.py` inside the container.
* **`%runscript`**: Specifies the command that will be executed when the container image is launched with `apptainer run` (or by executing the `.sif` file directly).

#### Building the SIF image

We build the container image using the `apptainer build` command:

    $ apptainer build hello.sif hello.def

> [!NOTE]
> If you are on a system configured with unprivileged user namespaces, you can also add `--fakeroot` when building images:
>
>     $ apptainer build --fakeroot hello.sif hello.def

Apptainer will pull the base layers, unpack them, copy `hello.py`, configure the runscript, and pack everything into a single file named `hello.sif`.

Notice that the resulting image is just a regular file in your directory:

    $ ls -lh hello.sif
    -rwxr-xr-x 1 jovyan users 55M Feb 13 15:30 hello.sif

You can inspect the metadata, runscript, and definition file stored inside the SIF image:

    $ apptainer inspect hello.sif
    $ apptainer inspect --runscript hello.sif
    $ apptainer inspect --deffile hello.sif

#### Running the image

Run your new container image with `apptainer run`:

    $ apptainer run hello.sif
    Hello World

Because SIF images are self-executable binaries, you can also run them directly from the shell:

    $ ./hello.sif
    Hello World

#### Executing commands and opening an interactive shell

You are not limited to running only the default `%runscript`. You can execute any arbitrary command inside the container environment using `apptainer exec`:

    $ apptainer exec hello.sif python -c "import sys; print(sys.version)"

You can also drop into an interactive shell inside the container using `apptainer shell`:

    $ apptainer shell hello.sif
    Apptainer> which python
    /usr/local/bin/python
    Apptainer> python /hello.py
    Hello World
    Apptainer> exit

Notice that while you are inside the container, your current working directory and files are immediately accessible, but software installations are isolated to the container's environment.

#### Versioning your images

In scientific computing, tracking versions of your code and environment is critical for reproducibility.

Edit `hello.py` to say:

```python
#!/usr/bin/env python3

print("Hello World Again!!!!")
```

Build a new version of the image:

    $ apptainer build hello-v2.sif hello.def

Now you have two distinct, immutable image files representing versions 1 and 2:

    $ ./hello.sif
    Hello World
    $ ./hello-v2.sif
    Hello World Again!!!!

You can archive `hello.sif` and `hello-v2.sif` alongside your scientific data or publish them to a repository with persistent identifiers (like DOIs).


### Network Store and Services: Apptainer Instances

In cyberinfrastructure systems, we often need services (such as databases, caches, or web APIs) running continuously in the background.

In Apptainer, background services are managed through **instances**.

#### Starting a Redis service

We will start a container running **Redis**, an in-memory key-value cache store widely used to support web portals and scientific data pipelines.

You can launch a named instance directly from an image hosted on Docker Hub without building a local `.def` file first:

    $ apptainer instance start docker://redis:latest redis-server

Apptainer downloads the image layers from Docker Hub, converts them to an SIF format in its cache, and starts the container in the background under the instance name `redis-server`.

List all running instances:

    $ apptainer instance list
    INSTANCE NAME    PID      IP              IMAGE
    redis-server     14205    127.0.0.1       ~/.apptainer/cache/oci-tmp/.../redis_latest.sif

You can execute commands inside the running instance using the `instance://` URI prefix:

    $ apptainer exec instance://redis-server redis-cli ping
    PONG

#### Networking in Apptainer

In Docker, containers run inside an isolated virtual network bridge and require port mapping flags (like `-p 6379:6379`).

In Apptainer, containers **share the host's network namespace by default**. When Redis listens on port `6379`, it is immediately available on `localhost:6379` (`127.0.0.1:6379`) on the host machine.

#### Interacting with Redis using Python

Install the Python client library for Redis:

    pip install redis

Open an interactive Python session:

    $ python
    >>> import redis
    >>> r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    >>> r.get("qwerty")
    >>> r.set("qwerty", "this key is the first")
    True
    >>> r.get("qwerty")
    'this key is the first'

Keys in Redis can also be set with expiration times (useful for temporary caching):

    >>> r.set("test", "this will be gone in 30 seconds", ex=30)
    True
    >>> r.get("test")
    'this will be gone in 30 seconds'
    >>> # Wait 30 seconds...
    >>> r.get("test")
    >>> exit()

#### Running a Web UI for Redis (RedisInsight)

We can also launch a web-based dashboard to visualize our Redis store. We will launch RedisInsight as a second Apptainer instance:

    $ apptainer instance start docker://redis/redisinsight:latest redisinsight

Check that both instances are active:

    $ apptainer instance list
    INSTANCE NAME    PID      IP              IMAGE
    redis-server     14205    127.0.0.1       ...
    redisinsight     14312    127.0.0.1       ...

Because Apptainer instances share the host network, RedisInsight will listen directly on port `5540`:
1. Open a browser window to `http://localhost:5540` (or `http://127.0.0.1:5540`).
2. Agree to the EULA, and choose **Add Redis database**.
3. Set the Host to `127.0.0.1` and Port to `6379`. (Unlike Docker, you do not need to look up private container IP addresses; both services communicate over `localhost`).
4. In the RedisInsight database browser, add a new key named `fib-45` with type **String** and the value `""` (an empty string).

Now, run the provided script `store.py`:

    $ python store.py

The script scans for keys matching `fib-*`, calculates the corresponding Fibonacci number, and updates Redis.

Switch back to the RedisInsight browser tab. The value for `fib-45` will now display:

    1134903170

#### Stopping Apptainer instances

When you are finished with the services, stop the instances:

    $ apptainer instance stop redisinsight
    $ apptainer instance stop redis-server

Or stop all running instances at once:

    $ apptainer instance stop --all
    $ apptainer instance list
    INSTANCE NAME    PID    IP    IMAGE


## Debugging

Finding and diagnosing bugs is a core skill when building cyberinfrastructure software.

### The Python Debugger (`pdb`)

When an error occurs or a script produces incorrect results, interactive debugging allows you to step through code execution line by line, inspect variable states, and verify assumptions.

In this directory, there is a script called `exercise-1.py` and a dataset of values in `numbers.txt`.
The script is intended to find the highest average among all contiguous sub-sequences of a given length $N$.

Run the script on `numbers.txt` looking for sub-sequences of length 5:

    $ ./exercise-1.py numbers.txt 5
    497.0

Now run the automated test suite:

    $ make
    # or: pytest test.py

The test fails!

```text
______________________________ test_exercise_1 _______________________________
    def test_exercise_1():
        result = subprocess.run(["./exercise-1.py", "numbers.txt", "5"], capture_output=True)
        assert(result.returncode == 0)
        output = result.stdout.decode()
>       assert(float(output) == 498)
E       assert 497.0 == 498.0
```

The script returned `497.0`, but the actual maximum average is `498.0`. There is an off-by-one bug in `exercise-1.py`.

#### Stepping through with pdb

Run the script under the Python debugger:

    $ python -m pdb exercise-1.py numbers.txt 5

The debugger will pause on the first line of the script:

```text
> /.../exercise-1.py(5)<module>()
-> import argparse
(Pdb)
```

Common `pdb` commands:
* **`l` (list)**: Show current source lines around the execution point.
* **`n` (next)**: Execute the current line and advance to the next line in the current function.
* **`s` (step)**: Step into the function call on the current line.
* **`c` (continue)**: Continue running until the next breakpoint or program completion.
* **`p <expression>` (print)**: Evaluate and print the value of an expression or variable.
* **`b <line_number>` (breakpoint)**: Set a breakpoint on the specified line number.
* **`q` (quit)**: Exit the debugger immediately.

Let's set a breakpoint inside `find_max_region`:

    (Pdb) b find_max_region
    Breakpoint 1 at /.../exercise-1.py:8
    (Pdb) c

Execution continues until entering `find_max_region`:

    (Pdb) l
      8 B   def find_max_region(numbers, n):
      9         """
     10         Finds the largest mean of sub-sequences of length n in numbers
     11         """
     12         means = []
     13  ->     for i in range(len(numbers)-n):
     14             mean = np.mean(numbers[i:i+n])
     15             means.append((i,mean))

Look closely at line 13:

    for i in range(len(numbers)-n):

If `numbers` has 10 elements and `n` is 5, `range(10 - 5)` is `range(5)`, which only yields indices `0, 1, 2, 3, 4`.
The sub-sequence starting at index `5` (spanning elements `5` through `9`) is never evaluated!

To include the final valid window, the range should be:

    for i in range(len(numbers) - n + 1):

Quit `pdb` by typing `q`. Edit `exercise-1.py` to fix line 13:

```python
    for i in range(len(numbers) - n + 1):
```

Now re-run the tests:

    $ make
    pytest test.py
    ============================== 1 passed in 0.05s ==============================

The test passes!


### Other Debugging & Tracing Tools

When print statements or debuggers are not sufficient—especially when debugging containerized processes or interacting with the OS kernel—system tracing tools provide detailed execution logs.

#### System Call Tracing (`strace`)

The `strace` utility logs every system call made by a process to standard error:

    $ strace python hello.py
    execve("/usr/local/bin/python", ["python", "hello.py"], 0x7ffd179a6d88) = 0
    brk(NULL)                               = 0x57b513b24000
    mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x763891923000
    readlinkat(AT_FDCWD, "/proc/self/exe", "/usr/local/bin/python3.13", 4096) = 25
    ...

#### Python Execution Tracing (`trace`)

Python includes a built-in `trace` module that prints every line of Python code as it is executed:

    $ python -m trace -t hello.py
     --- modulename: hello, funcname: <module>
    hello.py(3):  print("Hello World")
    Hello World

## Resources

- [Apptainer User Guide](https://apptainer.org/docs/user/latest/)
- [Apptainer Definition Files Reference](https://apptainer.org/docs/user/latest/definition_files.html)
- [Running Services with Apptainer Instances](https://apptainer.org/docs/user/latest/running_services.html)
- [Python `pdb` Debugger Documentation](https://docs.python.org/3/library/pdb.html)
- [Reprozip](https://www.reprozip.org/) is a cool tool that will watch a program run (using the strace mechanism) and then save all the files opened and their contents into a zip file. It then has the ability to create a container from the zip file.
- [Redis Documentation](https://redis.io/docs/)
- [RedisInsight User Guide](https://redis.io/docs/latest/operate/redisinsight/)
- [jq - Command Line JSON Processor](https://jqlang.github.io/jq/) is a great command line tool for working with JSON files. And there is a [playground](https://jqplay.org/) for messing around.
- [List of Docker images for the IceCube Neutrino Observatory](https://hub.docker.com/u/icecube)
  and their [instructions](https://docs.icecube.aq/icetray/main/index.html)
  for using the software.
- [misadventures in process containment](https://apenwarr.ca/log/?m=201901)
- [Fibonacci Sequence](https://oeis.org/A000045) on the OEIS.
- A [tutorial on using GNSS reflection data](https://gnssrefl.readthedocs.io/en/latest/pages/docker_cl_instructions.html)
  to measure snow and water height that uses a docker image.

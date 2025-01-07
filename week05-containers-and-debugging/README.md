# CICF Week 5

The goals for week 5 lab are:

1. Make and run a simple Docker image.
1. Run a service packaged in an external Docker image.
1. Use the Python debugger (pdb).

## Tutorial

install docker

    ./install-docker.sh

You will need to then enter your password for sudo. and press 'Y' to agree to installing the packages.
Then we need to add us to the docker group.

    sudo usermod -aG docker $USER

Now choose "Log Out..." from the menu in the upper right corner and then sign back in to get the group membership to be cached.

Log back in and docker should be set up.
We can verify this by running

    docker ps

This lists all the containers that are currently running.
There should be no containers are running, but the important thing is that there are no errors.

### Build an image

Our first task is to make a container image.
The `Dockerfile-hello` contains the instructions on how to build the image.

    cat Dockerfile-hello

We start with the official base python image, we copy in our script, and then we specificy the command to run when the container is started.

    docker build -t hello -f Dockerfile-hello .

This is making an image from that instruction file and we are naming the image `hello`.

    docker images

And then to run the image we use:

    docker run hello

We can see the layers, (i.e. sequence of commands to make the image) with the "history" command:

    docker history hello

The most recent change is at the top and the oldest change is at the bottom.
We can see the all the containers (whether running or not) with the "-a" option on the "ps" command:

    docker ps -a

Okay, lets see if the execution envrionment is really restricted:

    docker run -it hello bash

This has less of everything:

    env
    ping
    python3

Also by default containers have no network access.


### Object Store

We are going to run a service using docker.
This is something called a object store, which we will cover next week with cloud computing.
For now the important thing is that we will run it inside a container.

First, get the container image:

    docker pull minio/minio

See that it has been downloaded:

    docker images

We will now run it.
This looks complicated since we need to pass some configuration on the command line.
By default containers don't have network access, so we first need to tell docker to allow
us to access this container on the ports 9000 and 9001.
We then need to configure where we want the service to store data.
And we need to configure a root user and password.

    mkdir -p data

    docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -e "MINIO_ROOT_USER=cicf" -e "MINIO_ROOT_PASSWORD=cicf1234" minio/minio server /data --console-address ":9001"

The container should have started and be running in the background.
Docker printed the id for this container.
We will let `{id}` refer to the first few letters/digits of this id.

    docker ps
    docker logs {id}

Okay, lets set it up. In the webbrowser visit `http://localhost:9001`
Sign in with our user and password `cicf` and `cicf1234`
Create a new bucket named "cicf-data".

Create a new access key named "test-account".
Download the secret info and move it into our current directory:


    mv ~/Downloads/credentials.json .

This is in JSON format.

    cat credentials.json

Aside: there is a great tool for working with JSON files.

    sudo apt install jq
    jq . credentials.json

Give the new key enough access privileges.
Copy the `minio-policy` policy file:

    cat minio-policy

Edit the key we just made by pasting in the file contents.
And then save it.

Now upload some files.
We want hello.py.

Install the Python Minio library

    sudo apt install python3-pip
    pip3 install minio

Copy the credentials into the store.py file.
Run `store.py`.
Refresh the bucket, nothing should have happened.
Now upload the `fib-first` file to the bucket and rerun `store.py`.
Refresh the bucket, there should be a new object named `result-first`
It should contain the 16th Fibonacci number, which is 987.

The name is not quite right.
Lets put a breakpoint into the file
Before line 25 insert the line `breakpoint()`.

When we run the script, it will stop in the debugger.
We can see variables with `p` prefix.
There are three ways to advance execution: stepping, next, or continue.
Step will take the smallest possible increase, in that it will go into functions and stop.
Next will stop at the next line of the program.
Continue will keep running until another breakpoint or until the program ends.



## Resources

- [Python pdb debugger](https://docs.python.org/3/library/pdb.html)
- [Reprozip](https://www.reprozip.org/) is a cool tool that will watch a program run (using the strace mechanism) and then save all the files opened and their contents into a zip file. It then has the ability to create a container from the zip file.
- [Apptainer](https://apptainer.org/) ([docs](https://apptainer.org/docs/user/latest/)) is a container system, like Docker, that is more common in High Performance Computing envrionments.
- [List of Docker images for the IceCube Neutrino Observatory](https://hub.docker.com/u/icecube) and their [instructions](https://docs.icecube.aq/icetray/main/index.html) for using the software.
- [Minio docs](https://min.io/docs/minio/container/index.html) (The object store we used in the tutorial).
- [jq](https://jqlang.github.io/jq/) is a great command line tool for working with JSON files. And there is a [playground](https://jqplay.org/) for messing around.
- [misadventures in process containment](https://apenwarr.ca/log/?m=201901)
- [Fibonacci Sequence](https://oeis.org/A000045) on the OEIS.
- Minio Python client [reference documentation](https://min.io/docs/minio/linux/developers/python/API.html#put_object)

- A [tutorial on using GNSS reflection data](https://gnssrefl.readthedocs.io/en/latest/pages/docker_cl_instructions.html) to measure snow and water height that uses a docker image.

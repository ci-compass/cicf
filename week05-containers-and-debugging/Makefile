
all: test

test:
	pytest test.py

build-hello:
	apptainer build hello.sif hello.def

start-redis:
	apptainer instance start docker://redis:latest redis-server

stop-redis:
	apptainer instance stop redis-server

start-redisinsight:
	apptainer instance start docker://redis/redisinsight:latest redisinsight

stop-redisinsight:
	apptainer instance stop redisinsight

stop-all:
	apptainer instance stop --all

list-instances:
	apptainer instance list

clean:
	rm -f hello*.sif

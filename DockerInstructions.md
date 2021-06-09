
# December 23rd 2020
## Running in Docker Container

This installation was shown as the best in order to not run into version issues which makes complete sense.
However some people might not be familiar with how docker works therefore will have some instructions here.
So a docker image is essentially the application that you want to run, in this case "gfootball".
Any containers would be instances of the image.

One thing to note is that the instructions did not have instructions on how to start the CPU version.
Below is the command for that:

```console
docker run -e DISPLAY=$DISPLAY -it -v /tmp/.X11-unix:/tmp/.X11-unix:rw gfootball bash
```
Once I was in the container I still had to run the setup.py 

```console
python3 setup.py install
```

## Managing Containers
In order to quit the container simply run the exit command
Type in the following command to see the container ID

```console
sudo docker ps -a
```
The above command lists all containers in the given format

| CONTAINER ID | IMAGE     | COMMAND     | CREATED        | STATUS                       | PORTS | NAMES         |
|--------------|-----------|-------------|----------------|------------------------------|-------|---------------|
| [GIVEN ID]   | gfootball | "/bin/bash" | [time created] | how long it has been running |       | [random name] |


You can also see your container ID while you are in the container itself
```console
root@container_id
```

If you want to stop the container
```console
sudo docker stop [conainter_id]
```

**starting existing container**
This step is important that many people might get stuck on and might have to create many containers over and over again.
The *docker run* command creates new containers so once you did the initial container you should not run it again.
Instead use the command below and make sure to put the *-i* flag for interactive mode.
This will save you a lot of hassle and time.
Make sure to go into the same container as a new container will be completely blank and any files created will not be tracked.
```console
sudo docker start [conainter_id] -i
```

## File Management

**Copy Files from host to container**
```console
docker cp /host/destination/folder [container_id]:/path/to/file 
```
td
**Copy Files from container to host**
```console
docker cp  [container_id]:/path/to/file /host/destination/folder
```

Running the command to start the game as instructed
```console
python3 -m gfootball.play_game --action_set=full
```

Gave me the following error:
```console
pygame.error: No available video device
```
Therefore it is more of a rendering issue than anything.
Note: Have not found the solution to this problem yet as of December 23rd (morning).

* Resolved the rendering issue above by using the GPU version of the docker image (June 7th)


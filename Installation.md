
# Docker on WSL2 with GPU support
Windows Subsystems for Linux (WSL) aleviated many problems for users Windows users. WSL2 works seamlessly with Windows 11 and I took advantage of that to restart this project after a long haitus. The advantage is that my windows machine also has an NVIDIA graphics card, albeit not a very hefty one, an MX150, but it is still useful. The WSL2 distributing I am running for this project is Ubuntu 20.04.

Furthermore, the framework I chose to use is none other than Docker for fast deployment (if you are familiar with Docker). The official Instructions on how to get started with Google Research Football with docker is hyperlinked here: [Google Research Football Docker Image](https://github.com/google-research/football/blob/master/gfootball/doc/docker.md). There are a couple changes that I made in order to get my image to run smoothly. The main change I made in my setup was the base image used to have an docker image that can be run with a GPU and the correct tensorflow version, also added command to run the image as a container and being able to render it via X11.

## Requirements
Couple of great videos and resources that can help in getting your computer set-up.

[Install WSL2 on Windows 11 with NVIDIA CUDA 11.8](https://www.youtube.com/watch?v=1HzYU2_t3yc)

[Install WSL2 on Windows 11 with NVIDIA GPU and Docker Support](https://www.youtube.com/watch?v=CO43b6XWHNI&t=10s)

## Build

Used a base image from [NVIDIA NGC](https://catalog.ngc.nvidia.com/containers), main reason is because their images come configured to run on host systems with NVIDIA Drivers. So long as you are able to find the right base image that has the same driver version as your host, the next thing is to make sure it meets the software package requirements, in this case Tensorflow version 1.15. 

My recommendation is that if you are running your own tests as I am doing here is that the original google football repository gets cloded in a root directory next to your own. You don't have to include the original repo inside your own as it is quite big and most of the files are unecessary. For example:

```console
/root_directory$ tree
.
├── football
└── your_experimentation_repo

### proceed to build with the original docker image

git clone https://github.com/google-research/football.git

cd football

docker build --build-arg DOCKER_BASE=nvcr.io/nvidia/tensorflow:20.02-tf1-py3 . -t gfootball
```

## Docker run
The other difference between the official setup and mine is that more recently, the easiest way to run GUI apps through Docker and or WSL is using X11 Forwarding on Windows or Linux.

* [How to Use X11 Forwarding on Windows or Linux](https://www.youtube.com/watch?v=FlHVuA_98SA)

* [Xming Download](https://sourceforge.net/projects/xming/)

* [Using the Xming X server to display graphical programs](https://docs.vscentrum.be/access/using_the_xming_x_server_to_display_graphical_programs.html)


As mentioned above the best thing to do is separate the original repository and your github experiment repo. While in the root directory that has both of them as subdirectory, the best thing to do is bing mount your experimental repository to the runninng container.

```console
export DISPLAY=:0

docker run --gpus all -e DISPLAY=$DISPLAY -it -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v ./your_experimentation_repo:/workspace gfootball_gpu bash
```

## Running the command to start the game as instructed
Once you are inside the container, launching the environment should be very simple.

```console
python3 -m gfootball.play_game --action_set=full
```

# Docker Tips/Instructions
Although this repository is not a course on Docker, I thought it would be useful to have a few hints and tips that would help get up and started and use Docker well enough since some people might not be familiar with Docker.
So a docker image is essentially the application that you want to run, in this case "gfootball". Any containers would be instances of the image.

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

**Copy Files from container to host**
```console
docker cp  [container_id]:/path/to/file /host/destination/folder
```
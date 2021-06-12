
# December 15th 2020
Had to install Google Football on my linux (ubuntu 20.04) machine as the windows installation was giving me some issues
Even with linux installation I ran into an error "No SETUP file exists" after following the step-by-step instructions in the main
repository.

Overcame the problem by installing PyGame standalone before running the pip3 install gfootball.

# December 18th 2020
Running the command to start the game as instructed

```console
python3 -m gfootball.play_game --action_set=full
```
Indeed worked well but I had fears of version issues. I googled the previously indicated 'No SETUP file exists' and it had to do with pygame not working well with python3 versions other than 3.6. Therefore deleted my initial installation and went with the docker installation in a virtual environment instead and everything is working fine.

**Instructions on how to install with docker linked here:** [Google Research Football Docker Image](https://github.com/google-research/football/blob/master/gfootball/doc/docker.md).


# June 7th 2021
Wanted to work on this again, I think the fast that it was during the holiday season and had a lot going on distracted me from the project.
Also installed Ubuntu 20.04 on an SSD from which I could boot from on my regular computer which happens to have a gpu.
Therefore re-installed the docker with the following command.
My default installation will have a tensorflow base and called **gfootball** while the non-gpu version will be called **gfootball_nogpu**.

### GPU Installation

```console
docker build --build-arg DOCKER_BASE=tensorflow/tensorflow:1.15.2-gpu-py3 . -t gfootball
```

### Non GPU installation

```console
docker build --build-arg DOCKER_BASE=ubuntu:20.04 . -t gfootball_nogpu
```

Using the gpu version gave me the following warning

```console
WARNING: You are running this container as root, which can cause new files in
mounted volumes to be created as the root user on your host machine.

To avoid this, run the container by specifying your user's userid:

$ docker run -u $(id -u):$(id -g) args

```

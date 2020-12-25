# Google-Research-Football-Environment-Experiment

![<img src="https://images.app.goo.gl/ZRAzajAccMrWeZsb7">]('r https://images.app.goo.gl/ZRAzajAccMrWeZsb7')

#![]('r https://images.app.goo.gl/ZRAzajAccMrWeZsb7')

In this repository, I will be Experimenting with Google Research Football Environment.
Football has been a passion of mine since I can remember, it is fantastic that I can use a passion of mine to continue learning about my field of study.

Having had the chance to actually play the sport at a semi-professional level maybe I can provide some unprecedented insight and help train the models.

Created a function that takes screenshots from that used pyautogui's _.screenshot_
Full Doc at Link: [pyautogui-screenshot function](https://pyautogui.readthedocs.io/en/latest/screenshot.html)

**NOTE** Had not read the published paper linked here: [Google Research Football: A Novel Reinforcement Learning Environment](https://arxiv.org/pdf/1907.11180.pdf). Until December 24th.

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

# December 19th 2020
Now begins the real experiments with the Google Research Football!

Using the following link: [Tutorial Colab Notebook!](https://colab.research.google.com/github/google-research/football/blob/master/gfootball/colabs/gfootball_example_from_prebuild.ipynb) 
Honnestly does not teach much. Not sure it was inteded to teach anything or simply as a quickstart.


# December 20th 2020
Created a directory titled "ColabScripts" where I will be running the above notebook as .py files.
Please refer to the readme file titled "ColabScripts\_log" for specifics.

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

## Docker Instructions
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


# December 24th 2020
After yesterday's 5 different trials with the tutorial to get a reward, none of them actually had a reward.
Please see folder [Colab_summary](https://github.com/GateraGael/Google-Research-Football-Environment-Experiment/blob/main/ColabTutorial/colab_summary.md) file for an overview of my trials.

Started Reading the actual paper in order to get better insight into the environments, actions and other variables to be taken.

Page 4 explains that the football engine rewards the team or agent when a goal is scored (+1) and rewards a (-1) when a goal is scored against.
Therefore only my Trial #2 successfully scored a goal while all the other attemps had the ball taken away.





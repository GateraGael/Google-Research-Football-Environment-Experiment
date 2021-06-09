# Google-Research-Football-Environment-Experiment

![](https://www.androidpolice.com/wp-content/themes/ap2/ap_resize/ap_resize.php?src=https%3A%2F%2Fwww.androidpolice.com%2Fwp-content%2Fuploads%2F2018%2F05%2Fgoogle-ai-hero.png&w=728)



# Table of contents
1. [Introduction](#introduction)

<!--
see how to make table of contents in markdown: https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents


2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)
-->
## Introduction <a name="introduction"></a>

In this repository, I will be Experimenting with Google Research Football Environment.
Football has been a passion of mine since I can remember, it is fantastic that I can use a passion of mine to continue learning about my field of study.

Having had the chance to actually play the sport at a semi-professional level maybe I can provide some unprecedented insight and help train the models.

Created a function that takes screenshots from that used pyautogui's _.screenshot_
Full Doc at Link: [pyautogui-screenshot function](https://pyautogui.readthedocs.io/en/latest/screenshot.html)

Published paper linked here: [Google Research Football: A Novel Reinforcement Learning Environment](https://arxiv.org/pdf/1907.11180.pdf).


<!--
## Some paragraph <a name="paragraph1"></a>
The first paragraph text

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text

-->

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

# December 19th 2020
Now begins the real experiments with the Google Research Football!

Using the following link: [Tutorial Colab Notebook!](https://colab.research.google.com/github/google-research/football/blob/master/gfootball/colabs/gfootball_example_from_prebuild.ipynb) 
Honnestly does not teach much. Not sure it was inteded to teach anything or simply as a quickstart.


# December 20th 2020
Created a directory titled "ColabScripts" where I will be running the above notebook as .py files.
Please refer to the readme file titled "Ccolab_summary.md" hyperlinked: [Colab_summary](https://github.com/GateraGael/Google-Research-Football-Environment-Experiment/blob/main/ColabTutorial/colab_summary.md) for specifics.


# December 24th 2020
After Decmber 23rd different trials with the tutorial to get a reward, none of them actually had a reward.
Please see folder [Colab_summary](https://github.com/GateraGael/Google-Research-Football-Environment-Experiment/blob/main/ColabTutorial/colab_summary.md) file for an overview of my trials.

Started Reading the actual paper in order to get better insight into the environments, actions and other variables to be taken.

Page 4 of the resarch paper explains that the football engine rewards the team or agent when a goal is scored (+1) and rewards a (-1) when a goal is scored against. Therefore only my Trial #2 successfully scored a goal while all the other attemps had the ball taken away.
At Trial #10 I was able to make our agent Alan Turing dribble directly into the goal.
Unfortunately no A.I. yet, simply needed to do this to get an understanding of the football engine.

![](ColabTutorial/trial10_logs/screenshots/00m40s.png)

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




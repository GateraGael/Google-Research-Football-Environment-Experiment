# Google-Research-Football-Environment-Experiment

![](https://www.androidpolice.com/wp-content/themes/ap2/ap_resize/ap_resize.php?src=https%3A%2F%2Fwww.androidpolice.com%2Fwp-content%2Fuploads%2F2018%2F05%2Fgoogle-ai-hero.png&w=728)


# Table of contents
1. [Introduction](#introduction)
    1. [Installation](#Installation)
    2. [Test with Colab Notebook](#ColabNotebook)
<!--
see how to make table of contents in markdown: https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents


2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)
-->
## Introduction <a name="introduction"></a>

In this repository, I will be experimenting with Google Research Football Environment. Football (soccer) has been a passion of mine since I can remember. It is fantastic that I can use a passion of mine to continue learning about my field of study.

Published paper linked here: [Google Research Football: A Novel Reinforcement Learning Environment](https://arxiv.org/pdf/1907.11180.pdf).


### Installation <a name="Installation"></a>
After struggling with the different installation instructions. The docker image with gpu support and tensorflow base was by far the best and that actually rendered the game.


**Instructions on how to install with docker linked here:** [Google Research Football Docker Image](https://github.com/google-research/football/blob/master/gfootball/doc/docker.md).


[My Own Installations hyperlinked here](./Installation.md)

### Test with Colab Notebook<a name="ColabNotebook"></a>

Using the following link: [Tutorial Colab Notebook!](https://colab.research.google.com/github/google-research/football/blob/master/gfootball/colabs/gfootball_example_from_prebuild.ipynb) 
Honnestly does not teach much. Not sure it was inteded to teach anything or simply as a quickstart. Created a directory titled "ColabTutorial" where I will be running the above notebook as .py files. 

Please see following markdown [summary](https://github.com/GateraGael/Google-Research-Football-Environment-Experiment/blob/main/ActionSpaceExplore/summary.md) file for an overview of my trials.

<!--
## Some paragraph <a name="paragraph1"></a>
The first paragraph text

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text
-->

# First Steps

Ran different trials with the getting started tutorial notebook to get a reward, some of them had a reward, while some other did not. Therefore wanted to get a more thorough understanding of what was going on in the background.

Also have been refering to the the actual paper in order to get better insight into the environments, variables and actions the agents take. Page 4 of the resarch paper explains that the football engine rewards the team or agent when a goal is scored (+1) and rewards a (-1) when a goal is scored against.


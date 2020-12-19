# Google-Research-Football-Environment-Experiment
In this repository, I will be Experimenting with Google Research Football Environment.
Football has been a passion of mine since I can remember, it is fantastic that I can use a passion of mine to continue learning about my field of study.

Having had the chance to actually play the sport at a semi-professional level maybe I can provide some unprecedented insight and help train the models.

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






# December 20th
Experimenting with quick start colab notebook.
Format is .py files instead of .ipynb files

## Original.py
The first file that I used is called **original.py**
This file is the first and only cell in the sample notebook after the installation cell ran without any changes at all.

Full Script Below:

```python
import gfootball.env as football_env
env = football_env.create_environment(env_name="academy_empty_goal_close", stacked=False, logdir='/tmp/football', write_goal_dumps=False, write_full_episode_dumps=False, render=False)
env.reset()
steps = 0
while True:
  obs, rew, done, info = env.step(env.action_space.sample())
  steps += 1
  if steps % 100 == 0:
    print("Step %d Reward: %f" % (steps, rew))
  if done:
    break

print("Steps: %d Reward: %.2f" % (steps, rew))
```


# December 20th 

```console
python3 original.py
```

## Trial #1
```output_stdout
Steps: 85 Reward: 0.00
```

# December 23rd
No Changes made to **original.py**

## Trial #2

#### Output
```output_stdout
Steps: 25 Reward: 1.00
```

So far no conlusions can be made since the second trial had different output than the first without any changes made.
It only seems that the reward given to the agent is a fuction of the steps taken - less steps actually gives a reward while more given less.

## Trial #3
Changed to log directory to the current directory to make it faster to find
Added the following (before the env variable declaration):

```python
import os

log_dir_tutorial = 'tutorial_logs' + '/'

if not os.path.exists(log_dir_tutorial):
     os.makedirs(log_dir_tutorial)
# Replaced the logdir='/tmp/football' with logdir=log_dir_tutorial
```

#### Output
```output_stdout
Step 100 Reward: 0.0000
Steps: 139 Reward: 0.00
```
Notice how after there is a print after the 100th step.
Also the conclusion made earlier that the more steps taken the reward is less.

## Trial #4
Changed to print every 5 steps (first if statement in the while loop)


```python
while True:
  obs, rew, done, info = env.step(env.action_space.sample())
  steps += 1
  if steps % 5 == 0:
    print("Step %d Reward: %f" % (steps, rew))
```

#### Output
```output_stdout


```



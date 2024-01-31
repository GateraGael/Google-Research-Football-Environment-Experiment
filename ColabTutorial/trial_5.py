import gfootball.env as football_env
import os
import matplotlib.pyplot as plt

sys.path.append("../utils/")
from graphing_utils import GraphingUtils

log_dir_tutorial = os.path.join('./logs', 'trial5')

if not os.path.exists(log_dir_tutorial):
    os.makedirs(log_dir_tutorial)


env = football_env.create_environment(env_name="academy_empty_goal_close", stacked=False, logdir=log_dir_tutorial,
                                     write_goal_dumps=False, write_full_episode_dumps=False, render=True)

env.reset()

all_steps = []
all_rewards = []

steps = 0 
while True:
    obs, rew, done, info = env.step(env.action_space.sample())
    steps += 1
    if steps % 1 == 0:
        all_steps.append(int(steps))
        all_rewards.append(float(rew))
        print("Step %d Reward: %f" %(steps, rew))
    if done:
        break


graph_util = GraphingUtils()
graph_util.plot_and_save_rewards(all_steps, all_rewards, log_dir_tutorial)
import gfootball.env as football_env
import os, sys
import matplotlib.pyplot as plt

sys.path.append("../utils/")
from graphing_utils import GraphingUtils

log_dir_tutorial = os.path.join('./logs', 'trial6')

if not os.path.exists(log_dir_tutorial):
    os.makedirs(log_dir_tutorial)

env = football_env.create_environment(env_name="academy_empty_goal_close", stacked=False, logdir=log_dir_tutorial,
                                     write_goal_dumps=False, write_full_episode_dumps=False, render=True)

env.reset()

all_steps = []
all_rewards = []
info_list = []
observation_list = []

steps = 0 
while True:
    obs, rew, done, info = env.step(env.action_space.sample())

    steps += 1
    if steps % 1 == 0:
        all_steps.append(int(steps))
        all_rewards.append(float(rew))
        info_list.append(info)
        observation_list.append(obs)
        print("Step %d Reward: %f" %(steps, rew))
        #print("Step: %d Reward: %f Observation: %s Done: %s Info: %s" %(steps, rew, obs, done, info))
    if done:
        break

print(f"Observation Object Type {type(observation_list[0])}")
print(f"Observation Shape {observation_list[0].shape}")

print(f"Info Object Type {type(info_list[0])}")
print(f"Info Object Type {info_list[0].keys()}")
print(f"Info 'score_reward' value {info_list[0]['score_reward']}")

print(f"Reward {all_rewards[0]}")

graph_util = GraphingUtils()
graph_util.plot_and_save_rewards(all_steps, all_rewards, log_dir_tutorial)
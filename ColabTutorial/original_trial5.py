import gfootball.env as football_env
import os


log_dir_tutorial = 'tutorial_logs' + '/'
number_of_screenshots = 1

if not os.path.exists(log_dir_tutorial):
    os.makedirs(log_dir_tutorial)

screenshots_dir = log_dir_tutorial + '/screenshots/'

if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

env = football_env.create_environment(env_name="academy_empty_goal_close", stacked=False, logdir=log_dir_tutorial,
                                     write_goal_dumps=False, write_full_episode_dumps=False, render=True)

env.reset()

StepsVreward_log = []

steps = 0 
while True:
    obs, rew, done, info = env.step(env.action_space.sample())
    steps += 1
    if steps % 10 == 0:
        StepsVreward_log.append(f"{steps}, {rew} \n")
        print("Step %d Reward: %f" %(steps, rew))
    if done:
        break

print("Steps: %d Reward: %.2f" % (steps, rew))
StepsVreward_log.append(f"{steps}, {rew} \n")

with open(log_dir_tutorial + "TrainStepsvsReward.csv", "w") as log_file:
    log_file.writelines(StepsVreward_log)
    

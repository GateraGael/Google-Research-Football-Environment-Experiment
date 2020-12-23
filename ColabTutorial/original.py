import gfootball.env as football_env

env = football_env.create_environment(env_name="academy_empty_goal_close", stacked=False, logdir='/tmp/football',
                                     write_goal_dumps=False, write_full_episode_dumps=False, render=False)

env.reset()
steps = 0
while True:
    obs, rew, done, info = env.step(env.action_space.sample())
    steps += 1
    if steps % 100 == 0:
        print("Step %d Reward: %f" %(steps, rew))
    if done:
        break

print("Steps: %d Reward: %.2f" % (steps, rew))


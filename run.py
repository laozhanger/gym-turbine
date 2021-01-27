import numpy as np
import matplotlib.pyplot as plt
import gym
import gym_turbine
import os
from time import time
import argparse

import utils
from stable_baselines3 import PPO

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--agent',
        help='Path to agent .pkl file.',
    )
    args = parser.parse_args()

    agent_path = args.agent
    env = gym.make("TurbineStab-v0")
    agent = PPO.load(agent_path)
    sim_df = utils.simulate_environment(env, agent)

    agent_path_list = agent_path.split("\\")
    simdata_dir = os.path.join("logs", "sim_data", agent_path_list[-2])
    os.makedirs(simdata_dir, exist_ok=True)

    # Save file to logs\sim_data\<EXPERIMENT_ID>ppo\<agent_file_name>_simdata.csv
    sim_df.to_csv(os.path.join(simdata_dir, agent_path_list[-1][0:-4] + "_simdata.csv"))
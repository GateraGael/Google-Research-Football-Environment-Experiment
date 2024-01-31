import matplotlib.pyplot as plt
import os



class GraphingUtils:
    def __init__(self):
        # You can add initialization parameters if needed
        pass

    def plot_and_save_rewards(self, steps_list, rewards_list, save_dir, file_name="reward_plot.png"):
        """
        Plots the rewards over steps and saves the plot to a specified directory.

        Args:
        steps_list, rewards_list (lists): A list of log entries where each entry is a string "step, reward".
        save_dir (str): Directory path where the plot will be saved.
        file_name (str): Name of the file to save the plot. Defaults to 'reward_plot.png'.

        Returns:
        str: The path to the saved plot.
        """


        # Now, plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(steps_list, rewards_list, marker='o')  # 'o' adds a circle marker at each data point
        plt.title("Reward vs Steps")
        plt.xlabel("Steps")
        plt.ylabel("Reward")
        plt.grid(True)

        # Save the plot
        file_path = os.path.join(save_dir, file_name)
        plt.savefig(file_path, format='png')

        # Optionally, close the plot if you're not displaying it
        plt.close()

        return file_path
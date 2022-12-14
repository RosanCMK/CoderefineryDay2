import pandas as pd
from matplotlib import pyplot as plt


def compute_statistics(data):
    # compute statistics
    mean = sum(data) / len(data)
    return mean

def plot_data(data, mean, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.plot(data, "r-")
    ax.axhline(y=mean, color="b", linestyle="--")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return (fig, ax)

def create_name(num):
    name = f"plot_{str(num)}.png"
    return name

def save_plot(fig, num):
    name = create_name(num)
    fig.savefig(name)
    fig.clf

def read_data(num_measurements, filename="temperatures.csv", colname="Air temperature (degC)"):
    # read data from file
    data = pd.read_csv("temperatures.csv", nrows=num_measurements)
    data_read = data[colname]
    return data_read


for num_measurements in [25, 100, 500]:
    temperatures = read_data(num_measurements=num_measurements)
    mean = compute_statistics(temperatures)
    file_name = create_name(num_measurements)
    fig, ax = plot_data(data = temperatures,
                        mean = mean,
                        xlabel = "Measurements",
                        ylabel = "Air temperature (C)")
    save_plot(fig, num_measurements)
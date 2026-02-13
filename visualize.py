def plot_data(data):
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.title('Data Visualization')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()


def visualize_distribution(data):
    import seaborn as sns
    sns.histplot(data, kde=True)
    plt.title('Data Distribution')
    plt.show()


def compare_series(data1, data2):
    import matplotlib.pyplot as plt
    plt.plot(data1, label='Series 1')
    plt.plot(data2, label='Series 2')
    plt.title('Comparison of Two Data Series')
    plt.legend()
    plt.show()
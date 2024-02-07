import matplotlib.pyplot as plt

def test_plot():
    plt.ion()
    plt.figure()
    plt.plot([1, 2, 3, 4])
    plt.ylabel('Simple Plot Test')
    plt.show()

test_plot()
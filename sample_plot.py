import matplotlib.pyplot as plt

if __name__ == "__main__":

    # 2d
    # x = [1, 2, 3]
    # y = [4, 5, 6]
    # plt.scatter(x,y)
    # plt.xlabel("X axis")
    # plt.show()

    # 3d
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')

    x = [1, 2, 3, 4]
    y = [4, 5, 1, 7]
    z = [7,3,9, 1]
    ax.scatter(x,y,z)
    ax.set_xlabel("X axis")
    plt.show()
from FileCtrl import *
import os


training_data = [
    [[1, 0], [1]],
    [[0, 1], [1]],
    [[1, 1], [0]],
    [[0, 0], [0]]
]

if os.path.exists("Data.txt"):
    nn = read_nn(2,10,1)
else:
    nn = NeuralNetwork(2,10,1)


while True:
    if input("Train this network?(y/n)").lower() == "y":
        for _ in range(10000):
            randInt = random.randrange(0,4)
            nn.train(training_data[randInt][0], training_data[randInt][1])

    print(nn.feedforward([1,0]))
    print(nn.feedforward([0,1]))
    print(nn.feedforward([1,1]))
    print(nn.feedforward([0,0]))

    if input("Go again?(y/n)").lower() != "y":
        break

save_nn(nn)

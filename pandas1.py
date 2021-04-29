import pandas as pd
df = pd.read_csv("MNIST_100.csv")
label = df["label"]
data = df.drop(["label"])
print(data)

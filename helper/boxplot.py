import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    "Experiment": [0] * 10 + [1] * 10 + [2] * 10 + [3] * 10 + [4] * 10,
    "Run": [i for i in range(10)] * 5,
    "Time (sec)": [
        351.102,
        8609.863,
        4185.378,
        8214.24,
        1358.385,
        1379.836,
        1391.663,
        4187.049,
        1409.269,
        7036.99,
        1415.45,
        1410.28,
        1392.249,
        1404.984,
        1400.441,
        1381.018,
        1389.009,
        1370.024,
        1395.832,
        1371.188,
        1410.22,
        1414.867,
        1393.646,
        1357.545,
        1319.111,
        1310.743,
        3891.76,
        1290.74,
        1337.436,
        1287.826,
        1296.519,
        1296.767,
        1280.781,
        1302.062,
        1304.716,
        1284.213,
        1295.508,
        1284.052,
        1297.572,
        1291.892,
        1369.78,
        1327.015,
        1416.237,
        1409.437,
        6060.46,
        1409.1,
        1418.68,
        1420.1,
        410.43,
        1500,
    ],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Generate boxplot
plt.figure(figsize=(10, 6))
boxplot = df.boxplot(column="Time (sec)", by="Experiment")
plt.title("Boxplot of Time (sec) by Experiment")
plt.xlabel("Experiment")
plt.ylabel("Time (sec)")

# Save the plot as a PNG image
plt.savefig("boxplot.png")

plt.show()

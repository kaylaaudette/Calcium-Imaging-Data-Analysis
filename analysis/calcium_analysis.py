import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("../data/sample_calcium_data.csv")

time = data["time"]
neurons = data.drop(columns=["time"])

# ΔF/F normalization
def delta_f_over_f(signal):
    baseline = np.percentile(signal, 10)
    return (signal - baseline) / baseline

normalized = neurons.apply(delta_f_over_f)

# Plot
plt.figure()

for col in normalized.columns:
    plt.plot(time, normalized[col], label=col)

plt.xlabel("Time")
plt.ylabel("ΔF/F")
plt.title("Calcium Imaging Activity")
plt.legend()

plt.savefig("../figures/calcium_activity.png")
plt.show()

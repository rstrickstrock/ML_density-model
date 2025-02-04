import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Example DataFrame
data = pd.DataFrame({
    "type": ["a", "a", "b", "b", "c", "c", "c"],
    "time": [1.2, 2.4, 3.5, 2.2, 1.8, 2.9, 3.1],
    "category": ["x", "y", "x", "z", "y", "z", "x"]
})

# Define a color map for the 'category'
color_map = {"x": "red", "y": "blue", "z": "green"}

# Define offsets for subcategories
offset_map = {"x": -0.2, "y": 0, "z": 0.2}  # x, y, and z offsets from the main x-axis category

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Unique x-axis categories
x_categories = data["type"].unique()
x_positions_base = {cat: i for i, cat in enumerate(x_categories)}

# Plot each point with an offset
for cat in data["category"].unique():
    subset = data[data["category"] == cat]
    x_positions = [x_positions_base[t] + offset_map[cat] for t in subset["type"]]
    ax.scatter(x_positions, subset["time"], label=cat, color=color_map[cat])

# Customize the x-axis to show the categories
ax.set_xticks(range(len(x_categories)))
ax.set_xticklabels(x_categories, fontsize=10)

# Add labels, title, and legend
ax.set_xlabel("Type (Categories)", fontsize=12)
ax.set_ylabel("Required Time", fontsize=12)
ax.set_title("Category-wise Time Distribution with Subcategory Offsets", fontsize=14)
ax.legend(title="Category", title_fontsize=10)
ax.grid(axis="y", linestyle="--", alpha=0.7)

# Adjust layout and show plot
plt.tight_layout()
plt.show()

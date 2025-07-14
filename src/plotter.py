import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_weather(df, city):
    sns.set(style="whitegrid")
    melted = df.melt(id_vars=["City"], var_name="Metric", value_name="Value")
    
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(data=melted, x="Metric", y="Value", palette="viridis")
    plt.title(f"Current Weather in {city}")
    plt.xticks(rotation=20)
    plt.tight_layout()

    os.makedirs("visuals", exist_ok=True)
    filename = f"visuals/plot_{city.lower().replace(' ', '_')}.png"
    plt.savefig(filename)
    print(f"Plot saved to {filename}")
    plt.show()

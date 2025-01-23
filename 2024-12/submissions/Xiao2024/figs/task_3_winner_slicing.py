import matplotlib.pyplot as plt
import numpy as np

categories = [
    ["Finance", "Sports", "Music", "Movie", "Open"],
    ["Real-time", "Fast-changing", "Slow-changing", "Static"],
    ["Web", "Head", "Torso", "Tail"],
    [
        "Simple",
        "Simple w. Condition",
        "Set",
        "Comparison",
        "Aggregation",
        "Multi-hop",
        "Post-processing",
        "False Premise",
    ],
]

systems = ['Top-1: db3', 'Top-2: APEX', 'Top-3: vsluy-team']
panels = ["(a) Domain", "(b) Dynamism", "(c) Popularity", "(d) Question type"]
scores = [[[17.7, 5.8, 1.8], [27.8, 23.6, 18.7], [31.5, 29.0, 36.3], [41.0, 24.6, 11.9], [31.1, 30.8, 31.2]], [[17.7, 0.0, 0.0], [12.8, 8.0, 0.0], [16.8, 17.4, 9.2], [43.1, 31.7, 29.8]], [[31.7, 29.9, 28.0], [31.2, 16.6, 9.4], [29.9, 14.7, 7.5], [24.9, 8.6, 3.4]], [[41.4, 18.4, 7.1], [19.0, 18.8, 24.3], [20.8, 20.0, 28.8], [21.9, 15.4, 15.8], [15.5, 20.6, 15.4], [16.2, 10.6, 20.8], [0.0, 6.9, 16.7], [67.4, 55.6, 27.4]]]
scores = [[[round(num) for num in inner_list] for inner_list in outer_list] for outer_list in scores]

fig, axs = plt.subplots(2, 2, figsize=(20, 10))
bar_width = 0.18
colors = ["#F0AB00", "#F9E0A2", "#4CB140", "#BDE2B9"]

for i, ax in enumerate(axs.flat):
    for j, system in enumerate(systems):
        results = [scores[i][k][j] for k in range(len(categories[i]))]
        r = np.arange(len(categories[i]))
        bars = ax.bar(
            r + j * bar_width,
            results,
            width=bar_width,
            color=colors[j],
            edgecolor="grey",
            label=system,
        )

        # Add the numeric values on top of the bars
        #'''
        for bar in bars:
            yval = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                yval,
                round(yval, 2),
                ha="center",
                va="bottom",
                fontsize=10 if len(categories[i]) > 5 else 14,
            )
        #'''

    ax.set_ylabel('Truthfulness')
    ax.set_title(panels[i], fontsize=20)

    ax.tick_params(axis="y", which="major", labelsize=14)

    ax.set_xticks(r + bar_width * 1)

    ax.set_xticklabels(
        categories[i], rotation=20 if len(categories[i]) > 5 else 0, fontsize=14
    )

    ax.axhline(y=0, linewidth=1, color="k")


# Adjust the space between the panels
# plt.subplots_adjust(wspace=0.1, hspace=0.2)

# Global legend
handles, labels = axs[0][0].get_legend_handles_labels()
fig.legend(
    handles,
    labels,
    loc="lower left",
    ncol=len(systems) // 2,
    fontsize=16,
    bbox_to_anchor=(0, -0.05),
)

# Save the figure and show
plt.tight_layout()
plt.savefig("/Users/xiaoyangfb/Downloads/task_3_winner_slicing.pdf", bbox_inches="tight")
# plt.show()
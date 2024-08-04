import seaborn as sns
import matplotlib.pyplot as plt

def cm_heatmap(cm, color_map):
    
    # heatmap
    sns.heatmap(
        cm,
        cmap = color_map,
        annot = True,
        fmt = 'd'
    )
    
    # axes labels
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    # x axis on top
    plt.gca().xaxis.set_label_position('top')
    plt.gca().xaxis.tick_top()

import matplotlib.pyplot as plt


def customize_figure(fig, axis_linewidth=2, label_fontsize=14, tick_fontsize=12):
    """
    Customize a Matplotlib figure to have bold axis lines and large font for labels and ticks.

    Parameters:
    - fig: Matplotlib figure object to customize.
    - axis_linewidth: Line width for the axis lines (default is 2).
    - label_fontsize: Font size for the axis labels (default is 14).
    - tick_fontsize: Font size for the tick labels (default is 12).

    Returns:
    - fig: Customized Matplotlib figure object.
    """
    # Iterate over all the axes in the figure
    for ax in fig.get_axes():
        # Set the linewidth of the axis lines
        ax.spines['top'].set_linewidth(axis_linewidth)
        ax.spines['right'].set_linewidth(axis_linewidth)
        ax.spines['bottom'].set_linewidth(axis_linewidth)
        ax.spines['left'].set_linewidth(axis_linewidth)

        # Set the font size of the axis labels
        ax.xaxis.label.set_size(label_fontsize)
        ax.yaxis.label.set_size(label_fontsize)

        # Set the font size of the tick labels
        ax.tick_params(axis='both', which='major', labelsize=tick_fontsize)

    return fig


# Example usage
if __name__ == "__main__":
    # Create a sample figure
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_title('Sample Plot')

    # Customize the figure
    fig = customize_figure(fig)

    # Show the customized figure
    plt.show()
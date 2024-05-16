# Write plot functions here
from project_package.data import config

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def demo_fig():
    """
    A demo figure
    """
    demofile = config.INTERMEDIATE_DATA_FOLDER / "demo_clean.csv"
    demo_df = pd.read_csv(demofile)
    demo_fig = demo_df.plot(x="Age", y="Salary", kind="scatter")
    figure_file = config.FIGURES_FOLDER / "demo.png"
    demo_fig.get_figure().savefig(figure_file)
    print(f"Saved figure to {figure_file}")


def plot_latest_t2m(data):
    """
    Plots the latest T2M data from an xarray dataset with a custom colormap.

    Parameters:
    data (xr.Dataset): The xarray dataset containing the T2M data variable.

    Returns:
    matplotlib.figure.Figure: The figure object containing the plot.
    """

    latest_t2m = data.T2M

    colors = [(0, "blue"), (1, "red")]  # 0 degrees as blue, 30 degrees as red
    custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    plot = latest_t2m.plot(ax=ax, cmap=custom_cmap, cbar_kwargs={"label": "Air Temperature [°C]", "shrink": 0.8})

    # Customize the plot
    ax.set_title("Latest Temperature at 2 Meters (T2M)", fontsize=18, pad=20)
    ax.set_xlabel("X Coordinate of Projection [m]", fontsize=14)
    ax.set_ylabel("Y Coordinate of Projection [m]", fontsize=14)

    # Set colorbar limits
    plot.set_clim(0, 30)
    plt.close("all")

    return fig

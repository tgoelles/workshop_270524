from project_package.visualization.visualize import demo_fig, plot_latest_t2m
from project_package.data import config
import xarray as xr


if __name__ == "__main__":
    print("redoing all plots")

    # ADD All PLOTTING FUNCTIONS HERE
    graz_intermediate_file = config.INTERMEDIATE_DATA_FOLDER / "graz_latest.nc"
    graz_intermediate = xr.open_dataset(graz_intermediate_file)
    graz_plot = plot_latest_t2m(graz_intermediate)
    graz_plot.savefig(config.FIGURES_FOLDER / "graz_latest_t2m.png")

    print("done")

from project_package.data import config
from pathlib import Path

import pandas as pd
import xarray as xr


# Enter code here for the final generation of processed data
def process_rawdata() -> None:
    """Convert all datasets and saves them in the intermediate folder"""
    # code comes here
    process_graz()
    print("Processed data saved to intermediate folder")
    return None


def process_graz():
    graz_file = config.RAW_DATA_FOLDER / "graz_may_2024_inca_20240501T0000_20240515T2300.nc"
    graz = xr.open_dataset(graz_file)
    graz_latest = graz.isel(time=-1)
    graz_latest.to_netcdf(config.INTERMEDIATE_DATA_FOLDER / "graz_latest.nc")

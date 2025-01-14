from __future__ import annotations

import cv2 as cv
import numpy as np
import xarray as xr

from magnify import utils
import magnify.registry as registry


@registry.component("filter_expression")
def filter_expression(assay: xr.Dataset, search_channel: str | list[str] | None = "egfp"):
    if search_channel == "all":
        search_channels = assay.channel
    else:
        search_channels = utils.to_list(search_channel)

    valid = xr.zeros_like(assay.valid, dtype=bool)
    for channel in search_channels:
        subassay = assay.isel(time=0).sel(channel=channel)
        # Compute the intensity differences between every pair of backgrounds on the first timestep.
        bg = subassay.roi.where(subassay.bg).median(dim=["roi_x", "roi_y"]).compute()
        bg_n = bg.to_numpy().flatten()
        diffs = bg_n[:, np.newaxis] - bg_n[np.newaxis, :]
        offdiag = np.ones_like(diffs, dtype=bool) & (~np.eye(len(diffs), dtype=bool))
        diffs = diffs[offdiag]

        # Include any markers where the fg - bg is above 5 sigma of the mean difference.
        upper_bound = 5 * diffs.std()
        fg = subassay.roi.where(subassay.fg).median(dim=["roi_x", "roi_y"]).compute()
        valid |= fg - bg > upper_bound

    assay["valid"] &= valid
    return assay


@registry.component("filter_nonround")
def filter_nonround(
    assay: xr.Dataset, min_roundness: float = 0.85, search_channel: str | list[str] | None = "egfp"
):
    if search_channel == "all":
        search_channels = assay.channel
    else:
        search_channels = utils.to_list(search_channel)

    for channel in search_channels:
        subassay = assay.isel(time=0).sel(channel=channel)
        fg = utils.to_uint8(subassay.fg.to_numpy())
        areas = subassay.fg.sum(dim=["roi_x", "roi_y"]).compute()
        for i in range(assay.sizes["mark"]):
            contours, _ = cv.findContours(fg[i], cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            perimeter = sum(cv.arcLength(c, True) for c in contours)
            area = sum(cv.contourArea(c) for c in contours)
            if perimeter == 0:
                assay.valid[i] = False
                continue
            roundness = 4 * np.pi * float(areas[i]) / perimeter**2
            assay.valid[i] &= roundness > min_roundness

    return assay


@registry.component("filter_leaky")
def filter_leaky_buttons(assay: xr.Dataset, search_channel: str | list[str] | None = "egfp"):
    if search_channel == "all":
        search_channels = assay.channel
    else:
        search_channels = utils.to_list(search_channel)

    for channel in search_channels:
        subassay = assay.isel(time=0).sel(channel=channel)
        # Compute the intensity differences between every pair of backgrounds on the first timestep.
        bg = subassay.roi.where(subassay.bg).median(dim=["roi_x", "roi_y"]).compute()
        bg_n = bg.to_numpy().flatten()
        diffs = bg_n[:, np.newaxis] - bg_n[np.newaxis, :]
        offdiag = np.ones_like(diffs, dtype=bool) & (~np.eye(len(diffs), dtype=bool))
        diffs = diffs[offdiag]

        # Find markers where the fg - bg is below 5 sigma of the mean difference.
        upper_bound = 5 * diffs.std()
        fg = subassay.roi.where(subassay.fg).median(dim=["roi_x", "roi_y"]).compute()
        empty = fg - bg < upper_bound
        for i in range(assay.sizes["mark"]):
            row = int(assay.mark_row[i])
            if subassay.tag[i] == "":
                continue
            if row > 0 and subassay.tag[i - 1] == "":
                assay.valid[i] &= empty[i - 1]
            if row < assay.mark_row.max() and subassay.tag[i + 1] == "":
                assay.valid[i] &= empty[i + 1]

    return assay

import pypsa
import numpy as np

network = pypsa.Network()
#import pypsa
## Download the file 'wecc_homework6.nc' and upload it to the 'files' folder in Google Colab
import matplotlib.pyplot as plt
network = pypsa.Network('wecc_homework6.nc')
network.optimize()
print(network)

from pypsa.plot import add_legend_patches
import cartopy.crs as ccrs
import random

carriers = network.generators.carrier.unique()
colors = ["#%06x" % random.randint(0, 0xFFFFFF) for _ in carriers]
network.madd("Carrier", carriers, color=colors)


fig = plt.figure()
ax = plt.axes(projection=ccrs.EqualEarth())
capacities = network.generators.groupby(["bus", "carrier"]).p_nom.sum()

network.plot(
    ax=ax,
    bus_sizes=capacities / 2e5,
    margin=0.2
)

add_legend_patches(ax, colors, carriers)
print("Hellow")

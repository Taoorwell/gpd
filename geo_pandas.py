import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

pwd = r'G:/GF/JL/sg/'
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

sg = gpd.read_file(pwd + '100_05_05.shp')


# # No.1
# # world dataframe and world map
# print(world.head())
# world.plot()
# plt.show()

# No.2
# get polygone centroid and centroid plot
# world['centroid'] = world.centroid
# world = world.set_geometry('centroid')
# world = world.drop(columns='geometry')
# print(world.head())
# world.plot()
# plt.show()

# sg['centroid'] = sg.centroid
# sg = sg.set_geometry('centroid')
# sg = sg.drop(columns='geometry')
# sg.plot(color='white', edgecolor='blue')
# plt.show()

# # No.3
# # output file to shapefile
# world.to_file("countries_centroid.shp")
# print("Finish output successfully")

# # No.4
# # read and load shapefile
# centroid = gpd.read_file(pwd + 'countries_centroid.shp')
# print(centroid.head())
# centroid.plot()
# plt.show()

# sg = gpd.read_file(pwd + '100_05_05.shp')
# print(sg.head())
# sg.plot(color='white', edgecolor='blue')
# plt.show()



# # No.5
# # Plot map by field value
# # align plot ax and legend
# fig, ax = plt.subplots(1, 1)
# divider = make_axes_locatable(ax)
# cax = divider.append_axes('right', size='5%', pad=0.1)
#
# world = world[(world.pop_est > 0) & (world.name != 'Antarctica')]
# world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
# world.plot(column='gdp_per_cap', ax=ax, legend=True, cax=cax, cmap='OrRd')
# plt.show()

# # No.4
# # making a map with multiple layers
# fig, ax = plt.subplots()
# ax.set_aspect('equal')
#
# world.plot(ax=ax, color='white', edgecolor='blue')
#
# cities.plot(ax=ax, marker='o', color='red', markersize=5)
#
# plt.show()

fig, ax = plt.subplots()
ax.set_aspect('equal')
sg.plot(ax=ax, color='white', edgecolor='grey')
sg.centroid.plot(ax=ax, marker='*', color='red', markersize=5)
plt.show()

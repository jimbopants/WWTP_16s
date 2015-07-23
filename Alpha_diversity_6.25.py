# IPython log file


# Written by JG
# 6/24/15

import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.dates as mdate
import datetime

# This notebook does 3 things to summarize alpha diversity between different samples
# 0. Import text files with rarefaction data
# x. Calculate average and SD for each sample using the set of 10 rarefaction curves
# x. For the moment, just take 1 rarefaction, not the actual curve, 
#   but eventually I will want to do stuff with rarefactin curves themselves maybe?
# x3. Put all of the data into a single dataframe so I can use groupby to sort and plot 
# 1. Sort samples into different basins by date
# 2. Plot time series of all 6 basins by date
# 3. Calculate ANOVA test of difference of mean for different basins. 
get_ipython().magic(u'matplotlib inline')
# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")

fig,ax=plt.subplots(1)

for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    #print date_sorted
    dates = date_sorted.Date.values
    #print dates
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    print dates
    plt.errorbar(date_sorted["Date"], chao1, yerr=error)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
#    print name
#    print group

# Now sort this based on the information in mapdf. How to sort?


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)



# Trying to figure out what the fuck happened to half of the samples that didn't convert, got it above
#print mean
#print len(mean)
#print type(single_pt_float.iloc[0,0])
#print single_pt.ix[:,3]
#print single_pt.ix[:,3].mean(axis=0)
#mean.to_csv("/Users/jimbo/Desktop/mean")
#single_pt.to_csv("/Users/jimbo/Desktop/singlept.csv")
#print single_pt.ix[:,30:70]
# 
#new_df
# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")

fig,ax=plt.subplots(1)

for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    #print date_sorted
    dates = date_sorted.Date.values
    #print dates
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    print dates
    plt.errorbar(date_sorted["Date"], chao1, yerr=error)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
#    print name
#    print group

# Now sort this based on the information in mapdf. How to sort?


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)



# Trying to figure out what the fuck happened to half of the samples that didn't convert, got it above
#print mean
#print len(mean)
#print type(single_pt_float.iloc[0,0])
#print single_pt.ix[:,3]
#print single_pt.ix[:,3].mean(axis=0)
#mean.to_csv("/Users/jimbo/Desktop/mean")
#single_pt.to_csv("/Users/jimbo/Desktop/singlept.csv")
#print single_pt.ix[:,30:70]
# 
#new_df
# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
get_ipython().magic(u'pinfo savefig')



# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
#?savefig()
get_ipython().magic(u'pinfo pwd')


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
#?savefig()
pwd


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
#?savefig()
get_ipython().magic(u'pinfo pwd')


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
#?savefig()
get_ipython().magic(u'pwd')


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

import matplotlib
matplotlib.matplotlib_fname()
# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.
get_ipython().magic(u'pwd')


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

get_ipython().magic(u'savefig')
get_ipython().magic(u'pinfo savefig')
# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.eps")



# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

ipython profile create
# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.eps")



# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.eps")



# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.pdf")



# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()
plt.show()
savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.pdf", bbox_inches="tight")



# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.pdf", bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':6})

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.pdf", bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])

# Sort dataframe into different groups and plot
grouped  = new_df.groupby("Basin")
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position and show plot
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.pdf", bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "Chao1"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % Metric )
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.pdf", bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "Chao1"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

savefig("./Alpha_diversity_results/latest_alpha_diversity_figure.pdf", bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

datetime.datetime.now().time()
str(datetime.datetime.now().time())
timez =str(datetime.datetime.now().time())
print timez.split(".")[0]
timez =str(datetime.datetime.now().time()).split(".")[0]
print timez
# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "Chao1"
#print mapdf


def func1(metric_df, map_df):
    """ Take a single metric file and a mapping file, 
    return a dataframe with samples as rows and 
    columns: Metric-mean, Metric-SD, Date, Basin, Month, Description""""
    
    return new_df

def ambiguously_named_function(stuff):
    """ Takes a df from previous function, plots the data and saves it to a file with the name + time"""


# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0]
savefig("./Alpha_diversity_results/AD_fig%s.pdf" %timez, bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "Chao1"
#print mapdf


#def func1(metric_df, map_df):
#    """ Take a single metric file and a mapping file, 
#    return a dataframe with samples as rows and 
#    columns: Metric-mean, Metric-SD, Date, Basin, Month, Description""""
    
#    return new_df

#def ambiguously_named_function(stuff):
#    """ Takes a df from previous function, plots the data and saves it to a file with the name + time"""


# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0]
savefig("./Alpha_diversity_results/AD_fig%s.pdf" %timez, bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "Chao1"
#print mapdf


#def func1(metric_df, map_df):
#    """ Take a single metric file and a mapping file, 
#    return a dataframe with samples as rows and 
#    columns: Metric-mean, Metric-SD, Date, Basin, Month, Description""""
    
#    return new_df

#def ambiguously_named_function(stuff):
#    """ Takes a df from previous function, plots the data and saves it to a file with the name + time"""


# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig%s.pdf" %timez, bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Importing alpha diversity data
directory = "../alpha_rare/alpha_div_collated/*"
alpha_data = glob.glob(directory)
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "Chao1"
#print mapdf


#def func1(metric_df, map_df):
#    """ Take a single metric file and a mapping file, 
#    return a dataframe with samples as rows and 
#    columns: Metric-mean, Metric-SD, Date, Basin, Month, Description""""
    
#    return new_df

#def ambiguously_named_function(stuff):
#    """ Takes a df from previous function, plots the data and saves it to a file with the name + time"""


# Importing one point of the rarefaction curve of a single metric and take numeric data
chao1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = chao1.ix[20:29, 3:]

# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["chao1_Mean", "chao1_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    chao1 = date_sorted.chao1_Mean.values
    error = date_sorted.chao1_SD.values
    plt.errorbar(date_sorted["Date"], chao1, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# Significance testing: (after plotting works)
#f_value, p_value = stats.f_oneway(data1, data2, data3, data4, ...)

# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "observed otus"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[0], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "Phylogenetic Distance"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[1], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "Shannon"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()

get_ipython().magic(u'pinfo df.corr')
get_ipython().magic(u'pinfo df.corr')
help(pd.corr)
help(df.corr)
help(pd.DataFrame.corr)
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    print date_sorted["Date"]
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# correlation plotting
# make a dataframe with 6 samples as columns and rows as samples.
df.corr
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    print date_sorted["Date"]
    print date_sorted["Metric"]
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# correlation plotting
# make a dataframe with 6 samples as columns and rows as samples.
df.corr
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    print date_sorted["Date"]
    print date_sorted["Metric_Mean"]
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# correlation plotting
# make a dataframe with 6 samples as columns and rows as samples.
df.corr
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

#alpha_names = [x.split[0]
al = alpha_data[0].split("/")[4]
print al

new_new_df = pd.DataFrame(columns = [])

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    print date_sorted["Date"]
    print date_sorted["Metric_Mean"]
    
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# correlation plotting
# make a dataframe with 6 samples as columns and rows as samples.
df.corr
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

#alpha_names = [x.split[0]
al = alpha_data[0].split("/")[2]
print al

new_new_df = pd.DataFrame(columns = [])

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    print date_sorted["Date"]
    print date_sorted["Metric_Mean"]
    
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# correlation plotting
# make a dataframe with 6 samples as columns and rows as samples.
df.corr
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

#alpha_names = [x.split[0]
al = alpha_data[0].split("/")[3]
print al

new_new_df = pd.DataFrame(columns = [])

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    print date_sorted["Date"]
    print date_sorted["Metric_Mean"]
    
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# correlation plotting
# make a dataframe with 6 samples as columns and rows as samples.
df.corr
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

#alpha_names = [x.split[0]
al = [x.split("/")[3] for x in alpha_data]
print al

new_new_df = pd.DataFrame(columns = [])

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    print date_sorted["Date"]
    print date_sorted["Metric_Mean"]
    
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# correlation plotting
# make a dataframe with 6 samples as columns and rows as samples.
df.corr
# Alpha diversity with correct rarefaction settings and non-Chao1 metrics 6/25/15
# Importing alpha diversity data
directory = "../alpha_rare_min_size/alpha_div_collated/*"
alpha_data = glob.glob(directory)
print alpha_data
map_data = "../map/map_v2-dates-fixed.txt"
mapdf = pd.read_csv(map_data, sep = "\t")
metric = "simpson_e"
#print mapdf

# Importing one point of the rarefaction curve of a single metric and take numeric data
met1 = pd.read_csv(alpha_data[2], sep = "\t")
single_pt = met1.ix[72:, 3:]


# Convert to float and calculate column means and std
single_pt_float = single_pt.astype("float")
mean = single_pt_float.mean(axis=0)
std = single_pt_float.std(axis=0)

# Merge sample alpha diversity data and map file data into a single dataframe.
new_df = pd.DataFrame(columns=["Metric_Mean", "Metric_SD", "Date", "Basin", "Month", "Description"])


# Convert column samples to rows in new dataframe
for column in single_pt_float.columns:
    row = mapdf[mapdf.SampleID==column].index
    date = mapdf.ix[row, "Datefixed"].values[0]
    basin = mapdf.ix[row, "Reactor"].values[0]
    month = mapdf.ix[row, "Month"].values[0]
    description = mapdf.ix[row, "Description"].values[0]
    new_df.loc[column] = [mean[column], std[column], date, basin, month, description]

# update column to datetime type
new_df['Date'] = pd.to_datetime(new_df['Date'])
# Sort dataframe into different groups 
grouped  = new_df.groupby("Basin")

# Create figure and adjust size property
fig,ax=plt.subplots(1)
fig.set_size_inches(9,6)

#alpha_names = [x.split[0]
names = [x.split("/")[3] for x in alpha_data]
print names

new_new_df = pd.DataFrame(columns = names)
print new_new_df

# Plot with error bar from rarefaction bootstrap resample
for name, group in grouped:
    date_sorted = group.sort(columns="Date")
    Metric = date_sorted.Metric_Mean.values
    error = date_sorted.Metric_SD.values
    #print date_sorted["Date"]
    #print date_sorted["Metric_Mean"]
    
    plt.errorbar(date_sorted["Date"], Metric, yerr=error, label=name)

# Add legend and 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size':10})

# Adjust x-axis label and position, add labels and show plot
plt.xlabel("Month")
plt.ylabel("Alpha diversity (%s)" % metric )
plt.title("Alpha Diversity (%s) over time" % metric)
ax.fmt_xdata = mdate.DateFormatter('%Y-%m-%d')
fig.autofmt_xdate()

timez =str(datetime.datetime.now().time()).split(".")[0].replace(":", "_")
savefig("./Alpha_diversity_results/AD_fig_%s.pdf" %timez, bbox_inches="tight")
plt.show()


# correlation plotting
# make a dataframe with 6 samples as columns and rows as samples.
df.corr

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.cm as cm

def feature_counts(ds, sort=False):
    ''' Returns a pandas series with the counts of occurrences of each index.  Sortsbased on index if sort = True.'''
    if sort == True:
        return ds.value_counts().sort_index()
    else:
        return ds.value_counts()

def feature_bar_plot(ax, data, plot_type, title, xlabel, ylabel, sort=False, bar_color ='turquoise'):
    '''Plot a bar chart with the value labeled for each bar.
    
    Parameters
    ----------
    ax: axes object
        axes for plot
    data: pandas data series object
        series to be plotted
    plot_type: str
        'v' for vertical bar chart, 'h' for horizontal bar chart
    title: str
        title of plot
    xlabel: str
        x label for plot
    ylabel: str
        y label for plot
    sort: boolean
        Flag to sort data series by its index before plotting
    bar_color: str
        desired bar color
    
    Returns
    -------
    None
    '''
    feature_obj = feature_counts(data, sort)
    if plot_type == 'h':
        bars = ax.barh(feature_obj.index, feature_obj.values, color = bar_color)
        
        # Add labels for each bar
        for bar in bars:
          width = bar.get_width()
          label_y_pos = bar.get_y() + bar.get_height() / 2
          ax.text(width, label_y_pos, s=f'{width}', va='center')
    else:
        bars = ax.bar(feature_obj.index, feature_obj.values, color = bar_color)
        
        # Add labels for each bar
        for bar in bars:
          height = bar.get_height()
          label_x_pos = bar.get_x() + bar.get_width() / 2
          ax.text(label_x_pos, height, s=f'{height}', ha='center')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

def galactic_plot(data, fig, ax, title, plot_earth=True):
    '''
    Plot a skymap in galactic coordinates.

    Parameters
    ----------
    data: pandas dataframe
        data to be plotted; must contain index labels 'glon', 'glat', and 'pl_rade'
    fig: figure object
        figure for plot
    ax: axes object
        axes to plot on
    title: string
        title of the plot
    plot_earth: boolean
        flag to plot Earth's position and annotate it
    
    Returns
    -------
    None
    '''
    earth_coords = (179,0)
    color = np.random.rand(len(data)) # Generate random numbers to identify different colors for plot markers
    ax.scatter(data['glon'], data['glat'], s= data['pl_rade']*2, c=color, cmap=cm.viridis, alpha = 0.5)
    # Plot Earth and annotate if plot flag set to True
    if plot_earth == True:
        ax.scatter(earth_coords[0], earth_coords[1], s=2,color = 'blue') # Plot Earth
        ax.annotate('Earth', xy=earth_coords, xytext= (200,5), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=18)
    
    ax.set_title(title)
    ax.set_ylabel('Galactic Latitude (deg)')
    ax.set_xlabel('Galactic Longitude (deg)')
    # Create legend
    sz = np.array([0.27, 1, 4.01, 11.2, 109.2])
    handles = [ax.scatter([], [], s=sz[i]*2) for i in range(len(sz))]
    labels = ['Moon', 'Earth', 'Uranus', 'Jupiter', 'Sun']
    fig.legend(handles=handles, labels=labels, scatterpoints=1, title='Exoplanet Size\n(Earth Radius)')

def box_facet(axs, data_list, col_name, titles):
    '''
    Facet box plots for one feature of a dataframe.

    Parameters
    ----------
    axs: list of axes objects
        axes to plot on; must have same number of elements as data_list
    data_list: list of pandas dataframes/series for each plot
        data to be plotted; must contain index labels 'glon', 'glat', and 'pl_rade'
    col_name: string
        feature (by column name) to facet across box plots
    titles: list of strings
        list of titles for each subplot
    
    Returns
    -------
    None
    '''
    y_maxs = []
    y_mins = []
    # Plot each subplot
    for i, ax in enumerate(axs):
        ax.boxplot(data_list[i][col_name].dropna(), showmeans = True)
        ax.set_title(titles[i])
        # Get and store y limits for each subplot
        y_min, y_max = ax.get_ylim()
        y_maxs.append(y_max)
        y_mins.append(y_min)
    # Ensure limits are the same for all axes
    for ax in axs:
        ax.set_ylim(min(y_mins),max(y_maxs))
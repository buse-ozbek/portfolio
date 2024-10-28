#This code analyzes a dataset of songs by genre, sorting by danceability and adding duration in seconds. 
# It creates two figures: a pie chart of song counts and a bar chart of average popularity by genre, 
# Followed by a plot of danceability vs. energy and a histogram of song durations.

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set pandas option to prevent data frame output from breaking across lines
pd.set_option('display.expand_frame_repr', False)

# Loading data from an Excel file containing song information
songs = pd.read_excel('music_genre.xlsx')

# Sorting songs by 'danceability' in ascending order
sorted_songs = songs.sort_values('danceability')

# Adding a new column 'duration_sec' to represent duration in seconds instead of milliseconds
sorted_songs['duration_sec'] = sorted_songs.duration / 1000

# Filtering data by genre for specific analyses
rock = sorted_songs[sorted_songs['music_genre'] == 'Rock']  # Rock genre songs
hh = sorted_songs[sorted_songs['music_genre'] == 'Hip-Hop']  # Hip-Hop genre songs
alternative = sorted_songs[sorted_songs['music_genre'] == 'Alternative']  # Alternative genre songs

# Plotting genre distribution with a pie chart
plt.figure(1)  # Opens a new figure window
plt.clf()  # Clears the figure window

# Labels for each genre in the pie chart
labels = 'Number of Rock', 'Number of Hip-Hop', 'Number of Alternative'

# Counts of songs per genre
len_r = len(rock)
len_h = len(hh)
len_a = len(alternative)

# Sizes for the pie chart based on counts
sizes = len_r, len_h, len_a

# Colors for each genre slice
colors = 'red', 'purple', 'brown'

plt.subplot(2, 1, 1)  # First subplot (top) for pie chart
plt.pie(sizes, labels=labels, colors=colors)  # Plotting pie chart

# Calculating mean popularity for each genre
mean_r = np.mean(rock.popularity)
mean_h = np.mean(hh.popularity)
mean_a = np.mean(sorted_songs.popularity)  # Mean popularity across all songs

# Storing means to plot them in a bar chart
means = mean_r, mean_h, mean_a

plt.subplot(2, 1, 2)  # Second subplot (bottom) for bar chart
plt.bar(['Rock', 'Hip Hop', 'All Genres'], means)  # Plotting bar chart with mean popularity

# New figure for additional analysis
plt.figure(2)
plt.clf()

# First subplot in new figure: Danceability vs Energy for Alternative and Rock genres
plt.subplot(1, 2, 1)  # Left subplot
aenergy = alternative.energy
adanceability = alternative.danceability
renergy = rock.energy
rdanceability = rock.danceability

# Plotting danceability vs energy for Alternative and Rock genres
plt.plot(adanceability, aenergy)
plt.plot(rdanceability, renergy)
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.title('Danceability vs Energy')
plt.legend(['Alternative Danceability', 'Rock Danceability'])

# Second subplot: Histogram of song durations
plt.subplot(1, 2, 2)  # Right subplot
plt.title('Distribution of the Song Duration (seconds)')
plt.xlabel('Duration (seconds)')

# Plotting histogram of song durations in seconds
hist_data = plt.hist(sorted_songs['duration_sec'], 4, color='green')

# Setting x-ticks based on histogram bin edges
plt.xticks(hist_data[1])

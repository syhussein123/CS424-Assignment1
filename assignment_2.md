## Task 1 : Revisiting Our Data and Questions

During assignment 1, we inspected our dataset more carefully and identified several problems that would limit our analysis. We decided it may be too late to pivot during Assignment 1, so we made changes now, as part of our Assignment 2. The original Google Form collected commute duration and distance as bucketed ranges (e.g. “45-60 minutes”, “25-30 miles”) and starting location as free text. This caused the following issues:

Bucketed values blocked scatterplots and true averages. We couldn’t analyze continuous relationships
Free-text locations were inconsistent. While normally this could be fixed with data cleaning, we figured it was an issue on our side with data collection being unclear, since we had vague entries like “suburb” and “city-Chicago” rather than specific area names.

To address these problems, we rebuilt the Google Form midway through collection. The new form collects one day per submission, uses exact numeric values for duration and distance, uses a fixed dropdown for starting location, and eliminates the N/A confusion by only asking about days the respondent actually commuted. We are continuing to collect data with the new form through mid-October, and compiled it to ‘data/raw/a2_commute_data.csv’

**Guiding Questions for Assignment 2:**

For this assignment, our goal is to understand the shape and limitations of our newly cleaned dataset while building working visualizations and before building our final visualizations. We will use the following data-exploration questions to guide our work in Task 3:

1. What does the majority of people use to commute?
2. What time windows have the highest volume of commuters?
3. Are there specific days where commute times spike?
4. Which data points (weather, distance, transport mode) show the most interaction with each other?
5. How many observations did we lose or gain by switching to the new form format?

These guiding questions will help us determine which of our domain questions from Assignment 1 are actually supported by the data before we commit to our final visual designs.

## Task 2 : Preparing the data

All data cleaning code is located in the `datacleaning.py` file. This file reads in the raw google form data from `data/raw/` and writes out the cleaned dataset to `data/processed/commutes_clean.csv`. The raw files are not edited by hand, so running the script should always reproduce the same output.

**Main Transformations Done:**

- **Renamed Columns**: The long form questions were renamed to short names for us to utilize as variables (e.g. `location`, `duration_minutes`) so they are easier to work with in code and charts.
- **Dropped `timestamp`**: this column only recorded the time of form submission, not when the commute happened, so `date` is used instead.
- **Converted types**: Dates, times, and numbers were stored as text. We converted them to real date, time, and numeric types so they can be sorted, compared, and plotted on continuous axes.
- **Standardized locations.** Respondents typed the same place in different ways (e.g. "little italy", "Little Italy, Chicago", "Taylor and Carpenter"). We mapped every variant to one name using a lookup table, `data/lookups/locations.csv`, and added a `location_region` column (Chicago or Suburb) for city vs. suburb comparisons.
- **Standardized mode and weather.** Merged equivalent labels such as "Car" and "Car (alone)", and "Clear" and "Sunny", so each category is counted once.
- **Added derived columns:**
  - `respondent_id`: an anonymous ID (R1, R2, ...) for each entry
  - `is_rainy`: whether it was raining, for weather comparisons
  - `near_uic`: whether the commute started within 5 miles of campus, to separate local commuters from long-distance ones
  - `duration_bucket`: 15-minute ranges matching our Assignment 1 sketches, for grouped charts

## Task 3 : Explore the data

### Commute Duration by Mode of Transportation

![Commute duration by mode](figures/task4_mode_duration.png)

This figure aims to answer the two following questions that we had:

- What does the majority of people use to commute?
- What time windows have the highest volume of commuters?

**Attributes used**:

- duration_minutes (quantitative)
- mode_of_transportation (categorical)

**Marks and channels**:

- Marks:
- Lines, one smooth curve per mode of transporation
- Points for modes with too few commutes to draw a curve
- Channels:
- Horizontal position for commute time in minutes
- Vertical position for how common that commute time is within each mode
- Color hue to tell modes apart

**Why did we try this approach**:
This approach was an attempt to reimplement Sketch 4 from assignment 1. In the original sketch, commute times were grouped into 15-minute buckets because the original form only collected ranges. With the new form collecting exact minutes, we replaced the buckets with a smoothed curve for each mode, so the shape of each distribution comes from the real values instead of fixed ranges. Each curve is scaled to its own mode, which keeps the refinement from our sketch: Train and Car do not dominate the chart just because they have more observations.

**What worked and What didn't**:
Some things that worked include: The staircase pattern in the sketch reflext the data accurately and shows us where peak times are for each of the different modes of transportation. Exact minutes being used also displays data that the buckets initially grouped up, allowing for the data to reveal what we didn't ntoice before. Like how car travel can be very unpredictable in comparison to train or walking.

Some things that didn't work include: Biking data only having a couple commutes, all being within the same time frame, so the curve is just a tall narrow spike in the data. Carpool also only has 2 data points, so we can't draw that many conclusions since we don't have much data. Since this is based on density, we don't know the exact counts at each minute interval since we smoothed the graph so we can make accurate comparisons.

**Whether we will keep, modify, combine, or abandon**:
It would be a good idea to modify this graph in the future. It is a strong direction in answering our domain question, but trying a version that displays counts or maybe shows the data in a way that reveals something else may benefit us.

## Task 4 : Implement visualization alternatives

## Task 5 : Interaction and multiple views

## Task 6 : Iterate and refine

## Task 7 : Current Design

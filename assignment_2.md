## Task 1 : Revisiting Our Data and Questions

During  assignment 1, we inspected our dataset more carefully and identified several problems that would limit our analysis. We decided it may be too late to pivot during Assignment 1, so we made changes now, as part of our Assignment 2. The original Google  Form collected commute duration and distance as bucketed ranges (e.g. “45-60 minutes”, “25-30 miles”) and starting location as free text. This caused the following issues: 

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

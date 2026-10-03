# **Task 1 Observation and Data Collection Plan** 

# **Task 2: Pilot and Data Collection**

Before collecting the complete dataset, we conducted a small pilot with approximately 10 observations to test the structure of our Google Form, our variable definitions, and whether the instructions were clear. We distributed the initial form to a few classmates and reviewed the responses together as a group.

## Were the attributes clear and easy to record?

Yes. Respondents were able to select their commute time, weather condition, duration, and mode of transportation without confusion. The grid format we used in our Google Form made it easy for respondents to report an entire week of commutes in one submission, rather than filling out the form five separate times.

## Were any observations difficult to classify?

Yes. The main difficulty was handling days when respondents do not commute to campus. It was unclear whether they should leave the row blank, select "N/A," or skip it entirely. We added an "N/A" option to every question for each day, which resolved most of the confusion. However, we noticed that some respondents still selected a mode of transportation (like "Other") on days they marked "N/A" for time and duration. This told us that respondents do not always interpret "N/A" consistently across all questions, and we flagged it as a data cleaning issue to address later.

## Did different group members interpret attributes differently?

No. The attributes and categories were straightforward, and both group members interpreted them the same way. We agreed on definitions before distributing the form to avoid inconsistency.

## Were important attributes missing?

Yes. During the pilot, we realized we had not asked respondents where they were commuting from. Without a location attribute, we could not do any spatial analysis or compare suburbs versus city commuters. We added a location question after the pilot, asking respondents for their starting city or neighborhood. Because the earliest pilot responses did not include location, those rows have missing location data. We documented this as a known limitation of the dataset.

## Were some attributes unnecessary?

No. Every attribute we collected maps to at least one domain question we want to investigate. We considered dropping the weather question at one point because it added complexity to the form, but we kept it because it enables comparisons between conditions (rain vs. sun) that are central to our project.

## Did the pilot change the kinds of questions you thought you could answer?

Yes. The pilot revealed two important limitations that changed how we approached our domain questions:

**Missing location data.** We originally planned to analyze commute patterns geographically, but without a location attribute, we could only compare distance buckets, not actual starting areas. After adding the location question, we can now ask questions like "do students from farther suburbs rely more on cars than trains?"

**Bucketed instead of numeric values.** We collected distance and duration as ranges (e.g., 15–30 minutes, 6–8 miles) rather than exact numbers. This means we cannot calculate precise averages or make true scatter plots. We can still compare groups and identify patterns, but our analysis is limited to ordinal comparisons rather than continuous correlations. We documented this as a tradeoff: bucketed data is easier for respondents to report quickly and accurately, but it limits the types of visualizations we can create.

## Revisions Made After the Pilot

Based on what we learned, we made the following changes before the full collection:

- Added a question asking respondents for their starting location (city or neighborhood)
- Clarified instructions for the N/A option so respondents understood it applies across all questions for that day
- Accepted that bucketed distance and duration would limit us to ordinal comparisons and planned our domain questions accordingly

## Full Data Collection

After revising the form, we distributed it through club Discord servers and to classmates. The form remained open for two weeks, so we can have two weeks of data to compare variables like weather. Each respondent reported their commute for all five weekdays in a single submission.

We collected 51 responses, giving us approximately 230 total observations (51 respondents × 5 days) before removing N/A entries.

The data was collected anonymously. No names, faces, license plates, or other personally identifiable information were recorded.

## Dataset and Data Dictionary

The final dataset is stored in the repository as `commute_data.csv` in long format, with one row per respondent per day.

### Data Dictionary

| Attribute | Type | Description | Example |
|---|---|---|---|
| respondent_id | Categorical | Unique identifier for each respondent (from form timestamp) | R001 |
| day | Categorical | Day of the week | Monday |
| time | Categorical | Hour of commute | 11am |
| weather | Categorical | Weather condition during commute | Cloudy |
| duration | Ordinal | Commute duration in bucketed ranges | 45-60 Minutes |
| mode | Categorical | Primary mode of transportation | Car |
| distance | Ordinal | Distance from starting point in bucketed ranges | 25-30 Miles |
| location | Categorical | Starting city or neighborhood | Pilsen, Chicago |

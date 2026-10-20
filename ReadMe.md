## CS 424 - Fall 2026 Group Project: Analysis on UIC Student's Commute

**Group Members:** Masa Milojkovic, Sara Alaidroos, Shuroq Hussein

### Assignmemnt 1:

Assignment details and answers location in file "Assignment_1.md" 
Navigate Assignment 1 [here](Assignment-1) 

### Assignment 2: 

Creating venv: python3 -m venv .venv
Activating venv: source .venv/bin/activate
pip install pandas

`datacleaning.py` reads the raw form data from `data/raw/a2_commute_data.csv`, renames the form questions to short column names, drops the timestamp, strips extra spaces, converts dates, times, and numbers to proper types, and standardizes locations using `data/lookups/locations.csv`. The output is saved to `data/processed/commutes_clean.csv`. Use the `location_clean` column for charts.

to run task 5: 
python task5.py
open task5.html with liveserver

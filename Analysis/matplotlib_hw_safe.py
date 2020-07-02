# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

# Study data files
mouse_metadata_path = "..\\Resources\\Mouse_metadata.csv"
study_results_path = "..\\Resources\\Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset
mousemeta_studyresults_combined = pd.merge(mouse_metadata, study_results, on="Mouse ID")

# Display the data table for preview
mousemeta_studyresults_combined

# Checking the number of mice.
total_mice_with_duplicates = (mousemeta_studyresults_combined["Mouse ID"].count())
# Display
total_mice_with_duplicates = pd.DataFrame({"Total Number of Mice(with duplicates for each test)": total_mice_with_duplicates}, index=[0])
total_mice_with_duplicates

# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint.
duplicates = mousemeta_studyresults_combined[mousemeta_studyresults_combined.duplicated(['Mouse ID', 'Timepoint'])]
organized_df = duplicates[["Mouse ID"]]
rename_df = organized_df.rename(columns={"Mouse ID": "Duplicate ID number for Mouse ID and Timepoint"})
rename_df

# Optional: Get all the data for the duplicate mouse ID.
duplicates = mousemeta_studyresults_combined[mousemeta_studyresults_combined.duplicated(['Mouse ID', 'Timepoint'], keep= False)]
duplicates

# Create a clean DataFrame by dropping the duplicate mouse by its ID.
cleaned_df = mousemeta_studyresults_combined.drop_duplicates()
cleaned_df

# Checking the number of mice in the clean DataFrame.
total_mice = len(cleaned_df["Mouse ID"].value_counts())
# Display
total_mice = pd.DataFrame({"Actual Number of Mice": total_mice}, index=[0])
total_mice
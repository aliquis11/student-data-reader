import pandas as pd
import numpy as np

def read_marksheet(file):
    """Read a marksheet.csv and extract module metadata and marks.

    Parameters
    ----------
    file : str 
        Path to the marksheet.csv file. The marksheet should have the standard form used by the Department of Mathematcial Sciences at Loughborough University.   

    Returns
    -------
    metadata : dict
        Metadata extracted from the marksheet, including information
        such as the module title and module code.

    marks_df : pandas.DataFrame
        DataFrame containing the marks data for each student of the module.
    """
    # Read the first 6 rows of the CSV file to extract metadata
    meta_df = pd.read_csv(file,header=None,  nrows=6)

    # Import metadata from marksheet to dictionary metadata. 
    metadata = {
     "code": meta_df.iloc[0, 2],
     "title": meta_df.iloc[1, 2],
     "year": int(meta_df.iloc[2, 2]),
     "number_assessments": int(meta_df.iloc[5, 2])
    }

    # Import stduent numnbers adnassessment data from marksheet to dataframe marks_df. 
    skiprows = list(range(9))+[11]
    marks_df = pd.read_csv(file, skiprows=skiprows)
    marks_df = marks_df.drop(marks_df.columns[[1, 2, 3]], axis=1)

    # Extract assessment names and weights from marks_df
    assessment_names = list(marks_df.columns[1:metadata["number_assessments"]+1])
    weights_percentages = list(marks_df.iloc[0, 1:metadata["number_assessments"]+1])

    assessments = []
    for name, weight in zip(assessment_names, weights_percentages):
      assessments.append(
        {
            "name": name,
            "weight": float(weight.replace("%", "")) / 100
        }
        )

    # Add assessments to metadata
    metadata["assessments"] = assessments

    # Drop the first row of marks_df which contains the weights
    marks_df=marks_df.drop(0)

    # Drop rows with Regno that do not start with 'F' followed by digits
    marks_df = marks_df[
        marks_df["Regno"].astype(str).str.match(r"^F\d+")
    ]

    # Convert all columns except the first one to numeric, coercing errors to NaN
    for col in marks_df.columns[1:]:
        marks_df[col] = pd.to_numeric(
        marks_df[col],
        errors="coerce"
    )

    if metadata["number_assessments"]+1 < len(marks_df.columns):

        # Final mark column exists. Rename it to "Final Mark" for consistency.
        marks_df = marks_df.rename(
        columns={marks_df.columns[metadata["number_assessments"]+1]: "Final mark"})
        
        # Check if the final mark column is empty. 
        if marks_df.iloc[:, metadata["number_assessments"]+1].isna().all():
            compute_final = True
        else:
            compute_final = False
    else:
        compute_final = True 

    # Fill NaN values with 0
    marks_df = marks_df.fillna(0)

    # Compute final mark if needed
    if compute_final:
        marks_df["Final mark"] = 0
        # Compute the final mark based on the weights and assessment marks
        for assessment in metadata["assessments"]:
            name = assessment["name"]
            weight = assessment["weight"]
            marks_df["Final mark"] += marks_df[name] * weight

    # Rename the first column to "Regno"
    marks_df.rename(
        columns={marks_df.columns[0]: "Regno"},
        inplace=True
    )

    # Round final mark to nearest integer
    marks_df["Final mark"] = np.floor(marks_df["Final mark"] + 0.5).astype(int)

    # Add final mark to assessments list
    # assessments.append({"name": 'Final mark', "weight": 1})

    # Reset the index of marks_df
    marks_df = marks_df.reset_index(drop=True)

    # Keep only the columns for Regno, assessments, and final mark
    marks_df=marks_df.iloc[:, :metadata["number_assessments"]+2]

    return metadata, marks_df
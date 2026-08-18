# Student Data Reader
A small Python package containing functions for reading student marksheet and attendance data used in modules in the Department of Mathematical Sciences at Loughborough University.

## Features
- Read standard Loughborough University marksheet CSV files.
- Read standard Co-Tutor attendance XLSX files.
- Return the data as pandas DataFrames for use in analysis and reporting projects.

## Requirements
- Python 3.10 or later
- Required packages listed in `requirements.txt`

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Usage
The reader functions can be imported into Python projects using:

```python
from student_data_reader import read_marksheet, read_attendance
```

# End-of-module report writer
This notebook was developed to automatically generate basic end-of-module reports for modules taught in the Department of Mathematical Sciences at Loughborough University.

## Features
- Extract metadata and marks data from standard marksheet CSV file
- Extract attendance data from Co-Tutor-generated XLSX file. 
- Carry out an automated analysis of the data.
- Produce a LaTeX report (modulecode_report.tex) with text, tables and figures describing the statistical outcomes of the module.


## Usage
1. Clone or download this repository.

2. Obtain the marksheet csv file. The marksheet should follow the standard format used by the Department of Mathematical Sciences at Loughborough University. Place the file in the data folder and rename it marksheet.csv, replacing the illustrative file currently supplied with the repository. If the marksheet does not already contain a final column with the final mark, this will be computed.

3. Optional: Obtain the attendance xlsx file from Co-Tutor (Digital Registers → View Module Register → Export to Excel). Place the file in the data folder and rename it attendance.xlsx, replacing the illustrative file currently supplied with the repository.

4. Open report.ipynb. If an attendance file is not available, set attendance_file = None in cell [8].

5. Run all cells.

The notebook will load the data automatically, generate the a LaTeX report and figures, and will save them in the outputs folder.

## Project structure

```text
student-data-reader/
├── student_data_reader/
│   ├── __init__.py
│   ├── marks.py
│   └── attendance.py
├── data/
├── README.md
├── requirements.txt
└── LICENSE
```

### student_data_reader/marks.py
Contains the functions used to read standard Loughborough University marksheet CSV files.

### student_data_reader/attendance.py
Contains the functions used to read standard Co-Tutor attendance XLSX files.

### student_data_reader/__init__.py
Makes the reader functions available directly from the `student_data_reader` package.

## Data
No real student data is included in this repository. The files provided in the data folder were generated for illustrative purposes only. The outputs folder contains example outputs, including a compiled PDF report generated from the illustrative data.

## Development workflow

New functionality is developed on feature branches rather than directly on
`master`. Changes are tested before being merged into `master` and included
in a new release.

Current development:

- `attendance-additional-columns` — feature branch for modifying the attendance reader to include individual lecture records
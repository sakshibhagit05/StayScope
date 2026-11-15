# StayScope – Airbnb Data Analysis

## Project Overview

StayScope is a data analysis project based on the New York City Airbnb 2019 dataset.

The project explores Airbnb listing patterns, pricing trends, room types, neighbourhood distributions, and listing title text patterns using Python and data analysis techniques.

## Dataset

- **Dataset Name:** AB_NYC_2019.csv
- **Source:** New York City Airbnb Open Data
- **Format:** CSV
- **Location:** New York City, USA
- **Year:** 2019

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Plotly

## Project Analysis

The project includes the following analysis tasks:

1. Data inspection and cleaning
2. Exploratory Data Analysis (EDA)
3. Price distribution analysis
4. Outlier analysis
5. Room type analysis
6. Neighbourhood analysis
7. K-Means clustering
8. Listing title text mining
9. Word frequency and bigram analysis
10. Price pattern analysis

## Project Structure

```text
StayScope/
├── data/
│   ├── AB_NYC_2019.csv
│   ├── cleaned_airbnb.csv
│   └── New_York_City_.png
├── notebooks/
│   └── StayScope_Analysis.ipynb
├── outputs/
│   ├── Analysis visualizations
│   └── Analysis CSV files
├── src/
│   ├── clean_data.py
│   ├── clustering.py
│   ├── eda_analysis.py
│   ├── inspect_data.py
│   ├── outlier_analysis.py
│   ├── pattern_analysis.py
│   └── text_mining.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sakshibhagit05/StayScope.git
```

### 2. Navigate to the Project Directory

```bash
cd StayScope
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 6. Start Jupyter Notebook

```bash
jupyter notebook
```

Open `notebooks/StayScope_Analysis.ipynb` and run all cells.

## Output

The project generates visualizations and CSV files containing analysis results, including:

- Price distribution visualizations
- Room type comparisons
- Neighbourhood analysis
- Outlier analysis
- K-Means clustering results
- Word frequency and bigram analysis
- Price pattern visualizations

## Conclusion

StayScope explores the 2019 New York City Airbnb dataset to identify historical pricing trends, neighbourhood patterns, room type distributions, and listing clusters.

Since the analysis is based on 2019 data, the findings represent historical market patterns and should not be interpreted as current Airbnb market trends.
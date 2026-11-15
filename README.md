# StayScope – Airbnb Data Analysis

## Project Overview
StayScope is a data analysis project based on the New York City Airbnb 2019 dataset.

The project explores Airbnb listing patterns, pricing trends, room types, neighbourhood distributions, and listing title text patterns using Python and data analysis techniques.

## Dataset
- Dataset: AB_NYC_2019.csv
- Source: New York City Airbnb Open Data
- Format: CSV
- Dataset Year: 2019

**Note:** This project uses historical data from 2019. Therefore, the findings represent patterns in the Airbnb market during that period and should not be considered current market trends.

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
│   └── cleaned_airbnb.csv
├── notebooks/
│   └── StayScope_Analysis.ipynb
├── outputs/
├── src/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone or download the project.
2. Navigate to the project directory.
3. Create and activate a virtual environment.

```bash
python -m venv venv
```

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

4. Install the required libraries:

```bash
pip install -r requirements.txt
```

5. Launch Jupyter Notebook:

```bash
jupyter notebook
```

6. Open `notebooks/StayScope_Analysis.ipynb` and run the notebook cells.

## Output

The project generates visualizations and CSV files containing analysis results, including price distributions, clustering, neighbourhood patterns, and text mining results.

## Conclusion

StayScope provides an exploratory analysis of the New York City Airbnb 2019 dataset. It identifies historical pricing patterns, neighbourhood distributions, room type trends, and listing clusters using data analysis and machine learning techniques.

The results reflect the Airbnb market conditions represented by the 2019 dataset and do not necessarily indicate present-day market conditions.
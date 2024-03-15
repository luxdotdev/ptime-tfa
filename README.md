# Overwatch Match Data Cleaner

## Overview
This repository contains a set of Python scripts designed for cleaning and analyzing Overwatch match data. The project structures the match data to identify key gameplay events such as staggers and first kills within each fight, enriches the data with hero role information, and provides tools for connecting to and querying a database. The analysis part of the project helps in understanding team performance by fights won.

## Repository Structure

- `cleaning.py`: Contains functions for cleaning and structuring Overwatch match data, including identifying stagger events and first kills in fights, and merging hero roles.
- `collect_data.py`: A script for connecting to a database to retrieve match data, clean it using functions from `cleaning.py`, and prepare it for analysis.
- `db_connect.py`: Includes functions for parsing database connection URLs and establishing connections to a PostgreSQL database.
- `hero_mappings.py`: Defines mappings between Overwatch heroes and their respective roles (Damage, Tank, Support), used for enriching the match data.
- `two_way_table.py`: A simple analysis script that groups cleaned data by attacker team and whether they won the fight, summarizing team performance.

## Setup

### Prerequisites

- Python 3.8+
- pandas
- psycopg2
- python-dotenv

### Installation

1. Clone the repository to your local machine.
2. Ensure you have Python 3.8 or newer installed.
3. Install the required Python packages:
   ```
   pip install pandas psycopg2 python-dotenv
   ```
4. Create a `.env` file in the root of the project directory containing your database connection URL:
   ```
   prod_url=YOUR_DATABASE_CONNECTION_URL_HERE
   ```

### Usage

1. **Data Collection and Cleaning**:
   - Execute `collect_data.py` to collect match data from your database, clean it, and prepare it for analysis. This script integrates data cleaning, role enrichment, and database interactions seamlessly.
   - Ensure your database contains the required tables and schema as expected by the query in `collect_data.py`.

2. **Data Analysis**:
   - After cleaning, you can use `two_way_table.py` to analyze team performance based on the cleaned data. This script provides a simple analysis, grouping data by attacker team and whether they won the fight.

## Contributing

Contributions are welcome! If you have suggestions for improving the code, please open an issue or submit a pull request.

### Important Notes

- Remember to update your `.env` file with the correct database connection URL before running `collect_data.py`.
- The scripts assume specific database schema and table structures. Adjust the SQL queries in `collect_data.py` and `db_connect.py` as necessary to match your database setup.
- For detailed analysis or additional functionality, consider extending `two_way_table.py` or creating new analysis scripts based on the cleaned data.


If you have any questions or need further assistance, feel free to reach out or open an issue in the repository.
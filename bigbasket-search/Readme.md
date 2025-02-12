# Keyword Search Script

This script automates the keyword search process and takes a list of keywords as input (e.g. Hair fall shampoo, Conditioner,
Shampoo), perform a search in the specified retailer site and find out the
best rank for brands Tresemme, Loreal and Dove in the result.

## Prerequisites

Ensure you have Python 3 installed on your system.

## Setup Instructions

1. **Create a Virtual Environment**  
   Run the following command to create a virtual environment:
   ```sh
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**  
   On macOS and Linux:
   ```sh
   source ./venv/bin/activate
   ```
   On Windows:
   ```sh
   venv\Scripts\activate
   ```

3. **Install Required Packages**  
   Install the necessary dependencies from `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Script

Execute the script using:
```sh
python3 keyword_search.py
```

## Output

The results will be saved in `results.json`.



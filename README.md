# Google Sheets and API Demo with Python

This project demonstrates how to:
- Read and write data to Google Sheets using `pygsheets`.
- Retrieve data from an external API and process it with `pandas`.
- Insert filtered data into a Google Spreadsheet.

## Requirements

- Python 3.x
- pandas
- pygsheets
- requests
- A `credentials.json` file for a Google Service Account with access to the spreadsheets.

Install dependencies with:
```bash
pip install pandas pygsheets requests
```

## Usage

1. Open the notebook in VS Code or Jupyter.
2. Run the cells in order:
   - Authenticate and load data from Google Sheets.
   - Insert rows from another sheet.
   - Fetch products from an external API.
   - Filter and insert expensive products into the Google Sheet.

---

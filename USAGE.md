# Handelsbanken OFX Statement Parser User Guide

This tool helps you convert transaction statements from Handelsbanken (Sweden)
into OFX format, which can be imported into various financial software like
GnuCash.

## Prerequisites

Before you start, make sure you have:

- Python 3.7 or newer installed
- pip (Python package installer)
- A transaction statement from Handelsbanken in Excel format (.xlsx)

## Installation

1. Install the ofxstatement package and the Handelsbanken plugin:

```bash
pip install ofxstatement
pip install git+https://github.com/gurkodil/ofxstatement-handelsbanken.git
```

## Getting Your Transaction Data

1. Log in to Handelsbanken
2. Navigate to your account transactions
3. Click on "Export" or "Download"
4. Choose Excel format (.xlsx)
5. Save the file to your computer

## Converting the Statement

1. Open a terminal/command prompt
2. Navigate to the directory where you saved your transaction file
3. Run the conversion command:

```bash
ofxstatement convert -t handelsbanken transactions.xlsx output/transactions.ofx
```

Where:

- `-t handelsbanken` specifies that we're using the Handelsbanken plugin
- `transactions.xlsx` is your downloaded transaction file
- `output/transactions.ofx` is where you want to save the converted file

## Troubleshooting

Common issues and solutions:

1. **"Plugin not found" error**
   - Make sure you have installed ofxstatement-handelsbanken correctly
   - Verify the plugin is listed when running: `ofxstatement list-plugins`

2. **"Invalid format" error**
   - Ensure you're using the correct Excel export format from Handelsbanken
   - Check that the file hasn't been modified

## Support

If you encounter any issues:

1. Check if your Excel file matches the expected format
2. Make sure you're using the latest version of the plugin
3. Open an issue on the GitHub repository if the problem persists

## Importing to Financial Software

After converting your statement to OFX format, you can import it into your
financial software:

### GnuCash

1. Open GnuCash
2. Go to File > Import > Import OFX/QFX
3. Select your converted .ofx file
4. Follow the import wizard

### Other Software

Most financial software supports OFX import. Consult your software's
documentation for specific instructions.

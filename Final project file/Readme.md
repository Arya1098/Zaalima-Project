# Invoice Automation (Email → PDF → Excel)

This project automates fetching invoice PDFs from Gmail, extracting invoice details, and storing them in an Excel file.

## Features
- Fetches the latest invoice PDF from Gmail
- Extracts invoice details (Invoice Number, Date, Amount, Vendor)
- Handles multiple invoices in a single PDF
- Stores extracted data into `invoice_log.xlsx`
- Skips duplicates automatically
- Tkinter UI for Gmail credentials


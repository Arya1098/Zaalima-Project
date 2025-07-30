import pandas as pd
import os

EXCEL_FILE = "invoice_log.xlsx"

def store_invoice_list(invoice_list):
    if not invoice_list:
        return "No data to store."

    try:
        if os.path.exists(EXCEL_FILE):
            df_existing = pd.read_excel(EXCEL_FILE)
        else:
            df_existing = pd.DataFrame(columns=invoice_list[0].keys())

        new_df = pd.DataFrame(invoice_list)
        new_df = new_df[~new_df["Invoice Number"].isin(df_existing["Invoice Number"])]

        if new_df.empty:
            return "No new invoices to add (all were duplicates)."

        df_combined = pd.concat([df_existing, new_df], ignore_index=True)
        df_combined.to_excel(EXCEL_FILE, index=False)
        return f"{len(new_df)} new invoices saved to Excel."
    except Exception as e:
        return f"Excel save error: {e}"

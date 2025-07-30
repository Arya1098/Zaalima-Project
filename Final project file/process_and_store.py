from extract_invoice_data import extract_all_invoices_from_latest_pdf
from store_to_excel import store_invoice_list

invoices = extract_all_invoices_from_latest_pdf()
print("Extracted:", len(invoices), "invoices")

for invoice in invoices:
    print(invoice)

result = store_invoice_list(invoices)
print(result)

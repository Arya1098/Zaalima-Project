import pdfplumber
import re
import os

def get_latest_pdf(path="./invoices"):
    pdfs = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".pdf")]
    if not pdfs:
        return None
    return max(pdfs, key=os.path.getctime)

def extract_all_invoices_from_latest_pdf():
    pdf_path = get_latest_pdf()
    if not pdf_path:
        return []

    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    invoice_pattern = re.compile(
        r"Invoice Number:\s*(\S+).*?"
        r"Date:\s*([\d\-\/.]+).*?"
        r"Total:\s*Rs\.\s*([\d,.]+).*?"
        r"Vendor:\s*(.*?)\s+Thank you",
        re.DOTALL
    )

    matches = invoice_pattern.findall(text)
    results = []

    for match in matches:
        invoice_no, date, amount, vendor = match
        results.append({
            "Invoice Number": invoice_no.strip(),
            "Date": date.strip(),
            "Amount": amount.strip(),
            "Vendor": vendor.strip()
        })

    return results

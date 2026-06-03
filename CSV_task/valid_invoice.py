import pandas as pd
from datetime import datetime, date

def validate_invoices(csv_file):
    df = pd.read_csv(csv_file)

    for index, row in df.iterrows():
        invoice_no = row["invoice_no"]
        vendor_name = row["vendor_name"]
        invoice_date = row["invoice_date"]
        amount = row["amount"]

        errors = []

        try:
            invoice_date_obj = datetime.strptime(invoice_date, "%Y-%m-%d").date()

            if invoice_date_obj > date.today():
                errors.append("Invoice date is in the future")

        except ValueError:
            errors.append("Invalid date format")

        if amount <= 0:
            errors.append("Amount must be greater than zero")

        print("--------------------------------")
        print(f"Invoice No: {invoice_no}")
        print(f"Vendor Name: {vendor_name}")
        print(f"Date: {invoice_date}")
        print(f"Amount: {amount}")

        if errors:
            print("Status: INVALID")
            print("Errors:")
            for error in errors:
                print(f"- {error}")
        else:
            print("Status: VALID")
            print("No errors found")

validate_invoices("INVOICES.csv")
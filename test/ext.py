import pdfplumber
import json

def extract_tables_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        b = 1
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                json_output = json.dumps(table)
                with open(f"{b}.json", "w") as f:
                    f.write(json_output)
                b += 1

# Extract tables from the modified PDF
extract_tables_from_pdf("b_modified.pdf")

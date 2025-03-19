import json
from fpdf import FPDF

class PDFMaker(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Receipt', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_item(self, item):
        self.set_font('Arial', '', 10)
        self.cell(0, 10, f"Name: {item['name'][:48]}", 0, 1)
        self.cell(0, 10, f"ID: {str(item['id'])[:48]}", 0, 1)
        self.cell(0, 10, f"Value: ${item['value']}", 0, 1)
        self.cell(0, 10, f"Stock Quantity: {item['stock_quantity']}", 0, 1)
        self.cell(0, 10, f"Category: {item['category'][:48]}", 0, 1)
        self.ln(10)

def create_receipt(items, output_path):
    pdf = PDFMaker('P', 'mm', (80, 200))  # Adjust page size for POS printer
    pdf.add_page()
    for item in items:
        pdf.add_item(item)
    pdf.output(output_path)

def load_items_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

items = load_items_from_json('data/user_data.json')
create_receipt(items, 'receipt.pdf')

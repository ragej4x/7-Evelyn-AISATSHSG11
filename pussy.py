import win32print
import textwrap
import PyPDF2

class PosSys():
    def __init__(self, pdf_path):
        self.printer_name = "POS-58"
        self.pdf_path = pdf_path
        self.text_to_print = self.extract_text_from_pdf()

    def extract_text_from_pdf(self):
        text = ""
        try:
            with open(self.pdf_path, "rb") as file:
                reader = PyPDF2.PdfFileReader(file)
                for page_num in range(reader.numPages):
                    page = reader.getPage(page_num)
                    text += page.extract_text()
        except Exception as e:
            print(f"Error reading PDF: {e}")
        return text

    def print_receipt(self):
        # wrapper lngto
        wrapped_text = textwrap.fill(self.text_to_print, width=32, break_long_words=False)

        try:
            printer = win32print.OpenPrinter(self.printer_name)
            win32print.StartDocPrinter(printer, 1, ("Receipt", None, "RAW"))
            win32print.StartPagePrinter(printer)

            win32print.WritePrinter(printer, b'\x1B\x40')  
            win32print.WritePrinter(printer, b'\x1B\x21\x00')  
            win32print.WritePrinter(printer, b'\x1B\x61\x00')  

            win32print.WritePrinter(printer, wrapped_text.encode("utf-8"))

            win32print.WritePrinter(printer, b'\x1B\x21\x00')  
            win32print.WritePrinter(printer, b'\x1B\x61\x00')  

            win32print.WritePrinter(printer, b'\n')
            win32print.WritePrinter(printer, b'\x1D\x56\x00') 

            win32print.EndPagePrinter(printer)
            win32print.EndDocPrinter(printer)
            win32print.ClosePrinter(printer)
            print("Receipt printed successfully!")
        except Exception as e:
            print(f"Error: {e}")

pdf_path = "test.pdf"
pos_sys = PosSys(pdf_path)
pos_sys.print_receipt()
from pypdf import PdfReader,PdfWriter

path="Pdf/Inventor2022ObjectModel.pdf"
reader = PdfReader(path)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)
writer.add_blank_page() #https://pypdf.readthedocs.io/en/latest/modules/PdfWriter.html
writer.add_blank_page(width=100,height=100) #https://pypdf.readthedocs.io/en/latest/modules/PdfWriter.html
# Make a black rectangle in the bottom-left corner with the link
for count,page in enumerate(writer.pages):
    try:

        writer.add_uri(
            pagenum=count-1,
            uri="https://www.google.de/",
            rect=(10, 10, 100, 50)
        )
    except:
        print("fail")

with open("Pdf/out.pdf", "wb") as fp:
    writer.write(fp)
from spire.pdf.common import *
from spire.pdf import *

# Create a pdf document
pdf = PdfDocument()

# Add a page to the PDF
page = pdf.Pages.Add()

# Specify title text and paragraph content
titleText = "Probando spire.PDF"
paraText = """Spire.PDF for Python is a professional PDF development component that enables developers
						to create, read, edit, convert, and save PDF files in Python programs without depending on any external
						applications or libraries. This Python PDF class library provides developers with various functions to
						create PDF files from scratch or process existing PDF documents completely through Python programs."""

# Create solid brushes
titleBrush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
paraBrush = PdfSolidBrush(PdfRGBColor(Color.get_Black()))

# Create fonts
titleFont = PdfFont(PdfFontFamily.Helvetica, 14.0, PdfFontStyle.Bold)
paraFont = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)

# Set the text alignment
textAlignment = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)

# Draw title on the page
page.Canvas.DrawString(titleText, titleFont, titleBrush, page.Canvas.ClientSize.Width / 2, 40.0, textAlignment)

# Create a PdfTextWidget object to hold the paragraph content
textWidget = PdfTextWidget(paraText, paraFont, paraBrush)

# Create a rectangle where the paragraph content will be placed
rect = RectangleF(PointF(0.0, 50.0), page.Canvas.ClientSize)

# Set the text layout
textLayout = PdfTextLayout()
textLayout.Layout = PdfLayoutType.Paginate

# Draw the widget on the page
textWidget.Draw(page, rect, textLayout)

# Load an image
# image = PdfImage.FromFile("Python.png")

# Draw the image at a specified location on the page
 # page.Canvas.DrawImage(image, 12.0, 130.0)

#Save the PDF document
pdf.SaveToFile("CreatePDF.pdf")
pdf.Close()
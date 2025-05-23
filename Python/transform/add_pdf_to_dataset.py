from transforms.api import Output, transform
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


@transform(
     file_output=Output("/Training Environment-574ad4/[Training] Sandbox Folders/KKokot/JacobsComApi/testNoSchema1")
)
def save_pdf_file(ctx, file_output):
    pdf_bytes = create_pdf_document()
    output_file_path_hash = "document.pdf"
    with file_output.filesystem().open(output_file_path_hash, "wb") as out_f:
        out_f.write(pdf_bytes)

def create_pdf_document():
    """
    Create a PDF document and return its bytes
    """
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer)
    
    # Define the text content
    text_content = "This is a custom test PDF generated for Palantir Foundry MediaSet integration."
    
    # Add more content to make it more realistic
    c.drawString(100, 750, text_content)
    c.drawString(100, 710, "Document ID: PDF-001")
    c.drawString(100, 690, "Purpose: Foundry MediaSet Testing")
    
    # Add a title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 780, "Foundry Integration Test Document")
    
    # Save the PDF
    c.save()
    
    # Get the PDF bytes
    pdf_bytes = pdf_buffer.getvalue()
    pdf_buffer.close()
    
    return pdf_bytes
import json
from pyspark.sql import types as T
from transforms.api import Output, transform
from jacobsComAPI.utils.static_data import raw_json_project, raw_json_newsroom
from jacobsComAPI.utils.extract_content import extract_cleaned_content
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from transforms.mediasets import MediaSetOutput
import io

# This MediaSet need to be created in the Foundry UI first
@transform(output=MediaSetOutput("/Training Environment-574ad4/[Training] Sandbox Folders/KKokot/JacobsComApi/test"))

def write_pdf_to_mediaset(ctx, output):
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer)
    text_content = "This is a custom test PDF generated for Palantir Foundry MediaSet integration."
    c.drawString(100, 750, text_content)
    c.save()
    
    pdf_bytes = pdf_buffer.getvalue()
    
    output.put_media_item(pdf_bytes, "custom_test.pdf")
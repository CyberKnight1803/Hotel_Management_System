from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

def renderPDF(template_path, context, outputfile):
    template = get_template(template_path)
    html  = template.render(context)
    pdf = open(outputfile, "w+b")
    pisa.CreatePDF(html, dest=pdf)
    pdf.close()
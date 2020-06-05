from django.views.generic.base import TemplateView, View
from .tables import ProfileTable
from django.views.generic import FormView
from user.models import GraduateProfile, GraduateFolder
from user.forms import AccurateFolderForm
from django_tables2 import SingleTableView
from django.http import FileResponse, Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import AccurateDocs
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.pdfbase.pdfmetrics import stringWidth
import locale
from datetime import datetime


# services view that list graduates
class TableView(SingleTableView):
	template_name = "services/home.html"
	model = GraduateProfile
	
	table_class = ProfileTable
	table_pagination = {
		"per_page": 15
	}

# view for approve documents of graduate 
class ApproveView(FormView):
	graduate = None
	form_class = AccurateDocs
	template_name = "services/approve-documents.html"
	def get_initial(self):

		initial = super(FormView, self).get_initial()
		try:
			if self.request.method == 'Get':

				# set initial value to checklist documents
				folder = GraduateFolder.objects.get(folder_id=graduate.folder_id)
				initial['birth_certificate'] = folder.birth_certificate
				initial['curp'] = folder.curp
				initial['degree_certificate'] = folder.degree_certificate
				initial['hschool_certificate'] = folder.hschool_certificate
				print(initial)
		except:
			print("error")
		
		return initial
		
	def form_valid(self, form):
		global graduate
		print(form.cleaned_data['birth_certificate'])
		return redirect(reverse_lazy('adminHome'))

	def get_context_data(self, **kwargs):
		# set gradualeprofile to context
		global graduate
		graduate = GraduateProfile.objects.get(enrollment=self.kwargs['id'])
		context = super(ApproveView, self).get_context_data(**kwargs)
		context['graduate'] = graduate
		context['form'] = self.form_class
		
		return context

class SetApprove(View):
	form_class = AccurateFolderForm
	def form_valid():
		print("ha entrado en el post")

def some_view(request, id):
    graduate = GraduateProfile.objects.get(enrollment=id)
    locale.setlocale(locale.LC_TIME, 'es-ES')
    dt = datetime.now()
    date = 'Ensenada, Baja California a '+dt.strftime("%d de %B de %Y ")

    # 
    w, h = A4 
    print(str(w)+'        '+str(h))
    
    logo = 'static/icons/logo.png'
    im = Image(logo, 2*inch, 2*inch)

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    # vectors
    x = 55 
    y = h- 110

    p.rect(55, h- 110, 485.2755905511812, 66)
    #p.line(x, y+49.5, x+485.2755905511812, y+49.5)
    p.line(x+319, y+33, x+485.2755905511812, y+33)
    p.line(x+89, y+16.5, x+485.2755905511812, y+16.5)
  
    p.line(x+89, y, x+89, y+66)
    p.setFont("Helvetica", 11) #choose your font type and font size
    p.drawString(x+92,  y+4, "Referencia a la Norma ISO 9001:2015   8.5.1")

    p.line(x+319, y, x+319, y+66)
    p.drawString(x+322,  y+4, "Página 1 de 2")

    p.drawString(x+92,   y+20.5, "Protocolario para la Titulación Integral ")
    p.drawString(x+322,  y+20.5, "Revisión: O ")

    p.drawString(x+92,   y+37, "Constancia de NO Inconveniencia para Acto ")

    p.drawString(x+322,  y+53.5, "Código: ITE-AC-PO-006-02")
    p.drawString(x+92,   y+53.4, "Nombre del documento:     Formato     de")
    
    p.drawImage("static/icons/logo.png", x+15, y+4, width=60, height=60)
    


    center = 297.6377952755906
    yh = 40
    text = 'CONSTANCIA DE NO INCONVENIENCIA PARA EL ACTO PROTOCOLARIO PARA LA'
    wtext = stringWidth(text, 'Helvetica', 11)
    p.drawString(center-(wtext/2),  y-yh, text)
    yh = yh + 15
    text = 'TITULACIÓN INTEGRAL.'
    wtext = stringWidth(text, 'Helvetica', 11)
    p.drawString(center-(wtext/2),  y-yh, text)

    yh = yh + 70
    wtext = stringWidth(date, 'Helvetica', 11)
    p.drawString(540.2755905511812-wtext,  y-yh, date)



    yh = yh+65
    p.drawString(x,  y-yh, 'C. '+graduate.first_name+' '+graduate.last_name)


    yh = yh+50
    text = 'Me permito informarle de acuerdo a su solicitud, que no existe inconveniente para que pueda UD.'
    wtext = stringWidth(text, 'Helvetica', 11)
    p.drawString(center-(wtext/2),  y-yh, text)
    yh = yh+25
    p.drawString(center-(wtext/2), y-yh, 'presentar su Acto Protocolario para la Titulación Integral, ya que su expediente quedó integrado')
    yh = yh+25
    p.drawString(center-(wtext/2), y-yh, 'para tal efecto.')

    yh= yh+100
    text = 'A T E N T A M E N T E'
    wtext = stringWidth(text, 'Helvetica', 11)
    p.drawString(center-(wtext/2),  y-yh, text)

    yh= yh+90
    text= 'JEFE (A) DEL DEPARTAMENTO DE SERVICIOS ESCOLARES'
    wtext = stringWidth(text, 'Helvetica', 11)
    p.drawString(center-(wtext/2),  y-yh, text)

    yh= yh+50
    text = 'c.c.p- División de Estudios Profesionales'
    wtext = stringWidth(text, 'Helvetica', 11)
    p.drawString(x,  y-yh, text)
    yh= yh+30
    text = 'c.c.p- Archivo'
    wtext = stringWidth(text, 'Helvetica', 11)
    p.drawString(x,  y-yh, text)

    p.setFont("Helvetica", 9) #choose your font type and font size
    yh= yh+200
    text = 'ITE-AC-PO-006-02 Toda copia en PAPEL es un "Documento No Controlado" a excepción del original Rev. O'
    wtext = stringWidth(text, 'Helvetica', 9)
    p.drawString(center-(wtext/2),  40, text)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=str(id)+'-carta-no-inconveniencia.pdf')
def stringWidth2(string, font, size, charspace):
		width = stringWidth(string, font, size)
		width += (len(string) - 1) * charspace
		return width
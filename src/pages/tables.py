import django_tables2 as tables
from user.models import GraduateProfile

class ProfileTable(tables.Table):
	enrollment = tables.Column(verbose_name= 'Matrícula', attrs={"th": {"id": "enrollment"}})
	first_name = tables.Column(verbose_name= 'Nombre(s)')
	last_name = tables.Column(verbose_name= 'Apellido(s)')
	career = tables.Column(verbose_name= 'Carrera')
	gender = tables.Column(verbose_name= 'Género')
	type_degree = tables.Column(verbose_name= 'Titulación')
	status = tables.Column(verbose_name= 'Estatus')
	class Meta:
		model= GraduateProfile
		#sequence = ("id", "patient","status")
		attrs = {
			'class'	:	'table table-hover'
		}
		exclude = ('account','folder', 'accurate_docs')
		row_attrs = {
			"id": lambda record: record.pk,
			'class' :"row-custom"
		}

		

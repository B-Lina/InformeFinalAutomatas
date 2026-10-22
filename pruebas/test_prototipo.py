from automatas.validador import validar
from grafos.dependencias import evaluar,construir_grafo
from ia.clasificador import clasificar
from ia.extractor import campos
from motor import procesar

def texto(tipo,numero='12345678'):
 encabezado={'identidad':'cedula de ciudadania documento de identidad',
 'registro':'formulario de registro inscripcion',
 'academico':'certificado academico estudios universidad',
 'antecedentes':'certificado de antecedentes judiciales policia'}[tipo]
 return f'{encabezado}\nNombre: Ana Prueba\nDocumento: {numero}\nFecha: 2026-10-22'

def test_clasificador():
 for t in ('identidad','registro','academico','antecedentes'):
  assert clasificar(texto(t))['tipo']==t

def test_campos(): assert campos(texto('identidad'))['documento']=='12345678'
def test_afd_completo(): assert validar('identidad',campos(texto('identidad')))['estado']=='aprobado'
def test_afd_incompleto(): assert validar('identidad',{'nombre':'Ana'})['estado']=='observado'
def test_afd_desconocido(): assert validar('otro',{})['estado']=='rechazado'
def test_grafo(): assert construir_grafo().number_of_edges()==3
def test_expediente_completo():
 r=procesar({t+'.pdf':texto(t) for t in ('identidad','registro','academico','antecedentes')})
 assert r['expediente']['estado']=='aprobado'
def test_faltante():
 r=procesar({t+'.pdf':texto(t) for t in ('identidad','registro','academico')})
 assert r['expediente']['estado']=='observado'
def test_inconsistencia():
 r=procesar({t+'.pdf':texto(t,'99999999' if t=='registro' else '12345678') for t in ('identidad','registro','academico','antecedentes')})
 assert r['expediente']['estado']=='rechazado'
def test_sin_archivos(): assert procesar({})['expediente']['estado']=='observado'

import streamlit as st
from ia.extractor import extraer_pdf
from motor import procesar
st.set_page_config(page_title='SIVID-IA',page_icon='📄')
st.title('SIVID-IA · Prototipo académico')
st.caption('Documentos simulados. No subir datos personales reales.')
archivos=st.file_uploader('Cargar PDF digitales',type=['pdf'],accept_multiple_files=True)
if st.button('Validar expediente'):
 if not archivos: st.warning('Cargue al menos un PDF.')
 else:
  textos={}
  for archivo in archivos:
   try:
    contenido=extraer_pdf(archivo.getvalue())
    if not contenido: st.warning(f'{archivo.name}: PDF sin texto; OCR no incluido en el MVP')
    else: textos[archivo.name]=contenido
   except Exception as e: st.error(f'No se pudo leer {archivo.name}: {type(e).__name__}')
  if textos:
   resultado=procesar(textos)
   st.subheader('Estado: '+resultado['expediente']['estado'].upper())
   for motivo in resultado['expediente']['motivos']: st.write('• '+motivo)
   st.json(resultado['documentos'])

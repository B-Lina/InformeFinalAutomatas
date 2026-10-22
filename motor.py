"""Orquestación del prototipo sin persistir información personal."""
from ia.clasificador import clasificar
from ia.extractor import campos
from automatas.validador import validar
from grafos.dependencias import evaluar

def procesar(textos):
 documentos={};avisos=[]
 for nombre,texto in textos.items():
  clase=clasificar(texto);tipo=clase['tipo']
  if tipo=='desconocido': avisos.append(nombre+': tipo no identificado');continue
  if tipo in documentos: avisos.append(nombre+': tipo duplicado '+tipo);continue
  c=campos(texto);documentos[tipo]={'archivo':nombre,'confianza':clase['confianza'],'campos':c,'validacion':validar(tipo,c)}
 resultado=evaluar(documentos)
 if avisos:
  resultado['motivos'].extend(avisos)
  if resultado['estado']=='aprobado': resultado['estado']='observado'
 return {'documentos':documentos,'expediente':resultado}

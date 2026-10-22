"""Extrae texto de PDF digital y campos de documentos simulados."""
import re
import fitz

def extraer_pdf(datos):
 with fitz.open(stream=datos,filetype='pdf') as pdf:
  return '\n'.join(p.get_text() for p in pdf).strip()

def campos(texto):
 def buscar(patron):
  m=re.search(patron,texto,re.I|re.M)
  return m.group(1).strip() if m else None
 return {'documento':buscar(r'^\s*(?:documento|identificaci[oó]n|c[eé]dula)\s*:\s*([0-9]{5,15})\s*$'),
         'nombre':buscar(r'^\s*nombre\s*:\s*([^\n]+)$'),
         'fecha':buscar(r'^\s*fecha\s*:\s*(\d{4}-\d{2}-\d{2})\s*$')}

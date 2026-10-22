# SIVID-IA · Prototipo académico

## Instalación
Desde esta carpeta: `python -m pip install -r requirements.txt`.

## Ejecución
- Pruebas: `python -m pytest pruebas -q`
- Interfaz: `streamlit run app.py`


## Alcance
Cuatro clases documentales; 
PDF digital con texto; 
campos simulados `Nombre:` y `Documento:`; 
Reglas formales, grafo de dependencias y clasificación TF-IDF + Naive Bayes. 
No verifica autenticidad oficial ni firma electrónica. Los textos de entrenamiento son sintéticos y el rendimiento no está validado en producción. No utilizar documentos personales reales.

## Convenciones
`q0` estado inicial; 
entrada `C` = completo, 
`F` = faltante, 
`I` = inconsistencia; 
estados finales `qA`, `qO`, `qR`. 

El AFD modela una decisión simplificada sobre un símbolo de resultado de reglas, no el procesamiento de OCR. Las discrepancias entre documentos se evalúan por el grafo.

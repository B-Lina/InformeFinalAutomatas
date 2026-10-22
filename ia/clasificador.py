"""Clasificador didáctico: entrenamiento exclusivamente con frases sintéticas."""
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
ETIQUETAS = ['identidad','registro','academico','antecedentes']
EJEMPLOS = {
 'identidad':['documento de identidad numero nombre apellidos fecha expedicion','cedula de ciudadania numero identificacion nombres apellidos','tarjeta de identidad datos personales numero de documento','identificacion personal cedula nombres apellidos'],
 'registro':['formulario de registro nombre documento correo','solicitud de inscripcion formulario datos personales','formato de registro numero de identidad correo','registro de aspirante nombre documento firma'],
 'academico':['certificado academico estudios institucion programa','constancia de estudios universidad calificaciones','certificacion academica nivel de estudios titulo','certificado de notas institucion educativa'],
 'antecedentes':['certificado de antecedentes disciplinarios identificacion','consulta de antecedentes judiciales numero documento','constancia antecedentes procuraduria nombre','certificado de antecedentes policia consulta']}
def modelo():
 x,y=[],[]
 for k,frases in EJEMPLOS.items():
  for f in frases: x.append(f);y.append(k)
 m=Pipeline([('vector',TfidfVectorizer(ngram_range=(1,2),strip_accents='unicode')),('nb',MultinomialNB())]);m.fit(x,y);return m
_MODELO=None
def clasificar(texto):
 global _MODELO
 if _MODELO is None: _MODELO=modelo()
 probabilidades=_MODELO.predict_proba([texto[:5000]])[0]
 i=probabilidades.argmax();etiqueta=_MODELO.classes_[i];confianza=float(probabilidades[i])
 return {'tipo':etiqueta if confianza>=0.32 else 'desconocido','confianza':round(confianza,3)}

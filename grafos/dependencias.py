"""Grafo dirigido de relaciones documentales y consolidación del expediente."""
import networkx as nx
TIPOS=('identidad','registro','academico','antecedentes')

def construir_grafo():
 g=nx.DiGraph();g.add_nodes_from(TIPOS)
 g.add_edge('identidad','registro',regla='coincidencia del numero de documento')
 g.add_edge('identidad','academico',regla='coincidencia del numero de documento')
 g.add_edge('identidad','antecedentes',regla='coincidencia del numero de documento')
 return g

def evaluar(documentos):
 """documentos: diccionario tipo -> {'campos':{},'validacion':{}}."""
 g=construir_grafo();motivos=[]
 faltantes=[t for t in TIPOS if t not in documentos]
 if faltantes: motivos.append('Documentos ausentes: '+', '.join(faltantes))
 for t,datos in documentos.items():
  estado=datos['validacion']['estado']
  if estado!='aprobado': motivos.append(t+': '+estado)
 for origen,destino in g.edges():
  if origen in documentos and destino in documentos:
   a=documentos[origen]['campos'].get('documento')
   b=documentos[destino]['campos'].get('documento')
   if a and b and a!=b: motivos.append('Inconsistencia de identificación: '+origen+' / '+destino)
 if any('Inconsistencia' in m for m in motivos) or any(d['validacion']['estado']=='rechazado' for d in documentos.values()): estado='rechazado'
 elif motivos: estado='observado'
 else: estado='aprobado'
 return {'estado':estado,'motivos':motivos,'nodos':list(g.nodes()),'aristas':list(g.edges())}

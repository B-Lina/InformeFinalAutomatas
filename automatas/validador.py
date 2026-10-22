"""Equivalente ejecutable del AFD modelado en JFLAP.
Alfabeto: C=campos completos, F=campos faltantes, I=inconsistencia.
"""
TRANSICIONES={('q0','C'):'qA',('q0','F'):'qO',('q0','I'):'qR'}

def validar(tipo,campos):
 if tipo not in ('identidad','registro','academico','antecedentes'):
  return {'estado':'rechazado','simbolo':'I','estado_afd':'qR','motivos':['Tipo documental no reconocido']}
 requeridos={'identidad':['documento','nombre'],'registro':['documento','nombre'],
             'academico':['documento','nombre'],'antecedentes':['documento','nombre']}
 faltantes=[k for k in requeridos[tipo] if not campos.get(k)]
 simbolo='F' if faltantes else 'C'
 final=TRANSICIONES[('q0',simbolo)]
 return {'estado':{'qA':'aprobado','qO':'observado','qR':'rechazado'}[final],
         'simbolo':simbolo,'estado_afd':final,
         'motivos':['Faltan campos: '+', '.join(faltantes)] if faltantes else []}

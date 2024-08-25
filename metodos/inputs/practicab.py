#caso a
cpmin= 2.5
cpprom= 4
cpmax= 7
cdalto= 1.5

daltvsrap= (cdalto/cpmin-1)*100
daltvslent= round((cdalto/cpmax-1)*100,3)
daltvsprom= round((cdalto/cpprom-1)*100,3)
#caso b
crudotros= 5
cruddalto= 3.5
crud_reducid_otros= round((cpprom/crudotros-1)*100, 3)
crud_reducid_dalto= round((cdalto/cruddalto-1)*100, 3)
#caso c: ver 10 h de este curso seria equivalente a ver 
#cuantas h de otros cursos?
var_min= cpmin/cdalto
var_prom= cpprom/cdalto
var_max= cpmax/cdalto
diesvsmin=10*var_min
diesvsprom= round(10*var_prom, 3)
diesvsmax= 10*var_max

print(f"El curso de Dalto dura un {daltvsrap}% menos que el más rápido")
print(f"El curso de Dalto dura un {daltvsprom}% menos que el promedio")
print(f"El curso de Dalto dura un {daltvslent}% menos que el más lento")
print(f"el curso promedio optimiza un {crud_reducid_otros}% del tiempo al editar")
print(f"el curso de Dalto optimiza un {crud_reducid_dalto}% del tiempo al editar")
print(f"Ver 10h de este curso equivale a ver {diesvsprom}h de otros cursos")
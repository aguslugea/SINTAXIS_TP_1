ESTADO_TRAMPA  =  "TRAMPA"

ESTADO_FINAL  =  "ACEPTADO"

ESTADO_NO_FINAL  =  "NO ACEPTADO"
                                    #VT = {=, para, desde, hasta, {, }, id, cte, *, +, (, ), si, entonces, sino, mostrar, aceptar, ;}
def  autómatas_para ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 4 ]

    para  caracter  en  cadena :
        
        si  estado_actual  ==  0  y  caracter  ==  "p" :
                estado_actual  =  1
        elif  estado_actual  ==  1  y  caracter  ==  "a" :
                estado_actual  =  2
        elif  estado_actual  ==  2  y  caracter  ==  "r" :
                estado_actual  =  3
        elif  estado_actual  ==  3  y  caracter  ==  "a" :
                estado_actual  =  4
        más :
                estado_actual  =  - 1
                descanso
    

    si  estado_actual  ==  - 1 :
        volver  ESTADO_TRAMPA
    si  estado_actual  en  estados_finales :
        volver  ESTADO_FINAL
    más :
        devolver  ESTADO_NO_FINAL
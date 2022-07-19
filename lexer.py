ESTADO_TRAMPA  =  "TRAMPA"

ESTADO_FINAL  =  "ACEPTADO"

ESTADO_NO_FINAL  =  "NO ACEPTADO"
                                    #VT = {=, para, desde, hasta, {, }, id, cte, *, +, (, ), si, entonces, sino, mostrar, aceptar, ;}
def  automatas_para ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 4 ]

    para  caracter  en  cadena :
        
        if  estado_actual  ==  0  y  caracter  ==  "p" :
                estado_actual  =  1
        elif  estado_actual  ==  1  y  caracter  ==  "a" :
                estado_actual  =  2
        elif  estado_actual  ==  2  y  caracter  ==  "r" :
                estado_actual  =  3
        elif  estado_actual  ==  3  y  caracter  ==  "a" :
                estado_actual  =  4
        else :
                estado_actual  =  - 1
                break
    

    if  estado_actual  ==  - 1 :
        volver  ESTADO_TRAMPA
    if  estado_actual  en  estados_finales :
        volver  ESTADO_FINAL
    else :
        print  ESTADO_NO_FINAL

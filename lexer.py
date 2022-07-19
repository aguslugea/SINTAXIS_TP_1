ESTADO_TRAMPA  =  "TRAMPA"

ESTADO_FINAL  =  "ACEPTADO"

ESTADO_NO_FINAL  =  "NO ACEPTADO"
        
        #VT = {=, para, desde, hasta, {, }, id, cte, *, +, (, ), si, entonces, sino, mostrar, aceptar, ;}
def  automatas_para ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 4 ]

    for  caracter  in  cadena :
        
        if  estado_actual  ==  0  and  caracter  ==  "p" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "a" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "r" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "a" :
                estado_actual  =  4
        else :
                estado_actual  =  - 1
                break
    

    if  estado_actual  ==  - 1 :
        print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)


def  automatas_desde ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 5 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "d" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "e" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "s" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "d" :
                estado_actual  =  4
        elif  estado_actual  ==  4  and  caracter  ==  "e" :
                estado_actual  =  5

        else :
                estado_actual  =  - 1
                break

    if  estado_actual  ==  - 1 :
        print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)
     

def  automatas_hasta ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 5 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "h" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "a" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "s" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "t" :
                estado_actual  =  4
        elif  estado_actual  ==  4  and  caracter  ==  "a" :
                estado_actual  =  5

        else :
                estado_actual  =  - 1
                break

    if  estado_actual  ==  - 1 :
        print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)
 

def  automatas_si ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 2 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "s" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "i" :
                estado_actual  =  2


        else :
                estado_actual  =  - 1
                break

    if  estado_actual  ==  - 1 :
        print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)

def  automatas_entonces ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 8 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0 and  caracter  ==  "e" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "n" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "t" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "o" :
                estado_actual  =  4
        elif  estado_actual  ==  4  and  caracter  ==  "n" :
                estado_actual  =  5
        elif  estado_actual  ==  5  and  caracter  ==  "c" :
                estado_actual  =  6
        elif  estado_actual  ==  6  and  caracter  ==  "e" :
                estado_actual  =  7
        elif  estado_actual  ==  7  and  caracter  ==  "s" :
                estado_actual  =  8

        else :
                estado_actual  =  - 1
                break

    if  estado_actual  ==  - 1 :
        print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)

def  automatas_entonces ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 4 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "s" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "i" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "n" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and caracter  ==  "o" :
                estado_actual  =  4

        else :
                estado_actual  =  - 1
                break


        if  estado_actual  ==  - 1 :
                print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)

def  autómatas_mostrar ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 7 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "m" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "o" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "s" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "t" :
                estado_actual  =  4
        elif  estado_actual  ==  4  and  caracter  ==  "r" :
                estado_actual  =  5
        elif  estado_actual  ==  5  and caracter  ==  "a" :
                estado_actual  =  6
        elif  estado_actual  ==  6  and  caracter  ==  "r" :
                estado_actual  =  7

        else :
                estado_actual  =  - 1
                break

    if  estado_actual  ==  - 1 :
                print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)

def  autómatas_mostrar ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 7 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "a" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "c" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "e" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "p" :
                estado_actual  =  4
        elif  estado_actual  ==  4  and  caracter  ==  "t" :
                estado_actual  =  5
        elif  estado_actual  ==  5  and  caracter  ==  "a" :
                estado_actual  =  6
        elif  estado_actual  ==  6  and  caracter  ==  "r" :
                estado_actual  =  7

        else :
                estado_actual  =  - 1
                break

    if  estado_actual  ==  - 1 :
                print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)

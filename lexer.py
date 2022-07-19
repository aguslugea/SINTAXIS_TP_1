ESTADO_TRAMPA  =  "TRAMPA"

ESTADO_FINAL  =  "ACEPTADO"

ESTADO_NO_FINAL  =  "NO ACEPTADO"
        
        #DEFINIMOS CADA VT 
        #VT = {eq, id, num, *, +, op, clp, si, entonces, sino, mostrar, aceptar, mientras, esMenorQue, hacer, (, )}


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

def  automatas_sino ( cadena ):

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

def  autómatas_aceptar ( cadena ):

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

def  autómatas_mientras ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 7 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "m" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "i" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "e" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "n" :
                estado_actual  =  4
        elif  estado_actual  ==  4  and  caracter  ==  "t" :
                estado_actual  =  5
        elif  estado_actual  ==  5  and  caracter  ==  "r" :
                estado_actual  =  6
        elif  estado_actual  ==  6  and  caracter  ==  "a" :
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

def  autómatas_esMenorQue ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 7 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "e" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "s" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "M" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "e" :
                estado_actual  =  4
        elif  estado_actual  ==  4  and  caracter  ==  "n" :
                estado_actual  =  5
        elif  estado_actual  ==  5  and  caracter  ==  "o" :
                estado_actual  =  6
        elif  estado_actual  ==  6  and  caracter  ==  "r" :
                estado_actual  =  7
        elif  estado_actual  ==  7  and  caracter  ==  "Q" :
                estado_actual  =  8
        elif  estado_actual  ==  8  and  caracter  ==  "u" :
                estado_actual  =  9
        elif  estado_actual  ==  9  and  caracter  ==  "e" :
                estado_actual  =  10


        else :
                estado_actual  =  - 1
                break

    if  estado_actual  ==  - 1 :
                print  (ESTADO_TRAMPA)
    if  estado_actual  in estados_finales :
        print   (ESTADO_FINAL)
    else :
        print  (ESTADO_NO_FINAL)

def  autómatas_esMenorQue ( cadena ):

    estado_actual  =  0
    estados_finales  = [ 7 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  ==  "h" :
                estado_actual  =  1
        elif  estado_actual  ==  1  and  caracter  ==  "a" :
                estado_actual  =  2
        elif  estado_actual  ==  2  and  caracter  ==  "c" :
                estado_actual  =  3
        elif  estado_actual  ==  3  and  caracter  ==  "e" :
                estado_actual  =  4
        elif  estado_actual  ==  4  and  caracter  ==  "r" :
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

def  autómatas_simbolos ( cadena ):
    simbolos  = [ "*" , "+" ]

    estado_actual  =  0
    estados_finales  = [ 1 ]

    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  in  simbolos :
            estado_actual  =  1
        else :
                estado_actual  =  - 1
                break

    if  estado_actual  ==  - 1 :
                   print  (ESTADO_TRAMPA)
    if  estado_actual  in  estados_finales :
                   print  (ESTADO_FINAL)
    else :
                  print  (ESTADO_NO_FINAL)

def  autómatas_abrir_parentesis ( cadena ):
    simbolos  = [ "(" ]

    estado_actual  =  0
    estados_finales  = [ 1 ]
    
    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  in  simbolos :
            estado_actual  =  1
        else :
                estado_actual  =  - 1
                break

                
    if  estado_actual  ==  - 1 :
                print  (ESTADO_TRAMPA)
    if  estado_actual  in  estados_finales :
                print  (ESTADO_FINAL)
    else :
                print  (ESTADO_NO_FINAL)

def  autómatas_cerrar_parentesis ( cadena ):
    simbolos  = [ ")" ]

    estado_actual  =  0
    estados_finales  = [ 1 ]
    
    for  caracter  in  cadena :
        if  estado_actual  ==  0  and  caracter  in  simbolos :
            estado_actual  =  1
        else :
                estado_actual  =  - 1
                break

                
    if  estado_actual  ==  - 1 :
                print  (ESTADO_TRAMPA)
    if  estado_actual  in  estados_finales :
                print  (ESTADO_FINAL)
    else :
                print  (ESTADO_NO_FINAL)
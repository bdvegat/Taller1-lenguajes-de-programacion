# $ pip install graphviz

import graphviz

def draw(estados, estadosFinales,funcion):

    g = graphviz.Digraph(format='pdf')
    g.graph_attr['rankdir'] = 'LR'
    g.node("dot", shape="point")

    for i in range (0,estados):
        if str(i) in estadosFinales:
            g.node(str(i),shape="doublecircle")
        else:
            g.node(str(i))
    for i in funcion:
        g.edge(str(i[0]),str(i[1]),label=str(i[2]))
    g.edge("dot","0")
    g.render(view=True)


#objetos para leer archivos
alf = open('alfabeto.txt','r')
est = open('estados.txt','r')
estf = open('estadosFinales.txt','r')
fun = open('funcion.txt','r')
cad = open('cadena.txt','r')

#comprueba que la cadena no contenga simbolos que no pertenecen al alfabeto
def comprobarCadena(alfabeto=[], cadena=""):
    comp=False
    for i in cadena:
        comp=False
        if alfabeto.__contains__(i):
            comp=True
        if comp==False:
            break
    return comp

#organiza la funcion de transicion en tuplas: estado de salida, estado de llegada, simbolo
def organizarFuncion(estados, funcion,alfabeto=[]):
    funcTupl=[]
    for i in range (1,estados+1):
        for j in range (1,len(alfabeto)+1):
            funcTupl.append([i-1,funcion[i][j],alfabeto[j-1]])
    return funcTupl

#devuelve el estado en el que termina una cadena, en caso de no estar definido devuleve -1
def afd (estados, estadosFinales, funcion, cadena):
    estado=0
    for i in cadena:
        for j in range(1,len(alfabeto)):
            if (i==funcion[0][j]):
                if int(funcion[estado+1][j])>=estados or int(funcion[estado+1][j])=="_":
                    estado=-1
                    break
                estado = int(funcion[estado+1][j])
                break
        if estado==-1:
            break
    return estado

#comprueba si el estado recibido es un estado final
def comprobarEstadoFinal(estado, estadosFinales=[]):
    estadosFinales=map(int,estadosFinales)
    if estadosFinales.__contains__(estado):
        return True
    else:
        return False



alfabeto = alf.read().strip().split()
estados = int(est.read().strip())
estadosFinales = estf.read().strip().split()
cadena = cad.read().strip()
funcion=[]
for i in range (0,estados+1):
    funcion.append(fun.readline().strip().split())
funcTup = organizarFuncion(estados,funcion,alfabeto)
est=afd(estados, estadosFinales, funcion, cadena)

if comprobarEstadoFinal(est,estadosFinales):
    print "la cadena fue aceptada, ", "el estado final fue ", est
else:
    print "la cadena no fue aceptada, ", "el ultimo estado fue ", est

draw(estados,estadosFinales,funcTup)
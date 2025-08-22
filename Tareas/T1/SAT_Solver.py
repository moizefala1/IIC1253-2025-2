from z3 import *
def SAT_Solver(n, celdas = False):
    solver = Solver()          
    # Definimos x[i][j][k] como una variable booleana
    x = [[[Bool(f"x_{i}_{j}_{k}") 
           for i in range(n)] 
           for j in range(n)] 
           for k in range(n)]

    #Restriccion 1: Cada casilla tiene al menos un numero
    for i in range(n):
        for j in range(n):
            solver.add(Or([x[i][j][k] for k in range(n)]))
            
    #Restriccion 2: Cada casilla tiene exactamente un numero
    for i in range(n):
        for j in range(n):
            for k in range(n-1):
                for m in range(k+1,n):
                    solver.add(Implies(x[i][j][k],Not(x[i][j][m])))
    #Restriccion 3: Cada elemento de la columna es distinto
    for i in range(n):
        for k in range (n):
            for j in range(n-1):
                for m in range(j+1,n):
                       solver.add(Implies(x[i][j][k],Not(x[i][m][k])))
    #Restriccion 4: Analogamente, cada fila debe tener numeros distintos
    for j in range(n):
        for k in range (n):
            for i in range(n-1):
                for m in range(i+1,n):
                       solver.add(Implies(x[i][j][k],Not(x[m][j][k])))
                       
    if celdas:
        for  celda in celdas:
            i = int(celda[0]-1)
            j = int(celda[1]-1)            
            k = int(celda[2]-1)
            solver.add(x[i][j][k] == True)
                       
    return solver, x

n = 4
celdas = [[1,1,2], [4,1,3], [3,2,4],[2,3,1], [3,4,3]] 

solver, variables = SAT_Solver(n, celdas)
if solver.check() == sat:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if solver.model().evaluate(variables[i][j][k]):
                    print(f"({i+1}, {j+1}) tiene el numero {k+1}")
    print("Satisfactible")
else:
    print("No satisfactible")
from z3 import *
def SAT_Solver(n):
    solver = Solver()          
    # Definimos x[i][j][k] como una variable booleana
    x = [[[Bool(f"x_{i}_{j}_{k}") 
           for k in range(n)] 
           for j in range(n)] 
           for i in range(n)]

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
    return solver, x

n = 4

solver, variables = SAT_Solver(n)
if solver.check() == sat:
    print(solver.model())
else:
    print("No satisfiable")
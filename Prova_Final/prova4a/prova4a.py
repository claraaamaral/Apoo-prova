
def turma_maior(lista):
    rcb_a = []
    rcb_b = []
    a = 0
    b = 0

    for i in range(len(lista)):
        if lista[1][0] == lista[i][0]:
            rcb_a = lista[i][0]
            a = a + 1
        else:
            rcb_b = lista[i][0]
            b = b + 1
    if a>b:
        return (rcb_a)
    else:
        return (rcb_b)

def turma(id_turma, lista):
    contador = 0
    for i in range(len(lista)):
        if id_turma == lista[i][0]:
            contador = contador + 1
    return(contador)

def alunos_por_turma(id_aluno, lista):
    resultado = []

    for i in range(len(lista)):
        if id_aluno == lista[i][1]:
            resultado.append([lista[i][0]])
    return(resultado)

def alunos_matriculados(id_turma, lista):
    resultado2 = []

    for i in range(len(lista)):
        if id_turma == lista[i][0]:
            resultado2.append([lista[i][1]])
    return(resultado2)

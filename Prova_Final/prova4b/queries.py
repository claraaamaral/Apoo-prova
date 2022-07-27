
from conexaoDB import *

def ler_todos_alunos(bd):
     return ler_bd(bd, "SELECT * FROM Aluno")

def ler_todas_Disciplinas(bd):
     return ler_bd(bd, "SELECT * FROM Disciplina")

def ler_aluno_nome(bd, nome):
    query = "SELECT * FROM Aluno WHERE nome = ?"  
    return ler_bd(bd, query, (nome,))

def ler_todos_alunos_por_curso(bd):
     return ler_bd(bd, "SELECT c.Nome, pp.Nome, pr.Nome FROM Matricula p LEFT JOIN Aluno c ON c.id = p.ID_Aluno LEFT JOIN Turma pp ON pp.ID= p.ID_Turma LEFT JOIN Disciplina pr ON pr.ID = pp.ID_Disciplina"
                    )

def ler_por_alunos_por_curso(bd, nome):
     query = "SELECT c.Nome, pp.Nome, pr.Nome FROM Matricula p LEFT JOIN Aluno c ON c.id = p.ID_Aluno LEFT JOIN Turma pp ON pp.ID= p.ID_Turma LEFT JOIN Disciplina pr ON pr.ID = pp.ID_Disciplina WHERE c.Nome = ?"
     return ler_bd(bd, query, (nome,))

def ler_por_turmas_por_curso(bd, nome):
     query = "SELECT c.Nome, pp.Nome, pr.Nome FROM Matricula p LEFT JOIN Aluno c ON c.id = p.ID_Aluno LEFT JOIN Turma pp ON pp.ID= p.ID_Turma LEFT JOIN Disciplina pr ON pr.ID = pp.ID_Disciplina where pr.Nome = ?"
     return ler_bd(bd, query, (nome,))


def ler_por_matricula_por_disciplina(bd, nome):
     query = "SELECT c.Nome Aluno, pp.Nome Turma, pr.Nome Disciplina FROM Matricula p LEFT JOIN Aluno c ON c.id = p.ID_Aluno LEFT JOIN Turma pp ON pp.ID= p.ID_Turma LEFT JOIN Disciplina pr ON pr.ID = pp.ID_Disciplina WHERE pr.Nome = ?"
     return ler_bd(bd, query, (nome,))     
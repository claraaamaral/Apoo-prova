from prova4a import *

import unittest




#FUNCIONALIDADES DO SISTEMA

#● Testes sem Banco de Dados

#1. Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
#[[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
#da função o id de uma turma (id_turma), indicar o número de alunos matriculados nela.

#2. Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
#[[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
#da função o id do aluno (id_aluno), indicar os ids das turmas nas quais ele está matriculado.

#3. Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
#[[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Indicar a turma com o maior
# número de alunos.

# 4. Receber uma lista com os alunos matriculados nas turmas da escola (id_turma, id_aluno)
# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]. Se for passado como parâmetro
# da função o id de uma turma (id_turma), indicar se todos os alunos estão matriculados nela.*/

class TestQuartaProva(unittest.TestCase):


    def test_turma(self):
        self.assertEqual(turma(1, ([(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)])), 3)


    def test_alunos_turma(self):
        self.assertEqual(alunos_por_turma(3, ([(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)])), [[1]])

    def test_turma_maior(self):
        self.assertEqual(turma_maior([(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)]), 1)

    def test_alunos_matriculados(self):
        self.assertEqual(alunos_matriculados(1, ([(1, 1), (1, 2), (1, 3), (2, 1), (2, 4)])), [[1], [2], [3]])
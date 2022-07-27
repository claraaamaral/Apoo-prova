from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from conexaoDB import *
from queries import *
class TestDB(MockBD):

#1. Listar o nome de todas as turmas que a aluna 'Carla' está matriculada     
     def test_filtro_nome_(self):
          retorno_esperado =  [('Carla', 'unidade 4' , 'Geografia'),
                              ('Carla',	'unidade 2', 'Geografia'),
                              ('Carla',	'unidade 3','Sociologia')]
          self.assertEqual(ler_por_alunos_por_curso(self.mock_db_config.get('bd'), 'Carla'), 
          retorno_esperado)

     def test_filtro_nome_(self):
          retorno_esperado =  [('Matheus','unidade 3', 'Sociologia')
                             ]
          self.assertEqual(ler_por_alunos_por_curso(self.mock_db_config.get('bd'), 'Matheus'), 
          retorno_esperado)

     def test_filtro_nome_(self):
          retorno_esperado =  [('Piedade', 'unidade 3', 'Sociologia')]
          self.assertEqual(ler_por_alunos_por_curso(self.mock_db_config.get('bd'), 'Piedade'), 
          retorno_esperado)



#2. Listar todos os alunos da escola          
     def test_select_all_matriculados(self):

          retorno_esperado = [('Das Dores',	'unidade 4','Geografia'),
                              ('Matheus','unidade 3',	'Sociologia'),
                              ('Muriely','unidade 1',	'Inglês'),
                              ('Cecilia','unidade 3',	'Sociologia'),
                              ('Piedade','unidade 3',	'Sociologia'),
                              ('Greici','unidade 1',	'Inglês'),
                              ('Carla',	'unidade 4',	'Geografia'),
                              ('Cecilia','unidade 2',	'Geografia'),
                              ('Das Dores','unidade 1','Inglês'),
                              ('Henry',	'unidade 1',	'Inglês'),
                              ('Carla',	'unidade 2',	'Geografia'),
                              ('Carla',	'unidade 3',	'Sociologia'),
                              ('Das Dores','unidade 3','Sociologia'),
                              ('Henry', 'unidade 3',	'Sociologia'),
                              ('Cecilia', 'unidade 4',	'Geografia'),
                              ('Cecilia','unidade 1',	'Inglês'),
                              ('Muriely','unidade 3',	'Sociologia')]
          self.assertEqual(ler_todos_alunos_por_curso(self.mock_db_config.get('bd')),
     retorno_esperado)



#3. Listar todas as turmas da disciplina 'Geografia'
     def test_filtro_turmas_curso(self):
          retorno_esperado =  [('Geografia', 'unidade 2'),
                              ('Geografia', 'unidade 4')]
          self.assertEqual(ler_por_turmas_por_curso(self.mock_db_config.get('bd'), 'Geografia'), 
          retorno_esperado)

#4. Listar todas as turmas da disciplina 'Geografia'
     def test_filtro_turmas_curso(self):
          retorno_esperado =  [('Das Dores',	'unidade 4','Geografia'),
                              ('Carla',	'unidade 4','Geografia'),
                              ('Cecilia','unidade 2','Geografia'),
                              ('Carla',	'unidade 2','Geografia'),
                              ('Cecilia','unidade 4','Geografia')]
          self.assertEqual(ler_por_turmas_por_curso(self.mock_db_config.get('bd'), 'Geografia'), 
          retorno_esperado)
          
          
     def test_select_all(self):

          retorno_esperado = [(1, 'Quimica'),
                              (2, 'Sociologia'),
                              (3, 'Inglês'),
                              (4, 'Geografia')]
          self.assertEqual(ler_todas_Disciplinas(self.mock_db_config.get('bd')),
     retorno_esperado)
          
from aluno import Aluno
from disciplina import Disciplina

# criar / instancair 1 aluno
aluno1 = Aluno("Enzo", "570035", "Ciência da Computação")

# criar 2 disciplinas
cs = Disciplina("Computer Science", "Lucas")
model_mat = Disciplina("Modelagem Matematica", "Christiam")

# matricular um aluno nas disciplinas
aluno1.matricular(cs)
aluno1.matricular(model_mat)

# adicionar notas do aluno referente a determinada disciplina
aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(cs, 8)
aluno1.adicionar_nota(model_mat, 5)
aluno1.adicionar_nota(model_mat, 4)

print(aluno1.calcular_media_geral())
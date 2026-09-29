from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Disciplina):
        """Adicionar a discipplina na lista de disciplinas do aluno"""
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        """Adiconar uma nota do aluno referente a uma disciplina"""
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def calcular_media_d(self, d: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(d.nome, [])
        if not notas:
            return 0
        return sum(notas) / len(notas)

    def calcular_media_geral(self) -> float:
        medias = []
        for d in self.disciplinas:
            media_d = self.calcular_media_d(d)
            medias.append(media_d)
        return sum(medias) / len(medias)


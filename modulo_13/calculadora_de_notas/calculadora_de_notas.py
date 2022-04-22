class Turma:
    def __init__(self):
        self._turma = []
        self._media = 0

    def get_media(self, turma):
        for aluno in turma:
            self._media += aluno[1]

        self._media //= len(turma)
        return self._media

    def get_maior_nota(self, turma):
        notas = []
        for aluno in turma:
            notas.append(aluno[1])
        notas.sort(reverse=True)
        return notas[0]

    def get_menor_nota(self, turma):
        notas = []
        for aluno in turma:
            notas.append(aluno[1])
        notas.sort()
        return notas[0]

    def get_aprovados(self, turma, media):
        aprovados = []
        for aluno in turma:
            if aluno[1] >= media:
                aprovados.append(aluno[0])
        return aprovados

    def get_reprovados(self, turma, media):
        reprovados = []
        for aluno in turma:
            if aluno[1] < media:
                reprovados.append(aluno[0])
        return reprovados

    def get_nota(self, nota):
        if nota == 10:
            return "A+"
        elif 9 <= nota < 10:
            return "A"
        elif 7 <= nota < 9:
            return "B"
        elif 5 <= nota < 7:
            return "C"
        elif 3 <= nota < 5:
            return "D"
        elif 1 <= nota < 3:
            return "E"
        elif 0 <= nota < 1:
            return "F"
        return nota

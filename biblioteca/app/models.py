from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=45)
    uf = models.CharField(max_length=5)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=45)
    site = models.CharField(max_length=80)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField(max_length=45)
    site = models.CharField(max_length=80)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=45)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    generos = models.ManyToManyField(Genero)
    preco = models.FloatField()
    data_publicacao = models.DateTimeField()

    def __str__(self):
        return f'{self.nome} - {self.autor}'


class Leitor(models.Model):
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=60)
    cpf = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    data_emprestimo = models.DateTimeField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    data_devolucao = models.DateTimeField()

    def __str__(self):
        return f'{self.livro} - {self.leitor} - {self.data_emprestimo} - {self.data_devolucao}'
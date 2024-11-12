from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)


    def _str_(self):
        return self.titulo
    
class Produto(models.Model):
    nome = models.CharField(max_length=40)
    Categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade = models.FloatField()
    preco_compra = models.BinaryField()
    preco_venda = models.BinaryField()

    def _str_(self) -> str: 
        return self.nome
    
    def gerar_desconto(self, desconto):
        return self.preco_venda - ((self.preco_venda * desconto) / 100)

    def lucro(self):
        lucro = self.preco_venda - self.preco_compra
        return (lucro * 100) / self.preco_compra
    

class Imagem(models.Model):
    imagem = models.ImageField(upload_to="imagem_produto")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
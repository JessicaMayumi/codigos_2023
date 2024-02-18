from jmskParecista import Parecista
from jmskArtigo import Artigo
from jmskAutor import Autor
from jmskLivro import Livro
from jmskObra import Obra
from jmskParecer import Parecer
from jmskPessoa import Pessoa

#teste

p1 = Parecista("p1", "01/01/01", "aaaaaa")
p2 = Parecista("p2", "02/02/02", "bbbbbb")

au1 = Autor("au1", "03/03/03", "cccccc")
au2 = Autor("au2", "04/04/03", "dddddd")

l1 = Livro("l1", 1, "g1", "e1", "01")
l2 = Livro("l2", 2, "g2", "e2", "02")
l3 = Livro("l3", 3, "g3", "e3", "03")

ar1 = Artigo("a1", 4, "r1", 4)
ar2 = Artigo("a2", 5, "r2", 5)

pa1 = Parecer(p1, "00/00/00", "blabla")
pa2 = Parecer(p2, "00/00/00", "blablabla")

l1.adicionaAutor(au1)
l1.adicionaParecer(pa1)

l2.adicionaAutor(au2)
l2.adicionaParecer(pa2)

print(l1)
print(l2)
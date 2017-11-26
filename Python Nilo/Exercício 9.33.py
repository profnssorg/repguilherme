## Nome do Programa: Imagens no HTML
## Autor: Guilherme Mendes
## Descrição: Cria uma página HTML com todas as imagens da pasta PICTURES
## Versão: 1.0
## Data: 26/11/2017


## Importação de módulos
import os
import os.path


## Declaração de variáveis
pictures = []

os.chdir("../../Pictures")

for l in os.listdir("."):
    if l.endswith(".jpg") or l.endswith(".png"):
        pictures.append(l)

os.chdir("../Desktop/Python")

pag = open("imagens.html", "w", encoding="utf-8")

pag.write("""
<!DOCTYPE html>
<html lang="pt-BR">

<head>
<meta charset="utf-8">
<title>Imagens</title>
</head>

<body>
""")

os.chdir("../../Pictures")
for pic in pictures:
    adr = os.getcwd() + "/" + pic
    pag.write("<p><img src=%s /></p>" % adr)

pag.write("""
</body>
</html>
""")

pag.close()

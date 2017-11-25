p = open("página.html", "w", encoding="utf-8")

p.write("""
<!DOCTYPE html>
<html lang="pt-BR">

<head>
<meta charset="utf-8">
<title>Título da Página</title>
</head>

<body>
Olá

""")

for l in range(100):
    p.write("<p>%d</p>" % l)

p.write("""

</body>
</html>
""")

p.close()

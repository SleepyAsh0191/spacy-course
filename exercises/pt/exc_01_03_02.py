# Importar a classe da língua inglesa (English) e criar um objeto nlp
from ____ import ____

nlp = ____

# Processar o texto
doc = ____("I like tree kangaroos and narwhals.")

# Uma partição do Doc para "tree kangaroos"
tree_kangaroos = ____
print(tree_kangaroos.text)

# Uma partição do Doc para "tree kangaroos and narwhals" (sem incluir o ".")
tree_kangaroos_and_narwhals = ____
print(tree_kangaroos_and_narwhals.text)

node_finder
============

GOALS (Brazilian Portuguese)
-

Imagine que dada uma página HTML de uma notícia, você precisa achar qual o elemento
HTML que melhor "represente" o conteúdo textual da notícia (contenha todo e apenas o texto
do artigo). Uma solução simples seria simplesmente pegar o nó com mais texto, mas aí sempre
pegaríamos a raiz :). Queremos pegar o nó que ​
melhor engloba o texto​
 de uma notícia. Seu
objetivo é implementar um código que dada uma página HTML de entrada retorne (como
texto/String) qual o nó HTML que mais provavelmente contém o texto da notícia. Para isso você
deve atribuir, para cada elemento, um "score" de o quão bem aquele nó engloba o texto da
notícia. O score deve ser calculado da seguinte forma:

Score(node) = text_length(node) + (0.5 * children_score(node))

Sendo ​
text_length(node) ​
 uma função, que dado um elemento HTML, retorna o tamanho
do texto contido APENAS naquele nó sem considerar o texto contido nos filhos. E
children_score(node) ​
 soma os scores dos filhos de ​
node ​
.

Duas dicas:
­ Você pode usar o próprio DOM para guardar a informação de score de cada elemento durante
o processamento.
­ Você pode usar uma biblioteca externa que faça o parser e manipulação do DOM HTML.


SOLUTION (Brazilian Portuguese)
-

Desenvolvimento de um programa que, dado um arquivo de entrada contendo código HTML:

1) Faz o parser do texto contendo o código HTML

2) Remove tags de "script" e "style"

3) Percorre todos elementos de "body" chamando a função "parse_node" responsável por calcular o score do nó atual.

4) Para cada node filho do item 3 chama recursivamente a função "parse_node", compondo assim a regra (0.5 * children_score(node)

5) Mantém um único "ponteiro" para o nó com maior score (ao invés de guardar o score de todos nós)

6) Retorna uma representação string do nó com maior score ou "None" caso nenhum nó tenha sido encontrado (ex: "body" é vazio)

obs: A pasta "tests" contém um teste unitário simples para validação da classe (TODO: mais cenários de teste)

INSTALLATION
-

1) Be sure your environment is ready to run Python (2.7x) applications (https://www.python.org/about/gettingstarted/)

2) Recommended use of virtual environment (Brazilian Portuguese reference: https://osantana.me/ambiente-isolado-para-python-com-virtualenv/)

3) Run install.sh file found at the root of the project


HELP OUTPUT
-

```
usage: node_finder.py [-h] [-f HTML_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f HTML_FILE, --html_file HTML_FILE
                        HTML source file path to parse and find node
```

USAGE EXAMPLE
-

```
cd node_finder
python node_finder.py -f example.html
```

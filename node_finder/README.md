node_finder
============

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


=== INSTALLATION

1) Prepare o ambiente para rodar aplicacoes python
2) Preferencialmente use um virtual environment (https://osantana.me/ambiente-isolado-para-python-com-virtualenv/)
3) Rode o arquivo install.sh


```
usage: node_finder.py [-h] [-f HTML_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -f HTML_FILE, --html_file HTML_FILE
                        HTML source file path to parse and find node
```

=== Example Usage

```
cd node_finder
python node_finder.py -f example.html
```

url_gather
============

Imagine que você quer coletar as páginas de um site e para cada página encontrar o conteúdo
textual das notícias dele.
Seu objetivo é implementar um coletor web que dada uma URL inicial (​
http://g1.com.br​
 por
exemplo) baixe todas os links contidos nela e depois baixe os links nessas páginas e assim por
diante. E para cada página execute a função do item anterior retornando o conteúdo textual da
notícia. Se você não escolheu fazer a questão ​
2) ​
use uma função/classe dummy no lugar da
extração do texto.

A profundidade da coleta deve ser parametrizável. Por exemplo, se a profundidade for igual a 0
você deve baixar apenas a URL inicial. Profundidade igual a 1 deve baixar a URL inicial e as
páginas linkadas a partir dela. E assim por diante.

Idealmente o processamento a ser feito em cada página deve ser customizável, ou seja, se eu
quiser usar outro algoritmo para extrair páginas (ou qualquer outra coisa) o coletor deve poder
me permitir isso.
Por fim, o programa deve ser capaz de usar o máximo de recursos possíveis seja de IO (baixar
páginas) ou de CPU (processamento de uma página).

Duas dicas:
­ Baixar apenas links apontando para o mesmo domínio já é suficiente (e mais rápido)
­ Baixar apenas os links da primeira página já é suficiente.

=== INSTALLATION

1) Prepare o ambiente para rodar aplicacoes python
2) Preferencialmente use um virtual environment (https://osantana.me/ambiente-isolado-para-python-com-virtualenv/)
3) Rode o arquivo install.sh


```
usage: url_gather.py [-h] [-u URL] [-d DEPTH] [-w WORKERS] [-o OUT]
                     [-cf COLLECTOR_FILE] [-cc COLLECTOR_CLASS]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Initial URL to gather
  -d DEPTH, --depth DEPTH
                        Gathering depth
  -w WORKERS, --workers WORKERS
                        Number of parallel workers
  -o OUT, --out OUT     Folder to save output files
  -cf COLLECTOR_FILE, --collector_file COLLECTOR_FILE
                        Path to custom .py file to act as collector
  -cc COLLECTOR_CLASS, --collector_class COLLECTOR_CLASS
                        Class name of custom collector
```


=== Example Usage

```
cd url_gather
python url_gather.py -u http://g1.globo.com/ -d 1 -w 5 -o /tmp/
```

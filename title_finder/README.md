# TitleFinder

GOALS (Brazilian Portuguese)
-

Imagine que temos uma arquivo texto onde cada linha contém o título de uma notícia: 
... 
Demora em votação pode deixar imposto mais alto, diz Levy 
Estátua de Tom Jobim tem parte danificada após brincadeira de jovem 
... 
 
Queremos poder encontrar, facilmente, quais títulos que possuem determinada palavra­chave. 
Seu objetivo é construir um programa que, em uma única execução, lê um arquivo de texto e 
possibilita que o usuário possa consultar passando uma palavra por vez (stdin). Para cada 
consulta o programa deve retornar todos os títulos de notícia que contém aquela palavra, 
ordenados pelo número de vezes que a palavra aparece naquele título. 
 
Observações: 

● O programa não precisa ter uma GUI 

● A parte de processamento do arquivo é feita "offline" e por isso pode demorar mais. A 
parte de consulta, feita "online" deve ser mais eficiente 

● É possível usar mais espaço em memória na parte offline se isso for deixar a parte de 
consulta mais rápida 

● Espera­se que para cada processamento do arquivo serão feito várias consultas 


SOLUTION (Brazilian Portuguese)
-

Desenvolvimento de um programa que, dado um arquivo de entrada contendo títulos de notícias:

1) Percorre as linhas do arquivo, sendo que para cada linha:
	
	1.1) Popula uma lista de títulos (string raw)
	
	1.2) Percorre as palavras do título atual, sendo que para cada palavra:
	
		1.2.1) Normaliza a palavra (minúsculo, sem acento, etc.) e verifica se não é uma "stop word"
		
		1.2.2) Popula um HashMap<(string) palavra, HashMap<(int) tituloID, (int) frequenciaDaPalavraNoTitulo>>
		
2) Transforma HashMap<(string) palavra <(int) tituloID, (int) frequenciaDaPalavraNoTitulo>> em HashMap<(string) palavra, List<(int) tituloID>>, sendo List<(int) tituloID> uma lista ordenada em ordem decrescente dos IDs de títulos onde a palavra é mais frequente

3) Entra em loop infinto pedindo uma palavra a ser pesquisada (Condição de Parada: nenhuma palavra informada).

4) Normaliza a palavra a ser pesquisada e busca a entrada da palavra normalizada em HashMap<(string) palavra, List<(int) tituloID>>

5) Se o HashMap contém a palavra, percorre os titulos IDs fazendo a tradução do ID para o título "raw" e escrevendo o título em System.out. Caso contrário, uma mensagem default é exibida indicando que nenhum título contém a palavra.


Considerações:


- Decidi manter uma lista separada com as strings do títulos e para cada palavra uma lista apenas de IDs visando diminuir o uso de memória. Sem a lista de títulos, cada HashMap de "palavra" teria que conter a string completa do título, o que acarretaria em um uso excessivo de memória, diminuindo performance e escalabilidade da solução. O contra dessa solução é ter que traduzir o ID antes de exibir o título mas a princípio parece que este custo vale a pena. Um estudo mais aprofundado seria necessário para confirmar essa hipótese.

- Feature adicional: carregamento de uma lista de "stop words" a partir do arquivo "[ROOT]/src/main/resources/stop_words.txt" a fim de mapear apenas palavras relevantes para a busca, aumentando assim a performance e diminuindo o uso de memória.

- A pasta "[ROOT]/src/test/java" contém alguns testes unitários que serão automaticamente executados durante a execução de "build.sh".


INSTALLATION
-

1) Be sure your environment is ready to run Java (1.7) applications and supporting Maven projects (See: https://java.com/en/download/help/index_installing.xml and https://maven.apache.org/install.html)

2) Run build.sh file found at the root of the project ("titlefinder-0.0.1-SNAPSHOT-jar-with-dependencies.jar" file should be generated at [ROOT]/target folder)


EXPECTED PARAMETERS
-


The unique expected parameter is the location of the .txt file to be processed. If no file is informed you'll be asked to use the default example file.

```
Could not get title file from arguments. Do you wanna use default example file ? (Y/n): 
```


USAGE EXAMPLE
-

```
java -jar target/titlefinder-0.0.1-SNAPSHOT-jar-with-dependencies.jar ./src/main/resources/example.txt
```


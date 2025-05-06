# Code Challenge Helper

Uma ferramenta para criar estruturas de pasta organizadas para o estudo de problemas de programação como LeetCode, HackerRank, etc.

## Instalação

```bash
pip install code_challenge_helper
```

## Uso

```bash
# Criar uma nova estrutura para um problema em Python
challenge-helper create-resolution
```

Você será solicitado a fornecer:

1. O nome do desafio
2. A linguagem de programação

### Linguagens Suportadas
- Python (.py)
- Java (.java)
- Go (.go)

Exemplo de execução:
```bash
$ challenge-helper create-resolution
Qual o nome da questão?: Testando BLA BLA BLA
Em qual linguagem deseja realizar? python

✅ Estrutura criada com sucesso: Testando BLA BLA BLA_06-05-2025
```

## Estrutura de pastas gerada

Para Python:
```
NomeQuestao_2023-05-05/
├── Anotacoes.txt
├── Rascunhos.excalidraw.md
├── Solution.py
└── Tests.py
```

Para Java:
```
NomeQuestao_2023-05-05/
├── Anotacoes.txt
├── Rascunhos.excalidraw.md
├── Solution.java
└── Tests.java
```

### Notas para os arquivos Java

Os testes em Java utilizam o JUnit 5. Para executá-los, você precisará adicionar o JUnit às dependências do seu projeto:

**Maven:**
```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.9.2</version>
    <scope>test</scope>
</dependency>
```

**Gradle:**
```groovy
testImplementation 'org.junit.jupiter:junit-jupiter:5.9.2'
```

# PRÓXIMOS PASSOS:

Em desenvolvimento futuro, o projeto será integrado com IA para fornecer assistência na resolução dos desafios. A funcionalidade será utilizada da seguinte maneira:

```bash
challenge-helper create-resolution -ai <link_questao>
```

O sistema criará a estrutura de pasta normalmente

Adicionalmente, fará uma consulta a uma API de IA com o prompt: "<link_questao> Me retorne um breve contexto dos conhecimentos necessários para resolver essa questão em {language} e organize-os em tópicos para facilitar possíveis pesquisas que precisarei fazer para conseguir solucionar"

A resposta da IA será salva no arquivo Anotacoes.txt que atualmente é criado vazio.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
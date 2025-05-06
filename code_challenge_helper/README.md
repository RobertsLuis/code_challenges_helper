# Code Challenge Helper

Uma ferramenta para criar estruturas de pasta organizadas para o estudo de problemas de programação como LeetCode, HackerRank, etc.

## Instalação

```bash
pip install code_challenge_helper
```

## Uso

```bash
# Criar uma nova estrutura para um problema em Python
challenge-helper create-resolution TwoSum py

# Criar uma nova estrutura para um problema em Java
challenge-helper create-resolution ValidParentheses java
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
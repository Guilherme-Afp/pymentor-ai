# Base de Conhecimento

## Dados Utilizados

O PyMentor AI utiliza uma combinação de conteúdo educacional estruturado, histórico de aprendizagem do estudante e métricas de desempenho para personalizar o processo de ensino.

| Arquivo | Formato | Utilização no Agente |
|----------|----------|----------|
| `roadmap_python.json` | JSON | Estrutura da trilha de aprendizagem em Python |
| `conceitos_python.json` | JSON | Base teórica de conceitos, definições e exemplos |
| `exercicios_python.json` | JSON | Banco de exercícios classificados por dificuldade |
| `projetos_python.json` | JSON | Catálogo de projetos práticos por nível |
| `historico_aluno.json` | JSON | Registro de progresso, tópicos estudados e desempenho |
| `erros_comuns.json` | JSON | Base de erros frequentes e estratégias de correção |
| `avaliacao_codigo.json` | JSON | Critérios de análise de qualidade e boas práticas |
| `documentacao_python.json` | JSON | Resumos e referências da documentação oficial |

### Possíveis Fontes Externas

O agente pode ser complementado com:

- Documentação oficial do Python.
- Repositórios de exercícios de programação.
- Bancos de questões acadêmicas.
- Datasets educacionais públicos.
- Guias de boas práticas de desenvolvimento.
- Conteúdos técnicos validados pela comunidade.

---

## Adaptações nos Dados

Os dados são enriquecidos para permitir personalização contínua do aprendizado.

As adaptações incluem:

- Classificação de exercícios por dificuldade.
- Mapeamento de pré-requisitos entre conteúdos.
- Associação de erros frequentes aos conceitos relacionados.
- Criação de indicadores de domínio por tópico.
- Registro histórico de desempenho individual.
- Organização de projetos em trilhas progressivas.

Além disso, o histórico do estudante é atualizado dinamicamente a cada interação para que o agente adapte explicações, desafios e recomendações futuras.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos de conhecimento são carregados durante a inicialização do agente.

Os conteúdos são indexados por categorias como:

- Fundamentos
- Estruturas de Controle
- Funções
- Coleções
- Arquivos
- Orientação a Objetos
- APIs
- Banco de Dados
- Projetos

O histórico individual do estudante é recuperado no início de cada sessão e atualizado continuamente.

### Como os dados são usados no prompt?

O agente utiliza uma abordagem híbrida:

#### Conhecimento Estático

Os conceitos fundamentais, exemplos e critérios de avaliação são incorporados à base de conhecimento principal.

#### Consulta Dinâmica

Durante cada interação, o agente consulta:

- Histórico do estudante.
- Conceitos dominados.
- Conceitos em dificuldade.
- Exercícios resolvidos.
- Projetos concluídos.
- Erros recorrentes.

Essas informações são inseridas dinamicamente no contexto da conversa para personalizar as respostas.

---

## Exemplo de Contexto Montado

```text
Perfil do Estudante:

- Nível atual: Iniciante
- Linguagem principal: Python
- Progresso geral: 32%

Conceitos dominados:

- Variáveis
- Tipos de dados
- Operadores

Conceitos em desenvolvimento:

- Estruturas condicionais
- Laços de repetição

Principais dificuldades:

- Uso de while
- Condições compostas
- Depuração de erros lógicos

Exercícios concluídos:

- Calculadora simples
- Conversor de temperatura
- Validador de idade

Projetos concluídos:

- Nenhum

Objetivo atual:

- Aprender estruturas de repetição

Últimos erros identificados:

- Loop infinito
- Atualização incorreta de variáveis de controle

Estratégia recomendada:

- Revisar while
- Resolver 3 exercícios intermediários
- Iniciar mini projeto de menu interativo
```

---

## Memória e Aprendizagem Contínua

O agente mantém um perfil evolutivo para cada estudante contendo:

- Tópicos estudados.
- Taxa de acerto.
- Tempo médio de resolução.
- Quantidade de dicas utilizadas.
- Projetos concluídos.
- Qualidade média do código.
- Conceitos dominados.
- Conceitos pendentes.

Esses dados permitem que o PyMentor AI adapte continuamente sua metodologia de ensino, atuando como um mentor personalizado em vez de apenas um assistente de perguntas e respostas.

---

## Política de Atualização da Base

A base de conhecimento deve ser atualizada periodicamente para incluir:

- Novos recursos do Python.
- Novas boas práticas.
- Exercícios adicionais.
- Projetos mais avançados.
- Tendências do mercado de desenvolvimento.
- Conteúdo solicitado frequentemente pelos estudantes.

Todas as atualizações devem ser validadas antes de serem incorporadas à base principal do agente.

---

## Estrutura Recomendada dos Arquivos

### roadmap_python.json

```json
{
  "trilha": [
    "Fundamentos",
    "Condicionais",
    "Laços",
    "Funções",
    "Coleções",
    "Arquivos",
    "POO",
    "APIs",
    "Banco de Dados",
    "Projetos"
  ]
}
```

### conceitos_python.json

```json
{
  "conceitos": [
    {
      "nome": "Variáveis",
      "nivel": "iniciante"
    },
    {
      "nome": "Funções",
      "nivel": "iniciante"
    },
    {
      "nome": "Classes",
      "nivel": "intermediario"
    }
  ]
}
```

### exercicios_python.json

```json
{
  "exercicios": [
    {
      "id": 1,
      "titulo": "Calculadora",
      "dificuldade": "iniciante"
    },
    {
      "id": 2,
      "titulo": "Sistema de Estoque",
      "dificuldade": "intermediario"
    }
  ]
}
```

### projetos_python.json

```json
{
  "projetos": [
    {
      "nome": "Lista de Tarefas",
      "nivel": "iniciante"
    },
    {
      "nome": "API REST",
      "nivel": "avancado"
    }
  ]
}
```

### historico_aluno.json

```json
{
  "aluno_modelo": {
    "progresso": 0,
    "conceitos_dominados": [],
    "dificuldades": []
  }
}
```

### erros_comuns.json

```json
{
  "erros": [
    {
      "erro": "Loop infinito",
      "causa": "condição nunca alterada"
    },
    {
      "erro": "IndexError",
      "causa": "índice fora da lista"
    }
  ]
}
```

### avaliacao_codigo.json

```json
{
  "criterios": [
    "Correção",
    "Legibilidade",
    "Modularização",
    "Eficiência",
    "PEP8"
  ]
}
```

### documentacao_python.json

```json
{
  "referencias": [
    {
      "topico": "Funções",
      "descricao": "Blocos reutilizáveis de código"
    }
  ]
}
```
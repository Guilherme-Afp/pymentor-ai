# PyMentor AI

> Um mentor inteligente de programação focado no ensino de Python através de aprendizagem adaptativa, feedback personalizado e desenvolvimento de autonomia.

---

## Sobre o Projeto

O **PyMentor AI** é um agente de inteligência artificial desenvolvido para auxiliar estudantes de programação em sua jornada de aprendizado de Python.

Diferente de chatbots tradicionais que fornecem respostas prontas, o PyMentor AI atua como um mentor virtual, incentivando o raciocínio lógico, a resolução de problemas e a construção gradual do conhecimento.

O sistema adapta explicações, exercícios e projetos ao nível do estudante, promovendo um aprendizado mais eficiente e personalizado.

---

## Objetivos

- Ensinar Python para usuários de todos os níveis.
- Desenvolver pensamento computacional.
- Estimular autonomia na resolução de problemas.
- Corrigir e avaliar código.
- Identificar lacunas de conhecimento.
- Criar trilhas de aprendizagem personalizadas.
- Acompanhar a evolução do estudante.
- Incentivar boas práticas de programação.

---

## Funcionalidades

### Ensino Adaptativo

O agente ajusta automaticamente:

- Complexidade das explicações.
- Dificuldade dos exercícios.
- Quantidade de dicas fornecidas.
- Projetos recomendados.
- Conteúdo de revisão.

### Correção de Código

Avaliação de:

- Erros sintáticos.
- Erros lógicos.
- Legibilidade.
- Modularização.
- Eficiência.
- Boas práticas.

### Geração de Exercícios

- Exercícios básicos.
- Exercícios intermediários.
- Exercícios avançados.
- Desafios progressivos.
- Problemas algorítmicos.

### Projetos Práticos

Exemplos:

- Calculadora.
- Agenda de contatos.
- Lista de tarefas.
- Sistema bancário.
- Sistema de estoque.
- API REST.
- Projetos orientados a objetos.

### Acompanhamento de Progresso

Registro de:

- Conceitos dominados.
- Conceitos pendentes.
- Exercícios concluídos.
- Projetos realizados.
- Dificuldades recorrentes.
- Evolução geral.

---

## Arquitetura

```text
Aluno
   │
   ▼
Interface Streamlit
   │
   ▼
PyMentor AI
   │
   ├── System Prompt
   ├── Base de Conhecimento
   ├── Histórico do Aluno
   └── Motor de Resposta
   │
   ▼
Resposta Personalizada
```

---

## Estrutura do Projeto

```text
pymentor-ai/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── requirements.txt
│
├── docs/
│   ├── documentacao_agente.md
│   ├── base_conhecimento.md
│   └── prompts.md
│
├── data/
│   ├── roadmap_python.json
│   ├── conceitos_python.json
│   ├── exercicios_python.json
│   ├── projetos_python.json
│   ├── historico_aluno.json
│   ├── erros_comuns.json
│   ├── avaliacao_codigo.json
│   └── documentacao_python.json
│
└── src/
    ├── app.py
    ├── agente.py
    ├── config.py
    ├── carregador_dados.py
    └── prompt_manager.py
```

---

## Tecnologias Utilizadas

- Python
- Streamlit
- OpenAI API
- JSON
- dotenv

---

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/pymentor-ai.git

cd pymentor-ai
```

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configuração

### Criar arquivo .env

Copie o modelo:

```bash
cp .env.example .env
```

ou no Windows:

```powershell
copy .env.example .env
```

Edite o arquivo:

```env
OPENAI_API_KEY=sua_chave_aqui
```

---

## Executando o Projeto

```bash
streamlit run src/app.py
```

Após executar, o navegador abrirá automaticamente.

Caso não abra:

```text
http://localhost:8501
```

---

## Base de Conhecimento

O projeto utiliza arquivos JSON para armazenar conhecimento estruturado.

### Arquivos Utilizados

| Arquivo | Descrição |
|----------|----------|
| roadmap_python.json | Trilha de aprendizagem |
| conceitos_python.json | Conceitos de Python |
| exercicios_python.json | Banco de exercícios |
| projetos_python.json | Projetos práticos |
| historico_aluno.json | Evolução do estudante |
| erros_comuns.json | Base de erros recorrentes |
| avaliacao_codigo.json | Critérios de avaliação |
| documentacao_python.json | Resumos técnicos |

---

## Exemplo de Uso

### Pergunta

```text
Me ajude a entender funções.
```

### Resposta Esperada

```text
Funções são blocos reutilizáveis de código.

Antes de continuarmos:

Você já entende o conceito de parâmetros e retorno?

Dependendo da sua resposta posso explicar com exemplos mais simples ou mais avançados.
```

---

## Filosofia de Ensino

O PyMentor AI segue os princípios:

- Aprendizagem ativa.
- Feedback contínuo.
- Dificuldade progressiva.
- Resolução de problemas.
- Autonomia do estudante.

O agente evita fornecer respostas prontas imediatamente e incentiva o desenvolvimento do raciocínio.

---

## Segurança

O sistema:

- Não compartilha dados sensíveis.
- Não fornece credenciais.
- Não gera código malicioso.
- Não realiza atividades ilegais.
- Não inventa informações quando não possui confiança suficiente.

---

## Limitações

O PyMentor AI não:

- Substitui professores.
- Garante aprovação em cursos.
- Faz provas ou avaliações pelo estudante.
- Executa código externo automaticamente.
- Fornece soluções completas sem contexto pedagógico.

---

## Roadmap Futuro

### Versão 1.0

- Interface Streamlit.
- Integração com OpenAI.
- Base de conhecimento em JSON.

### Versão 2.0

- Histórico persistente de alunos.
- Perfil adaptativo.
- Trilhas automáticas.

### Versão 3.0

- Avaliação automática de código.
- Sistema de pontuação.
- Gamificação.

### Versão 4.0

- Dashboard de desempenho.
- Métricas avançadas.
- Recomendações inteligentes.

---

## Contribuição

Contribuições são bem-vindas.

Fluxo recomendado:

```bash
git checkout -b minha-feature

git commit -m "feat: nova funcionalidade"

git push origin minha-feature
```

Abra um Pull Request descrevendo as alterações realizadas.

---

## Licença

Este projeto está licenciado sob a licença MIT.

---

## Autor

Desenvolvido como projeto educacional para criação de agentes inteligentes especializados em ensino de programação.

---

## Status do Projeto

🚧 Em desenvolvimento

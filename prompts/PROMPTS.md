# Prompts para Gerador de Senhas Seguras

Documento contendo prompts estruturados para gerar componentes e documentação do projeto utilizando GitHub Copilot.

---

## ✅ PROMPT 1 — Gerar README.md

**Contexto:**  
Estou desenvolvendo um MVP chamado Gerador de Senhas Seguras, utilizando Python. Preciso criar o arquivo README.md completo para publicar no GitHub.

**Objetivo:**  
Gerar um README profissional contendo: descrição do projeto, objetivos, requisitos, instalação, execução, exemplos de uso, estrutura de pastas, testes, tecnologias utilizadas e licença.

**Estilo:**  
Markdown organizado, com seções claras, títulos, listas e exemplos de código.

**Resposta:**  
Gerar o conteúdo completo do arquivo README.md.

---

## ✅ PROMPT 2 — Gerar .gitignore

**Contexto:**  
Estou preparando o repositório do projeto Gerador de Senhas Seguras para publicação no GitHub.

**Objetivo:**  
Gerar um arquivo .gitignore adequado para projetos Python, incluindo exclusão de: virtualenv, cache, logs, arquivos temporários e diretórios de testes.

**Estilo:**  
Lista simples de diretórios e padrões de exclusão.

**Resposta:**  
Gerar o conteúdo completo do arquivo .gitignore.

---

## ✅ PROMPT 3 — Gerar main.py

**Contexto:**  
Preciso criar o arquivo principal do projeto, responsável pela interface de linha de comando (CLI).

**Objetivo:**  
Gerar o arquivo main.py contendo:
- CLI com argparse
- Parâmetros: tamanho, incluir números, incluir maiúsculas, minúsculas e caracteres especiais
- Validação de entradas
- Chamada da função do módulo password_generator.py
- Exibição da senha gerada

**Estilo:**  
Código Python limpo, com boas práticas e docstrings.

**Resposta:**  
Gerar o conteúdo completo do arquivo main.py.

---

## ✅ PROMPT 4 — Gerar password_generator.py

**Contexto:**  
O projeto precisa de um módulo dedicado à lógica de geração de senhas.

**Objetivo:**  
Gerar o arquivo password_generator.py contendo:
- Função principal generate_password()
- Parâmetros configuráveis
- Validação de critérios
- Uso de random e string
- Docstrings completas

**Estilo:**  
Código Python organizado, seguro e fácil de entender.

**Resposta:**  
Gerar o conteúdo completo do arquivo password_generator.py.

---

## ✅ PROMPT 5 — Gerar diagrama Mermaid da arquitetura

**Contexto:**  
Preciso documentar a arquitetura do projeto no README.

**Objetivo:**  
Gerar um diagrama Mermaid mostrando o fluxo entre:
- CLI → Módulo de geração → Testes → Saída final

**Estilo:**  
Código Mermaid simples e claro.

**Resposta:**  
Gerar apenas o código Mermaid do diagrama.

---

## ✅ PROMPT 6 — Gerar testes unitários

**Contexto:**  
Quero garantir que a função de geração de senhas funciona corretamente.

**Objetivo:**  
Gerar testes unitários usando unittest, cobrindo:
- Tamanho da senha
- Inclusão de números
- Inclusão de maiúsculas
- Inclusão de minúsculas
- Inclusão de caracteres especiais
- Erros e validações

**Estilo:**  
Código Python com testes organizados e assertivas claras.

**Resposta:**  
Gerar o conteúdo completo do arquivo de testes unitários.

---

## ✅ PROMPT 7 — Gerar testes integrados

**Contexto:**  
Quero validar o fluxo completo do sistema via CLI.

**Objetivo:**  
Gerar testes integrados usando unittest + subprocess, simulando chamadas reais ao main.py e verificando a saída.

**Estilo:**  
Código Python com cenários realistas.

**Resposta:**  
Gerar o conteúdo completo do arquivo de testes integrados.

---

## ✅ PROMPT 8 — Gerar Makefile

**Contexto:**  
O projeto Gerador de Senhas Seguras já está completo, contendo main.py, password_generator.py, pasta tests/, requirements.txt e demais arquivos. Preciso criar um arquivo Makefile para facilitar a execução do projeto em qualquer máquina.

**Objetivo:**  
Gerar um Makefile contendo alvos para:
- Criar ambiente virtual
- Instalar dependências
- Executar o projeto
- Rodar testes unitários e integrados
- Formatar o código
- Limpar arquivos temporários

O Makefile deve ser compatível com Linux, macOS e Windows (via Git Bash).

**Estilo:**  
Comandos Makefile simples, diretos, organizados e com comentários explicativos. O conteúdo deve ser completo e pronto para uso.

**Resposta:**  
Gerar o conteúdo completo do arquivo Makefile conforme a estrutura real do projeto.

---

## ✅ PROMPT 9 — Gerar requirements.txt

**Contexto:**  
O projeto Gerador de Senhas Seguras já está completo e utiliza Python. Preciso criar o arquivo requirements.txt contendo todas as dependências necessárias para executar o projeto, incluindo bibliotecas usadas para testes, formatação e qualquer outra funcionalidade presente no código.

**Objetivo:**  
Gerar o conteúdo completo do arquivo requirements.txt, listando apenas as dependências realmente utilizadas no projeto, com versões fixadas para garantir reprodutibilidade em qualquer máquina.

**Estilo:**  
Lista simples, uma dependência por linha, seguindo o padrão oficial do Python Package Index (PyPI).

**Resposta:**  
Gerar o conteúdo completo do arquivo requirements.txt conforme as necessidades reais do projeto.

---

## 📋 Resumo de Prompts

| # | Artefato | Descrição | Status |
|---|----------|-----------|--------|
| 1 | README.md | Documentação completa do projeto | ✅ |
| 2 | .gitignore | Exclusões para repositório | ✅ |
| 3 | main.py | Interface CLI principal | ✅ |
| 4 | password_generator.py | Módulo de geração de senhas | ✅ |
| 5 | Diagrama Mermaid | Visualização da arquitetura | ✅ |
| 6 | Testes Unitários | Validação de funções | ✅ |
| 7 | Testes Integrados | Validação do sistema completo | ⏳ |
| 8 | Makefile | Automação de tarefas do projeto | ✅ |
| 9 | requirements.txt | Dependências do projeto | ✅ |

---

## 🎯 Como Usar Este Documento

1. **Copie o prompt desejado** da seção correspondente
2. **Cole no GitHub Copilot** ou em seu assistente de IA preferido
3. **Adapte conforme necessário** para seu contexto específico
4. **Revise o resultado** gerado antes de implementar

---

## 📝 Notas

- Todos os prompts foram estruturados para gerar código Python de qualidade
- Os prompts foram pensados para a geração com GitHub Copilot
- Recomenda-se revisar o código gerado antes de usar em produção
- Os testes podem ser ajustados conforme a especificação final do projeto

---

**Última atualização:** 23 de Abril de 2026  
**Projeto:** Gerador de Senhas Seguras - MVP Acadêmico

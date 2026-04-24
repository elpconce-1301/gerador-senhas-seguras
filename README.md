# Gerador de Senhas Seguras

MVP acadêmico desenvolvido com auxílio do GitHub Copilot

## Sobre o Projeto

Aplicação CLI (Command Line Interface) em Python para gerar senhas aleatórias seguras. O projeto permite personalizar o tamanho da senha e os tipos de caracteres a serem inclusos (maiúsculas, minúsculas, números e caracteres especiais).

## Funcionalidades

✅ Gerar senhas aleatórias com tamanho configurável (4-128 caracteres)  
✅ Escolher quais tipos de caracteres incluir:
- Letras maiúsculas (A-Z)
- Letras minúsculas (a-z)
- Números (0-9)
- Caracteres especiais (!@#$%...)

✅ Validação robusta de entradas do usuário  
✅ Interface amigável e intuitiva  
✅ Testes unitários abrangentes  
✅ Código comentado e bem estruturado  

## Requisitos

- Python 3.6+
- Apenas bibliotecas padrão do Python (nenhuma dependência externa)

## Estrutura do Projeto

```
gerador-senhas-seguras/
├── app/
│   ├── __init__.py
│   ├── main.py                      # Interface CLI principal
│   └── password_generator.py        # Módulo de geração de senhas
├── tests/
│   ├── __init__.py
│   └── test_password_generator.py   # Testes unitários
├── docs/
├── prompts/
├── PROJECT_SPEC.md                  # Especificações do projeto
├── requirements.txt                 # Dependências de produção
├── requirements-dev.txt             # Dependências de desenvolvimento
├── Makefile                         # Automação de tarefas
└── README.md                        # Este arquivo
```

## Como Executar

### 1. Execução Interativa

Navegue até o diretório do projeto e execute:

```bash
python -m app.main
```

Ou:

```bash
python3 -m app.main
```

Você também pode usar o Makefile:

```bash
make run
```

A aplicação será iniciada com uma interface interativa no terminal, solicitando:
1. O tamanho desejado para a senha
2. Os tipos de caracteres a incluir
3. Se deseja gerar outra senha

### 2. Execução dos Testes

Para executar todos os testes unitários:

```bash
python -m unittest discover tests
```

Ou para executar o arquivo de testes especificamente:

```bash
python -m unittest tests.test_password_generator
```

Para teste com saída detalhada:

```bash
python -m unittest tests.test_password_generator -v
```

Você também pode usar o Makefile:

```bash
make test       # Executar testes
make test-verbose   # Executar com saída detalhada
```

## Exemplo de Uso

```
==================================================
    GERADOR DE SENHAS SEGURAS
==================================================

Bem-vindo! Use este programa para gerar senhas seguras.

Digite o tamanho da senha (4-128): 16

Escolha os tipos de caracteres a incluir:
Incluir letras MAIÚSCULAS? (S/N): S
Incluir letras minúsculas? (S/N): S
Incluir NÚMEROS? (S/N): S
Incluir caracteres ESPECIAIS (!@#$%...)? (S/N): S

==================================================
✓ Senha gerada com sucesso!
  Tamanho: 16 caracteres
  Maiúsculas: Sim
  Minúsculas: Sim
  Números: Sim
  Especiais: Sim
==================================================

  SENHA: A7kL!mN2p@qR4sT9

==================================================

Deseja gerar outra senha? (S/N): N

✓ Obrigado por usar o Gerador de Senhas Seguras!
Até logo!
```

## Como o GitHub Copilot foi Utilizado

O GitHub Copilot foi utilizado de forma estratégica para:

1. **Geração de Estrutura Base**
   - Criação da estrutura geral do projeto com melhorias sugeridas
   - Padrão de organização do código em módulos

2. **Desenvolvimento da Lógica de Geração**
   - Implementação eficiente do gerador de senhas usando `random` e `string`
   - Validação de parâmetros de entrada com tratamento de erros

3. **Interface CLI Intuitiva**
   - Desenvolvimento de funções interativas para coleta de dados
   - Feedback visual com caracteres especiais (✓, ❌, ⚠️)
   - Tratamento de entradas variadas (maiúsculas/minúsculas, abreviações)

4. **Cobertura de Testes**
   - Geração de testes unitários abrangentes
   - Cenários de sucesso e casos de erro
   - Testes de integração e validação

5. **Documentação e Comentários**
   - Documentação em formato docstring (PEP 257)
   - Comentários inline explicando a lógica complexa
   - Exemplos de uso claro

## Arquivos Principais

### `password_generator.py`
Módulo responsável por gerar as senhas. Contém a classe `PasswordGenerator` com:
- Método `generate()`: gera uma senha aleatória com parâmetros customizáveis
- Método `_validate_parameters()`: valida as entradas do usuário
- Atributos: caracteres maiúsculos, minúsculos, dígitos e especiais

### `main.py`
Interface CLI que oferece:
- Função `get_password_length()`: solicita o tamanho da senha
- Função `get_character_options()`: solicita tipos de caracteres
- Função `generate_and_display_password()`: gera e exibe a senha
- Função `main()`: loop principal da aplicação

### `tests/test_password_generator.py`
Suite de testes com mais de 20 testes cobrindo:
- Geração com diferentes tipos de caracteres
- Validação de tamanhos mínimo e máximo
- Tratamento de erros e exceções
- Aleatoriedade das senhas geradas
- Testes de integração

## Tratamento de Erros

A aplicação trata diversos cenários de erro:

| Erro | Mensagem |
|------|----------|
| Tamanho < 4 | "Comprimento mínimo é 4 caracteres" |
| Tamanho > 128 | "Comprimento máximo é 128 caracteres" |
| Tamanho não numérico | "Comprimento deve ser um número inteiro" |
| Nenhum tipo selecionado | "Selecione pelo menos um tipo de caractere" |
| Entrada inválida (S/N) | "Digite 'S' (sim) ou 'N' (não)!" |

## Requisitos Técnicos Atendidos

✅ Linguagem: Python 3.6+  
✅ Apenas bibliotecas padrão (random, string, sys, os, unittest)  
✅ Interface CLI interativa  
✅ Código simples, legível e comentado  
✅ Testes unitários com múltiplos cenários  
✅ README detalhado explicando execução e uso do Copilot  

## Melhorias Futuras

Possíveis extensões do projeto:
- Opção de excluir caracteres ambíguos (i, l, 1, o, 0, O)
- Salvar senhas geradas em arquivo
- Interface gráfica (GUI) complementar
- Força da senha (indicador visual)
- Importação de listas de caracteres customizadas

## Licença

Projeto acadêmico - UFG

## Autor

Desenvolvido com auxílio do GitHub Copilot como parte do currículo de Engenharia de Software.

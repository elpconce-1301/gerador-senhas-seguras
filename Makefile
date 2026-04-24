.PHONY: help venv install run test clean format lint all

# Variáveis
PYTHON := python3
PIP := pip3
VENV_DIR := venv
PROJECT_NAME := gerador-senhas-seguras

# Cores para output
GREEN := \033[0;32m
BLUE := \033[0;34m
YELLOW := \033[1;33m
NC := \033[0m # No Color

help:
	@echo "$(BLUE)===================================$(NC)"
	@echo "$(BLUE)Gerador de Senhas Seguras - Makefile$(NC)"
	@echo "$(BLUE)===================================$(NC)"
	@echo ""
	@echo "$(GREEN)Alvos disponíveis:$(NC)"
	@echo "  $(YELLOW)make help$(NC)        - Exibe esta mensagem de ajuda"
	@echo "  $(YELLOW)make venv$(NC)        - Cria ambiente virtual Python"
	@echo "  $(YELLOW)make install$(NC)     - Instala dependências do projeto"
	@echo "  $(YELLOW)make run$(NC)         - Executa a aplicação principal"
	@echo "  $(YELLOW)make test$(NC)        - Executa testes unitários"
	@echo "  $(YELLOW)make test-verbose$(NC)- Executa testes com saída detalhada"
	@echo "  $(YELLOW)make lint$(NC)        - Valida sintaxe Python"
	@echo "  $(YELLOW)make format$(NC)      - Formata código (futuro com black/autopep8)"
	@echo "  $(YELLOW)make clean$(NC)       - Remove arquivos temporários e cache"
	@echo "  $(YELLOW)make clean-venv$(NC)  - Remove ambiente virtual"
	@echo "  $(YELLOW)make all$(NC)         - Executa: venv, install, test"
	@echo ""
	@echo "$(GREEN)Exemplos de uso:$(NC)"
	@echo "  make venv       # Criar ambiente virtual"
	@echo "  make install    # Instalar dependências"
	@echo "  make run        # Executar aplicação"
	@echo "  make test       # Rodar testes"
	@echo "  make clean      # Limpar temporários"
	@echo ""

venv:
	@echo "$(BLUE)Criando ambiente virtual...$(NC)"
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "$(GREEN)✓ Ambiente virtual criado em $(VENV_DIR)/$(NC)"
	@echo ""
	@echo "$(YELLOW)Ative o ambiente com:$(NC)"
	@echo "  Linux/macOS: source $(VENV_DIR)/bin/activate"
	@echo "  Windows: $(VENV_DIR)\\Scripts\\activate"
	@echo ""

install: venv
	@echo "$(BLUE)Instalando dependências...$(NC)"
	. $(VENV_DIR)/bin/activate && $(PIP) install --upgrade pip
	@echo "$(GREEN)✓ Dependências instaladas$(NC)"
	@echo ""

run:
	@echo "$(BLUE)Executando aplicação...$(NC)"
	@echo ""
	$(PYTHON) -m app.main

test:
	@echo "$(BLUE)Executando testes unitários...$(NC)"
	$(PYTHON) -m unittest discover tests -p "test_*.py"
	@echo ""
	@echo "$(GREEN)✓ Testes executados com sucesso!$(NC)"
	@echo ""

test-verbose:
	@echo "$(BLUE)Executando testes com saída detalhada...$(NC)"
	$(PYTHON) -m unittest discover tests -p "test_*.py" -v
	@echo ""
	@echo "$(GREEN)✓ Testes executados com sucesso!$(NC)"
	@echo ""

lint:
	@echo "$(BLUE)Validando sintaxe Python...$(NC)"
	$(PYTHON) -m py_compile app/main.py app/password_generator.py
	@echo "$(GREEN)✓ Sintaxe válida!$(NC)"
	@echo ""

format:
	@echo "$(BLUE)Formatando código...$(NC)"
	@echo "$(YELLOW)Nota: use 'pip install black' para formatar com Black$(NC)"
	@echo "      ou 'pip install autopep8' para formatar com autopep8"
	@echo ""
	@echo "Exemplo com autopep8:"
	@echo "  autopep8 --in-place --aggressive --aggressive main.py"
	@echo ""

clean:
	@echo "$(BLUE)Limpando arquivos temporários...$(NC)"
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type f -name "*.egg-info" -delete 2>/dev/null || true
	@echo "$(GREEN)✓ Arquivos temporários removidos$(NC)"
	@echo ""

clean-venv:
	@echo "$(BLUE)Removendo ambiente virtual...$(NC)"
	rm -rf $(VENV_DIR)
	@echo "$(GREEN)✓ Ambiente virtual removido$(NC)"
	@echo ""

clean-all: clean clean-venv
	@echo "$(GREEN)✓ Limpeza completa realizada$(NC)"
	@echo ""

all: venv install test
	@echo "$(GREEN)✓ Instalação e testes completos!$(NC)"
	@echo ""
	@echo "Para executar a aplicação:"
	@echo "  make run"
	@echo ""

.DEFAULT_GOAL := help

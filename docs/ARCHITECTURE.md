# Diagrama de Arquitetura - Gerador de Senhas Seguras

## Fluxo da Aplicação

```mermaid
graph TD
    A["👤 Entrada do Usuário<br/>(CLI - app/main.py)"] -->|Solicita Parâmetros| B["⚙️ Validação de Entradas<br/>(get_password_length)<br/>(get_character_options)"]
    
    B -->|Parâmetros Válidos| C["🔐 Módulo de Geração<br/>(app/password_generator.py)"]
    B -->|Parâmetros Inválidos| D["❌ Mensagem de Erro<br/>Solicita Nova Entrada"]
    D -->|Tenta Novamente| B
    
    C -->|Gera Senha Aleatória| E["✓ Testes de Validação<br/>(Tamanho, Caracteres,<br/>Critérios)"]
    
    E -->|Teste Aprovado| F["✅ Exibe Resultado<br/>(app/main.py)"]
    E -->|Teste Falho| G["⚠️ Rejeita Senha<br/>Gera Nova"]
    G -->|Tenta Novamente| C
    
    F -->|Exibe Senha Gerada| H["📤 Saída Final<br/>(Senha no Terminal)"]
    H -->|Fim| I["👋 Encerramento<br/>ou Gerar Outra"]
```

---

## Componentes do Sistema

### 1️⃣ **CLI (app/main.py)**
- Interface com o usuário
- Coleta de parâmetros
- Exibição de resultados

### 2️⃣ **Validação de Entrada**
- `get_password_length()` → Valida tamanho (4-128)
- `get_character_options()` → Valida tipos de caracteres
- Mensagens de erro específicas

### 3️⃣ **Módulo de Geração (app/password_generator.py)**
- Classe `PasswordGenerator`
- Método `generate()` → Cria senha aleatória
- Critérios configuráveis
- Uso de `random` e `string`

### 4️⃣ **Testes**
- `tests/test_password_generator.py` → Testes unitários
- Cobertura de cenários de sucesso e erro
- 20+ testes implementados

### 5️⃣ **Saída Final**
- Exibição formatada da senha
- Informações dos critérios utilizados
- Opção de gerar nova senha

---

## Estrutura de Pastas

```mermaid
graph LR
    A["gerador-senhas-seguras/"] --> B["main.py"]
    A --> C["password_generator.py"]
    A --> D["tests/"]
    A --> E["docs/"]
    A --> F["prompts/"]
    A --> G["README.md"]
    A --> H["PROJECT_SPEC.md"]
    A --> I[".gitignore"]
    
    D --> D1["test_password_generator.py"]
    D --> D2["__init__.py"]
    
    E --> E1["ARCHITECTURE.md"]
    E --> E2["architecture.mmd"]
    
    F --> F1["PROMPTS.md"]
    
    style A fill:#e1f5ff
    style B fill:#fff3e0
    style C fill:#fff3e0
    style D fill:#f3e5f5
    style E fill:#e8f5e9
    style F fill:#fce4ec
    style G fill:#fff9c4
    style H fill:#fff9c4
    style I fill:#f1f8e9
```

---

## Fluxo de Dados

```mermaid
sequenceDiagram
    participant User as 👤 Usuário
    participant CLI as 🖥️ CLI (main.py)
    participant Validator as ✅ Validador
    participant Generator as 🔐 Gerador
    participant Output as 📤 Saída
    
    User->>CLI: Inicia programa
    CLI->>User: Exibe menu
    User->>CLI: Insere tamanho e opções
    
    CLI->>Validator: Valida entradas
    alt Válido
        Validator->>CLI: ✓ Parâmetros OK
        CLI->>Generator: Chama generate()
        Generator->>Generator: Cria senha aleatória
        Generator->>CLI: Retorna senha
        CLI->>Output: Formata resultado
        Output->>User: Exibe senha
    else Inválido
        Validator->>CLI: ❌ Erro de validação
        CLI->>User: Mensagem de erro
        User->>CLI: Tenta novamente
    end
    
    User->>CLI: Gerar outra? S/N
    alt Sim
        CLI->>User: Volta ao menu
    else Não
        CLI->>User: Encerra programa
    end
```

---

## Camadas da Aplicação

```mermaid
graph TB
    subgraph UI["🎨 Camada de Interface"]
        A["print_header()"]
        B["get_password_length()"]
        C["get_character_options()"]
        D["get_yes_no()"]
    end
    
    subgraph Logic["⚙️ Camada de Lógica"]
        E["PasswordGenerator"]
        F["generate()"]
        G["_validate_parameters()"]
    end
    
    subgraph Data["📊 Camada de Dados"]
        H["string.ascii_uppercase"]
        I["string.ascii_lowercase"]
        J["string.digits"]
        K["string.punctuation"]
    end
    
    subgraph Tests["✓ Camada de Testes"]
        L["TestPasswordGenerator"]
        M["TestPasswordGeneratorIntegration"]
    end
    
    A --> E
    B --> G
    C --> E
    D --> B
    
    F --> H
    F --> I
    F --> J
    F --> K
    
    E -.->|testado por| L
    F -.->|testado por| M
    
    style UI fill:#e3f2fd
    style Logic fill:#f3e5f5
    style Data fill:#fff3e0
    style Tests fill:#e8f5e9
```

---

## Cenários de Fluxo

### ✅ Cenário de Sucesso

```mermaid
graph LR
    A["Usuário<br/>inicia"] --> B["Seleciona<br/>tamanho: 16"]
    B --> C["Seleciona<br/>critérios"]
    C --> D["Validação<br/>✓ OK"]
    D --> E["Geração<br/>de senha"]
    E --> F["Exibição<br/>resultado"]
    F --> G["Senha<br/>gerada"]
    
    style G fill:#c8e6c9,stroke:#2e7d32,stroke-width:3px
```

### ❌ Cenário de Erro

```mermaid
graph LR
    A["Usuário<br/>digita: 2"] --> B["Validação<br/>❌ ERRO"]
    B --> C["Mensagem:<br/>Mín. 4"]
    C --> D["Solicita<br/>novo valor"]
    D --> E["Usuário<br/>digita: 12"]
    E --> F["Validação<br/>✓ OK"]
    F --> G["Continua<br/>fluxo"]
    
    style B fill:#ffcdd2,stroke:#c62828,stroke-width:2px
    style G fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
```

---

## Ciclo de Vida da Aplicação

```mermaid
stateDiagram-v2
    [*] --> Inicio: python main.py
    
    Inicio --> Solicitacao: Exibe menu
    
    Solicitacao --> Validacao: Usuário insere dados
    
    Validacao --> Validacao: Dados inválidos
    Validacao --> Geracao: ✓ Dados válidos
    
    Geracao --> Exibicao: Senha gerada
    
    Exibicao --> Pergunta: Senha exibida
    
    Pergunta --> Solicitacao: S = Gerar outra
    Pergunta --> Finalizacao: N = Encerrar
    
    Finalizacao --> [*]: Programa finalizado
    
    note right of Validacao
        get_password_length()
        get_character_options()
        get_yes_no()
    end note
    
    note right of Geracao
        PasswordGenerator.generate()
        random.choice()
    end note
```

---

**Diagrama gerado em Markdown Mermaid**  
**Projeto:** Gerador de Senhas Seguras - MVP Acadêmico  
**Data:** 23 de Abril de 2026

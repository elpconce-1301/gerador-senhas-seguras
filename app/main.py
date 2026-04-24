"""
Gerador de Senhas Seguras - Interface CLI

Aplicação de linha de comando para gerar senhas aleatórias seguras.
Permite personalizar o tamanho e os tipos de caracteres inclusos.
"""

import sys
from .password_generator import PasswordGenerator


def print_header():
    """Exibe o cabeçalho da aplicação com formatação visual."""
    print("\n" + "=" * 50)
    print("    GERADOR DE SENHAS SEGURAS")
    print("=" * 50 + "\n")


def get_password_length() -> int:
    """
    Solicita ao usuário o tamanho da senha.

    Returns:
        int: Tamanho da senha

    Raises:
        ValueError: Se a entrada for inválida
    """
    while True:
        try:
            length = input("Digite o tamanho da senha (4-128): ").strip()
            if not length:
                print("⚠️  Comprimento deve ser um número inteiro")
                continue
            length = int(length)
            if length < 4:
                print("⚠️  Comprimento mínimo é 4 caracteres")
                continue
            if length > 128:
                print("⚠️  Comprimento máximo é 128 caracteres")
                continue
            return length
        except ValueError:
            print("⚠️  Comprimento deve ser um número inteiro")


def get_character_options() -> dict:
    """
    Solicita ao usuário quais tipos de caracteres incluir na senha.

    Returns:
        dict: Dicionário com as opções selecionadas
    """
    options = {
        "use_uppercase": False,
        "use_lowercase": False,
        "use_digits": False,
        "use_special": False,
    }

    print("\nEscolha os tipos de caracteres a incluir:")

    while True:
        # Solicitar cada tipo
        options["use_uppercase"] = get_yes_no("Incluir letras MAIÚSCULAS? (S/N): ")
        options["use_lowercase"] = get_yes_no("Incluir letras minúsculas? (S/N): ")
        options["use_digits"] = get_yes_no("Incluir NÚMEROS? (S/N): ")
        options["use_special"] = get_yes_no(
            "Incluir caracteres ESPECIAIS (!@#$%...)? (S/N): "
        )

        # Validar se pelo menos um tipo foi selecionado
        if any(options.values()):
            return options
        else:
            print(
                "⚠️  Selecione pelo menos um tipo de caractere!\n"
            )


def get_yes_no(prompt: str) -> bool:
    """
    Solicita uma resposta sim/não ao usuário.

    Args:
        prompt: Texto a exibir

    Returns:
        bool: True para sim, False para não
    """
    while True:
        response = input(prompt).strip().upper()
        if response in ["S", "SIM", "Y", "YES"]:
            return True
        elif response in ["N", "NÃO", "NO"]:
            return False
        else:
            print("⚠️  Digite 'S' (sim) ou 'N' (não)!")


def generate_and_display_password(generator: PasswordGenerator):
    """
    Gera e exibe uma nova senha.

    Args:
        generator: Instância do gerador de senhas
    """
    try:
        length = get_password_length()
        options = get_character_options()

        password = generator.generate(
            length=length,
            use_uppercase=options["use_uppercase"],
            use_lowercase=options["use_lowercase"],
            use_digits=options["use_digits"],
            use_special=options["use_special"],
        )

        print("\n" + "=" * 50)
        print(f"✓ Senha gerada com sucesso!")
        print(f"  Tamanho: {length} caracteres")
        print(f"  Maiúsculas: {'Sim' if options['use_uppercase'] else 'Não'}")
        print(f"  Minúsculas: {'Sim' if options['use_lowercase'] else 'Não'}")
        print(f"  Números: {'Sim' if options['use_digits'] else 'Não'}")
        print(f"  Especiais: {'Sim' if options['use_special'] else 'Não'}")
        print("=" * 50)
        print(f"\n  SENHA: {password}\n")
        print("=" * 50 + "\n")

    except ValueError as e:
        print(f"❌ Erro: {e}\n")


def main():
    """Função principal - executa a aplicação CLI."""
    generator = PasswordGenerator()

    print_header()
    print("Bem-vindo! Use este programa para gerar senhas seguras.\n")

    while True:
        try:
            generate_and_display_password(generator)

            # Perguntar se deseja gerar outra senha
            again = input("Deseja gerar outra senha? (S/N): ").strip().upper()
            if again in ["N", "NÃO", "NO"]:
                print("\n✓ Obrigado por usar o Gerador de Senhas Seguras!")
                print("Até logo!\n")
                break

        except KeyboardInterrupt:
            print("\n\n❌ Programa interrompido pelo usuário.")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Erro inesperado: {e}\n")


if __name__ == "__main__":
    main()

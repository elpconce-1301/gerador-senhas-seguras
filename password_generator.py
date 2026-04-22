"""
Módulo para geração de senhas seguras.
Fornece funcionalidades para criar senhas aleatórias com critérios personalizáveis.
"""

import random
import string


class PasswordGenerator:
    """Classe responsável pela geração de senhas seguras."""

    def __init__(self):
        """Inicializa o gerador de senhas."""
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def generate(
        self,
        length: int,
        use_uppercase: bool = True,
        use_lowercase: bool = True,
        use_digits: bool = True,
        use_special: bool = False,
    ) -> str:
        """
        Gera uma senha aleatória conforme os critérios especificados.

        Args:
            length: Tamanho da senha (mínimo 4, máximo 128)
            use_uppercase: Incluir letras maiúsculas
            use_lowercase: Incluir letras minúsculas
            use_digits: Incluir números
            use_special: Incluir caracteres especiais

        Returns:
            str: Senha gerada

        Raises:
            ValueError: Se os parâmetros forem inválidos
        """
        self._validate_parameters(
            length, use_uppercase, use_lowercase, use_digits, use_special
        )

        # Construir o conjunto de caracteres disponíveis
        available_chars = ""
        if use_uppercase:
            available_chars += self.uppercase
        if use_lowercase:
            available_chars += self.lowercase
        if use_digits:
            available_chars += self.digits
        if use_special:
            available_chars += self.special_chars

        # Gerar a senha
        password = "".join(random.choice(available_chars) for _ in range(length))

        return password

    def _validate_parameters(
        self,
        length: int,
        use_uppercase: bool,
        use_lowercase: bool,
        use_digits: bool,
        use_special: bool,
    ) -> None:
        """
        Valida os parâmetros de entrada.

        Args:
            length: Tamanho da senha
            use_uppercase: Usar maiúsculas
            use_lowercase: Usar minúsculas
            use_digits: Usar dígitos
            use_special: Usar caracteres especiais

        Raises:
            ValueError: Se algum parâmetro for inválido
        """
        # Validar comprimento
        if not isinstance(length, int):
            raise ValueError("Comprimento deve ser um número inteiro")
        if length < 4:
            raise ValueError("Comprimento mínimo é 4 caracteres")
        if length > 128:
            raise ValueError("Comprimento máximo é 128 caracteres")

        # Validar se pelo menos um tipo de caractere foi selecionado
        if not any([use_uppercase, use_lowercase, use_digits, use_special]):
            raise ValueError(
                "Selecione pelo menos um tipo de caractere: maiúsculas, minúsculas, números ou especiais"
            )

        # Validar tipos booleanos
        for value in [use_uppercase, use_lowercase, use_digits, use_special]:
            if not isinstance(value, bool):
                raise ValueError("Opções de caracteres devem ser verdadeiras ou falsas")

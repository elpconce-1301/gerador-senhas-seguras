"""
Testes unitários para o módulo de geração de senhas.

Cobre cenários de sucesso e erros para validar a funcionalidade
do gerador de senhas seguras.
"""

import unittest
import sys
import os

# Adicionar o diretório pai ao path para importar o módulo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):
    """Testes unitários para a classe PasswordGenerator."""

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.generator = PasswordGenerator()

    # Testes de sucesso
    def test_generate_basic_password(self):
        """Testa a geração de uma senha básica."""
        password = self.generator.generate(length=8)
        self.assertEqual(len(password), 8)
        self.assertIsInstance(password, str)

    def test_generate_with_uppercase(self):
        """Testa geração com apenas letras maiúsculas."""
        password = self.generator.generate(
            length=10, use_uppercase=True, use_lowercase=False, use_digits=False
        )
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c.isupper() or c.isalpha() for c in password))

    def test_generate_with_lowercase(self):
        """Testa geração com apenas letras minúsculas."""
        password = self.generator.generate(
            length=10, use_uppercase=False, use_lowercase=True, use_digits=False
        )
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c.islower() for c in password))

    def test_generate_with_digits(self):
        """Testa geração com apenas números."""
        password = self.generator.generate(
            length=10,
            use_uppercase=False,
            use_lowercase=False,
            use_digits=True,
        )
        self.assertEqual(len(password), 10)
        self.assertTrue(password.isdigit())

    def test_generate_with_special_chars(self):
        """Testa geração com caracteres especiais."""
        password = self.generator.generate(
            length=10,
            use_uppercase=False,
            use_lowercase=False,
            use_digits=False,
            use_special=True,
        )
        self.assertEqual(len(password), 10)
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.assertTrue(all(c in special_chars for c in password))

    def test_generate_mixed_characters(self):
        """Testa geração com múltiplos tipos de caracteres."""
        password = self.generator.generate(
            length=20,
            use_uppercase=True,
            use_lowercase=True,
            use_digits=True,
            use_special=True,
        )
        self.assertEqual(len(password), 20)
        self.assertIsInstance(password, str)

    def test_minimum_length(self):
        """Testa a geração de senha com tamanho mínimo."""
        password = self.generator.generate(length=4)
        self.assertEqual(len(password), 4)

    def test_maximum_length(self):
        """Testa a geração de senha com tamanho máximo."""
        password = self.generator.generate(length=128)
        self.assertEqual(len(password), 128)

    def test_different_lengths(self):
        """Testa a geração de senhas com diferentes tamanhos."""
        for length in [4, 10, 20, 50, 100, 128]:
            password = self.generator.generate(length=length)
            self.assertEqual(len(password), length)

    def test_randomness(self):
        """Testa se as senhas geradas são diferentes."""
        passwords = [self.generator.generate(length=10) for _ in range(10)]
        # Verifica se há pelo menos 8 senhas diferentes (improvável ser idêntica por acaso)
        self.assertGreater(len(set(passwords)), 7)

    # Testes de erro - Validação
    def test_invalid_length_string(self):
        """Testa erro quando tamanho é uma string."""
        with self.assertRaises(ValueError):
            self.generator.generate(length="abc")

    def test_invalid_length_below_minimum(self):
        """Testa erro quando tamanho é menor que 4."""
        with self.assertRaises(ValueError):
            self.generator.generate(length=3)

    def test_invalid_length_zero(self):
        """Testa erro quando tamanho é zero."""
        with self.assertRaises(ValueError):
            self.generator.generate(length=0)

    def test_invalid_length_negative(self):
        """Testa erro quando tamanho é negativo."""
        with self.assertRaises(ValueError):
            self.generator.generate(length=-5)

    def test_invalid_length_above_maximum(self):
        """Testa erro quando tamanho é maior que 128."""
        with self.assertRaises(ValueError):
            self.generator.generate(length=129)

    def test_no_character_types_selected(self):
        """Testa erro quando nenhum tipo de caractere é selecionado."""
        with self.assertRaises(ValueError):
            self.generator.generate(
                length=8,
                use_uppercase=False,
                use_lowercase=False,
                use_digits=False,
                use_special=False,
            )

    def test_invalid_boolean_parameter(self):
        """Testa erro quando um parâmetro booleano é inválido."""
        with self.assertRaises(ValueError):
            self.generator.generate(length=8, use_uppercase="sim")

    def test_invalid_float_length(self):
        """Testa erro quando tamanho é um float."""
        with self.assertRaises(ValueError):
            self.generator.generate(length=8.5)


class TestPasswordGeneratorIntegration(unittest.TestCase):
    """Testes de integração para cenários combinados."""

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.generator = PasswordGenerator()

    def test_typical_secure_password(self):
        """Testa geração de uma senha típica segura."""
        password = self.generator.generate(
            length=16,
            use_uppercase=True,
            use_lowercase=True,
            use_digits=True,
            use_special=True,
        )
        self.assertEqual(len(password), 16)
        self.assertIsInstance(password, str)
        # Verifica se contém pelo menos alguns dos tipos esperados
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))

    def test_multiple_password_generation(self):
        """Testa geração de múltiplas senhas sem erros."""
        for _ in range(100):
            password = self.generator.generate(
                length=12,
                use_uppercase=True,
                use_lowercase=True,
                use_digits=True,
            )
            self.assertEqual(len(password), 12)


if __name__ == "__main__":
    unittest.main()

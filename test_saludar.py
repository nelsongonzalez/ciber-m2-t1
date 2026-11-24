from __future__ import annotations

from unittest.mock import patch

import pytest

import saludar


class TestSaludar:
    def test_saludo1(self) -> None:
        assert "Hola" == saludar.saludo1()

    def test_saludo2(self) -> None:
        assert "Buenos días" == saludar.saludo2()

    def test_saludo3(self) -> None:
        assert "Hola, ¿Qué tal?" == saludar.saludo3()

    @pytest.mark.parametrize(
        "valor_aleatorio, esperado",
        [
            (0, "Hola"),
            (1, "Buenos días"),
            (2, "Hola, ¿Qué tal?"),
            (3, "Adios"),
            (-1, "Adios"),
        ],
    )
    def test_main_branches(
        self,
        valor_aleatorio: int,
        esperado: str,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        with patch("saludar.random.randint", return_value=valor_aleatorio):
            saludar.main()

        captured = capsys.readouterr()
        assert esperado == captured.out.strip()
        assert "" == captured.err

    def test_main_calls_randint_with_expected_bounds(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        with patch("saludar.random.randint", return_value=0) as mock_randint:
            saludar.main()

        mock_randint.assert_called_once_with(0, 2)
        assert "Hola" == capsys.readouterr().out.strip()

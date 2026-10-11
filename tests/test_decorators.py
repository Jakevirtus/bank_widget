import pytest

from src.decorators import log


class TestLogToConsole:
    """Тесты декоратора log с выводом в консоль."""

    def test_success_prints_to_console(self, capsys):
        """Успешное выполнение функции — вывод в консоль."""

        @log()
        def add(x, y):
            return x + y

        result = add(1, 2)

        captured = capsys.readouterr()
        assert result == 3
        assert "add ok" in captured.out

    def test_error_prints_to_console(self, capsys):
        """Ошибка — вывод в консоль с параметрами."""

        @log()
        def divide(x, y):
            return x / y

        with pytest.raises(ZeroDivisionError):
            divide(1, 0)

        captured = capsys.readouterr()
        assert "divide error" in captured.out
        assert "Inputs: (1, 0), {}" in captured.out

    def test_error_message_contains_error_type(self, capsys):
        """Сообщение об ошибке содержит тип ошибки."""

        @log()
        def raise_value_error():
            raise ValueError("неверное значение")

        with pytest.raises(ValueError):
            raise_value_error()

        captured = capsys.readouterr()
        assert "raise_value_error error" in captured.out
        assert "неверное значение" in captured.out

    def test_kwargs_logged(self, capsys):
        """Проверяет логирование kwargs."""

        @log()
        def greet(name, greeting="Привет"):
            return f"{greeting}, {name}"

        greet("Иван", greeting="Здравствуйте")

        captured = capsys.readouterr()
        assert "greet ok" in captured.out


class TestLogToFile:
    """Тесты декоратора log с записью в файл."""

    def test_success_writes_to_file(self, tmp_path):
        """Успешное выполнение — запись в файл."""
        log_file = tmp_path / "test.log"

        @log(filename=str(log_file))
        def multiply(x, y):
            return x * y

        result = multiply(3, 4)

        assert result == 12
        content = log_file.read_text(encoding="utf-8")
        assert "multiply ok" in content

    def test_error_writes_to_file(self, tmp_path):
        """Ошибка — запись в файл с параметрами."""
        log_file = tmp_path / "error.log"

        @log(filename=str(log_file))
        def divide(x, y):
            return x / y

        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

        content = log_file.read_text(encoding="utf-8")
        assert "divide error" in content
        assert "Inputs: (10, 0), {}" in content

    def test_file_appends_multiple_calls(self, tmp_path):
        """Несколько вызовов — несколько строк в файле."""
        log_file = tmp_path / "multi.log"

        @log(filename=str(log_file))
        def square(x):
            return x ** 2

        square(2)
        square(3)

        content = log_file.read_text(encoding="utf-8")
        assert content.count("square ok") == 2

    def test_console_silent_when_file_given(self, tmp_path, capsys):
        """Если filename задан — в консоль ничего не пишется."""
        log_file = tmp_path / "silent.log"

        @log(filename=str(log_file))
        def hello():
            return "world"

        hello()

        captured = capsys.readouterr()
        assert captured.out == ""


class TestLogReturnValue:
    """Проверяет, что декоратор не искажает возвращаемое значение."""

    def test_return_value_preserved(self):
        """Функция возвращает то же, что и без декоратора."""

        @log()
        def get_data():
            return {"key": "value"}

        assert get_data() == {"key": "value"}

    def test_function_metadata_preserved(self):
        """@wraps сохраняет имя и docstring функции."""

        @log()
        def documented():
            """Это docstring."""
            return 42

        assert documented.__name__ == "documented"
        assert documented.__doc__ == "Это docstring."

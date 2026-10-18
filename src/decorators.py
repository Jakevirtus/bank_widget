from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функций.

    Логирует имя функции и результат при успешном выполнении,
    либо имя функции, текст ошибки и входные параметры при исключении.

    Args:
        filename: Имя файла для записи логов. Если None — вывод в консоль.

    Returns:
        Декоратор, оборачивающий функцию.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                _write_log(message, filename)
                return result
            except Exception as error:
                message = (
                    f"{func.__name__} error: {error}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(message, filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    """Записывает сообщение в файл или консоль.

    Args:
        message: Текст сообщения.
        filename: Имя файла. Если None — вывод в консоль.
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
    else:
        print(message)

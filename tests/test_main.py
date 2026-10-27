from unittest.mock import patch

from src.main import main


@patch("builtins.input", side_effect=["1", "EXECUTED", "нет", "нет", "нет"])
@patch("src.main.load_transactions")
def test_main_json_flow(mock_load, mock_input, capsys):
    # Обрати внимание на фигурные скобки и запятые внутри!
    mock_load.return_value = [
        {
            "state": "EXECUTED",
            "date": "2024-03-11T02:26:18.671407",
            "description": "Перевод",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "руб.", "code": "RUB"},
            },
        }
    ]

    main()

    captured = capsys.readouterr()
    assert "Всего банковских операций в выборке: 1" in captured.out

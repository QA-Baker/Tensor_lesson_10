# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


# Тест с параметрами, используя @pytest.mark.parametrize
@pytest.mark.parametrize(
    "args, expected",
    [
        pytest.param((10, 2), 5, marks=pytest.mark.smoke),  # smoke-тест
        ((100, 2, 5), 10),  # обычный тест
        pytest.param((-20, 2), -10, marks=pytest.mark.skip(reason="Negative case skipped")),  # скипнутый тест
        ((5.0, 2), 2.5),  # обычный тест
        pytest.param((10, 0), None, marks=pytest.mark.xfail(raises=ZeroDivisionError)),  # тест, ожидающий исключение
    ],
)
def test_all_division(args, expected):
    if expected is None:
        with pytest.raises(ZeroDivisionError):
            all_division(*args)
    else:
        assert all_division(*args) == expected

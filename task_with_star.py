# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    # Получаем маркер id_check
    marker = request.node.get_closest_marker("id_check")
    if marker:
        # Выводим аргументы маркера
        print(", ".join(map(str, marker.args)))

# для выполнения теста в консоли pytest task_with_star.py -s

# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


class TestExample:
    @pytest.fixture(autouse=True, scope="class")
    def setup_class(self, request):
        # Эта фикстура автоматически выполняется перед всеми тестами класса
        start_time = time.time()
        print(f"\n[INFO] Начало тестов класса {request.node.name} в {time.strftime('%H:%M:%S')}")
        yield
        end_time = time.time()
        print(f"\n[INFO] Завершение тестов класса {request.node.name} в {time.strftime('%H:%M:%S')}")
        print(f"[INFO] Общая продолжительность выполнения: {end_time - start_time:.2f} секунд")

    @pytest.mark.usefixtures("track_test_time")
    def test_example_1(self):
        time.sleep(1)
        assert 1 + 1 == 2

    def test_example_2(self):
        time.sleep(2)
        assert 2 * 2 == 4

    @pytest.mark.usefixtures("track_test_time")
    def test_example_3(self):
        time.sleep(0.5)
        assert 3 - 1 == 2

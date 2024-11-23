import pytest
import time


@pytest.fixture
def track_test_time(request):
    # Фикстура для замера времени выполнения отдельного теста
    start_time = time.time()
    print(f"\n[INFO] Тест {request.node.name} начался в {time.strftime('%H:%M:%S')}")
    yield
    end_time = time.time()
    print(f"[INFO] Тест {request.node.name} закончился в {time.strftime('%H:%M:%S')}")
    print(f"[INFO] Продолжительность теста {request.node.name}: {end_time - start_time:.2f} секунд")

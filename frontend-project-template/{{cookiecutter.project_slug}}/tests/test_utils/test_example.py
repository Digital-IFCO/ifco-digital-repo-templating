from backend.sum import sum_values
from frontend.models.sidebar import SideBarModel

side_bar_model = SideBarModel(first_number=2, second_number=3)


def test_my_func():
    assert sum_values(side_bar_model) == 5

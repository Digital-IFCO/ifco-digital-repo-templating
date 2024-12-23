from frontend.models.sidebar import SideBarModel


def sum_values(side_bar_model: SideBarModel) -> int:
    return side_bar_model.first_number + side_bar_model.second_number
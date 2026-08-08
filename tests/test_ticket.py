import pytest
from ticket_service import calculate_ticket_price

# TC01: Bình thường - Người lớn, giờ thường
def test_tc01_normal_adult_regular_hour():
    assert calculate_ticket_price(25, 14) == 100000

# TC02: Bình thường - Trẻ em, giờ vàng
def test_tc02_normal_child_peak_hour():
    assert calculate_ticket_price(8, 19) == 70000

# TC03: Boundary Case - Biên dưới tuổi (age = 0)
def test_tc03_boundary_min_age():
    assert calculate_ticket_price(0, 10) == 50000

# TC04: Boundary Case - Mốc tuổi 12
def test_tc04_boundary_age_12():
    assert calculate_ticket_price(12, 10) == 100000

# TC05: Boundary Case - Mốc bắt đầu giờ vàng (hour = 18)
def test_tc05_boundary_peak_hour_start():
    assert calculate_ticket_price(30, 18) == 120000

# TC06: Edge Case - Tuổi max (120), giờ muộn (23)
def test_tc06_edge_max_age_and_late_hour():
    assert calculate_ticket_price(120, 23) == 70000

# TC07: Dữ liệu sai - Tuổi âm (age = -5)
def test_tc07_invalid_negative_age():
    with pytest.raises(ValueError, match="Độ tuổi không hợp lệ"):
        calculate_ticket_price(-5, 15)

# TC08: Dữ liệu sai - Giờ vượt quá 23 (hour = 24)
def test_tc08_invalid_hour_overflow():
    with pytest.raises(ValueError, match="Khung giờ chiếu phải từ 0 đến 23"):
        calculate_ticket_price(20, 24)

# TC09: Dữ liệu rỗng - Tham số None
def test_tc09_null_input():
    with pytest.raises(TypeError):
        calculate_ticket_price(None, 10)

# TC10: Error Handling - Sai kiểu dữ liệu
def test_tc10_invalid_data_type():
    with pytest.raises(TypeError, match="Tuổi và giờ chiếu phải là số nguyên"):
        calculate_ticket_price("20", 10)
""""
Module: ticket_service.py
Chức năng: Tính giá vé xem phim dựa trên độ tuổi và khung giờ chiếu.
"""

def calculate_ticket_price(age: int, hour: int) -> int:
    # Check kiểu dữ liệu
    if not isinstance(age, int) or not isinstance(hour, int) or isinstance(age, bool) or isinstance(hour, bool):
        raise TypeError("Tuổi và giờ chiếu phải là số nguyên (int).")

    # Check độ tuổi
    if age < 0:
        raise ValueError("Độ tuổi không hợp lệ.")

    # Check khung giờ
    if hour < 0 or hour > 23:
        raise ValueError("Khung giờ chiếu phải từ 0 đến 23.")

    # Tính giá cơ bản
    if age < 12:
        price = 50000
    elif age <= 60:
        price = 100000
    else:
        price = 70000

    # Phụ thu giờ vàng
    if 18 <= hour <= 21:
        price += 20000

    return price
# KẾ HOẠCH KIỂM THỬ (TEST PLAN)

## 1. Giới thiệu & Phạm vi
Kiểm thử tự động hàm `calculate_ticket_price` nhằm đảm bảo thuật toán tính giá vé đúng theo độ tuổi, giờ vàng và xử lý ngoại lệ đầu vào chuẩn xác.

## 2. Danh sách 10 Test Cases

| Mã TC | Phân loại | Tên Test Case | Input | Kết quả kỳ vọng |
| :--- | :--- | :--- | :--- | :--- |
| **TC01** | Normal | Người lớn, giờ thường | `age=25, hour=14` | Return `100,000` |
| **TC02** | Normal | Trẻ em, giờ vàng | `age=8, hour=19` | Return `70,000` |
| **TC03** | Boundary | Biên dưới độ tuổi | `age=0, hour=10` | Return `50,000` |
| **TC04** | Boundary | Mốc chuyển tiếp độ tuổi | `age=12, hour=10` | Return `100,000` |
| **TC05** | Boundary | Mốc bắt đầu giờ vàng | `age=30, hour=18` | Return `120,000` |
| **TC06** | Edge Case | Cực hạn tuổi & giờ | `age=120, hour=23` | Return `70,000` |
| **TC07** | Invalid | Dữ liệu tuổi âm | `age=-5, hour=15` | Raise `ValueError` |
| **TC08** | Invalid | Giờ ngoài khoảng 0-23 | `age=20, hour=24` | Raise `ValueError` |
| **TC09** | Null/Empty | Tham số rỗng/Null | `age=None, hour=10` | Raise `TypeError` |
| **TC10** | Error Handling | Sai kiểu dữ liệu truyền vào | `age="20", hour=10` | Raise `TypeError` |
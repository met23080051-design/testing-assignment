# BÁO CÁO KẾT QUẢ KIỂM THỬ VÀ ỨNG DỤNG AGENT SKILLS IN TESTING

---

## 1. Báo cáo tổng quan (Final Test Summary)

* **Tổng số Test Cases:** 10
* **Số Test Pass (Chạy lần 1 - Mã nguồn gốc):** 8 / 10
* **Số Test Fail (Chạy lần 1 - Mã nguồn gốc):** 2 / 10 (`TC05`, `TC07`)
* **Số Test Pass sau khi Sửa lỗi (Chạy lần 2 - Retest):** 10 / 10 (Tỷ lệ đạt 100%)

---

## 2. Chi tiết Lỗi phát hiện (Bugs) và Cách sửa đổi

### Lỗi 1: Bỏ sót giá trị biên giờ vàng (TC05 - Boundary Case)
* **Test kiểm tra gì:** Kiểm tra chức năng áp dụng phụ thu 20,000 VNĐ giờ vàng khi khách hàng xem phim vào đúng mốc **18:00** (`hour = 18`).
* **Tại sao Fail:** Mã nguồn ban đầu sử dụng phép so sánh `hour > 18` thay vì `hour >= 18`. Khi dữ liệu đầu vào là `hour = 18`, biểu thức so sánh trả về `False`, khiến chương trình bỏ qua khoản phụ thu 20,000 VNĐ.
* **Tại sao cách sửa phù hợp:** Sửa điều kiện so sánh thành `18 <= hour <= 21`. Việc sử dụng toán tử `>=` ở biên dưới đảm bảo tính đúng phụ thu cho tất cả suất chiếu bắt đầu từ đúng 18 giờ 00 phút đến 21 giờ 00 phút theo đúng Yêu cầu Nghiệp vụ (Business Requirement).

### Lỗi 2: Bỏ sót kiểm tra dữ liệu đầu vào không hợp lệ (TC07 - Invalid / Error Handling)
* **Test kiểm tra gì:** Đảm bảo hệ thống ném ra ngoại lệ `ValueError` với thông báo hợp lệ khi người dùng truyền giá trị độ tuổi âm (`age = -5`).
* **Tại sao Fail:** Mã nguồn gốc hoàn toàn thiếu câu lệnh kiểm tra điều kiện biên dưới của tham số `age`. Khi truyền `age = -5`, chương trình nhảy thẳng vào nhánh kiểm tra `age < 12` và trả về mức giá 50,000 VNĐ thay vì báo lỗi.
* **Tại sao cách sửa phù hợp:** Thêm câu lệnh Guard Clause `if age < 0 or age > 120: raise ValueError("Độ tuổi không hợp lệ.")` ở ngay đầu hàm. Việc chặn dữ liệu sai ngay từ luồng đầu vào giúp bảo vệ tính toàn vẹn dữ liệu, tránh việc hệ thống tính toán sai lệch trên các tham số không có thực trong thực tế.

---

## 3. Phân tích vai trò: AI đã hỗ trợ gì vs Sinh viên tự kiểm tra / quyết định

| Nội dung | AI Agent / Agent Skills hỗ trợ | Sinh viên tự kiểm tra & ra quyết định (Human-in-the-Loop) |
| :--- | :--- | :--- |
| **Phân tích dự án** | Tự động đọc mã nguồn, phân tích các luồng điều kiện (if/else) và gợi ý các vùng tiềm ẩn rủi ro lỗi logic. | Đọc lại cấu trúc chức năng, xác định quy tắc nghiệp vụ (Business Rules) chính của bài toán để làm cơ sở đánh giá. |
| **Tạo Test Case** | Tự động sinh file script PyTest chuẩn cú pháp, phủ rộng các kịch bản (Normal, Boundary, Edge, Error Handling). | Review toàn bộ 10 kịch bản AI đề xuất, điều chỉnh lại giá trị kỳ vọng (Expected Output) cho đúng với logic bài toán thực tế. |
| **Debug & Sửa code** | Phân tích log lỗi (Stack Trace) từ Terminal khi test Fail, chỉ ra chính xác dòng code bị bug và đề xuất mã vá lỗi (Patch). | Đánh giá đoạn code sửa của AI xem có vi phạm logic chung không, trực tiếp duyệt (Approve) code trước khi áp dụng vào file chính. |
| **Đảm bảo chất lượng** | Hỗ trợ thực thi lệnh test tự động nhanh chóng. | Tự tay thao tác chạy lại toàn bộ bộ test trên Terminal (`Re-test`) để đảm bảo không phát sinh lỗi ẩn mới (Regression). |

---

## 4. Báo cáo sử dụng Agent Skills in Testing

### 🟢 Các Agent Skills đã sử dụng:
1. **Codebase Analysis Skill:** Dùng để đọc hiểu cây thư mục, quy trình xử lý dữ liệu và cấu trúc điều kiện trong `ticket_service.py`.
2. **Test Generation Skill:** Dùng để áp dụng kỹ thuật Phân vùng tương đương (Equivalence Partitioning) và Phân tích giá trị biên (Boundary Value Analysis) nhằm tạo bộ kịch bản test phủ kín các trường hợp.
3. **Automated Debug & Patch Skill:** Dùng để phân tích nguyên nhân gốc (Root Cause Analysis) khi test FAILED và tự động sinh mã sửa lỗi.

### ❓ Tại sao dùng các Skills này?
* **Tối ưu thời gian và công sức:** Giúp tự động hóa công việc viết mã test lặp đi lặp lại và phát hiện lỗi tức thì thay vì phải test thủ công từng giá trị bằng hàm `print()`.
* **Nâng cao độ bao phủ (Test Coverage):** Đảm bảo bài kiểm thử không bị bỏ sót các trường hợp cực hạn (Edge Cases) hoặc trường hợp dữ liệu sai mà lập trình viên thường quên xử lý.
* **Đảm bảo chuẩn quy trình QA/QC chuyên nghiệp:** Thể hiện rõ mô hình tương tác giữa con người và AI (Human-in-the-loop), trong đó AI đóng vai trò là trợ lý thực thi tốc độ cao, còn sinh viên đóng vai trò là QA Lead kiểm soát chất lượng và đưa ra quyết định cuối cùng.
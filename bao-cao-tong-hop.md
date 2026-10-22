# Báo cáo tổng hợp dự án quản lý dữ liệu mỹ phẩm

## 1. Mục tiêu dự án

Dự án này nhằm:

- chuẩn hóa dữ liệu sản phẩm từ file Excel sang JSON và CSV
- kiểm tra và sửa lỗi dữ liệu: tên sản phẩm, dung tích, giá tiền, công dụng, ảnh
- tạo giao diện hiển thị sản phẩm dạng card
- hỗ trợ tìm kiếm, lọc theo danh mục, thêm/sửa/xóa sản phẩm
- cho phép chọn dung tích và hiển thị giá tương ứng đúng theo từng mức dung tích
- lưu dữ liệu đã chỉnh sửa vào file JSON hiện hành

## 2. Tài nguyên và nguồn dữ liệu

- File Excel nguồn: `data/Data mỹ phẩm.xlsx`
- Thư mục ảnh: `data/Hình ảnh mỹ phẩm/`
- File dữ liệu làm việc: `data/products_clean.json`
- File CSV export: `data/products_clean.csv`
- File frontend: `frontend/index.html`
- File xử lý dữ liệu: `scripts/normalize_product_data.py`

## 3. Vấn đề dữ liệu đã xử lý

### 3.1 Lỗi về công dụng sản phẩm

- Công dụng trước đây bị lấy chung cho nhiều sản phẩm, không theo từng dòng dữ liệu.
- Một số sản phẩm thiếu hoặc bị gán sai nội dung công dụng.
- Đã sửa bằng cách lấy dữ liệu từ đúng cột công dụng theo từng sản phẩm, thay vì dùng giá trị chung.

### 3.2 Lỗi về giá tiền và dung tích

- Giá tiền xuất hiện với nhiều định dạng khác nhau như:
  - `245.000 ₫`
  - `245000`
  - `245.000_399.000_599.000`
  - `245000_399000_599000`
- Dung tích cũng xuất hiện dưới nhiều kiểu như:
  - `100ml_250ml_500ml`
  - `100ml;250ml;500ml`
  - `100ml/250ml/500ml`
- Đã chuẩn hóa về một format thống nhất:
  - giá tiền dạng số nguyên không ký hiệu: `245000_399000_599000`
  - dung tích dạng chuẩn: `100ml_250ml_500ml`

### 3.3 Lỗi ảnh sản phẩm

- Một số sản phẩm không có ảnh hoặc ảnh bị sai đường dẫn.
- Có sản phẩm bị trùng ảnh hoặc trùng tên tương đồng.
- Đã kiểm tra lại và đồng bộ đường dẫn ảnh sao cho hợp lệ.

## 4. Chức năng giao diện đã hoàn thiện

### 4.1 Hiển thị sản phẩm dạng card

- Hiển thị tên, thương hiệu, loại da, danh mục và công dụng
- Hiển thị ảnh đại diện của sản phẩm
- Hiển thị giá theo từng dung tích

### 4.2 Tìm kiếm và lọc

- Tìm kiếm theo tên và các thuộc tính sản phẩm
- Lọc theo danh mục

### 4.3 Quản lý sản phẩm

- Thêm sản phẩm mới
- Chỉnh sửa thông tin sản phẩm
- Xóa sản phẩm
- Upload ảnh từ máy tính
- Lưu dữ liệu trực tiếp vào file JSON đang dùng

### 4.4 Chọn dung tích theo giá tương ứng

- Mỗi sản phẩm có thể có nhiều mức dung tích
- Khi click vào nút dung tích, giá hiển thị thay đổi theo đúng mức tương ứng
- Ví dụ:
  - 100ml -> 245.000₫
  - 250ml -> 445.000₫
  - 500ml -> 560.000₫

## 5. Quy trình xử lý dữ liệu

1. Đọc dữ liệu từ file Excel hoặc fallback sang file CSV nếu Excel bị khóa.
2. Chuẩn hóa từng cột dữ liệu: tên cột, chữ hoa/thường, dấu cách, ký hiệu.
3. Tách giá và dung tích theo cấu trúc phân tách như `_`, `;`, `/`, `-`.
4. Chuẩn hóa tiền về dạng số nguyên không ký hiệu.
5. Map dung tích với giá đúng thứ tự tương ứng.
6. Tìm kiếm và gán ảnh phù hợp cho từng sản phẩm.
7. Xuất dữ liệu ra JSON và CSV sạch.

## 6. Kết quả đạt được

- Dữ liệu sản phẩm đã được chuẩn hóa rõ ràng hơn
- Công dụng không còn bị lặp hoặc nhầm giữa các sản phẩm
- Giá tiền được chuẩn hóa đúng định dạng và hiển thị rõ ràng
- UI cho phép chọn dung tích và đổi giá tương ứng chính xác
- Hệ thống quản lý sản phẩm hoạt động tốt hơn về mặt dữ liệu và giao diện

## 7. Một số lưu ý kỹ thuật

- File Excel nguồn có thể bị khóa bởi Windows nếu đang mở ở chế độ khác, nên script có cơ chế fallback đến file CSV để tránh lỗi.
- Dữ liệu cần được kiểm tra định kỳ khi có cập nhật mới từ file Excel.
- Nên lưu dữ liệu chuẩn cuối cùng vào JSON làm dữ liệu nguồn chính để frontend luôn đọc đúng.

## 8. Kết luận

Dự án đã đạt được mục tiêu chính: chuẩn hóa dữ liệu mỹ phẩm, sửa lỗi về công dụng, giá và dung tích, đồng thời nâng cấp giao diện để hiển thị và quản lý sản phẩm dễ dàng hơn. Đây là nền tảng phù hợp để tiếp tục phát triển các tính năng bán hàng, lọc và thống kê sau này.

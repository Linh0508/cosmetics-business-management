# Cosmetics Sales Management

Hệ thống quản lý và phân tích bán hàng ngành mỹ phẩm tích hợp trí tuệ nhân tạo chạy cục bộ, hỗ trợ phân tích dữ liệu, dự báo nhu cầu và ra quyết định kinh doanh.

## 📌 Giới thiệu

Cosmetics Sales Management là hệ thống hỗ trợ quản lý hoạt động kinh doanh mỹ phẩm, bao gồm quản lý sản phẩm, kho hàng, đơn hàng, khách hàng và doanh thu.

Hệ thống tích hợp các chức năng phân tích dữ liệu và trí tuệ nhân tạo chạy cục bộ nhằm hỗ trợ người dùng truy vấn dữ liệu bằng ngôn ngữ tự nhiên, phân tích hoạt động kinh doanh, dự báo nhu cầu sản phẩm, phát hiện bất thường và tạo báo cáo.

Các thành phần AI được tích hợp thông qua các công nghệ và mô hình có sẵn, trong đó Ollama được sử dụng để triển khai mô hình ngôn ngữ lớn tại môi trường cục bộ.

---

## 🎯 Mục tiêu

- Xây dựng hệ thống quản lý bán hàng ngành mỹ phẩm.
- Quản lý sản phẩm, danh mục, thương hiệu và kho hàng.
- Quản lý khách hàng, đơn hàng và thanh toán.
- Xây dựng dashboard trực quan hóa dữ liệu kinh doanh.
- Phân tích doanh thu, sản phẩm, khách hàng và tồn kho.
- Dự báo nhu cầu sản phẩm dựa trên dữ liệu bán hàng.
- Phát hiện các bất thường trong hoạt động kinh doanh.
- Tích hợp AI chạy cục bộ thông qua Ollama.
- Cho phép truy vấn dữ liệu bằng ngôn ngữ tự nhiên.
- Xây dựng hệ thống RAG hỗ trợ tra cứu thông tin sản phẩm và kiến thức liên quan.
- Hỗ trợ tạo báo cáo và cung cấp thông tin phục vụ ra quyết định.

---

## 🚀 Chức năng chính

### 1. Quản lý sản phẩm

- Thêm, sửa, xóa sản phẩm.
- Quản lý danh mục.
- Quản lý thương hiệu.
- Quản lý giá bán và giá nhập.
- Quản lý hình ảnh sản phẩm.
- Quản lý thông tin sản phẩm và thành phần.
- Phân loại sản phẩm theo loại da và công dụng.

### 2. Quản lý kho

- Theo dõi số lượng tồn kho.
- Nhập kho và xuất kho.
- Theo dõi lịch sử biến động kho.
- Quản lý lô sản phẩm.
- Theo dõi hạn sử dụng.
- Cảnh báo sản phẩm sắp hết hàng.
- Cảnh báo sản phẩm sắp hết hạn.

### 3. Quản lý bán hàng

- Quản lý đơn hàng.
- Chi tiết đơn hàng.
- Thanh toán.
- Khuyến mãi.
- Theo dõi trạng thái đơn hàng.
- Quản lý lịch sử bán hàng.

### 4. Quản lý khách hàng

- Thông tin khách hàng.
- Lịch sử mua hàng.
- Phân nhóm khách hàng.
- Phân tích hành vi mua hàng.

### 5. Dashboard và phân tích

Dashboard cung cấp các chỉ số:

- Tổng doanh thu.
- Tổng số đơn hàng.
- Lợi nhuận.
- Giá trị đơn hàng trung bình.
- Sản phẩm bán chạy.
- Danh mục bán chạy.
- Thương hiệu bán chạy.
- Tình trạng tồn kho.
- Doanh thu theo thời gian.
- Xu hướng doanh thu.
- Khách hàng mới và khách hàng quay lại.

### 6. Dự báo

Hệ thống sử dụng mô hình Machine Learning để hỗ trợ:

- Dự báo nhu cầu sản phẩm.
- Dự báo số lượng bán.
- Phân tích xu hướng.
- Hỗ trợ lập kế hoạch nhập hàng.

### 7. AI Assistant

AI Assistant cho phép người dùng đặt câu hỏi bằng ngôn ngữ tự nhiên.

Ví dụ:

> Doanh thu tháng này là bao nhiêu?

> Sản phẩm nào bán chạy nhất?

> Sản phẩm nào đang sắp hết hàng?

> Serum nào dành cho da dầu đang bán chạy nhất?

> Doanh thu tháng này thay đổi như thế nào so với tháng trước?

AI có thể kết hợp dữ liệu từ cơ sở dữ liệu và kho kiến thức để tạo câu trả lời.

### 8. RAG

Hệ thống RAG hỗ trợ truy xuất thông tin từ kho kiến thức.

Nguồn dữ liệu có thể bao gồm:

- Thông tin sản phẩm.
- Thành phần.
- Công dụng.
- Loại da phù hợp.
- Hướng dẫn sử dụng.
- Kiến thức chăm sóc da.
- Chính sách bán hàng.
- Câu hỏi thường gặp.

Ví dụ:

> Sản phẩm này phù hợp với loại da nào?

> Serum này có công dụng gì?

> Chính sách đổi trả của cửa hàng như thế nào?

---

## 🧠 Kiến trúc hệ thống

```text
                    ┌─────────────────────┐
                    │      Frontend       │
                    │   React + TypeScript│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Backend       │
                    │       FastAPI       │
                    └──────┬───────┬──────┘
                           │       │
             ┌─────────────┘       └─────────────┐
             ▼                                   ▼
    ┌─────────────────┐                ┌─────────────────┐
    │   PostgreSQL    │                │   AI / ML       │
    │   Database      │                │    Services     │
    └─────────────────┘                └───────┬─────────┘
                                               │
                              ┌────────────────┼───────────────┐
                              ▼                ▼               ▼
                         ┌────────┐       ┌────────┐     ┌──────────┐
                         │ Ollama │       │  RAG   │     │Forecasting│
                         └────────┘       └────────┘     └──────────┘
````

---

## 🛠️ Công nghệ sử dụng

### Frontend

* React
* TypeScript
* Tailwind CSS
* Recharts / ECharts

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication

### AI

* Ollama
* Large Language Model chạy cục bộ
* RAG
* Embedding Model
* Vector Database / pgvector

### Machine Learning

* Python
* Scikit-learn
* Các mô hình dự báo chuỗi thời gian
* Anomaly Detection

### DevOps

* Docker
* Docker Compose
* Git / GitHub

---

## 📂 Cấu trúc dự án

```text
cosmetics-sales-management/
│
├── frontend/
├── backend/
├── ai/
├── ml/
├── data/
├── database/
├── docs/
├── scripts/
├── docker/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/<username>/cosmetics-sales-management.git

cd cosmetics-sales-management
```

### 2. Cấu hình môi trường

```bash
cp .env.example .env
```

Cấu hình các thông tin cần thiết trong `.env`.

### 3. Khởi động hệ thống

```bash
docker compose up -d
```

### 4. Khởi động Ollama

Cài đặt Ollama và tải mô hình ngôn ngữ phù hợp với cấu hình máy.

Ví dụ:

```bash
ollama pull <model>
```

### 5. Chạy Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### 6. Chạy Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📊 Luồng xử lý AI

```text
Người dùng đặt câu hỏi
          │
          ▼
     AI Assistant
          │
          ▼
    Phân tích yêu cầu
          │
      ┌───┴────┐
      ▼        ▼
    SQL       RAG
      │        │
      └───┬────┘
          ▼
      Ollama / LLM
          │
          ▼
    Câu trả lời
```

---

## 📈 Luồng dự báo

```text
Dữ liệu bán hàng
       │
       ▼
Tiền xử lý dữ liệu
       │
       ▼
Huấn luyện mô hình
       │
       ▼
Dự báo nhu cầu
       │
       ▼
Phân tích kết quả
       │
       ▼
Dashboard / Cảnh báo
```

---

## 🔐 Bảo mật

Hệ thống dự kiến hỗ trợ:

* JWT Authentication.
* Phân quyền người dùng.
* Quản lý vai trò.
* Bảo vệ API.
* Quản lý biến môi trường.
* Không lưu thông tin nhạy cảm trực tiếp trong source code.

---

## 🗺️ Roadmap

* [ ] Thiết kế cơ sở dữ liệu.
* [ ] Xây dựng Backend API.
* [ ] Xây dựng giao diện quản lý.
* [ ] Xây dựng module bán hàng.
* [ ] Xây dựng quản lý kho.
* [ ] Xây dựng Dashboard.
* [ ] Xây dựng module phân tích dữ liệu.
* [ ] Xây dựng mô hình dự báo.
* [ ] Tích hợp Ollama.
* [ ] Xây dựng AI Assistant.
* [ ] Xây dựng RAG.
* [ ] Xây dựng cảnh báo thông minh.
* [ ] Hoàn thiện báo cáo.
* [ ] Docker hóa hệ thống.
* [ ] Kiểm thử và đánh giá.

---

## 📚 Tài liệu

Tài liệu thiết kế và phát triển được lưu tại thư mục:

```text
docs/
```

Bao gồm:

* Kiến trúc hệ thống.
* Thiết kế cơ sở dữ liệu.
* API.
* Thiết kế AI.
* RAG.
* Mô hình dự báo.
* Các sơ đồ UML.

---

## 👨‍💻 Tác giả

**[Tên sinh viên]**

Đồ án tốt nghiệp ngành Công nghệ thông tin.
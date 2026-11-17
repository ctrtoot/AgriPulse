# AgriPulse – Demo GIS đánh giá thích nghi cây trồng Gia Lai

AgriPulse là bản demo GIS hỗ trợ xem xét mức độ thích nghi sơ bộ của **ngô lấy hạt** và **lạc lấy củ** theo tháng gieo trên lưới không gian xấp xỉ 1 km tại Gia Lai.

> **Lưu ý học thuật:** Đây là hệ thống phân hạng theo quy tắc sơ bộ, không phải mô hình Machine Learning đã huấn luyện. Các lớp S1/S2/S3/N chưa được kiểm chứng bằng năng suất hoặc khảo sát thực địa. Không sử dụng kết quả làm khuyến nghị canh tác chính thức.

## Chức năng

- Bản đồ tương tác gồm 22.160 ô lưới.
- Chọn cây trồng: ngô lấy hạt hoặc lạc lấy củ.
- Chọn tháng gieo từ 1 đến 12 và xem lớp S1/S2/S3/N.
- Xem thuộc tính của ô lưới: địa hình, đất, khí hậu, chất lượng dữ liệu.
- Chuyển lớp bản đồ: thích nghi, độ dốc, độ cao, pH.
- Tra cứu bằng tọa độ hoặc GPS của thiết bị.
- Vẽ polygon thửa đất và tổng hợp chỉ số theo diện tích giao cắt với ô lưới.

## Chạy trên Windows

1. Cài Python 3.10 trở lên.
2. Tải hoặc clone repository.
3. Mở thư mục dự án.
4. Nhấp đúp `run_demo.bat`.
5. Trình duyệt mở `http://127.0.0.1:8000`.

Không cần cài package Python bên ngoài. Ứng dụng cần Internet để tải Leaflet, Leaflet Draw, Turf.js, OpenTopoMap và font chữ từ CDN.

## Chạy trên macOS / Linux

```bash
python3 server.py
```

Sau đó mở `http://127.0.0.1:8000`.

## Kiểm tra tính toàn vẹn dữ liệu

```bash
python tests/validate_data.py
python -m py_compile server.py
```

Health check: `http://127.0.0.1:8000/health`.

## Cấu trúc repository

```text
AgriPulse/
├── index.html
├── server.py
├── run_demo.bat
├── Procfile
├── render.yaml
├── README.md
├── DATA_SOURCES.md
├── DATA_LICENSE.md
├── LICENSE
├── QA_Report.csv
├── PRESENTATION_CHECKLIST.md
├── data/
│   ├── grid.geojson
│   ├── details.json.gz
│   ├── summary.json
│   └── Suitability_Summary.csv
├── tests/
│   └── validate_data.py
└── .github/workflows/validate.yml
```

## Đưa lên GitHub

```bash
git init
git add .
git commit -m "Initial AgriPulse Gia Lai demo"
git branch -M main
git remote add origin https://github.com/<USERNAME>/<REPOSITORY>.git
git push -u origin main
```

Các file dữ liệu đã được đóng gói cùng repository. `data/grid.geojson` khoảng 10,7 MB; `data/details.json.gz` khoảng 1,7 MB. Nếu cập nhật dữ liệu lớn hơn, cân nhắc Git LFS.

## Triển khai web

Ứng dụng sử dụng Python server để phục vụ `details.json.gz` với HTTP `Content-Encoding: gzip`; không thể chỉ tải `index.html` lên GitHub Pages rồi mong endpoint dữ liệu hoạt động.

Có thể triển khai lên Render bằng `render.yaml` hoặc dùng `Procfile`. Khi chạy trên nền tảng cloud, máy chủ đọc `HOST` và `PORT` từ biến môi trường. GPS trên web cần HTTPS và sự cho phép của trình duyệt.

## Nguồn dữ liệu và giới hạn

Xem [`DATA_SOURCES.md`](DATA_SOURCES.md) và [`DATA_LICENSE.md`](DATA_LICENSE.md). Tóm tắt quan trọng:

- Khí hậu NASA POWER lấy từ 13 điểm nguồn, giai đoạn 2005–2025; khoảng cách điểm nguồn tới ô lưới trung bình 23,14 km, tối đa 43,59 km. Không phải dữ liệu khí hậu quan trắc 1 km.
- Lượng mưa tích lũy được ước tính từ PRECTOTCORR trung bình ngày nhân số ngày tương ứng.
- SoilGrids là dữ liệu mô hình toàn cầu, không thay thế phân tích mẫu đất tại ruộng.
- Polygon được tổng hợp theo ô lưới 1 km, không mô tả đầy đủ biến thiên trong thửa ruộng nhỏ.
- Ngô chưa chấm nhiệt độ theo ba giai đoạn sinh trưởng; thuộc tính đất chưa được tích hợp đầy đủ vào phân hạng.

## Hỗ trợ

Nếu bản đồ nền không hiển thị, kiểm tra Internet. Nếu GPS không chạy, kiểm tra quyền vị trí và HTTPS/localhost. Không mở trực tiếp `index.html`; hãy chạy qua `server.py` hoặc `run_demo.bat`.

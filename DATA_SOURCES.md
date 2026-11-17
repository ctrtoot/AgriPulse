# Nguồn dữ liệu và ghi chú sử dụng

| Thành phần | Nguồn | Cách dùng trong demo | Giới hạn chính |
|---|---|---|---|
| Lưới không gian | Lưới nghiên cứu Gia Lai, EPSG:4326 trong GeoJSON | 22.160 ô lưới xấp xỉ 1 km | Ô lưới không đồng nghĩa ranh giới thửa ruộng |
| Khí hậu | NASA POWER, 13 điểm nguồn, giai đoạn 2005–2025 | Gán điểm gần nhất cho ô lưới; tạo thống kê khí hậu theo tháng/cửa sổ mùa vụ | Không phải dữ liệu khí hậu quan trắc 1 km; khoảng cách nguồn trung bình 23,14 km, tối đa 43,59 km |
| Đất | SoilGrids | Một số thuộc tính đất bề mặt và cờ đầy đủ dữ liệu | Dữ liệu mô hình toàn cầu; không thay thế kết quả phân tích mẫu đất tại ruộng |
| Địa hình | Copernicus DEM GLO-30 | Độ cao và độ dốc tổng hợp lên ô lưới | DEM có thể chứa ảnh hưởng bề mặt công trình/thực vật; thống kê ở 1 km |

## Phân hạng

Các lớp S1, S2, S3, N trong gói này là kết quả **quy tắc sơ bộ phục vụ demo**. Đây không phải mô hình Machine Learning đã huấn luyện, không có Accuracy, và chưa được xác nhận bằng năng suất hoặc khảo sát thực địa.

- Ngô lấy hạt: bản demo hiện chấm mưa 4 tháng, độ ẩm và độ dốc; chưa tích hợp đầy đủ nhiệt độ theo ba giai đoạn sinh trưởng.
- Lạc lấy củ: dùng các tiêu chí nhiệt độ, mưa mùa vụ, mưa tháng cuối và độ dốc theo cấu hình demo; cần chuyên gia địa phương rà soát ngưỡng.
- Các tháng là kịch bản so sánh dựa trên khí hậu lịch sử, không phải lịch gieo tối ưu đã xác nhận cho mọi địa bàn.
- Thiếu dữ liệu được giữ riêng, không tự động chuyển thành lớp N.

## Điều khoản dữ liệu

Mã nguồn ứng dụng được phát hành theo MIT License. Các bộ dữ liệu đầu vào/đầu ra vẫn chịu điều khoản, yêu cầu ghi công và giới hạn sử dụng của nhà cung cấp tương ứng. Trước khi tái phân phối dữ liệu trong sản phẩm thương mại, hãy kiểm tra điều khoản hiện hành của NASA POWER, ISRIC SoilGrids, Copernicus và nguồn dữ liệu ranh giới/lưới.

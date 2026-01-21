# 🛠️ Ter-Unlocker Del (V1.0)

**Ter-Unlocker Del** là công cụ mạnh mẽ được thiết kế để quét các tiến trình đang khóa (locker) và cưỡng chế xóa các tệp tin/thư mục cứng đầu trên Windows.(Bảo vệ bởi TrustedInstaller check hoặc đại loại thế)

## 1. Cơ chế hoạt động & Quyền hạn
* **Xác nhận UAC:** Khi khởi động, Windows sẽ hiện bảng UAC để yêu cầu quyền Administrator (hoặc không hiện ở một số máy/User tùy cài đặt). Bạn cứ mạnh dạn click `YES/OK` vì nếu bấm `NO` thì app sẽ bật lên bằng niềm tin 🗣🔥.

<img width="455" height="345" alt="image" src="https://github.com/user-attachments/assets/10d2524c-7d0f-45dc-b0d0-49f74bb43ac0" />

* **Cảnh báo Anti-Virus:** Đôi khi các phần mềm AV (mang tiếng là Anti-Virus nhưng thực chất là Anti-Malware thì đúng hơn) sẽ nhảy thông báo chặn. Lý do rất dễ hiểu: Tool cần can thiệp sâu vào hệ thống để "Kill locker" và thực hiện lệnh xóa vĩnh viễn **không trăn trối (dành cho file/folder bị kill)**.

## 2. Hiệu năng & Cảnh báo (LAG ALERT!)
* **Cực kỳ ngốn tài nguyên:** Vì cơ chế phải scan sâu toàn bộ tiến trình hệ thống nên khi chạy sẽ cực kỳ **LAG**.

<img width="637" height="550" alt="image" src="https://github.com/user-attachments/assets/399eedf5-cbb1-4222-97e3-55701180e655" />

* **CPU:** Xung nhịp sẽ tăng vọt lên 100% Base + số % CPU tăng thêm tùy theo độ phức tạp của tác vụ.
* **Lời khuyên cho máy yếu:** Nếu bạn đang dùng các dòng CPU yếu kiểu Atom hoặc Celeron đời cũ, tốt nhất là nên vào thẳng **WinRE** (Windows Recovery Environment) để xóa thủ công cho lành.
    * *Lưu ý quan trọng:* Trong môi trường WinRE, các ổ đĩa sẽ được mount theo thứ tự riêng. Ổ chứa file/folder bạn muốn "xử lý" chưa chắc đã là ổ C, hãy kiểm tra kỹ trước khi ra lệnh.

## 3. Tại sao lại Build?
* Đơn giản là vì **Thích thì build** thôi! Ngoài ra, việc build ra `.exe` giúp chạy đặc quyền Admin ổn định hơn và người dùng *không cần cài đặt môi trường Python phức tạp lằng ngoằng với **1 mả code / dòng lệnh mà chả hiểu ý nghĩa gì cả.***

## 4. Social Dev
* **Owner:** [Thanhnguyen123-men](https://github.com/Thanhnguyen123-men)
* **Discord User:** https://discord.com/users/1379310041903140895
* **Project:** Ter-Unlocker Del

5. Mã SHA256 
* Cách check : gõ powershell nhập : `Get-FileHash "Đường dẫn file đã tải\Ter-Unlocker_Del.exe" -Algorithm SHA256` 

* Mã của .exe gốc là `1725118CBCED72371062A3A5CD20BEFEDE9BC6F4AB08809B47322EAFE2BC7741`

<img width="862" height="735" alt="image" src="https://github.com/user-attachments/assets/515d19b6-2385-4ea8-8dc0-44e0d103de8c" />

---
>*Lưu ý: Luôn kiểm tra đường dẫn trước khi nhấn nút xóa.* 

>*Nó sẽ hỏi xóa không ?*

>*Giờ chọn yes / no hãy suy nghĩ ký vì lỡ xóa file / folder gì tao không chịu trách nhiệm gì hết*

> *Nếu muốn repo thì hãy DMs hoặc hợp tác hoặc repo một cách không xin* **(Vẫn phải để repo gốc là `https://github.com/Thanhnguyen123-men/Ter-Unlocker-Del` )**

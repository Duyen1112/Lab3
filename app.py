from flask import Flask, render_template
import os

# Khởi tạo Flask app
app = Flask(__name__)

# Route chính
@app.route('/')
def home():
    """Render trang chủ"""
    return render_template('index.html')

# Route mẫu có xử lý lỗi 404
@app.route('/about')
def about():
    """Render trang about"""
    try:
        return render_template('about.html')
    except:
        return "Trang không tồn tại", 404

# Xử lý lỗi 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Chạy ứng dụng
if __name__ == '__main__':
    # Đọc port từ biến môi trường (Render cung cấp) hoặc mặc định 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Chạy server với cấu hình production
    app.run(
        host='0.0.0.0',  # Bind ra all network interfaces
        port=port,        # Sử dụng port từ Render
        debug=False,      # Tắt debug mode trên production
        threaded=True     # Bật multi-threading
    )

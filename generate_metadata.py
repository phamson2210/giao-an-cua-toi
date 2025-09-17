import os
import json
import sys

# ==============================================================================
# CẤU HÌNH - BẠN CHỈ CẦN THAY ĐỔI 2 DÒNG NÀY NẾU CẦN
# ==============================================================================
GITHUB_USERNAME = "phamson2210"
REPO_NAME = "giao-an-cua-toi"
# ==============================================================================

def create_metadata():
    all_lessons = []
    # Vì script giờ nằm trong thư mục gốc, chúng ta dùng "." để đại diện cho nó
    root_directory = "." 
    
    print(f"Bắt đầu quét thư mục hiện tại '{os.getcwd()}'...")

    for category_folder, _, filenames in os.walk(root_directory):
        # Bỏ qua thư mục .github nơi chứa Action và thư mục .git
        if ".github" in category_folder or ".git" in category_folder:
            continue
            
        relative_category_path = os.path.relpath(category_folder, root_directory)
        if relative_category_path == '.':
            continue

        category_name = relative_category_path.replace("\\", "/")
        print(f"  -> Đang xử lý thư mục: {category_name}")

        for filename in filenames:
            # Bỏ qua chính file script và các file hệ thống khác
            if filename == os.path.basename(__file__) or filename.startswith('.'):
                continue

            relative_path = os.path.join(category_name, filename).replace("\\", "/")
            download_url = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main/{relative_path}"
            
            file_info = {
                "id": f"{category_name.lower().replace('/', '_')}_{os.path.splitext(filename)[0]}",
                "title": os.path.splitext(filename)[0].replace("_", " ").replace("-", " "),
                "category": category_name,
                "filename": filename,
                "download_url": download_url
            }
            all_lessons.append(file_info)
            print(f"    + Đã xử lý file: {filename}")

    output_data = {"lessons": all_lessons}
    output_filename = "metadata.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\nHOÀN TẤT! Đã tạo/cập nhật file '{output_filename}' với {len(all_lessons)} mục.")

if __name__ == "__main__":
    create_metadata()
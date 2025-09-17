import os
import json

# ==============================================================================
# CẤU HÌNH
# ==============================================================================
GITHUB_USERNAME = "phamson2210"
REPO_NAME = "giao-an-cua-toi"
# ==============================================================================

def create_metadata():
    all_lessons = []
    root_directory = "." 
    
    print(f"Bắt đầu quét thư mục: '{os.getcwd()}'")

    for dirpath, _, filenames in os.walk(root_directory):
        # Bỏ qua các thư mục đặc biệt
        if ".git" in dirpath or ".github" in dirpath:
            continue

        for filename in filenames:
            # Bỏ qua các file không phải là tài liệu
            if not (filename.lower().endswith(('.docx', '.pptx'))):
                continue
            
            # Lấy đường dẫn thư mục con tương đối (vd: Lớp 8)
            relative_dir = os.path.relpath(dirpath, root_directory).replace("\\", "/")
            # Bỏ qua trường hợp file nằm ở thư mục gốc
            if relative_dir == '.':
                continue

            category_name = relative_dir
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
            print(f"  + Đã xử lý: {relative_path}")

    output_data = {"lessons": all_lessons}
    output_filename = "metadata.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\nHOÀN TẤT! Đã tạo/cập nhật '{output_filename}' với {len(all_lessons)} mục.")

if __name__ == "__main__":
    create_metadata()

import os
import glob

# 定义要删除的文件类型
file_extensions = [
    "*.aux",
    "*.log",
    "*.synctex.gz",
    "*.toc",
    "*.bbl",
    "*.blg",
    "*.out",
    "*.lof",
    "*.lot",
    "*.fls",
    "*.fdb_latexmk"
]

def delete_latex_aux_files():
    deleted_files = []
    for ext in file_extensions:
        # 使用glob模块查找当前目录及子目录下的所有匹配文件
        for file in glob.glob(ext, recursive=True):
            try:
                os.remove(file)
                deleted_files.append(file)
                print(f"Deleted: {file}")
            except OSError as e:
                print(f"Error: {e.strerror} - {file}")
    
    # 打印删除文件总数
    print(f"\nTotal deleted files: {len(deleted_files)}")

if __name__ == "__main__":
    delete_latex_aux_files()

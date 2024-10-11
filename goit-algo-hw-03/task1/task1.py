import sys 
from pathlib import Path
import shutil
import os

def copy_files(src: Path, dst: Path):
    # Copy all files from src to dst recursively

    if not dst.exists():
        dst.mkdir(parents=True)
        print(f"Destination directory {dst} created")
    
    for item in src.iterdir():
        if item.is_file():
            file_extension = os.path.splitext(item)[1][1:].lower()
            if not file_extension:
                file_extension = 'no_extension'
            new_dir = dst / file_extension
            new_dir.mkdir(exist_ok=True)
            shutil.copy(item, new_dir)
        elif item.is_dir():
            new_dst_dir = dst / item.name
            copy_files(item, new_dst_dir)

            
def main():
    while True:
        src_path = input("Enter source directory (or type 'exit' to quit): ")
        if src_path.lower() == "exit":
            break
        src = Path(src_path)
        if not src.exists():
            print(f"Source directory {src} does not exist")
            return
    
        dst_path = input("Enter destination directory (or type 'exit' to quit): ")
        if dst_path.lower() == "exit":
            break
        if not dst_path:
                dst_path = os.path.join(os.getcwd(), 'dist')
        dst = Path(dst_path)
        
        # Ensure the copy function is defined before this, or import it if it's in another module.
        copy_files(src, dst)
        print(f"Files from {src} have been copied to {dst}")

if __name__ == '__main__':
    main()
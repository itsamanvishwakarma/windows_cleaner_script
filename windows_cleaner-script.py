import os
import shutil

def clean_directory(directory):
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                if os.path.isfile(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"Error deleting {item_path}: {e}")
        print(f"Cleaned {directory}")
    except Exception as e:
        print(f"Error accessing {directory}: {e}")

directories_to_clean = [
    r"C:\Windows\Temp",
    r"C:\Windows\Prefetch",
    r"C:\Users\itsam\AppData\Local\Temp"
]

for directory in directories_to_clean:
    clean_directory(directory)

print("Cleaning completed.")
import os
import shutil

try:
    with open("sample.txt", "w") as f:
        f.write("Hello, this is a sample file.\n")
        f.write("Python file handling demo.\n")
    print("✅ File created and written successfully.")

except Exception as e:
    print("❌ Error while writing file:", e)

try:
    with open("sample.txt", "r") as f:
        content = f.read()
    print("\n📖 File Content:\n", content)

except FileNotFoundError:
    print("❌ File not found.")
except Exception as e:
    print("❌ Error while reading file:", e)

try:
    os.rename("sample.txt", "renamed_sample.txt")
    print("✅ File renamed successfully.")
except FileNotFoundError:
    print("❌ File to rename not found.")
except Exception as e:
    print("❌ Error while renaming file:", e)


try:
    if not os.path.exists("backup"):
        os.mkdir("backup")

    shutil.move("renamed_sample.txt", "backup/renamed_sample.txt")
    print("✅ File moved to backup folder.")
except Exception as e:
    print("❌ Error while moving file:", e)


try:
    os.remove("backup/renamed_sample.txt")
    print("✅ File deleted successfully.")
except FileNotFoundError:
    print("❌ File not found for deletion.")
except Exception as e:
    print("❌ Error while deleting file:", e)

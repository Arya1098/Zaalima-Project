import os
import math

def analyze_directory(path):
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return
    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a directory.")
        return

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    if not files:
        print("No files found in the directory.")
        return

    total_files = len(files)
    longest_file = max(files, key=len)
    sqrt_files = round(math.sqrt(total_files), 2)
    rounded_files = math.ceil(total_files / 10) * 10

    print("\nFiles in Directory:")
    for f in files:
        print(f"  - {f}")

    print("\nAnalysis:")
    print(f"Total files       : {total_files}")
    print(f"Longest filename  : {longest_file}")
    print(f"Square root       : {sqrt_files}")
    print(f"Rounded (nearest 10): {rounded_files}")

path = "/content/sample_data"
analyze_directory(path)

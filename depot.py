import os, pathlib

ROOT = "C:\Program Files (x86)\Steam\steamapps\common"
BASE_PATCH = os.path.join(ROOT, "DOOMEternal 6.66 Rev 3")
GAME_ROOT = os.path.join(ROOT, "DOOMEternal")

for dirName, _, fileList in os.walk(BASE_PATCH):
    folder_name = os.path.relpath(dirName, BASE_PATCH)
    source_folder = os.path.join(BASE_PATCH, folder_name)
    target_folder = os.path.join(GAME_ROOT, folder_name)

    # Create folders if they don't exist
    if not os.path.exists(target_folder):
        pathlib.Path(target_folder).mkdir()

    for fname in fileList:
        source_file = os.path.join(source_folder, fname)
        target_file = os.path.join(target_folder, fname)

        # Create symlinks for files which don't exist
        if not os.path.exists(target_file):
            os.symlink(source_file, target_file)

print("Symbolic links created successfully from BASE PATCH")

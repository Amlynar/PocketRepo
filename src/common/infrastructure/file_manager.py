
import hashlib, os, shutil, zipfile
from pathlib import Path

class FileManager:
    # Files never copied to (or hashed for) an exported directory.
    COPY_IGNORE = staticmethod(shutil.ignore_patterns("__pycache__", "*.pyc"))

    def __init__(self):
        pass

    def delete_directory(self, path):
        shutil.rmtree(path, ignore_errors=True)

    def replace_directory(self, source, destination):
        """Delete destination (if present) and copy source into it.

        Unlike delete_directory, errors are NOT swallowed so callers can report them.
        """
        source = Path(source)
        destination = Path(destination)
        if not source.is_dir():
            raise FileNotFoundError(f"Source directory not found: {source}")
        if destination.exists():
            shutil.rmtree(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination, ignore=self.COPY_IGNORE)

    def hash_directory(self, path) -> str:
        """SHA-256 over the relative paths and contents of every file replace_directory would copy."""
        path = str(path)
        sha = hashlib.sha256()
        for root, dirs, files in os.walk(path):
            ignored = self.COPY_IGNORE(root, dirs + files)
            dirs[:] = sorted(d for d in dirs if d not in ignored)
            for fname in sorted(f for f in files if f not in ignored):
                fpath = os.path.join(root, fname)
                # Normalise separators so the hash is identical on Windows and iOS.
                sha.update(os.path.relpath(fpath, path).replace(os.sep, "/").encode("utf-8"))
                with open(fpath, "rb") as f:
                    sha.update(f.read())
        return sha.hexdigest()

    def get_documents_directory(self) -> Path:
        return Path.home() / "Documents"

    def get_project_directory(self, project_directory_name: str) -> Path:
        return self.get_documents_directory() / project_directory_name

    def create_directory(self, base_path, folder_name):
        os.makedirs(os.path.dirname(base_path / folder_name), exist_ok=True)

    def delete_file(self, file_path):
         if os.path.exists(file_path):
             os.remove(file_path)

    def extract_zip_file(self, output_zip, extract_path):
            # Extract the contents
            with zipfile.ZipFile(output_zip, 'r') as zip_ref:
                for member in zip_ref.infolist():
                    # 1. Get the raw filename from the ZIP
                    filename = member.filename
                    
                    # 2. Strip leading slashes and '.' prefixes (e.g., './src/main.py' -> 'src/main.py')
                    # Also handle the 'PocketRepo-main/' prefix added by GitHub
                    parts = filename.split('/')
                    # Remove empty strings from list caused by leading/trailing slashes
                    parts = [p for p in parts if p and p != '.']
                    
                    if len(parts) > 0:
                        # If the first part is the 'repo-main' folder, skip it
                        # We check if it contains '-main' or is the standard GitHub wrapper
                        if "main" in parts[0] or "-" in parts[0]:
                            parts.pop(0)
                        
                        new_filename = "/".join(parts)
                    else:
                        new_filename = filename
    
                    # 3. Construct the absolute path
                    target_path = Path(extract_path) / new_filename
                    
                    # 4. Create parents if they don't exist
                    # We ensure we are only creating directories
                    if target_path.parent.exists() and not target_path.parent.is_dir():
                        # This handles the case where a file exists with the same name as a folder
                        print(f"Warning: Path {target_path.parent} is a file, not a directory.")
                    else:
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # 5. Write the content
                    if not member.is_dir():
                        with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                            target.write(source.read())

from pathlib import Path
import shutil
import subprocess

root = Path.cwd()
license_choice = "{{ cookiecutter.license }}"
project_type = "{{ cookiecutter.project_type }}"
include_example = "{{ cookiecutter.include_example_code }}"
initialize_git = "{{ cookiecutter.initialize_git }}"

license_files = {
    "MIT": "LICENSE-MIT",
    "BSD-3-Clause": "LICENSE-BSD-3-Clause",
    "GPL-3.0-or-later": "LICENSE-GPL-3.0-or-later",
}
for filename in license_files.values():
    path = root / filename
    if filename == license_files.get(license_choice):
        path.rename(root / "LICENSE")
    elif path.exists():
        path.unlink()

if license_choice == "No license":
    for filename in license_files.values():
        (root / filename).unlink(missing_ok=True)

if project_type == "application":
    (root / "src" / "{{ cookiecutter.package_name }}" / "cli_library.py").unlink(missing_ok=True)
else:
    (root / "src" / "{{ cookiecutter.package_name }}" / "cli_application.py").unlink(missing_ok=True)

if include_example == "no":
    for filename in ["cli_application.py", "cli_library.py"]:
        (root / "src" / "{{ cookiecutter.package_name }}" / filename).unlink(missing_ok=True)
    (root / "tests" / "test_example.py").unlink(missing_ok=True)

if initialize_git == "yes":
    try:
        subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Warning: Git repository initialization was skipped.")

shutil.rmtree(root / ".template", ignore_errors=True)

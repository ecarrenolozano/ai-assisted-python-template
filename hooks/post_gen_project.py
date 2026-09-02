from pathlib import Path

import shutil
import subprocess


root = Path.cwd()

license_choice = "{{ cookiecutter.license }}"
project_type = "{{ cookiecutter.project_type }}"
initialize_git = "{{ cookiecutter.initialize_git }}"

license_files = {
    "MIT": "LICENSE-MIT",
    "BSD-3-Clause": "LICENSE-BSD-3-Clause",
    "GPL-3.0-or-later": "LICENSE-GPL-3.0-or-later",
}


# Configure license
for filename in license_files.values():
    path = root / filename

    if filename == license_files.get(license_choice):
        path.rename(root / "LICENSE")
    elif path.exists():
        path.unlink()

if license_choice == "No license":
    for filename in license_files.values():
        (root / filename).unlink(missing_ok=True)


# Configure project type
if project_type == "application":
    (
        root
        / "src"
        / "{{ cookiecutter.package_name }}"
        / "cli_library.py"
    ).unlink(missing_ok=True)
else:
    (
        root
        / "src"
        / "{{ cookiecutter.package_name }}"
        / "cli_application.py"
    ).unlink(missing_ok=True)


# Install AI SDLC skills
try:
    subprocess.run(
        [
            "npx",
            "--yes",
            "skills",
            "add",
            "ecarrenolozano/ai-sdlc-skills",
            "--all",
        ],
        cwd=root,
        check=True,
    )
except FileNotFoundError:
    raise RuntimeError(
        "Node.js/npm is required to install the AI SDLC skills. "
        "Install Node.js and generate the project again."
    )
except subprocess.CalledProcessError as exc:
    raise RuntimeError(
        "Failed to install AI SDLC skills."
    ) from exc


# Initialize Git repository
if initialize_git == "yes":
    try:
        subprocess.run(
            ["git", "init"],
            cwd=root,
            check=True,
            capture_output=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Warning: Git repository initialization was skipped.")


# Remove template-only files
shutil.rmtree(root / ".template", ignore_errors=True)
# Template Repo

This repo is intended as an easy starting template for other projects using a
combination of mostly Python and Bash code.

Copy the parts you want to use, and enjoy.

The expected usage of modules based on this template is:

- Clone the repo:
  ```bash
  git clone https://github.com/haftings/template.git
  cd template
  ```
- Build the repo (creates venv):
  ```bash
  ./build
  ```
- Test the built repo (runs checks, pyright, shellcheck):
  ```bash
  ./test
  ```
- Activate your repo and enjoy:
  ```bash
  . ./activate
  hello
  ```

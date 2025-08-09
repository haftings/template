# Template Repo

This repo is intended as an easy starting template for other projects using a
combination of mostly Python and Bash code.

Copy the parts you want to use, and enjoy.

The expected usage of modules based on this template is:

1) Clone the repo:
   ```bash
   $ git clone https://github.com/haftings/template.git
   # ...

   $ cd template
   ```

2) Build the repo (creates venv):
   ```bash
   $ ./build
   # ...
   ```

3) Test the repo (the `test` script runs checks, pyright, shellcheck):
   ```bash
   $ ./test
   # activated TEMPLATE=/Users/pch/repo/template
   # ------------------------------------------------------------------------------
   # Running doctest ...
   # ------------------------------------------------------------------------------
   # Running pyright ...
   # 0 errors, 0 warnings, 0 informations 
   # ------------------------------------------------------------------------------
   # Running shellcheck ...
   # ------------------------------------------------------------------------------
   # Tests complete, all tests passed.
   ```

4) Activate the repo in any of three ways:

   - Either source the `./activate` script, then run code in the repo:
     ```bash
     $ . ./activate
     # activated TEMPLATE=/Users/pch/repo/template

     $ hello
     # Hello, World!
     ```
   - Or execute `./activate` to start a new shell to run code in the repo:
     ```bash
     $ . ./activate
     # activated TEMPLATE=/Users/pch/repo/template
     # running in a bash sub-shell, exit to deactivate

     $ hello
     # Hello, World!

     $ exit
     ```
   - Or activate for just a single command:
     ```bash
     $ ./activate hello
     # Hello, World!
     ```

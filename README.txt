Physics 281 — Starter Files

This folder contains the starter files for Physics 281.

The course Python environment will be created separately in this folder.
It should be named p281.

After completing Part B of the setup handout, complete Part C:

    cd ~/course281
    python3.10 -m venv p281
    source p281/bin/activate
    python -m pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt

Do not put course programs inside the p281 folder.
The p281 folder contains installed software for this project.

To test the installation:

    python smoke_test.py
    pytest -q

The course uses:

    numpy
    scipy
    matplotlib
    pandas
    pytest

Git and GitHub will be introduced later in the semester.
Do not create a GitHub repository for these starter files yet.

# Mathematical Models of Metal Cutting

Python functions and Jupyter exercises for the formulas in the Sandvik Coromant *Metal Cutting Training Handbook* ("Formulas and definitions"). Students calculate the key parameters of turning, milling and drilling from given starting conditions, and their answers are checked automatically.

The structure follows the style of [cnc-machining-calculator](https://github.com/LiLu1626/cnc-machining-calculator): one small function per formula, units in every docstring, input validation, and pytest tests. This package extends that set with chip thickness, specific cutting force, power, torque, surface finish and tool life.

## Contents

| Path | Purpose |
|---|---|
| `metal_cutting_exercises.ipynb` | Student notebook: formulas, worked examples, exercises with `check()` |
| `metal_cutting_solutions.ipynb` | Same notebook with all solutions filled in |
| `metalcutting/turning.py` | vc, n, Q, chip thickness, power, cutting force, time, Ra and Rmax |
| `metalcutting/milling.py` | vf, fz, Q, hm and hex for side and face milling, chip thinning, power, torque |
| `metalcutting/drilling.py` | vf, Q, chip thickness, power, torque, feed force |
| `metalcutting/material.py` | kc = kc1 · hm^-mc · (1 - γ0/100) and a material table |
| `metalcutting/tool_life.py` | Taylor equation, fitting from two tests, economic tool life, cost per part |
| `metalcutting/checks.py` | Reference answers and the `check()` function |
| `tests/` | pytest tests, including numerical checks of the chip thickness and drilling power derivations |
| `build_notebooks.py` | Rebuilds both notebooks from one source |

## Usage

```bash
pip install numpy matplotlib pytest nbformat
pytest                      # 32 tests
python build_notebooks.py   # regenerate the notebooks after editing exercises
```

Open `metal_cutting_exercises.ipynb` from this folder so `import metalcutting` works.

## Before teaching with it

* **Material data.** The kc1 and mc values in `metalcutting/material.py` are illustrative. Replace them with the values from the handbook's material table; the reference answers update automatically.
* **Surface roughness.** `surface_roughness_ra` uses the exact result for a circular nose profile (Ra = fn² / (18√3 · rε)). Some handbook editions print a rounded constant; adjust if you want to match it exactly.
* **Answer visibility.** Reference answers are computed in `metalcutting/checks.py`, which students can read. For graded work, convert the exercises to an autograder such as otter-grader.

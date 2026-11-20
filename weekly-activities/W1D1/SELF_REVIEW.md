# W1D1 — Self-Review Checklist

## 1. Environment Setup

- [x] Python virtual environment configured.
- [x] NumPy installed and verified.
- [x] Jupyter Notebook installed and verified.
- [x] IPykernel installed and registered.
- [x] Dedicated Git branch created.

## 2. Implementation

- [x] Created 1D, 2D, and 3D NumPy arrays.
- [x] Verified array shapes, dimensions, and data types.
- [x] Demonstrated NumPy broadcasting.
- [x] Demonstrated vectorised operations without explicit Python loops.
- [x] Performed matrix multiplication using the `@` operator.
- [x] Loaded a real-world Iris CSV dataset.
- [x] Calculated feature-wise mean.
- [x] Calculated feature-wise population standard deviation (`ddof=0`).
- [x] Calculated the correlation matrix.
- [x] Added validation for missing and invalid numerical values.
- [x] Verified all three Python scripts execute successfully.

## 3. Documentation

- [x] Added README.md.
- [x] Added Jupyter Notebook with explanations and outputs.
- [x] Added requirements.txt with verified package versions.
- [x] Documented dataset source and attribution (UCI Machine Learning Repository, CC BY 4.0).
- [x] Captured execution evidence screenshots:
  - [x] `01_array_basics.png`
  - [x] `02_array_operations.png`
  - [x] `03_dataset_statistics.png`

## 4. Code Quality

- [x] Used descriptive variable and function names.
- [x] Added module-level and function docstrings.
- [x] Used type hints for function signatures.
- [x] Used pathlib for dataset path resolution in the Python script.
- [x] Avoided explicit Python loops for vectorised numerical operations.
- [x] Reviewed NumPy broadcasting and matrix multiplication implementations.
- [x] Applied minor PEP 8 spacing corrections.
- [x] Re-executed and verified all three Python scripts after code review.
- [x] Reviewed applicable AI-assisted suggestions.
- [ ] Resolved the Black formatter compatibility issue.

## 5. AI Usage and Review

- [x] Completed CIA interaction 1 using Full Stack Mentor Mode.
- [x] Reviewed `array_basics.py` and `array_operations.py`.
- [x] Completed CIA interaction 2 using Full Stack Mentor Mode.
- [x] Reviewed `dataset_statistics.py`.
- [x] Evaluated AI-assisted suggestions against the actual source code.
- [x] Distinguished genuine issues from optional enhancements.
- [x] Applied relevant PEP 8 corrections.
- [ ] Saved evidence of CIA interaction 1.
- [ ] Saved evidence of CIA interaction 2.

## 6. Git Workflow

- [x] Created feature branch `feat/aiml-W1-dhanush`.
- [ ] Completed at least two descriptive commits.
- [ ] Reviewed staged changes before committing.
- [ ] Pushed the feature branch to GitHub.
- [ ] Created a pull request.
- [ ] Verified that no virtual environment, secrets, or unnecessary files are committed.

## 7. Final Verification

- [x] All three Python scripts execute successfully.
- [x] Expected numerical outputs verified.
- [x] Project structure verified.
- [x] Execution evidence screenshots confirmed.
- [ ] Notebook executes successfully from beginning to end (final verification).
- [ ] README instructions verified.
- [ ] All required deliverables ready for submission.
- [ ] Final Git and pull request verification completed.

## Known Issue — Black Formatter

The Black formatter encountered a Windows Smart App Control restriction involving its compiled extension (`handle_ipynb_magics.cp311-win_amd64.pyd`).

- Smart App Control remains enabled.
- The security restriction has not been bypassed or disabled.
- Black formatting has not been successfully executed in the project environment.
- Awaiting mentor-approved guidance or an alternative formatting workflow.

This issue is documented and remains pending resolution.

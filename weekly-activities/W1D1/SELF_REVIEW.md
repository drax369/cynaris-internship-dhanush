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
- [x] Saved evidence of CIA interaction 1 (`CIA_review_1.png`).
- [x] Saved evidence of CIA interaction 2 (`CIA_review_2.png`).

## 6. Git Workflow

- [x] Created feature branch `feat/aiml-W1-dhanush`.
- [x] Completed at least two descriptive commits.
- [x] Reviewed staged changes before committing.
- [x] Pushed the feature branch to GitHub.
- [x] Created pull request #1 targeting `main`.
- [x] Verified that no virtual environment, secrets, or unnecessary files are committed.

### Commits

1. `eda370d` — `feat(w1d1): implement NumPy fundamentals and Iris statistics`
2. `ab88d0c` — `docs(w1d1): add notebook, dataset, and execution evidence`

### Pull Request

https://github.com/drax369/cynaris-internship-dhanush/pull/1

## 7. Final Verification

- [x] All three Python scripts execute successfully.
- [x] Expected numerical outputs verified.
- [x] Project structure verified.
- [x] Execution evidence screenshots confirmed.
- [x] Notebook executes successfully from beginning to end.
- [x] README instructions and execution commands documented.
- [x] All required W1D1 deliverables prepared and submitted through GitHub.
- [x] Final Git verification completed; working tree was clean before the final evidence update.
- [x] Pull request created and awaiting mentor review.

## Known Issue — Black Formatter

The Black formatter encountered a Windows Smart App Control restriction involving its compiled extension (`handle_ipynb_magics.cp311-win_amd64.pyd`).

- Smart App Control remains enabled.
- The security restriction has not been bypassed or disabled.
- Black formatting has not been successfully executed in the project environment.
- Awaiting mentor-approved guidance or an alternative formatting workflow.

This issue is documented and remains pending resolution.

## Pending External Actions

- [ ] Obtain mentor-approved guidance for the Black formatter issue.
- [ ] Receive mentor review and approval of pull request #1.
- [ ] Address any requested changes from the mentor.

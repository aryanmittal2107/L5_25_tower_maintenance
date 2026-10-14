# Static Analysis Issues and Fixes

| Tool | Issue identified | Fix applied | Result |
|---|---|---|---|
| Bandit | Use of `pickle` to load serialized data, which can execute malicious code | Removed `pickle` and used a safer snapshot approach | No issues identified in the final Bandit scan |
| Bandit | Hard-coded password in source code | Removed the hard-coded credential | No hard-coded password finding in the final scan |
| Bandit | SQL query built using string formatting | Replaced it with a parameterized SQL query | Reduced SQL injection risk |
| Flake8 | Lines exceeding the recommended maximum length | Reformatted long lines | No Flake8 violations in the final scan |
| Flake8 | Extra blank lines and whitespace around operators | Corrected spacing and formatting | No Flake8 violations in the final scan |
| Pylint | Naming, documentation, and code-style issues | Improved naming, docstrings, and code organization | Pylint score improved from 5.14/10 to 10.00/10 |

## Summary

Static analysis helped identify security risks, formatting problems, and maintainability issues. The fixes improved code readability and reduced potential security risks. The final reported results were Pylint 10.00/10, Bandit with no issues identified, and Flake8 with no reported violations.
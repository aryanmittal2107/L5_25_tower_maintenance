# Lab 5 Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

Formatting issues, such as extra blank lines, whitespace around operators, and long lines, were the easiest to fix because they required straightforward changes. Improving naming and adding docstrings were also relatively simple. The harder issues were replacing unsafe serialization, removing hard-coded credentials, and changing SQL queries to use parameters because these changes required understanding how the program handled data and interacted with the database.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

Based on the reports available, I did not confirm any false positives. The reported issues, including unsafe use of `pickle`, hard-coded credentials, and SQL string formatting, were reasonable warnings that deserved attention.

## 3. How would you integrate static analysis tools into your actual software development workflow?

I would run Flake8 and Pylint during development to identify style and maintainability issues early. I would use Bandit to check for common security risks. I would also configure these tools to run before commits and in a continuous integration pipeline so that issues are detected before code is merged.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The Pylint score improved from 5.14/10 to 10.00/10. Bandit reported no issues in the final scan, and Flake8 reported no violations. The code became more consistent and readable, while parameterized SQL reduced SQL injection risk. Removing unsafe deserialization and hard-coded credentials also improved the code's security posture.
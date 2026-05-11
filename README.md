# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey WouterVerbeeck!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/WouterVerbeeck/CopilotInitExercise/issues/1)

## Running Tests

This project uses `pytest` for backend tests.

1. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

2. Run the full test suite:

	```bash
	pytest -q
	```

3. Run only signup tests:

	```bash
	pytest -q -k signup
	```

4. Run only unregister tests:

	```bash
	pytest -q -k unregister
	```

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)


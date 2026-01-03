# Contributing to G4Starter

Thank you for your interest in contributing to G4Starter!

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/G4Starter.git
   cd G4Starter
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run from source**
   ```bash
   python src/main.py
   ```

## Project Structure

```
G4Starter/
├── src/
│   ├── main.py          # Entry point
│   ├── cli.py           # Interactive CLI (questionary)
│   └── generator.py     # Cookiecutter wrapper
├── cookiecutter-g4starter/
│   ├── cookiecutter.json
│   ├── hooks/
│   │   └── post_gen_project.py
│   └── {{cookiecutter.project_name}}/
│       ├── include/     # C++ header templates
│       └── src/         # C++ source templates
├── tests/
│   ├── test_generator.py    # Integration tests
│   └── test_executable.py   # Smoke tests for built executable
├── build.py             # Build script
└── G4Starter.spec       # PyInstaller config
```

## Testing

**Run integration tests**:
```bash
python tests/test_generator.py
```

**Test executable build**:
```bash
python build.py
python tests/test_executable.py
```

## Modifying Templates

C++ templates are in `cookiecutter-g4starter/{{cookiecutter.project_name}}/`

After modifying:
1. Test with `python src/main.py`
2. Run integration tests
3. Build executable and test

## Coding Guidelines

**Python**:
- Use type hints where appropriate
- Follow PEP 8
- Add docstrings to functions
- Use snake_case for functions/variables
- Use PascalCase for classes

**C++ Templates**:
- Follow Geant4 conventions
- Use `f` prefix for member variables (e.g., `fPrimary`)
- Include guards: `#ifndef ClassName_h`
- Modern C++: Use `override`, `= default` where appropriate
- No `a`/`an` prefix for function parameters (use direct names like `run`, `event`)

**Jinja2 Templates**:
- Use `{%-` to avoid blank lines
- Comment with `{# ... #}`
- Test rendering with different variable combinations

## Submitting Changes

1. Create a feature branch from `main`
2. Make your changes
3. Test thoroughly (both source and built executable)
4. Update documentation if needed
5. Submit a pull request with clear description

## Building for Release

1. Update version in relevant files
2. Update CLAUDE.md if architecture changed
3. Build executable: `python build.py`
4. Test on target platform(s)
5. Create tag: `git tag v1.0.0`
6. Push tag: `git push origin v1.0.0`

## Questions?

Open an issue or discussion on GitHub. We're happy to help!

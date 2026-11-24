"""Allow invocation with python -m devtools."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())

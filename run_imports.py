import importlib
import os
import sys
import traceback


def import_one(module_name: str) -> None:
    try:
        importlib.import_module(module_name)
        print(f"OK: {module_name}")
    except Exception as e:
        print(f"FAIL: {module_name}: {e.__class__.__name__}: {e}")
        traceback.print_exc()


def main() -> None:
    # Import targets for every Python file in this small repo.
    # We import modules only; no trading logic is invoked.
    targets = [
        "cli",
        "config",
        "trading_bot",
        "trading_bot.bot",
        "trading_bot.bot.logging_config",
        "trading_bot.bot.client",
        "trading_bot.bot.orders",
        "trading_bot.bot.validators",
        # package __init__ modules also cover side-effects
    ]

    # Ensure repo root is importable
    repo_root = os.path.dirname(os.path.abspath(__file__))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    for t in targets:
        import_one(t)


if __name__ == "__main__":
    main()


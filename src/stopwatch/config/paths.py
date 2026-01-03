from pathlib import Path


SRC = Path(__file__).parents[2]
ROOT = SRC.parent


if __name__ == "__main__":
    print(SRC)
    print(ROOT)
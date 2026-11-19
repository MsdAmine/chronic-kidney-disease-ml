"""Download the unchanged UCI CKD CSV without overwriting existing data."""

import os
import sys
from http.client import HTTPException
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.error import URLError
from urllib.request import urlopen

DATASET_URL = "https://archive.ics.uci.edu/static/public/336/data.csv"
DATASET_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "raw"
    / "chronic_kidney_disease.csv"
)
TIMEOUT_SECONDS = 30


def main() -> int:
    """Retrieve the raw bytes safely and return a command-line exit status."""
    if DATASET_PATH.exists():
        print(f"Dataset already exists; left unchanged: {DATASET_PATH}")
        return 0

    try:
        with urlopen(DATASET_URL, timeout=TIMEOUT_SECONDS) as response:
            data = response.read()
            expected_size = response.headers.get("Content-Length")

        if not data:
            raise ValueError("The server returned an empty response.")
        if expected_size is not None and len(data) != int(expected_size):
            raise ValueError("Response size does not match Content-Length.")

        DATASET_PATH.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(
            prefix=".ckd-download-", dir=DATASET_PATH.parent
        ) as temporary_directory:
            temporary_path = Path(temporary_directory) / DATASET_PATH.name
            temporary_path.write_bytes(data)
            try:
                # Publish complete bytes atomically without replacing a path.
                os.link(temporary_path, DATASET_PATH)
            except FileExistsError:
                print(
                    f"Dataset already exists; left unchanged: {DATASET_PATH}"
                )
                return 0
    except (OSError, URLError, HTTPException, ValueError) as error:
        print(f"Download failed: {error}", file=sys.stderr)
        return 1

    print(f"Downloaded {len(data)} bytes to {DATASET_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

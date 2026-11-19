"""Validate the local UCI CKD CSV without modifying the raw dataset."""

import unittest
from pathlib import Path

import pandas as pd

DATASET_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "raw"
    / "chronic_kidney_disease.csv"
)

# Independently verified against https://archive.ics.uci.edu/api/dataset?id=336
EXPECTED_COLUMNS = [
    "age", "bp", "sg", "al", "su", "rbc", "pc", "pcc", "ba", "bgr",
    "bu", "sc", "sod", "pot", "hemo", "pcv", "wbcc", "rbcc", "htn",
    "dm", "cad", "appet", "pe", "ane", "class",
]


class DatasetLoadingTests(unittest.TestCase):
    """Check the source schema and target labels using one shared read."""

    @classmethod
    def setUpClass(cls) -> None:
        """Load once; fail clearly when the local dataset is unavailable."""
        if not DATASET_PATH.is_file():
            raise FileNotFoundError(
                f"Dataset not found: {DATASET_PATH}. "
                "From the repository root, run: "
                ".\\.venv\\Scripts\\python.exe src/download_data.py"
            )
        cls.dataset = pd.read_csv(DATASET_PATH)

    def test_dataset_file_is_available(self) -> None:
        self.assertTrue(DATASET_PATH.is_file())
        self.assertGreater(DATASET_PATH.stat().st_size, 0)

    def test_csv_loads_successfully(self) -> None:
        self.assertIsInstance(self.dataset, pd.DataFrame)
        self.assertFalse(self.dataset.empty)

    def test_dataset_dimensions(self) -> None:
        self.assertEqual(self.dataset.shape, (400, 25))

    def test_exact_column_names_and_order(self) -> None:
        self.assertListEqual(self.dataset.columns.tolist(), EXPECTED_COLUMNS)

    def test_target_column_is_present(self) -> None:
        self.assertIn("class", self.dataset.columns)

    def test_target_labels_are_not_missing_or_empty(self) -> None:
        target = self.dataset["class"]
        self.assertFalse(target.isna().any(), "Target labels contain nulls.")
        self.assertFalse(
            target.str.strip().eq("").any(),
            "Target labels contain empty or whitespace-only strings.",
        )

    def test_expected_target_categories(self) -> None:
        # The source includes 'ckd\t'; strip only for this comparison.
        normalized_target = self.dataset["class"].str.strip()
        self.assertSetEqual(set(normalized_target), {"ckd", "notckd"})


if __name__ == "__main__":
    unittest.main()

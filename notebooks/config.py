from pathlib import Path
from datetime import date
import numpy as np

# PROJECT ROOT
PROJECT_ROOT = Path(r"D:\.workspace\Programming\Projects\E-cup_2026_by_Ozon_Tech")

# 00.1 - CV DATES
CV_AS_OF = date(2026, 1, 14)
CV_TARGET_START = date(2026, 1, 15)
CV_TARGET_END = date(2026, 2, 13)

# 00.2 - TARGET DATES
TARGET_AS_OF = date(2026, 2, 13)
TARGET_START = date(2026, 2, 14)
TARGET_END = date(2026, 3, 15)

# 01.1 - DATASETS DIRECTORIES
DATA_DIR = PROJECT_ROOT / "data"
DATA_RAW_DIR = DATA_DIR / "raw"
DATA_PROCESSED_DIR = DATA_DIR / "processed"
DATA_FEATURES_DIR = DATA_PROCESSED_DIR / "features"
DATA_SUBMISSIONS_DIR = DATA_DIR / "submissions"

# 01.2 - DATASETS PATHS
TRAIN_PATH = DATA_RAW_DIR / "train.parquet"
CV_TARGET_PATH = DATA_PROCESSED_DIR / "cv_target_2026-01-14.parquet"
HISTORY_PATH = DATA_PROCESSED_DIR / "history_before_2026-01-14.parquet"
CV_FEATURES_PATH = DATA_FEATURES_DIR / "cv_features_2026-01-14.parquet"
TARGET_FEATURES_PATH = DATA_FEATURES_DIR / "target_features_2026-02-13.parquet"

# 02.1 - MODEL DIRECTORIES
MODELS_DIR = PROJECT_ROOT / "models"

# 03.1 REPORTS DIRECTORIES
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_GMV_DIR = REPORTS_DIR / "gmv"
REPORTS_CONV_FUNL_DIR = REPORTS_DIR / "conv_funl"
REPORTS_FEATURES_DIR = REPORTS_DIR / "features"

# 03.2 - MODEL LEARNING REPORTS DIRECTORIES
REPORTS_MODELS_DIR = REPORTS_DIR / "models"
REPORTS_MODELS_GRAPHS_DIR = REPORTS_MODELS_DIR / "graphs"
REPORTS_MODELS_LOGS_DIR = REPORTS_MODELS_DIR / "logs"

# REPEATABILITY OF EXPERIMENTS
RANDOM_STATE = 17
RANDOM_STATES_100 = np.linspace(1, 100, 1)

# GMV BINS
BIN_ORDER = ["0-1%", "1-5%", "5-10%", "10-20%", "20-50%", "50-100%"]

# WINDOWS FOR TIME SERIES FEATURES
WINDOWS = [7, 14, 28, 30, 60, 90]

# CREATE DIRECTORIES
def create_directories():
    """Creates all the necessary directories"""
    dirs = [
        # Datasets
        DATA_DIR,
        DATA_RAW_DIR, DATA_PROCESSED_DIR, DATA_FEATURES_DIR, DATA_SUBMISSIONS_DIR,

        # Models
        MODELS_DIR,

        # Reports
        REPORTS_DIR,
        REPORTS_GMV_DIR, REPORTS_CONV_FUNL_DIR,
        REPORTS_FEATURES_DIR,
        REPORTS_MODELS_DIR, REPORTS_MODELS_GRAPHS_DIR, REPORTS_MODELS_LOGS_DIR
    ]
    for d in dirs:
        d.mkdir(parents = True, exist_ok = True)
    print("All directories created successfully")

# VALIDATION
def validate_data_exists():
    """Checks for the necessary files"""
    checks = [
        ("TRAIN_PATH", TRAIN_PATH)
    ]
    
    all_ok = True
    for name, path in checks:
        if path.exists():
            size_mb = path.stat().st_size / 1024 / 1024
            print(f"{name}: {size_mb:.2f} MB")
        else:
            print(f"{name}: NOT FOUND at {path}")
            all_ok = False
    
    if all_ok:
        print("\nAll data files are present")
    else:
        print("\nSome data files are missing")
    
    return all_ok
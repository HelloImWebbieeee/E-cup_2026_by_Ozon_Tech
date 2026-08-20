from pathlib import Path
from datetime import date

# PROJECT ROOT
PROJECT_ROOT = Path(r"D:\.workspace\Programming\Projects\E-cup_2026_by_Ozon_Tech")

# DATES
AS_OF = date(2026, 1, 14)
TARGET_START = date(2026, 1, 15)
TARGET_END = date(2026, 2, 13)

# DATA DIRECTORIES
DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DATA_FEATURES_DIR = DATA_PROCESSED_DIR / "features"

# DATA PATHS
TRAIN_PATH = DATA_RAW_DIR / "train.parquet"
CV_TARGET_PATH = DATA_PROCESSED_DIR / "cv_target_2026-01-14.parquet"
HISTORY_PATH = DATA_PROCESSED_DIR / "history_before_2026-01-14.parquet"
CV_FEATURES_PATH = DATA_FEATURES_DIR / "cv_features_2026-01-14.parquet"

# REPORTS PATHS
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_GMV_DIR = REPORTS_DIR / "gmv"
REPORTS_CONV_FUNL_DIR = REPORTS_DIR / "conv_funl"
REPORTS_FEATURES_DIR = REPORTS_DIR / "features"
REPORTS_MODELS_DIR = REPORTS_DIR / "models"

# MODELS PATHS
MODELS_DIR = PROJECT_ROOT / "models"

# CREATE DIRECTORIES
def create_directories():
    """Creates all the necessary directories"""
    dirs = [
        DATA_RAW_DIR,
        DATA_PROCESSED_DIR,
        DATA_FEATURES_DIR,
        REPORTS_DIR,
        REPORTS_GMV_DIR,
        REPORTS_CONV_FUNL_DIR,
        REPORTS_FEATURES_DIR,
        REPORTS_MODELS_DIR,
        MODELS_DIR,
    ]
    for d in dirs:
        d.mkdir(parents = True, exist_ok = True)
    print("All directories created successfully.")

# FEATURE ENGINEERING CONFIG
WINDOWS = [7, 14, 30, 60, 90, 180, 365]

GMV_COLS = ["gmv", "gmv_search", "gmv_cat"]
ACTIVITY_COLS = ["search", "cat", "to_cart", "to_ord"]
CONVERSION_COLS = [
    "search_to_cart", "search_to_ord",
    "cat_to_cart", "cat_to_ord",
    "has_search_to_cart", "has_search_to_ord",
    "has_cat_to_cart", "has_cat_to_ord",
]

# GMV BINS
BIN_ORDER = ["0-1%", "1-5%", "5-10%", "10-20%", "20-50%", "50-100%"]

# VALIDATION
def validate_data_exists():
    """Checks for the necessary files"""
    checks = [
        ("TRAIN_PATH", TRAIN_PATH),
        ("CV_TARGET_PATH", CV_TARGET_PATH),
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
        print("\nAll data files are present.")
    else:
        print("\nSome data files are missing!")
    
    return all_ok
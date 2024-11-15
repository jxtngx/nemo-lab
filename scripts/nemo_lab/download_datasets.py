import os

from datasets import load_dataset

cache_dir = os.path.join(".lab-datasets/cache")

# load_dataset will check cache for existing download
# uncomment each dataset to download

# Stanford Alpaca
load_dataset("tatsu-lab/alpaca", cache_dir=cache_dir)

# NVIDIA ChatQA synthetic_convqa
load_dataset("nvidia/ChatQA-Training-Data", "synthetic_convqa", cache_dir=cache_dir)

# NVIDIA ChatQA Stanford Q&A
load_dataset("nvidia/ChatQA-Training-Data", "squad2.0", cache_dir=cache_dir)

# NVIDIA OpenMathInstruct-2
load_dataset("nvidia/OpenMathInstruct-2", cache_dir=cache_dir)

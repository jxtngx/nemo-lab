pip install -e ".[all]"
pip install git+https://github.com/NVIDIA/NeMo-Run.git
pip install git+https://github.com/NVIDIA/Megatron-LM.git
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" git+https://github.com/NVIDIA/apex.git
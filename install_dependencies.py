import subprocess
import sys

def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
  install("torch --index-url https://download.pytorch.org/whl/cpu")
  install("torchvision --index-url https://download.pytorch.org/whl/cpu")
  install("torchaudio --index-url https://download.pytorch.org/whl/cpu")

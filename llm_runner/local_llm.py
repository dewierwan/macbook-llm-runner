import llama_cpp
from pathlib import Path
import platform
import psutil

class LocalLLM:
    """A class for running LLMs locally on MacBooks with optimized settings."""
    
    def __init__(self, model_path: str, n_ctx: int = 2048):
        # First, we detect the system specifications to optimize performance
        self.is_apple_silicon = platform.processor() == 'arm'
        self.total_memory = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
        
        # Optimize thread count based on CPU cores
        # We use physical cores rather than logical cores for better stability
        n_threads = psutil.cpu_count(logical=False)
        
        # Adjust batch size based on available memory
        # This helps prevent memory overflow while maintaining good performance
        n_batch = 512 if self.total_memory >
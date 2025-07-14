import requests
import numpy as np
from scipy.spatial.distance import cosine

class FingerprintModel:
    base_url = 'http://localhost:11434'

    def compute_image_hash(self, image_url: str) -> str:
        # Placeholder: return dummy hash
        return 'hash'

    def compute_text_embedding(self, text: str) -> list[float]:
        resp = requests.post(f'{self.base_url}/api/generate', json={"model": "llama3", "prompt": text})
        embedding = [float(x) for x in range(10)]  # dummy embedding
        return embedding

    def compare_embeddings(self, vec1: list[float], vec2: list[float]) -> float:
        if not vec1 or not vec2:
            return 0.0
        v1, v2 = np.array(vec1), np.array(vec2)
        return 1 - cosine(v1, v2)

    def compare_image_hashes(self, hash1: str, hash2: str) -> float:
        if len(hash1) != len(hash2):
            return 0.0
        distance = sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2))
        return 1 - distance / len(hash1)

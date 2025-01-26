import os
import yaml
from functools import lru_cache

class ContentLoader:
    def __init__(self, content_dir):
        self.content_dir = content_dir
        self.base_content = self._load_yaml('base.yml')
        
    def _merge_dicts(self, dict1, dict2):
        """Deep merge two dictionaries"""
        result = dict1.copy()
        for key, value in dict2.items():
            if isinstance(value, dict) and key in result and isinstance(result[key], dict):
                result[key] = self._merge_dicts(result[key], value)
            else:
                result[key] = value
        return result

    @lru_cache(maxsize=32)
    def get_page_content(self, page_name):
        """Load content for a specific page"""
        page_content = self._load_yaml(f'pages/{page_name}.yml')
        return self._merge_dicts(self.base_content, page_content)
    
    def _load_yaml(self, relative_path):
        """Load YAML file from content directory"""
        full_path = os.path.join(self.content_dir, relative_path)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return {}

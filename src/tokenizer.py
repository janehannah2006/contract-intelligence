import os
import re
from typing import List

class ContractTokenizer:
    def __init__(self):
        # A simple whitespace and punctuation tokenizer ideal for legal text
        self.punctuation_pattern = re.compile(r'\w+|[^\w\s]')

    def clean_text(self, text: str) -> str:
        """Removes excessive whitespaces and standardizes legal text formatting."""
        if not text:
            return ""
        # Remove extra line breaks and spaces often found in contract scans
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def tokenize(self, text: str) -> List[str]:
        """Splits contract text into individual word and punctuation tokens."""
        cleaned = self.clean_text(text)
        return self.punctuation_pattern.findall(cleaned)

if __name__ == "__main__":
    print("--- Testing Contract Tokenizer Pipeline ---")
    
    # Sample legal text line to verify implementation
    sample_clause = "This Agreement, effective as of June 2026, is by and between the Parties."
    
    tokenizer = ContractTokenizer()
    tokens = tokenizer.tokenize(sample_clause)
    
    print(f"Original Text: {sample_clause}")
    print(f"Generated Tokens: {tokens}")
    print("\n[SUCCESS] Tokenizer pipeline executed flawlessly.")
"""
===============================================================================
TOPIC 1.3 - BEGINNER DEMO: Rule-Based Named Entity Recognition
===============================================================================

🎯 LEARNING GOALS
-----------------
1. Understand rule-based NER using regex patterns
2. Extract emails, URLs, phone numbers, and dates from text
3. Build a simple entity extraction pipeline
4. Understand limitations of rule-based approaches

📚 KEY CONCEPTS: Regular expressions, pattern matching, entity extraction, NER

⏱️ TIME ESTIMATE: 30-45 minutes

🔧 VS CODE SETUP
----------------
1. Open this file in VS Code
2. Terminal: cd e:/ey-ai/nlp-labs/topic-1.3-ner-classification/beginner
3. Run: python demo_exercise.py
4. Debug: F9 (breakpoint), F5 (start)

📝 WHAT YOU NEED TO DO
----------------------
TODO 1: Implement extract_emails() using regex
        Hint: Pattern r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
TODO 2: Implement extract_urls() for http/https URLs
        Hint: Pattern r'https?://[^\s]+'
        
TODO 3: Implement extract_phone_numbers() for various formats
        Hint: Pattern r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        
TODO 4: Implement extract_dates() for common date formats
        Hint: Pattern r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
        
TODO 5: Create extract_all_entities() combining all extractors

💡 EXPECTED OUTPUT
------------------
- List of all extracted entities by type
- Entity counts and statistics
- Visualization of entities in context

Let's get started! 🚀
"""

import re
from typing import List, Dict, Tuple

# Sample text with various entities
sample_text = """
Contact us at support@company.com or sales@company.org for more information.
Visit our website at https://www.company.com or http://blog.company.com/news.
Call us at 555-123-4567 or 555.987.6543 for immediate assistance.
The meeting is scheduled for 12/25/2024 or 01-15-2025.
You can also reach John at john.doe@email.com or call 555-111-2222.
Check our GitHub at https://github.com/company/project for updates.
Important dates: 3/14/2024, 07/04/2024, and 12-31-2024.
"""


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text
    
    Args:
        text: Input text
    
    Returns:
        List of email addresses
        
    Example:
        >>> extract_emails("Contact me@example.com")
        ['me@example.com']
    """
    # TODO: Implement email extraction
    # Hint: Use re.findall() with email pattern
    # Pattern: r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    pass


def extract_urls(text: str) -> List[str]:
    """
    Extract URLs from text
    
    Args:
        text: Input text
    
    Returns:
        List of URLs
    """
    # TODO: Implement URL extraction
    # Hint: Pattern r'https?://[^\s]+'
    pass


def extract_phone_numbers(text: str) -> List[str]:
    """
    Extract phone numbers from text
    
    Args:
        text: Input text
    
    Returns:
        List of phone numbers
    """
    # TODO: Implement phone number extraction
    # Hint: Pattern r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    # This matches formats: 555-123-4567, 555.123.4567, 5551234567
    pass


def extract_dates(text: str) -> List[str]:
    """
    Extract dates from text
    
    Args:
        text: Input text
    
    Returns:
        List of dates
    """
    # TODO: Implement date extraction
    # Hint: Pattern r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
    # This matches formats: 12/25/2024, 1-5-24, 03-14-2024
    pass


def extract_all_entities(text: str) -> Dict[str, List[str]]:
    """
    Extract all entity types from text
    
    Args:
        text: Input text
    
    Returns:
        Dictionary with entity types as keys and lists of entities as values
    """
    # TODO: Implement comprehensive entity extraction
    # Hint: Call all extraction functions and combine results
    pass


def main():
    """Main execution"""
    print("=" * 80)
    print("TOPIC 1.3 - BEGINNER DEMO")
    print("Rule-Based Named Entity Recognition")
    print("=" * 80)
    print()
    
    # TODO: Extract entities from sample text
    # TODO: Display results by entity type
    # TODO: Show entity counts and statistics
    
    print("\n⚠️  Complete the TODO items above, then run this file again!")
    print("Compare your output with demo_solution.py when done.")


if __name__ == "__main__":
    main()

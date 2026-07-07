"""
===============================================================================
✅ COMPLETE SOLUTION
TOPIC 1.3 - BEGINNER DEMO: Rule-Based Named Entity Recognition
===============================================================================
"""

import re
from typing import List, Dict

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
    """Extract email addresses"""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)


def extract_urls(text: str) -> List[str]:
    """Extract URLs"""
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)


def extract_phone_numbers(text: str) -> List[str]:
    """Extract phone numbers"""
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)


def extract_dates(text: str) -> List[str]:
    """Extract dates"""
    pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
    return re.findall(pattern, text)


def extract_all_entities(text: str) -> Dict[str, List[str]]:
    """Extract all entity types"""
    return {
        'emails': extract_emails(text),
        'urls': extract_urls(text),
        'phone_numbers': extract_phone_numbers(text),
        'dates': extract_dates(text)
    }


def highlight_entities_in_text(text: str, entities: Dict[str, List[str]]):
    """Highlight entities in original text"""
    print("\n" + "="*80)
    print("ENTITIES HIGHLIGHTED IN TEXT")
    print("="*80)
    
    highlighted = text
    
    # Replace entities with highlighted versions
    for email in entities['emails']:
        highlighted = highlighted.replace(email, f"[EMAIL: {email}]")
    
    for url in entities['urls']:
        highlighted = highlighted.replace(url, f"[URL: {url}]")
    
    for phone in entities['phone_numbers']:
        highlighted = highlighted.replace(phone, f"[PHONE: {phone}]")
    
    for date in entities['dates']:
        highlighted = highlighted.replace(date, f"[DATE: {date}]")
    
    print(highlighted)


def main():
    """Main demonstration"""
    print("=" * 80)
    print("TOPIC 1.3 - BEGINNER DEMO SOLUTION")
    print("Rule-Based Named Entity Recognition")
    print("=" * 80)
    
    print("\n📄 Original Text:")
    print(sample_text)
    
    # Extract all entities
    print("\n⚙️  Extracting entities...")
    entities = extract_all_entities(sample_text)
    
    # Display results
    print("\n" + "="*80)
    print("EXTRACTED ENTITIES")
    print("="*80)
    
    print(f"\n📧 Emails ({len(entities['emails'])}):")
    for email in entities['emails']:
        print(f"   - {email}")
    
    print(f"\n🌐 URLs ({len(entities['urls'])}):")
    for url in entities['urls']:
        print(f"   - {url}")
    
    print(f"\n📞 Phone Numbers ({len(entities['phone_numbers'])}):")
    for phone in entities['phone_numbers']:
        print(f"   - {phone}")
    
    print(f"\n📅 Dates ({len(entities['dates'])}):")
    for date in entities['dates']:
        print(f"   - {date}")
    
    # Statistics
    print("\n" + "="*80)
    print("EXTRACTION STATISTICS")
    print("="*80)
    
    total = sum(len(v) for v in entities.values())
    print(f"\n📊 Total entities found: {total}")
    print(f"   Emails: {len(entities['emails'])}")
    print(f"   URLs: {len(entities['urls'])}")
    print(f"   Phone Numbers: {len(entities['phone_numbers'])}")
    print(f"   Dates: {len(entities['dates'])}")
    
    # Highlight in text
    highlight_entities_in_text(sample_text, entities)
    
    # Demonstrate limitations
    print("\n" + "="*80)
    print("LIMITATIONS OF RULE-BASED NER")
    print("="*80)
    
    print("\n⚠️  Rule-based NER limitations:")
    print("1. Only finds exact patterns (misses variations)")
    print("2. No context understanding (can't distinguish 'Apple' company vs fruit)")
    print("3. Hard to maintain (need rules for every pattern)")
    print("4. Language-specific (rules don't transfer to other languages)")
    print("5. Misses complex entities (named persons, organizations without patterns)")
    
    test_text = "Apple CEO Tim Cook announced new products. Dr. Smith lives at 123 Main St."
    print(f"\n📝 Example text: '{test_text}'")
    print(f"   ❌ Cannot extract: 'Apple' (company), 'Tim Cook' (person),")
    print(f"      'Dr. Smith' (person), '123 Main St' (address)")
    print(f"   ✅ For these, we need ML-based NER (spaCy, transformers)")
    
    print("\n" + "="*80)
    print("✅ SOLUTION COMPLETE!")
    print("="*80)
    print("\n📚 KEY TAKEAWAYS:")
    print("1. Rule-based NER uses regex patterns to find entities")
    print("2. Works well for structured entities (emails, URLs, dates)")
    print("3. Fast and no training data needed")
    print("4. Limited to exact patterns, no semantic understanding")
    print("5. Use ML-based NER (spaCy, BERT) for complex entities")
    
    print("\n💡 TRY THIS:")
    print("- Add patterns for credit cards, SSNs, IP addresses")
    print("- Extract hashtags and mentions from social media text")
    print("- Build a data anonymization tool")
    print("- Combine with spaCy for hybrid NER (next exercise!)")


if __name__ == "__main__":
    main()

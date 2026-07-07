# Lab 1D — Named Entity Recognition on Enterprise Documents

**Module:** 1 — NLP Fundamentals  
**Difficulty:** Intermediate  
**Duration:** 45 minutes  
**What you'll build:** A script that extracts structured information from loan agreements using three different methods — regex rules, spaCy NER, and an LLM — then compares their accuracy.

---

## Why This Matters

Banks process thousands of loan documents every day. Manually extracting borrower name, loan amount, interest rate, and repayment dates from each document is expensive and error-prone. Automating this with NER (Named Entity Recognition) can reduce processing time from hours to seconds. But which method is most accurate and practical?

---

## Learning Objectives

1. Write regex patterns to extract structured fields.
2. Use spaCy's NER to extract entities and map them to a schema.
3. Use Azure OpenAI to extract entities using a prompt (LLM-based approach).
4. Compare all three methods against a manually verified ground truth.
5. Choose the right approach for different enterprise scenarios.

---

## Prerequisites

```bash
pip install spacy pandas openai python-dotenv
python -m spacy download en_core_web_sm
```

If you have Azure OpenAI access, create a `.env` file in your project folder:
```
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

**No Azure access?** The lab works without it — the LLM step is optional (Steps 7–8). You can compare regex vs spaCy only.

---

## Dataset

12 fictional loan agreement excerpts are embedded directly in the code below.

---

## Step 1 — Import Libraries

```python
import re
import json
import pandas as pd
import spacy
from typing import Dict, Optional
import os

# Optional: Azure OpenAI
try:
    from openai import AzureOpenAI
    from dotenv import load_dotenv
    load_dotenv()
    HAS_AZURE = bool(os.getenv("AZURE_OPENAI_API_KEY"))
except ImportError:
    HAS_AZURE = False
    print("Note: openai/dotenv not installed. LLM step will be skipped.")

# Load spaCy
nlp = spacy.load("en_core_web_sm")

print(f"spaCy loaded. Azure OpenAI available: {HAS_AZURE}")
```

---

## Step 2 — Load the Loan Agreement Dataset

```python
loan_agreements = [
    {
        "doc_id": "LOAN_001",
        "text": """LOAN AGREEMENT

This Loan Agreement is entered into on the 15th day of March, 2024, between 
Borrower: Rajesh Kumar Sharma, residing at 42, MG Road, Bangalore - 560001, 
and Lender: Horizon Bank Ltd.

Loan Amount: The bank agrees to lend a principal amount of INR 25,00,000 
(Indian Rupees Twenty-Five Lakhs Only).

Interest Rate: The loan shall carry an interest rate of 8.75% per annum, 
calculated on a reducing balance basis.

Repayment Period: The loan shall be repaid over a tenure of 180 months (15 years) 
commencing from April 15, 2024.

Monthly EMI: INR 24,891/-

Late Payment Penalty: A penalty of 2% per month shall be levied on any 
overdue installment beyond 30 days from the due date.

Security: The loan is secured by mortgage of residential property located at 
42, MG Road, Bangalore."""
    },
    {
        "doc_id": "LOAN_002",
        "text": """PERSONAL LOAN AGREEMENT

Date: 22 January 2024

Borrower Details:
Name: Priya Venkataraman
PAN: ABCPV1234D
Address: Flat 5B, Sunrise Apartments, Chennai - 600042

Lender: Metropolis Finance Corporation

Principal Amount: Rs. 5,00,000/- (Rupees Five Lakhs)
Annual Interest Rate: 13.5% p.a. (fixed)
Loan Tenure: 36 months
Processing Fee: 1.5% of loan amount (Rs. 7,500/-)

Repayment: 36 equal monthly installments of Rs. 16,963/- each, 
commencing February 22, 2024.

Pre-payment Charges: 4% of outstanding principal if prepaid within 12 months; 
Nil thereafter.

In case of default for more than 90 days, the entire outstanding amount 
becomes immediately due and payable."""
    },
    {
        "doc_id": "LOAN_003",
        "text": """COMMERCIAL VEHICLE LOAN AGREEMENT

Agreement No: CVL-2024-00847

This agreement dated February 10, 2024 is between:
Borrower: M/s Sharma Logistics Pvt. Ltd., represented by its Director, 
Anil Sharma, 8, Industrial Area Phase II, Chandigarh.

Financier: Capital Auto Finance Ltd.

Vehicle Financed: Tata Prima 4928.S (32-ton truck)
Invoice Value: INR 42,00,000/-
Down Payment: INR 8,40,000/- (20%)
Loan Amount: INR 33,60,000/-
Rate of Interest: 9.25% per annum (floating, linked to MCLR)
Repayment Period: 60 months
EMI Amount: INR 69,957/-

Security: Hypothecation of the financed vehicle. The bank holds RC book.
Personal Guarantee: Anil Sharma (Director)

Foreclosure: Allowed after 6 EMI payments with 3% foreclosure charges."""
    },
    {
        "doc_id": "LOAN_004",
        "text": """EDUCATION LOAN SANCTION LETTER

Date: 5th April 2024
Reference No: EDU/2024/KOL/4412

Dear Ms. Sunita Bose,

We are pleased to sanction an education loan as per the following terms:

Student Name: Sunita Bose
Co-borrower: Debashish Bose (Father)
Course: M.S. Computer Science, Stanford University, USA
Loan Amount Sanctioned: USD 75,000 (equivalent to approx. INR 62,25,000 
at current exchange rate)

Interest Rate: 9.00% per annum during course period; 
10.50% per annum during repayment period.
Moratorium Period: Course duration + 12 months (max 6 years)
Repayment Period: 10 years from end of moratorium
Estimated EMI: INR 68,450/- per month (post-moratorium)

Collateral: Residential property valued at INR 85,00,000 
pledged by Debashish Bose.

Penalty for default: 2% above normal interest rate on overdue amount."""
    },
    {
        "doc_id": "LOAN_005",
        "text": """HOME LOAN AGREEMENT

This agreement, dated 30 June 2024, is executed between:

BORROWER: Mohammed Irfan Khan, S/O Late Aziz Khan
Address: House No. 7, Nizam Colony, Hyderabad - 500064
Co-Borrower: Fatima Khan (Spouse)

LENDER: National Housing Bank Ltd.

Sanctioned Amount: INR 45,00,000/-
Purpose: Purchase of residential apartment, 3BHK, 
"Green Valley" Complex, Gachibowli, Hyderabad.

Rate of Interest: 8.40% per annum (floating), linked to repo rate.
Loan Term: 240 months (20 years)
EMI: INR 38,716/-

Prepayment: No charges for partial or full prepayment as per 
RBI circular dated November 2, 2022.

Penalty on default: 24% per annum on overdue amount.
SARFAESI provisions applicable in case of default exceeding 90 days."""
    },
    {
        "doc_id": "LOAN_006",
        "text": """GOLD LOAN AGREEMENT

Agreement Date: July 18, 2024
Branch: Kochi Main Branch

Borrower: Thankamma Joseph
Address: TC 45/2891, Pattom, Thiruvananthapuram - 695004

Gold Weight Pledged: 85 grams (22 Karat)
Market Value of Gold: INR 5,27,000/-
Loan to Value (LTV): 75%
Loan Amount: INR 3,95,250/-
Interest Rate: 11% per annum (monthly reducing)
Loan Period: 12 months
Monthly Interest: INR 3,621/-
Bullet Repayment: Full principal + interest by July 18, 2025.

Late penalty: INR 500 flat per month beyond due date.
Auction clause: Gold to be auctioned if loan unpaid for 3 months beyond maturity."""
    },
    {
        "doc_id": "LOAN_007",
        "text": """MSME TERM LOAN AGREEMENT

Dated: 12 August 2024
Sanction Reference: MSME/2024/MUM/7739

Borrower: M/s Patel Auto Components, a Partnership Firm, 
Partner: Mahesh Patel, GSTIN: 27ABCDE1234F1Z1
Registered Office: Shop 14, MIDC, Andheri East, Mumbai - 400093.

Loan Type: Working Capital Term Loan
Loan Amount: INR 1,50,00,000/- (One Crore Fifty Lakhs)
Interest Rate: 10.75% per annum (quarterly reset, linked to MCLR)
Repayment: 84 monthly installments of INR 2,57,912/-
First EMI Due: September 12, 2024

Primary Security: Hypothecation of stock-in-trade and book debts.
Collateral: Commercial property at MIDC, Andheri East (value: INR 2.2 Cr).
Guarantee: Personal guarantee of Mahesh Patel.

Default clause: Two consecutive EMI defaults trigger recall notice."""
    },
    {
        "doc_id": "LOAN_008",
        "text": """TWO-WHEELER LOAN AGREEMENT

Date: 3 September 2024

Borrower: Kavitha Ramachandran
Address: No. 22, 3rd Cross, Rajajinagar, Bangalore - 560010
Occupation: Nurse, Apollo Hospital, Bangalore.

Lender: Quick Ride Finance Pvt. Ltd.

Vehicle: Honda Activa 6G (Petrol)
Ex-Showroom Price: INR 74,000/-
Down Payment: INR 14,800/-
Loan Amount: INR 62,700/-
Interest Rate: 15.5% per annum (flat rate)
Tenure: 24 months
Monthly EMI: INR 3,259/-

Overdue charges: Rs. 250/- per week after 7-day grace period.
Repossession: Vehicle to be repossessed after 3 consecutive EMI defaults."""
    },
    {
        "doc_id": "LOAN_009",
        "text": """LOAN AGAINST PROPERTY (LAP) AGREEMENT

This Agreement is dated October 1, 2024.

BORROWER: Dr. Sanjay Mehta, M.D. (Orthopedics)
Clinic: Mehta Orthopedic Center, 101 Park Street, Kolkata - 700016

LENDER: Eastside Credit Union

Property Mortgaged: Commercial property at 101 Park Street, Kolkata.
Current Market Value: INR 1,20,00,000/-
LTV: 65%
Loan Sanctioned: INR 78,00,000/-

Rate of Interest: 9.85% per annum (floating, annual reset)
Tenure: 120 months
EMI: INR 1,02,476/-

Pre-payment: Allowed anytime; 2% penalty if within first 3 years.
Legal action: DRT (Debt Recovery Tribunal) proceedings for default over 6 months."""
    },
    {
        "doc_id": "LOAN_010",
        "text": """CONSUMER DURABLE LOAN AGREEMENT

Date: November 15, 2024

Name of Borrower: Sneha Kulkarni
Address: Flat 302, Saideep Heights, Pune - 411007

Product Financed: Samsung 65-inch QLED Smart TV (Model: QA65QN90C)
Product Price: INR 1,29,990/-
Down Payment: INR 19,999/-
Loan Amount: INR 1,09,991/-
No-Cost EMI: 0% interest for 12 months (interest subvented by manufacturer)
Monthly EMI: INR 9,166/-

Pre-closure: Allowed with 2% fee if closed within 6 months.
Late payment: Rs. 450/- flat fee per delayed EMI."""
    },
    {
        "doc_id": "LOAN_011",
        "text": """AGRICULTURAL LOAN AGREEMENT

Date: 1 December 2024
Reference: AGRI/KCC/2024/RJ/00341

Borrower: Ramchandra Yadav, 
Village: Ganeshpur, Tehsil: Jaipur Rural, District: Jaipur, Rajasthan - 303004.
Land Holdings: 4.5 acres (Khasra No: 145, 146, 147)

Scheme: Kisan Credit Card (KCC)
Bank: Rajasthan Grameen Bank

Credit Limit: INR 2,20,000/- (Two Lakhs Twenty Thousand)
Interest Rate: 7% per annum (after 2% government subvention, effective rate 5% p.a.)
Repayment: Annual — due within 12 months from disbursement.
Collateral: Mortgage of agricultural land (4.5 acres).

Penalty: 1% per quarter on overdue balance beyond due date."""
    },
    {
        "doc_id": "LOAN_012",
        "text": """MICROFINANCE LOAN AGREEMENT

Group Name: Shakti Self-Help Group
Meeting Center: Anganwadi, Ward 4, Tumkur, Karnataka.

Lead Borrower: Lakshmi Devi
Member ID: KA-SHG-2024-00831

Loan Cycle: 3rd Cycle
Loan Amount: INR 50,000/- (Fifty Thousand)
Purpose: Purchase of sewing machines for tailoring business.
Disbursement Date: December 10, 2024.

Interest Rate: 22% per annum (reducing balance)
Repayment: 52 weekly installments of INR 1,106/-
First Installment Due: December 17, 2024.

Group Guarantee: All 10 group members are jointly and severally liable.
Insurance: Credit life insurance premium of INR 500/- collected upfront."""
    },
]

df_loans = pd.DataFrame(loan_agreements)
print(f"Loaded {len(df_loans)} loan agreement documents.")
print("\n--- Preview of document IDs ---")
print(df_loans['doc_id'].tolist())
```

---

## Step 3 — Define the Extraction Schema

All three methods will try to extract these fields:

```python
# The target extraction schema
SCHEMA_FIELDS = [
    'borrower_name',
    'loan_amount_inr',
    'interest_rate_pct',
    'repayment_tenure_months',
    'monthly_emi_inr',
    'penalty_clause',
]

def empty_result(doc_id):
    """Return a blank result dict for a document."""
    result = {'doc_id': doc_id}
    for field in SCHEMA_FIELDS:
        result[field] = None
    return result

print("Schema fields defined:", SCHEMA_FIELDS)
```

---

## Step 4 — Method 1: Rule-Based Extraction with Regex

Regex is fast, free, and fully controllable — but you must manually write a pattern for every field.

```python
def extract_with_regex(text, doc_id):
    """Extract loan fields using regular expressions."""
    result = empty_result(doc_id)
    
    # --- Borrower Name ---
    # Pattern: "Borrower: <Name>" or "Name: <Name>" or "Borrower: <Name>,"
    name_patterns = [
        r'(?:Borrower|Name of Borrower|Lead Borrower|Student Name)\s*:\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,4})',
        r'between\s+Borrower:\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,4})',
    ]
    for pattern in name_patterns:
        match = re.search(pattern, text)
        if match:
            result['borrower_name'] = match.group(1).strip()
            break
    
    # --- Loan Amount (INR) ---
    # Handles: "INR 25,00,000", "Rs. 5,00,000", "INR 1,50,00,000"
    amount_patterns = [
        r'(?:Loan Amount|Principal Amount|Credit Limit|Loan Sanctioned)[:\s]+(?:INR|Rs\.?)\s*([\d,]+)',
        r'(?:Sanctioned Amount)[:\s]+(?:INR|Rs\.?)\s*([\d,]+)',
    ]
    for pattern in amount_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            raw = match.group(1).replace(',', '')
            result['loan_amount_inr'] = int(raw)
            break
    
    # --- Interest Rate ---
    # Handles: "8.75% per annum", "13.5% p.a.", "9.25% per annum"
    rate_match = re.search(
        r'(?:interest rate|rate of interest)[:\s]+[\w\s,\.]+?([\d]+\.?\d*)\s*%\s*(?:per annum|p\.a\.|per year)',
        text, re.IGNORECASE
    )
    if rate_match:
        result['interest_rate_pct'] = float(rate_match.group(1))
    
    # --- Tenure in Months ---
    # Handles: "180 months", "36 months", "60 months", "20 years", "10 years"
    tenure_patterns = [
        r'(\d+)\s*months?\b(?:\s+\(\d+\s*years?\))?',
        r'(?:tenure|period)[:\s]+(\d+)\s*months?',
    ]
    for pattern in tenure_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            result['repayment_tenure_months'] = int(match.group(1))
            break
    
    # --- Monthly EMI ---
    emi_match = re.search(
        r'(?:monthly\s+emi|emi amount|emi|monthly installment)[:\s]+(?:INR|Rs\.?)\s*([\d,]+)',
        text, re.IGNORECASE
    )
    if emi_match:
        result['monthly_emi_inr'] = int(emi_match.group(1).replace(',', ''))
    
    # --- Penalty Clause ---
    penalty_match = re.search(
        r'(?:penalty|late payment|overdue charge)[^.]*\.',
        text, re.IGNORECASE
    )
    if penalty_match:
        result['penalty_clause'] = penalty_match.group(0).strip()
    
    return result

# Run regex extraction on all documents
print("Running regex extraction...")
regex_results = [extract_with_regex(row['text'], row['doc_id']) 
                 for _, row in df_loans.iterrows()]
df_regex = pd.DataFrame(regex_results)

print("Done. Preview:")
print(df_regex[['doc_id', 'borrower_name', 'loan_amount_inr', 'interest_rate_pct']].head(5).to_string())
```

---

## Step 5 — Method 2: spaCy NER

spaCy identifies entities like PERSON, MONEY, PERCENT, DATE, ORG automatically.

```python
def extract_with_spacy(text, doc_id):
    """Extract loan fields using spaCy NER."""
    result = empty_result(doc_id)
    doc = nlp(text)
    
    # Collect all detected entities by label
    entities_by_label = {}
    for ent in doc.ents:
        label = ent.label_
        if label not in entities_by_label:
            entities_by_label[label] = []
        entities_by_label[label].append(ent.text.strip())
    
    # --- Borrower Name: First PERSON entity ---
    if 'PERSON' in entities_by_label:
        result['borrower_name'] = entities_by_label['PERSON'][0]
    
    # --- Loan Amount: First MONEY entity ---
    if 'MONEY' in entities_by_label:
        # Try to find one that looks like a large loan amount
        for money_str in entities_by_label['MONEY']:
            cleaned = re.sub(r'[^\d]', '', money_str)
            if cleaned and len(cleaned) >= 4:
                result['loan_amount_inr'] = int(cleaned)
                break
    
    # --- Interest Rate: PERCENT entities ---
    if 'PERCENT' in entities_by_label:
        for pct_str in entities_by_label['PERCENT']:
            try:
                pct = float(re.search(r'[\d.]+', pct_str).group())
                result['interest_rate_pct'] = pct
                break
            except (AttributeError, ValueError):
                continue
    
    # --- Tenure: Look for DATE or CARDINAL + "months" ---
    tenure_match = re.search(r'(\d+)\s*months?', text, re.IGNORECASE)
    if tenure_match:
        result['repayment_tenure_months'] = int(tenure_match.group(1))
    
    # --- EMI: Look for MONEY near "EMI" keyword ---
    emi_context = re.search(r'EMI[^.]*?(?:INR|Rs\.?)\s*([\d,]+)', text, re.IGNORECASE)
    if emi_context:
        result['monthly_emi_inr'] = int(emi_context.group(1).replace(',', ''))
    
    # --- Penalty: Look for sentence containing penalty keywords ---
    penalty_match = re.search(r'[^.]*(?:penalty|late payment|overdue)[^.]*\.', text, re.IGNORECASE)
    if penalty_match:
        result['penalty_clause'] = penalty_match.group(0).strip()
    
    return result

print("Running spaCy NER extraction...")
spacy_results = [extract_with_spacy(row['text'], row['doc_id']) 
                 for _, row in df_loans.iterrows()]
df_spacy = pd.DataFrame(spacy_results)

print("Done. Preview:")
print(df_spacy[['doc_id', 'borrower_name', 'loan_amount_inr', 'interest_rate_pct']].head(5).to_string())
```

---

## Step 6 — Method 3: LLM-Based Extraction (Azure OpenAI)

If you have Azure OpenAI access, run this. Otherwise, skip to Step 7.

```python
def extract_with_llm(text, doc_id, client, deployment):
    """Extract loan fields using Azure OpenAI."""
    result = empty_result(doc_id)
    
    system_prompt = """You are a loan document parser. 
Extract the following fields from the loan agreement text and return ONLY valid JSON.
Fields to extract:
- borrower_name: string (primary borrower's full name only)
- loan_amount_inr: integer (loan amount in INR; if in USD convert using 83 INR/USD)
- interest_rate_pct: float (primary interest rate as a percentage number only)
- repayment_tenure_months: integer (total loan tenure in months)
- monthly_emi_inr: integer (monthly EMI amount in INR, null if not specified)
- penalty_clause: string (brief description of the late payment penalty, null if not specified)

Return ONLY the JSON object, no explanation, no markdown code fences."""

    user_prompt = f"Extract information from this loan agreement:\n\n{text[:2000]}"
    
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0,
            max_tokens=400
        )
        
        raw_json = response.choices[0].message.content.strip()
        # Clean up if model wraps in markdown
        raw_json = re.sub(r'```json\s*', '', raw_json)
        raw_json = re.sub(r'```\s*', '', raw_json)
        
        extracted = json.loads(raw_json)
        for field in SCHEMA_FIELDS:
            result[field] = extracted.get(field)
            
    except Exception as e:
        print(f"  LLM extraction failed for {doc_id}: {e}")
    
    return result

# Run LLM extraction (if Azure is available)
if HAS_AZURE:
    print("Running LLM extraction (this calls Azure OpenAI — may take 30-60 seconds)...")
    client = AzureOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2024-02-15-preview"
    )
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
    
    llm_results = [extract_with_llm(row['text'], row['doc_id'], client, deployment)
                   for _, row in df_loans.iterrows()]
    df_llm = pd.DataFrame(llm_results)
    print("Done.")
else:
    print("Azure OpenAI not available. Skipping LLM extraction.")
    df_llm = None
```

---

## Step 7 — Ground Truth and Accuracy Comparison

```python
# Manually verified ground truth for key fields
ground_truth = {
    'LOAN_001': {'borrower_name': 'Rajesh Kumar Sharma', 'loan_amount_inr': 2500000, 'interest_rate_pct': 8.75, 'repayment_tenure_months': 180, 'monthly_emi_inr': 24891},
    'LOAN_002': {'borrower_name': 'Priya Venkataraman', 'loan_amount_inr': 500000, 'interest_rate_pct': 13.5, 'repayment_tenure_months': 36, 'monthly_emi_inr': 16963},
    'LOAN_003': {'borrower_name': 'Anil Sharma', 'loan_amount_inr': 3360000, 'interest_rate_pct': 9.25, 'repayment_tenure_months': 60, 'monthly_emi_inr': 69957},
    'LOAN_004': {'borrower_name': 'Sunita Bose', 'loan_amount_inr': 6225000, 'interest_rate_pct': 9.0, 'repayment_tenure_months': 120, 'monthly_emi_inr': 68450},
    'LOAN_005': {'borrower_name': 'Mohammed Irfan Khan', 'loan_amount_inr': 4500000, 'interest_rate_pct': 8.4, 'repayment_tenure_months': 240, 'monthly_emi_inr': 38716},
    'LOAN_006': {'borrower_name': 'Thankamma Joseph', 'loan_amount_inr': 395250, 'interest_rate_pct': 11.0, 'repayment_tenure_months': 12, 'monthly_emi_inr': None},
    'LOAN_007': {'borrower_name': 'Mahesh Patel', 'loan_amount_inr': 15000000, 'interest_rate_pct': 10.75, 'repayment_tenure_months': 84, 'monthly_emi_inr': 257912},
    'LOAN_008': {'borrower_name': 'Kavitha Ramachandran', 'loan_amount_inr': 62700, 'interest_rate_pct': 15.5, 'repayment_tenure_months': 24, 'monthly_emi_inr': 3259},
    'LOAN_009': {'borrower_name': 'Sanjay Mehta', 'loan_amount_inr': 7800000, 'interest_rate_pct': 9.85, 'repayment_tenure_months': 120, 'monthly_emi_inr': 102476},
    'LOAN_010': {'borrower_name': 'Sneha Kulkarni', 'loan_amount_inr': 109991, 'interest_rate_pct': 0.0, 'repayment_tenure_months': 12, 'monthly_emi_inr': 9166},
    'LOAN_011': {'borrower_name': 'Ramchandra Yadav', 'loan_amount_inr': 220000, 'interest_rate_pct': 7.0, 'repayment_tenure_months': 12, 'monthly_emi_inr': None},
    'LOAN_012': {'borrower_name': 'Lakshmi Devi', 'loan_amount_inr': 50000, 'interest_rate_pct': 22.0, 'repayment_tenure_months': 12, 'monthly_emi_inr': None},
}

def evaluate_extraction(df_extracted, method_name, check_fields):
    """Compare extracted values against ground truth."""
    correct_counts = {f: 0 for f in check_fields}
    total_docs = len(df_extracted)
    
    rows = []
    for _, row in df_extracted.iterrows():
        doc_id = row['doc_id']
        if doc_id not in ground_truth:
            continue
        gt = ground_truth[doc_id]
        doc_row = {'doc_id': doc_id, 'method': method_name}
        
        for field in check_fields:
            extracted = row.get(field)
            expected = gt.get(field)
            
            if expected is None:
                doc_row[field] = 'N/A'
                continue
            
            # For numeric fields allow 5% tolerance
            if isinstance(expected, (int, float)) and extracted is not None:
                try:
                    tolerance = abs(expected) * 0.05
                    correct = abs(float(extracted) - float(expected)) <= max(tolerance, 1)
                except (TypeError, ValueError):
                    correct = False
            elif isinstance(expected, str) and extracted is not None:
                # For names, check if expected is a substring of extracted or vice versa
                correct = (expected.lower() in str(extracted).lower() or 
                           str(extracted).lower() in expected.lower())
            else:
                correct = extracted == expected
            
            doc_row[field] = '✓' if correct else f'✗ (got: {extracted}, expected: {expected})'
            if correct:
                correct_counts[field] += 1
        
        rows.append(doc_row)
    
    return pd.DataFrame(rows), correct_counts, total_docs

# Evaluate regex
eval_fields = ['borrower_name', 'loan_amount_inr', 'interest_rate_pct', 'repayment_tenure_months', 'monthly_emi_inr']

print("=== REGEX EXTRACTION EVALUATION ===")
regex_eval, regex_counts, n_docs = evaluate_extraction(df_regex, 'Regex', eval_fields)
print(regex_eval[['doc_id'] + eval_fields].to_string(index=False))
print(f"\nAccuracy per field:")
for f in eval_fields:
    print(f"  {f:<35} {regex_counts[f]}/{n_docs} = {regex_counts[f]/n_docs*100:.0f}%")

print("\n=== SPACY NER EVALUATION ===")
spacy_eval, spacy_counts, _ = evaluate_extraction(df_spacy, 'spaCy', eval_fields)
print(spacy_eval[['doc_id'] + eval_fields].to_string(index=False))
print(f"\nAccuracy per field:")
for f in eval_fields:
    print(f"  {f:<35} {spacy_counts[f]}/{n_docs} = {spacy_counts[f]/n_docs*100:.0f}%")

if df_llm is not None:
    print("\n=== LLM EXTRACTION EVALUATION ===")
    llm_eval, llm_counts, _ = evaluate_extraction(df_llm, 'LLM', eval_fields)
    print(llm_eval[['doc_id'] + eval_fields].to_string(index=False))
    print(f"\nAccuracy per field:")
    for f in eval_fields:
        print(f"  {f:<35} {llm_counts[f]}/{n_docs} = {llm_counts[f]/n_docs*100:.0f}%")
```

---

## Step 8 — Final Method Comparison Summary

```python
print("\n=== FINAL COMPARISON SUMMARY ===")

methods = ['Regex', 'spaCy']
counts = [regex_counts, spacy_counts]
if df_llm is not None:
    methods.append('LLM (Azure OpenAI)')
    counts.append(llm_counts)

summary_rows = []
for method, count_dict in zip(methods, counts):
    avg_acc = sum(count_dict.values()) / (len(eval_fields) * n_docs) * 100
    row = {'Method': method}
    for f in eval_fields:
        row[f] = f"{count_dict[f]}/{n_docs}"
    row['Avg Accuracy'] = f"{avg_acc:.1f}%"
    summary_rows.append(row)

summary_df = pd.DataFrame(summary_rows)
print(summary_df.to_string(index=False))

print("""
=== WHEN TO USE EACH METHOD ===

Regex:
  ✓ Best for: Documents with consistent, predictable formatting
  ✓ Advantages: Fast, free, fully transparent, no GPU/API needed
  ✗ Fails on: Format variations, typos, non-standard layouts
  Use when: You have strict SLA requirements and consistent templates

spaCy NER:
  ✓ Best for: Documents where standard entity types are present (PERSON, MONEY, PERCENT)
  ✓ Advantages: Handles some variation, no API cost, works offline
  ✗ Fails on: Domain-specific terms, complex conditional fields
  Use when: Documents vary in format but use standard language

LLM (Azure OpenAI):
  ✓ Best for: Varied formats, messy text, complex extraction logic
  ✓ Advantages: Highest accuracy, handles exceptions, understands context
  ✗ Fails on: Very long documents (token limits), has API cost, latency
  Use when: Accuracy is critical and cost/latency is acceptable
""")
```

---

## Expected Output Summary

| Method | Borrower Name | Loan Amount | Interest Rate |
|--------|--------------|-------------|---------------|
| Regex | ~70% accurate | ~60% accurate | ~80% accurate |
| spaCy | ~60% accurate | ~50% accurate | ~70% accurate |
| LLM | ~95% accurate | ~90% accurate | ~95% accurate |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `OSError: Can't find model 'en_core_web_sm'` | Run `python -m spacy download en_core_web_sm` |
| `json.JSONDecodeError` in LLM step | LLM returned non-JSON; add `temperature=0` and check system prompt |
| Regex extracts wrong number | Adjust the regex pattern; use `re.search(...).group()` to debug |
| spaCy misses PERSON entity | spaCy may not recognize Indian names well; consider a custom NER model |

---

## What to Submit

1. Your completed `lab1d_ner.py` or `.ipynb` with all cells run.
2. The printed accuracy table from Step 7.
3. The final comparison summary from Step 8 with your recommendation filled in.

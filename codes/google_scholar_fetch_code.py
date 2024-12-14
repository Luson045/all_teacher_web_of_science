import scholarly
from scholarly import scholarly
import json
from datetime import datetime
import os

def get_categories_from_interests(interests, publications):
    """Extract categories from research interests and publications"""
    categories = set()
    
    # Basic category mappings
    category_keywords = {
        "Computer Science": ["computer", "computing", "algorithm", "software", "programming", "data", "ai", "artificial intelligence", "machine learning", "deep learning", "neural", "cybersecurity", "security", "network", "cloud", "distributed", "database"],
        "Engineering": ["engineering", "system", "design", "architecture", "hardware", "embedded", "robotics", "automation", "control"],
        "Mathematics": ["mathematics", "mathematical", "statistics", "probability", "optimization", "numerical", "algebra", "calculus"],
        "Artificial Intelligence": ["artificial intelligence", "machine learning", "deep learning", "neural network", "ai", "ml", "nlp", "computer vision"],
        "Information Technology": ["information technology", "it", "cloud computing", "web", "internet", "database", "information system"],
        "Electronics": ["electronics", "electronic", "circuit", "vlsi", "microprocessor", "embedded system"],
        "Communication Systems": ["communication", "telecommunications", "wireless", "network", "mobile", "5g", "antenna", "signal processing"],
        "Data Science": ["data science", "big data", "analytics", "data mining", "statistical analysis", "data analytics"],
        "Software Engineering": ["software", "development", "programming", "coding", "application", "web development"],
        "Security": ["security", "cybersecurity", "crypto", "encryption", "privacy", "authentication"],
        "Networking": ["network", "protocol", "tcp/ip", "routing", "switching", "internet"],
        "IoT": ["iot", "internet of things", "sensor", "smart device", "embedded"],
        "Image Processing": ["image processing", "computer vision", "pattern recognition", "visual", "image analysis"],
        "Optimization": ["optimization", "genetic algorithm", "evolutionary", "meta-heuristic"],
        "Operating Systems": ["operating system", "os", "linux", "windows", "unix"],
        "Hardware": ["hardware", "computer architecture", "microprocessor", "digital"]
    }
    
    # Add base categories
    categories.add("Computer Science")
    categories.add("Engineering")
    
    # Process interests
    for interest in interests:
        interest_lower = interest.lower()
        for category, keywords in category_keywords.items():
            if any(keyword in interest_lower for keyword in keywords):
                categories.add(category)
    
    # Process publications
    for pub in publications:
        title = pub.get('title', '').lower()
        abstract = pub.get('abstract', '').lower()
        journal = pub.get('journal', '').lower()
        
        # Check title, abstract, and journal against keywords
        text_to_check = f"{title} {abstract} {journal}"
        for category, keywords in category_keywords.items():
            if any(keyword in text_to_check for keyword in keywords):
                categories.add(category)
    
    # Convert set to sorted list
    return sorted(list(categories))

def fetch_detailed_scholar_profile(author_name):
    try:
        print(f"Searching for {author_name}...")
        search_query = scholarly.search_author(author_name)
        author = next(search_query)
        
        print("Retrieving complete author details...")
        author_data = scholarly.fill(author)
        scholarly.fill(author_data, sections=['publications'])
        
        # Initialize variables for year tracking
        start_year = None
        end_year = None
        
        # Get publication years before creating profile
        if author_data.get('publications'):
            publication_years = [
                int(pub.get('bib', {}).get('year', 9999))
                for pub in author_data.get('publications', [])
                if pub.get('bib', {}).get('year', '').isdigit()
            ]
            if publication_years:
                start_year = min(publication_years)
                end_year = max(publication_years)
        
        # Process publications first to use in category generation
        publications = []
        yearly_citations = {}
        
        for pub in author_data.get('publications', []):
            try:
                pub_filled = scholarly.fill(pub)
                year = pub_filled.get('bib', {}).get('year', '')
                citations = pub_filled.get('num_citations', 0)
                
                # Count citations per year
                if year:
                    if year not in yearly_citations:
                        yearly_citations[year] = 0
                    yearly_citations[year] += citations
                
                publication = {
                    "title": pub_filled.get('bib', {}).get('title', ''),
                    "year": year,
                    "authors": pub_filled.get('bib', {}).get('author', []),
                    "citations": citations,
                    "journal": pub_filled.get('bib', {}).get('journal', ''),
                    "abstract": pub_filled.get('bib', {}).get('abstract', ''),
                    "url": pub_filled.get('pub_url', ''),
                    "citationUrl": pub_filled.get('citedby_url', '')
                }
                publications.append(publication)
                print(f"Processed publication: {publication['title'][:100]}...")
                
            except Exception as e:
                print(f"Error processing publication: {e}")
                continue
        
        # Generate categories based on interests and publications
        categories = get_categories_from_interests(
            author_data.get('interests', []),
            publications
        )
        
        # Structure the data in requested format
        profile = {
            "personalInfo": {
                "name": author_data.get('name', ''),
                "institution": "Dr B R Ambedkar National Institute of Technology Jalandhar",
                "department": "Computer Science and Engineering",
                "role": "Professor",
                "startDate": str(start_year) if start_year else "",
                "endDate": str(end_year) if end_year else "present",
                "url": author_data.get('url_picture', ''),
                "careerSpan": f"{start_year}-{end_year if end_year else 'present'}" if start_year else ""
            },
            "metrics": {
                "citations": {
                    "total": author_data.get('citedby', 0),
                    "h_index": author_data.get('hindex', 0),
                    "i10_index": author_data.get('i10index', 0),
                },
                "yearWiseCitations": dict(sorted(yearly_citations.items())),
                "averagePerItem": round(author_data.get('citedby', 0) / len(publications) if publications else 0, 2),
                "averagePerYear": round(author_data.get('citedby', 0) / ((end_year - start_year + 1) if start_year and end_year else 1), 2),
                "timesCited": author_data.get('citedby', 0),
                "dedupedTimesCited": author_data.get('citedby', 0),
                "activeYears": (end_year - start_year + 1) if start_year and end_year else 0
            },
            "researchFields": [
                {
                    "name": interest,
                    "url": f"/research_field/{interest.lower().replace(' ', '_')}"
                }
                for interest in author_data.get('interests', [])
            ],
            "publications": publications,
            "categories": categories
        }
        
        return profile
        
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_profile_data(data, base_filename):
    """Save the data with timestamp and return the full path"""
    data_dir = "scholar_data"
    os.makedirs(data_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{base_filename}_{timestamp}.json"
    full_path = os.path.join(data_dir, filename)
    
    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return os.path.abspath(full_path)

# Fetch and save data
author_name = "Harsh Kumar Verma"
print("Starting data collection...")
profile_data = fetch_detailed_scholar_profile(author_name)

if profile_data:
    # Save data
    saved_file_path = save_profile_data(profile_data, 'scholar_profile')
    print(f"\nData saved to: {saved_file_path}")
    
    # Print summary
    print("\n=== Profile Summary ===")
    print(f"Name: {profile_data['personalInfo']['name']}")
    print(f"Institution: {profile_data['personalInfo']['institution']}")
    print(f"Department: {profile_data['personalInfo']['department']}")
    print(f"Career Span: {profile_data['personalInfo']['careerSpan']}")
    
    print("\n=== Metrics ===")
    print(f"Total Citations: {profile_data['metrics']['citations']['total']}")
    print(f"H-index: {profile_data['metrics']['citations']['h_index']}")
    print(f"i10-index: {profile_data['metrics']['citations']['i10_index']}")
    print(f"Average Citations per Item: {profile_data['metrics']['averagePerItem']}")
    print(f"Average Citations per Year: {profile_data['metrics']['averagePerYear']}")
    print(f"Active Years: {profile_data['metrics']['activeYears']}")
    
    print("\n=== Categories ===")
    for category in profile_data['categories']:
        print(f"- {category}")
    
    print("\n=== Year-wise Citations ===")
    for year, citations in profile_data['metrics']['yearWiseCitations'].items():
        print(f"{year}: {citations} citations")
    
    print("\n=== Research Fields ===")
    for field in profile_data['researchFields']:
        print(f"- {field['name']}")
    
    print(f"\nTotal Publications: {len(profile_data['publications'])}")
else:
    print("Failed to fetch profile data")
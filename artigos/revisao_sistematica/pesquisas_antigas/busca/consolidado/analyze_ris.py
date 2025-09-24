#!/usr/bin/env python3
"""
Comprehensive Statistical Analysis of PBL Assessment Articles
Analyzes RIS file to extract detailed statistics aligned with ISO standards modeling
"""

import re
import collections
import json
from datetime import datetime
import pandas as pd
import numpy as np

def extract_country_from_venue(venue_name):
    """Extract country from publication venue name and patterns"""
    if not venue_name:
        return None
    
    venue_upper = venue_name.upper()
    
    # Conference/venue location patterns
    venue_patterns = {
        'USA': ['IEEE', 'ACM', 'SIGCSE', 'ASME', 'AMERICAN'],
        'International': ['INTERNATIONAL', 'GLOBAL', 'WORLD', 'IEEE TRANSACTIONS', 'INTERDISCIPLINARY'],
        'Spain': ['SPANISH', 'COMUNICAR', 'RETOS', 'ESTUDIOS', 'REVISTA MEDITERRANEA'],
        'Portugal': ['PORTUGUESE', 'CISPEE', 'COMUNICACOES'],
        'Brazil': ['BRAZILIAN', 'DIALOGIA', 'CONHECIMENTO'],
        'Ireland': ['IRISH'],
        'Romania': ['ROEDUNET'],
        'Latin America': ['LATIN AMERICAN', 'CLEI', 'EDUNINE'],
        'Europe': ['EUROPEAN'],
        'UK': ['BRITISH', 'LONDON'],
        'Malaysia': ['MALAYSIAN'],
        'Germany': ['GERMAN'],
        'Netherlands': ['DUTCH'],
        'Indonesia': ['ICOBAS'],
        'Philippines': ['ICOPIA'],
        'Singapore': ['SINGAPORE']
    }
    
    # Medical and scientific journals (often international)
    medical_journals = ['MEDICAL', 'HEALTH', 'NURSE', 'BMC', 'PERSPECTIVES ON MEDICAL', 
                       'MEDICAL SCIENCE', 'MEDICAL TEACHER', 'MEDICAL EDUCATION']
    
    # Science journals (often international)  
    science_journals = ['ATMOSPHERIC', 'CLIMATE', 'BIOINFORMATICS', 'REMOTE SENSING',
                       'PURE AND APPLIED', 'BOUNDARY-LAYER', 'AEROSOL', 'ATMOSPHERE',
                       'FEMS MICROBIOLOGY', 'BIOCHEMISTRY']
    
    # Check specific patterns
    for country, patterns in venue_patterns.items():
        for pattern in patterns:
            if pattern in venue_upper:
                return country
    
    # Check for medical/science journals
    if any(pattern in venue_upper for pattern in medical_journals):
        return 'International - Medical'
    
    if any(pattern in venue_upper for pattern in science_journals):
        return 'International - Science'
    
    return 'Unknown'

def extract_country_from_affiliation(affiliation):
    """Extract country from author affiliation"""
    if not affiliation:
        return None
    
    # Common country patterns in affiliations
    countries = {
        'USA': ['USA', 'United States', 'US', 'America'],
        'China': ['China', 'Chinese', 'Beijing', 'Shanghai', 'Guangzhou'],
        'Spain': ['Spain', 'Spanish', 'Madrid', 'Barcelona', 'Valencia'],
        'Germany': ['Germany', 'German', 'Berlin', 'Munich', 'Hamburg'],
        'UK': ['UK', 'United Kingdom', 'Britain', 'England', 'London', 'Oxford', 'Cambridge'],
        'Brazil': ['Brazil', 'Brazilian', 'Sao Paulo', 'Rio de Janeiro'],
        'Australia': ['Australia', 'Australian', 'Sydney', 'Melbourne'],
        'Canada': ['Canada', 'Canadian', 'Toronto', 'Vancouver'],
        'France': ['France', 'French', 'Paris', 'Lyon'],
        'Italy': ['Italy', 'Italian', 'Rome', 'Milan'],
        'Japan': ['Japan', 'Japanese', 'Tokyo', 'Osaka'],
        'South Korea': ['Korea', 'Korean', 'Seoul'],
        'India': ['India', 'Indian', 'Delhi', 'Mumbai'],
        'Netherlands': ['Netherlands', 'Dutch', 'Amsterdam'],
        'Taiwan': ['Taiwan', 'Taiwanese', 'Taipei'],
        'Portugal': ['Portugal', 'Portuguese', 'Lisbon'],
        'Finland': ['Finland', 'Finnish', 'Helsinki'],
        'Sweden': ['Sweden', 'Swedish', 'Stockholm'],
        'Norway': ['Norway', 'Norwegian', 'Oslo']
    }
    
    affiliation_upper = affiliation.upper()
    for country, patterns in countries.items():
        for pattern in patterns:
            if pattern.upper() in affiliation_upper:
                return country
    
    return 'Other'

def categorize_technology(title, abstract):
    """Categorize articles by technology focus - more precise categorization"""
    text = f"{title} {abstract}".lower()
    
    categories = {
        'Digital Twins': ['digital twin', 'digital twins', 'virtual model', 'cyber-physical system', 'digital replica'],
        'DevOps/CI-CD': ['devops', 'continuous integration', 'ci/cd', 'continuous deployment', 'docker', 'kubernetes', 'jenkins', 'gitlab'],
        'Software Architecture': ['software architecture', 'system architecture', 'microservices', 'design patterns', 'architectural design', 'software design'],
        'Learning Analytics': ['learning analytics', 'educational data mining', 'student modeling', 'predictive analytics', 'academic analytics'],
        'Automated Assessment': ['automated assessment', 'automatic evaluation', 'auto-grading', 'computer-aided assessment', 'automatic scoring'],
        'Virtual Reality/AR': ['virtual reality', ' vr ', 'augmented reality', ' ar ', 'immersive technology', 'virtual environment', '3d environment'],
        'Machine Learning/AI': ['machine learning', 'artificial intelligence', ' ai ', 'neural network', 'deep learning', 'classification algorithm'],
        'Mobile Learning': ['mobile learning', 'm-learning', 'mobile application', 'smartphone learning', 'tablet learning', 'mobile device'],
        'Collaborative Tools': ['collaborative platform', 'team collaboration', 'collaborative environment', 'group collaboration tool'],
        'Programming Tools': ['programming environment', 'ide', 'integrated development', 'compiler', 'debugger', 'code analysis'],
        'Process Modeling': ['process modeling', 'workflow modeling', 'business process', 'process mining', 'process simulation'],
        'Assessment Tools': ['assessment tool', 'evaluation platform', 'testing framework', 'grading system', 'rubric system'],
        'Web Technologies': ['web-based', 'online platform', 'web application', 'internet-based', 'browser-based']
    }
    
    found_categories = []
    for category, keywords in categories.items():
        if any(keyword in text for keyword in keywords):
            found_categories.append(category)
    
    # If no specific technology found but mentions general tech terms, classify as General Technology
    general_tech_terms = ['technology', 'digital', 'computer', 'software', 'system', 'platform', 'tool']
    if not found_categories and any(term in text for term in general_tech_terms):
        found_categories = ['General Technology']
    
    return found_categories if found_categories else ['General PBL']

def categorize_assessment_type(title, abstract):
    """Categorize assessment approaches"""
    text = f"{title} {abstract}".lower()
    
    types = {
        'Peer Assessment': ['peer assessment', 'peer evaluation', 'peer review', 'peer feedback'],
        'Self Assessment': ['self assessment', 'self evaluation', 'self reflection', 'self-assessment'],
        'Formative Assessment': ['formative', 'continuous assessment', 'ongoing evaluation', 'real-time feedback'],
        'Summative Assessment': ['summative', 'final assessment', 'grading', 'scoring'],
        'Automated Assessment': ['automated', 'automatic', 'computer-based assessment', 'algorithmic'],
        'Portfolio Assessment': ['portfolio', 'artifact', 'collection of work'],
        'Project Assessment': ['project assessment', 'project evaluation', 'project-based assessment']
    }
    
    found_types = []
    for assessment_type, keywords in types.items():
        if any(keyword in text for keyword in keywords):
            found_types.append(assessment_type)
    
    return found_types if found_types else ['General Assessment']

def analyze_ris_file(filepath):
    """Main analysis function"""
    
    # Read the RIS file
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Split into individual records
    records = content.split('ER  -')[:-1]
    
    # Initialize analysis data
    analysis_data = {
        'temporal': {'years': [], 'year_counts': {}},
        'geographical': {'countries': [], 'affiliations': []},
        'technological': {'categories': [], 'tech_distribution': {}},
        'methodological': {'assessment_types': [], 'assessment_distribution': {}},
        'publication': {'venues': [], 'types': [], 'venue_counts': {}},
        'iso_alignment': {'architecture_patterns': [], 'stakeholder_views': []},
        'articles': []
    }
    
    print(f"Processing {len(records)} records...")
    
    # Process each record
    for i, record in enumerate(records):
        if not record.strip():
            continue
            
        lines = record.strip().split('\n')
        current_record = {
            'authors': [],
            'title': '',
            'abstract': '',
            'year': None,
            'venue': '',
            'type': '',
            'affiliations': [],
            'doi': '',
            'keywords': []
        }
        
        for line in lines:
            if '  - ' in line:
                field, value = line.split('  - ', 1)
                field = field.strip()
                value = value.strip()
                
                # Map RIS fields
                if field == 'AU':
                    current_record['authors'].append(value)
                elif field == 'TI':
                    current_record['title'] = value
                elif field == 'AB':
                    current_record['abstract'] = value
                elif field == 'PY':
                    if value.isdigit():
                        current_record['year'] = int(value)
                elif field == 'T2' or field == 'JO':
                    current_record['venue'] = value
                elif field == 'TY':
                    current_record['type'] = value
                elif field == 'AD':
                    current_record['affiliations'].append(value)
                elif field == 'DO':
                    current_record['doi'] = value
                elif field == 'KW':
                    current_record['keywords'].append(value)
        
        # Skip if essential data missing
        if not current_record['title'] or not current_record['year']:
            continue
        
        # Temporal analysis
        if current_record['year']:
            analysis_data['temporal']['years'].append(current_record['year'])
            analysis_data['temporal']['year_counts'][current_record['year']] = \
                analysis_data['temporal']['year_counts'].get(current_record['year'], 0) + 1
        
        # Geographical analysis (based on publication venue)
        if current_record['venue']:
            country = extract_country_from_venue(current_record['venue'])
            if country and country != 'Unknown':
                analysis_data['geographical']['countries'].append(country)
        
        # Also try affiliations if available
        for affiliation in current_record['affiliations']:
            country = extract_country_from_affiliation(affiliation)
            if country and country != 'Other':
                analysis_data['geographical']['countries'].append(country)
        
        # Technology categorization
        tech_categories = categorize_technology(current_record['title'], current_record['abstract'])
        analysis_data['technological']['categories'].extend(tech_categories)
        for cat in tech_categories:
            analysis_data['technological']['tech_distribution'][cat] = \
                analysis_data['technological']['tech_distribution'].get(cat, 0) + 1
        
        # Assessment methodology
        assessment_types = categorize_assessment_type(current_record['title'], current_record['abstract'])
        analysis_data['methodological']['assessment_types'].extend(assessment_types)
        for atype in assessment_types:
            analysis_data['methodological']['assessment_distribution'][atype] = \
                analysis_data['methodological']['assessment_distribution'].get(atype, 0) + 1
        
        # Publication venues
        if current_record['venue']:
            analysis_data['publication']['venues'].append(current_record['venue'])
            analysis_data['publication']['venue_counts'][current_record['venue']] = \
                analysis_data['publication']['venue_counts'].get(current_record['venue'], 0) + 1
        
        if current_record['type']:
            analysis_data['publication']['types'].append(current_record['type'])
        
        # ISO alignment analysis (based on keywords and abstracts)
        text = f"{current_record['title']} {current_record['abstract']}".lower()
        
        # Architecture patterns
        arch_patterns = []
        if 'microservice' in text or 'service-oriented' in text:
            arch_patterns.append('Service-Oriented Architecture')
        if 'layered' in text or 'layer' in text:
            arch_patterns.append('Layered Architecture')
        if 'mvc' in text or 'model-view-controller' in text:
            arch_patterns.append('MVC Pattern')
        if 'component' in text:
            arch_patterns.append('Component-Based Architecture')
        if 'distributed' in text:
            arch_patterns.append('Distributed Systems')
        
        analysis_data['iso_alignment']['architecture_patterns'].extend(arch_patterns)
        
        # Stakeholder views
        stakeholder_views = []
        if 'student' in text:
            stakeholder_views.append('Student View')
        if 'teacher' in text or 'instructor' in text or 'educator' in text:
            stakeholder_views.append('Educator View')
        if 'administrator' in text or 'admin' in text:
            stakeholder_views.append('Administrative View')
        if 'industry' in text or 'professional' in text:
            stakeholder_views.append('Industry View')
        
        analysis_data['iso_alignment']['stakeholder_views'].extend(stakeholder_views)
        
        # Store complete record
        current_record['tech_categories'] = tech_categories
        current_record['assessment_types'] = assessment_types
        analysis_data['articles'].append(current_record)
    
    return analysis_data

def generate_statistics_report(analysis_data):
    """Generate comprehensive statistics report"""
    
    total_articles = len(analysis_data['articles'])
    
    report = f"""# Comprehensive Statistical Analysis of PBL Assessment Technology Research
## Analysis of {total_articles} Selected Articles from Systematic Review

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 1. TEMPORAL ANALYSIS

### 1.1 Distribution by Year (2015-2025)
"""
    
    # Year distribution
    year_counts = analysis_data['temporal']['year_counts']
    years_sorted = sorted(year_counts.keys())
    
    report += "| Year | Articles | Percentage | Cumulative % |\n"
    report += "|------|----------|------------|---------------|\n"
    
    cumulative = 0
    for year in years_sorted:
        count = year_counts[year]
        percentage = (count / total_articles) * 100
        cumulative += percentage
        report += f"| {year} | {count} | {percentage:.1f}% | {cumulative:.1f}% |\n"
    
    # Growth trends
    recent_years = [y for y in years_sorted if y >= 2020]
    recent_total = sum(year_counts[y] for y in recent_years)
    report += f"\n**Key Insights:**\n"
    report += f"- Total articles from 2020-2025: {recent_total} ({(recent_total/total_articles)*100:.1f}%)\n"
    report += f"- Peak publication year: {max(year_counts, key=year_counts.get)} ({year_counts[max(year_counts, key=year_counts.get)]} articles)\n"
    report += f"- Average articles per year: {total_articles/len(years_sorted):.1f}\n"
    
    # Technology distribution
    report += "\n## 2. TECHNOLOGICAL CATEGORIZATION\n\n"
    tech_dist = analysis_data['technological']['tech_distribution']
    tech_sorted = sorted(tech_dist.items(), key=lambda x: x[1], reverse=True)
    
    report += "| Technology Category | Articles | Percentage |\n"
    report += "|---------------------|----------|------------|\n"
    
    for tech, count in tech_sorted:
        percentage = (count / total_articles) * 100
        report += f"| {tech} | {count} | {percentage:.1f}% |\n"
    
    # Assessment methodology
    report += "\n## 3. METHODOLOGICAL CLASSIFICATION\n\n"
    assess_dist = analysis_data['methodological']['assessment_distribution']
    assess_sorted = sorted(assess_dist.items(), key=lambda x: x[1], reverse=True)
    
    report += "| Assessment Type | Articles | Percentage |\n"
    report += "|-----------------|----------|------------|\n"
    
    for assess_type, count in assess_sorted:
        percentage = (count / total_articles) * 100
        report += f"| {assess_type} | {percentage:.1f}% | {count} |\n"
    
    # Geographical distribution
    report += "\n## 4. GEOGRAPHICAL DISTRIBUTION\n\n"
    country_counts = collections.Counter(analysis_data['geographical']['countries'])
    country_sorted = country_counts.most_common(15)
    
    report += "| Country/Region | Articles | Percentage |\n"
    report += "|----------------|----------|------------|\n"
    
    total_with_country = sum(country_counts.values())
    for country, count in country_sorted:
        percentage = (count / total_with_country) * 100 if total_with_country > 0 else 0
        report += f"| {country} | {count} | {percentage:.1f}% |\n"
    
    # Publication venues
    report += "\n## 5. PUBLICATION VENUES\n\n"
    venue_counts = analysis_data['publication']['venue_counts']
    venue_sorted = sorted(venue_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    
    report += "| Publication Venue | Articles | Percentage |\n"
    report += "|-------------------|----------|------------|\n"
    
    for venue, count in venue_sorted:
        percentage = (count / total_articles) * 100
        report += f"| {venue} | {count} | {percentage:.1f}% |\n"
    
    # ISO alignment analysis
    report += "\n## 6. ISO-ALIGNED ANALYSIS\n\n"
    report += "### 6.1 Architecture Patterns (ISO 42010 Perspectives)\n\n"
    
    arch_patterns = collections.Counter(analysis_data['iso_alignment']['architecture_patterns'])
    if arch_patterns:
        report += "| Architecture Pattern | Frequency |\n"
        report += "|---------------------|----------|\n"
        for pattern, count in arch_patterns.most_common():
            report += f"| {pattern} | {count} |\n"
    else:
        report += "No explicit architecture patterns identified in the abstracts.\n"
    
    report += "\n### 6.2 Stakeholder Views\n\n"
    stakeholder_views = collections.Counter(analysis_data['iso_alignment']['stakeholder_views'])
    if stakeholder_views:
        report += "| Stakeholder View | Frequency |\n"
        report += "|-----------------|-----------|\n"
        for view, count in stakeholder_views.most_common():
            report += f"| {view} | {count} |\n"
    
    # Key insights and gaps
    report += "\n## 7. KEY INSIGHTS AND RESEARCH GAPS\n\n"
    
    # Digital Twins analysis
    dt_articles = [a for a in analysis_data['articles'] if 'Digital Twins' in a['tech_categories']]
    report += f"### 7.1 Digital Twins in Educational Context\n"
    report += f"- Articles explicitly mentioning Digital Twins: **{len(dt_articles)}** ({(len(dt_articles)/total_articles)*100:.1f}%)\n"
    
    if dt_articles:
        report += f"- Years of DT publications: {sorted(set(a['year'] for a in dt_articles))}\n"
        report += "- **Gap**: Limited research on Digital Twins for PBL assessment\n\n"
    else:
        report += "- **Major Gap**: No explicit Digital Twins applications found in PBL assessment\n\n"
    
    # DevOps analysis
    devops_articles = [a for a in analysis_data['articles'] if 'DevOps/CI-CD' in a['tech_categories']]
    report += f"### 7.2 DevOps/CI-CD in Education\n"
    report += f"- Articles on DevOps/CI-CD: **{len(devops_articles)}** ({(len(devops_articles)/total_articles)*100:.1f}%)\n"
    
    # Assessment technology gaps
    automated_articles = [a for a in analysis_data['articles'] if 'Automated Assessment' in a['tech_categories']]
    report += f"### 7.3 Automated Assessment Technologies\n"
    report += f"- Automated assessment articles: **{len(automated_articles)}** ({(len(automated_articles)/total_articles)*100:.1f}%)\n"
    
    report += "\n### 7.4 Research Trends and Opportunities\n\n"
    report += "**Emerging Technologies:**\n"
    
    # Recent technology trends
    recent_articles = [a for a in analysis_data['articles'] if a['year'] >= 2022]
    recent_techs = collections.Counter()
    for article in recent_articles:
        for tech in article['tech_categories']:
            recent_techs[tech] += 1
    
    for tech, count in recent_techs.most_common(5):
        percentage = (count / len(recent_articles)) * 100 if recent_articles else 0
        report += f"- {tech}: {count} articles ({percentage:.1f}% of 2022-2025 articles)\n"
    
    report += "\n**Key Research Gaps Identified:**\n"
    report += "1. **Digital Twins Integration**: Limited research on DT for educational process modeling\n"
    report += "2. **Scalable Assessment Architectures**: Need for ISO 42010-compliant assessment systems\n"
    report += "3. **Real-time Instructor Support**: Gap in technologies supporting real-time instructor evaluation\n"
    report += "4. **Cross-cultural Assessment**: Limited geographical diversity in research\n"
    report += "5. **Industry-Academia Collaboration**: Insufficient industry perspective in assessment tools\n"
    
    # Summary statistics for visualization
    report += "\n## 8. DATA FOR VISUALIZATION\n\n"
    report += "### Temporal Distribution (CSV format)\n"
    report += "Year,Count\\n"
    for year in sorted(year_counts.keys()):
        report += f"{year},{year_counts[year]}\\n"
    
    report += "\n### Technology Categories (CSV format)\n"
    report += "Category,Count\\n"
    for tech, count in tech_sorted:
        report += f"\"{tech}\",{count}\\n"
    
    report += "\n### Assessment Types (CSV format)\n"
    report += "Type,Count\\n"
    for assess_type, count in assess_sorted:
        report += f"\"{assess_type}\",{count}\\n"
    
    report += "\n### Top Countries (CSV format)\n"
    report += "Country,Count\\n"
    for country, count in country_sorted:
        report += f"{country},{count}\\n"
    
    return report

if __name__ == "__main__":
    # Analyze the RIS file
    ris_file = "/home/afonsolelis/pesquisa_modelo_gd_apb/artigos/revisao_sistematica/busca/consolidado/artigos_relevantes_pbl_avaliacao.ris"
    
    print("Starting comprehensive analysis...")
    analysis_data = analyze_ris_file(ris_file)
    
    print("Generating statistics report...")
    report = generate_statistics_report(analysis_data)
    
    # Save the detailed analysis
    output_file = "/home/afonsolelis/pesquisa_modelo_gd_apb/artigos/revisao_sistematica/busca/consolidado/analise_estatistica_descritiva.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Analysis complete! Report saved to: {output_file}")
    
    # Save raw data as JSON for further processing
    json_file = "/home/afonsolelis/pesquisa_modelo_gd_apb/artigos/revisao_sistematica/busca/consolidado/analysis_data.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        # Convert to JSON-serializable format
        json_data = {
            'total_articles': len(analysis_data['articles']),
            'temporal': {
                'year_counts': analysis_data['temporal']['year_counts'],
                'years_range': [min(analysis_data['temporal']['years']), max(analysis_data['temporal']['years'])]
            },
            'technological': analysis_data['technological']['tech_distribution'],
            'methodological': analysis_data['methodological']['assessment_distribution'],
            'geographical': dict(collections.Counter(analysis_data['geographical']['countries']).most_common()),
            'publication_venues': analysis_data['publication']['venue_counts']
        }
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    print(f"Raw data saved to: {json_file}")
    print(f"Processed {len(analysis_data['articles'])} articles successfully.")
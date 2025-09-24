#!/usr/bin/env python3
"""
RIS File Analyzer for PBL Assessment Articles
Filters articles based on specific criteria related to Project-Based Learning assessment challenges
"""

import os
import re
from collections import defaultdict
from typing import List, Dict, Set

class RISAnalyzer:
    def __init__(self):
        # Keywords aligned with PBL assessment challenges
        self.pbl_keywords = [
            'project-based learning', 'project based learning', 'pbl', 
            'project learning', 'project-oriented learning'
        ]
        
        # Assessment-related keywords aligned with research questions
        self.assessment_keywords = [
            'assessment', 'evaluation', 'formative assessment', 'summative assessment',
            'grading', 'scoring', 'feedback', 'rubric', 'criteria', 'measurement',
            'performance evaluation', 'student evaluation', 'peer assessment',
            'self-assessment', 'authentic assessment', 'portfolio assessment',
            'process assessment', 'ongoing assessment', 'continuous assessment'
        ]
        
        # Challenges and difficulties keywords
        self.challenge_keywords = [
            'challenge', 'difficulty', 'problem', 'issue', 'barrier', 'obstacle',
            'dilemma', 'complexity', 'limitation', 'constraint', 'gap'
        ]
        
        # Instruments and tools keywords
        self.instrument_keywords = [
            'instrument', 'tool', 'method', 'rubric', 'framework', 'model',
            'scale', 'questionnaire', 'survey', 'protocol', 'approach'
        ]
        
        # Technology keywords for objective/scalable assessment
        self.technology_keywords = [
            'technology', 'automated', 'system', 'platform', 'software', 
            'application', 'artificial intelligence', 'machine learning', 
            'analytics', 'dashboard', 'interface', 'objective', 'scalable'
        ]
        
        # Collaborative and processual assessment keywords
        self.collaborative_keywords = [
            'collaborative', 'team', 'group', 'peer', 'individual', 
            'cooperative', 'collective', 'process', 'formative', 'ongoing',
            'continuous', 'competenc', 'skill', 'critical thinking', 
            'creativity', 'communication', 'transversal'
        ]
        
        # Exclusion keywords
        self.excluded_keywords = [
            'meta-analysis', 'systematic review', 'literature review',
            'industrial application', 'manufacturing', 'production',
            'conference abstract', 'poster'
        ]
        
        self.valid_languages = ['english', 'portuguese', 'spanish', 'en', 'pt', 'es']
        self.min_year = 2015
        
    def parse_ris_file(self, filepath: str) -> List[Dict]:
        """Parse RIS file and return list of article records"""
        articles = []
        current_article = {}
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # Split by ER - (end of record)
            records = content.split('ER  -')
            
            for record in records:
                if not record.strip():
                    continue
                    
                article = {}
                lines = record.strip().split('\n')
                
                for line in lines:
                    line = line.strip()
                    if not line or line.startswith('﻿'):
                        continue
                    
                    # Extract field code and content
                    match = re.match(r'^([A-Z][A-Z0-9]?)\s*-\s*(.*)$', line)
                    if match:
                        field_code = match.group(1)
                        content = match.group(2).strip()
                        
                        if field_code in article:
                            # Handle multiple values for same field
                            if isinstance(article[field_code], list):
                                article[field_code].append(content)
                            else:
                                article[field_code] = [article[field_code], content]
                        else:
                            article[field_code] = content
                
                if article:  # Only add if article has content
                    articles.append(article)
                    
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            
        return articles
    
    def extract_year(self, article: Dict) -> int:
        """Extract publication year from article"""
        year_fields = ['PY', 'DA', 'Y1']
        
        for field in year_fields:
            if field in article:
                year_text = str(article[field])
                # Extract 4-digit year
                year_match = re.search(r'\b(19|20)\d{2}\b', year_text)
                if year_match:
                    return int(year_match.group())
        
        return 0
    
    def check_language(self, article: Dict) -> bool:
        """Check if article is in valid language"""
        # Check language field
        if 'LA' in article:
            lang = str(article['LA']).lower()
            if any(valid_lang in lang for valid_lang in self.valid_languages):
                return True
        
        # If no language field or not recognized, assume English for WoS articles
        return True
    
    def contains_keywords(self, text: str, keywords: List[str]) -> List[str]:
        """Check if text contains any of the keywords (case insensitive)"""
        if not text:
            return []
        
        text_lower = text.lower()
        found_keywords = []
        
        for keyword in keywords:
            if keyword.lower() in text_lower:
                found_keywords.append(keyword)
                
        return found_keywords
    
    def is_relevant_article(self, article: Dict) -> Dict:
        """Check if article is relevant based on PBL assessment challenges criteria"""
        result = {
            'relevant': False,
            'reasons': [],
            'pbl_keywords': [],
            'assessment_keywords': [],
            'challenge_keywords': [],
            'instrument_keywords': [],
            'tech_keywords': [],
            'collaborative_keywords': [],
            'excluded_keywords': [],
            'year': 0
        }
        
        # Extract text fields for analysis
        searchable_text = ""
        for field in ['TI', 'AB', 'KW', 'T2']:  # Title, Abstract, Keywords, Journal
            if field in article:
                if isinstance(article[field], list):
                    searchable_text += " ".join(article[field]) + " "
                else:
                    searchable_text += str(article[field]) + " "
        
        # Check exclusion criteria first
        excluded = self.contains_keywords(searchable_text, self.excluded_keywords)
        result['excluded_keywords'] = excluded
        if excluded:
            result['reasons'].append(f"Excluded due to keywords: {', '.join(excluded)}")
            return result
        
        # Check year
        year = self.extract_year(article)
        result['year'] = year
        if year < self.min_year:
            result['reasons'].append(f"Published before {self.min_year} (year: {year})")
            return result
        
        # Check language
        if not self.check_language(article):
            result['reasons'].append("Not in valid language")
            return result
        
        # Check for PBL keywords
        pbl_found = self.contains_keywords(searchable_text, self.pbl_keywords)
        result['pbl_keywords'] = pbl_found
        
        # Check for assessment keywords
        assessment_found = self.contains_keywords(searchable_text, self.assessment_keywords)
        result['assessment_keywords'] = assessment_found
        
        # Check for challenge keywords
        challenge_found = self.contains_keywords(searchable_text, self.challenge_keywords)
        result['challenge_keywords'] = challenge_found
        
        # Check for instrument keywords
        instrument_found = self.contains_keywords(searchable_text, self.instrument_keywords)
        result['instrument_keywords'] = instrument_found
        
        # Check for technology keywords
        tech_found = self.contains_keywords(searchable_text, self.technology_keywords)
        result['tech_keywords'] = tech_found
        
        # Check for collaborative/processual keywords
        collaborative_found = self.contains_keywords(searchable_text, self.collaborative_keywords)
        result['collaborative_keywords'] = collaborative_found
        
        # Determine relevance based on research questions
        has_pbl = len(pbl_found) > 0
        has_assessment = len(assessment_found) > 0
        
        # For RQ1: PBL + assessment + challenges
        has_challenges = len(challenge_found) > 0
        
        # For RQ2: PBL + assessment + instruments
        has_instruments = len(instrument_found) > 0
        
        # For RQ3: PBL + assessment + technology
        has_technology = len(tech_found) > 0
        
        # For RQ4: PBL + assessment + collaborative/processual
        has_collaborative = len(collaborative_found) > 0
        
        # Main relevance criteria - must have PBL and assessment
        if has_pbl and has_assessment:
            result['relevant'] = True
            result['reasons'].append("Contains PBL and assessment keywords")
            
            # Add specific reasons based on what else was found
            if has_challenges:
                result['reasons'].append("Addresses assessment challenges")
            if has_instruments:
                result['reasons'].append("Discusses assessment instruments")
            if has_technology:
                result['reasons'].append("Involves technology for assessment")
            if has_collaborative:
                result['reasons'].append("Covers collaborative/processual assessment")
        else:
            if not has_pbl:
                result['reasons'].append("No PBL keywords found")
            if not has_assessment:
                result['reasons'].append("No assessment keywords found")
        
        return result
    
    def format_article_ris(self, article: Dict) -> str:
        """Format article back to RIS format"""
        ris_lines = []
        
        # Standard field order for RIS
        field_order = ['TY', 'AU', 'TI', 'T2', 'AB', 'KW', 'PY', 'DA', 'VL', 'IS', 'SP', 'EP', 'SN', 'DO', 'UR', 'AN', 'LA']
        
        # Add fields in order
        for field in field_order:
            if field in article:
                if isinstance(article[field], list):
                    for value in article[field]:
                        ris_lines.append(f"{field}  - {value}")
                else:
                    ris_lines.append(f"{field}  - {article[field]}")
        
        # Add any remaining fields not in standard order
        for field, value in article.items():
            if field not in field_order:
                if isinstance(value, list):
                    for v in value:
                        ris_lines.append(f"{field}  - {v}")
                else:
                    ris_lines.append(f"{field}  - {value}")
        
        ris_lines.append("ER  -")
        ris_lines.append("")
        
        return "\n".join(ris_lines)
    
    def analyze_directory(self, base_dir: str) -> Dict:
        """Analyze all RIS files in directory structure"""
        results = {
            'files_analyzed': [],
            'relevant_articles': [],
            'statistics': {
                'total_articles': 0,
                'relevant_articles': 0,
                'by_layer': defaultdict(lambda: {'total': 0, 'relevant': 0}),
                'by_year': defaultdict(int),
                'themes': defaultdict(int)
            }
        }
        
        # Find all RIS files
        ris_files = []
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith('.ris'):
                    ris_files.append(os.path.join(root, file))
        
        print(f"Found {len(ris_files)} RIS files to analyze")
        
        for filepath in ris_files:
            print(f"Analyzing: {filepath}")
            
            # Determine layer from path
            layer = "unknown"
            if "camada1" in filepath:
                layer = "camada1"
            elif "camada2" in filepath:
                layer = "camada2"
            elif "camada3" in filepath:
                layer = "camada3"
            elif "camada4" in filepath:
                layer = "camada4"
            elif "camada5" in filepath:
                layer = "camada5"
            
            articles = self.parse_ris_file(filepath)
            results['files_analyzed'].append({
                'filepath': filepath,
                'layer': layer,
                'total_articles': len(articles)
            })
            
            results['statistics']['total_articles'] += len(articles)
            results['statistics']['by_layer'][layer]['total'] += len(articles)
            
            for article in articles:
                relevance = self.is_relevant_article(article)
                
                if relevance['relevant']:
                    results['relevant_articles'].append({
                        'article': article,
                        'source_file': filepath,
                        'layer': layer,
                        'relevance_info': relevance
                    })
                    results['statistics']['relevant_articles'] += 1
                    results['statistics']['by_layer'][layer]['relevant'] += 1
                    results['statistics']['by_year'][relevance['year']] += 1
                    
                    # Count themes
                    for keyword in relevance['pbl_keywords']:
                        results['statistics']['themes'][f"PBL: {keyword}"] += 1
                    for keyword in relevance['assessment_keywords']:
                        results['statistics']['themes'][f"Assessment: {keyword}"] += 1
                    for keyword in relevance['challenge_keywords']:
                        results['statistics']['themes'][f"Challenge: {keyword}"] += 1
                    for keyword in relevance['instrument_keywords']:
                        results['statistics']['themes'][f"Instrument: {keyword}"] += 1
                    for keyword in relevance['tech_keywords']:
                        results['statistics']['themes'][f"Technology: {keyword}"] += 1
                    for keyword in relevance['collaborative_keywords']:
                        results['statistics']['themes'][f"Collaborative: {keyword}"] += 1
        
        return results
    
    def generate_consolidated_ris(self, results: Dict, output_path: str):
        """Generate consolidated RIS file with relevant articles"""
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in results['relevant_articles']:
                f.write(self.format_article_ris(item['article']))
                f.write("\n")
    
    def generate_report(self, results: Dict) -> str:
        """Generate analysis report"""
        report = []
        report.append("=" * 80)
        report.append("RIS ANALYSIS REPORT - PBL ASSESSMENT ARTICLES")
        report.append("=" * 80)
        report.append("")
        
        # Summary statistics
        stats = results['statistics']
        report.append("SUMMARY STATISTICS")
        report.append("-" * 40)
        report.append(f"Total articles analyzed: {stats['total_articles']}")
        report.append(f"Relevant articles found: {stats['relevant_articles']}")
        report.append(f"Selection rate: {(stats['relevant_articles']/stats['total_articles']*100):.1f}%")
        report.append("")
        
        # By layer breakdown
        report.append("BREAKDOWN BY SOURCE LAYER")
        report.append("-" * 40)
        for layer, data in stats['by_layer'].items():
            if data['total'] > 0:
                rate = (data['relevant']/data['total']*100) if data['total'] > 0 else 0
                report.append(f"{layer}: {data['relevant']}/{data['total']} ({rate:.1f}%)")
        report.append("")
        
        # By year
        report.append("BREAKDOWN BY YEAR")
        report.append("-" * 40)
        for year in sorted(stats['by_year'].keys(), reverse=True):
            if year > 0:
                report.append(f"{year}: {stats['by_year'][year]} articles")
        report.append("")
        
        # Top themes
        report.append("TOP THEMES IDENTIFIED")
        report.append("-" * 40)
        sorted_themes = sorted(stats['themes'].items(), key=lambda x: x[1], reverse=True)
        for theme, count in sorted_themes[:15]:  # Top 15 themes
            report.append(f"{theme}: {count} articles")
        report.append("")
        
        # Files analyzed
        report.append("FILES ANALYZED")
        report.append("-" * 40)
        for file_info in results['files_analyzed']:
            report.append(f"{file_info['filepath']}: {file_info['total_articles']} articles")
        report.append("")
        
        # Sample relevant articles
        report.append("SAMPLE RELEVANT ARTICLES")
        report.append("-" * 40)
        for i, item in enumerate(results['relevant_articles'][:10]):  # Show first 10
            article = item['article']
            relevance = item['relevance_info']
            
            title = article.get('TI', 'No title')
            year = relevance.get('year', 'Unknown')
            layer = item.get('layer', 'Unknown')
            
            report.append(f"{i+1}. [{year}] {title}")
            report.append(f"   Source: {layer}")
            report.append(f"   Relevance: {', '.join(relevance['reasons'])}")
            if relevance['pbl_keywords']:
                report.append(f"   PBL keywords: {', '.join(relevance['pbl_keywords'])}")
            if relevance['assessment_keywords']:
                report.append(f"   Assessment keywords: {', '.join(relevance['assessment_keywords'])}")
            if relevance['challenge_keywords']:
                report.append(f"   Challenge keywords: {', '.join(relevance['challenge_keywords'])}")
            if relevance['instrument_keywords']:
                report.append(f"   Instrument keywords: {', '.join(relevance['instrument_keywords'])}")
            report.append("")
        
        if len(results['relevant_articles']) > 10:
            report.append(f"... and {len(results['relevant_articles']) - 10} more articles")
        
        return "\n".join(report)


if __name__ == "__main__":
    analyzer = RISAnalyzer()
    base_directory = "/home/afonsolelis/202508_revisao_sistematica_pbl/busca/"
    
    print("Starting RIS analysis...")
    results = analyzer.analyze_directory(base_directory)
    
    # Generate consolidated RIS file
    output_ris = "/home/afonsolelis/202508_revisao_sistematica_pbl/busca/consolidado/artigos_relevantes_pbl_avaliacao.ris"
    os.makedirs(os.path.dirname(output_ris), exist_ok=True)
    analyzer.generate_consolidated_ris(results, output_ris)
    
    # Generate report
    report = analyzer.generate_report(results)
    
    # Save report
    report_path = "/home/afonsolelis/202508_revisao_sistematica_pbl/busca/consolidado/analysis_report.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nAnalysis complete!")
    print(f"Consolidated RIS file saved to: {output_ris}")
    print(f"Analysis report saved to: {report_path}")
    print(f"\nFound {results['statistics']['relevant_articles']} relevant articles out of {results['statistics']['total_articles']} total articles")
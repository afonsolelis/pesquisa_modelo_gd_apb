# JSEP LaTeX Template

## Overview

This LaTeX template follows the APA format (Purdue University style) adapted for the Journal of Software Engineering and Practice (JSEP), incorporating the specific exceptions mentioned in the author guidelines.

## Key Features

### APA Format Compliance
- 12-point font size
- 1-inch margins on all sides
- Single spacing throughout the document
- Proper APA citation style
- Centered section headings
- Bold subsection headings
- Italicized subsubsection headings

### JSEP-Specific Modifications
- **No separate title page**: Title and author information appear at the top of the first page
- **No table of contents**: As per JSEP guidelines
- **No page breaks between sections**: Continuous flow between sections
- **No headers or footers**: These will be added by the journal
- **Single spacing**: Instead of double spacing typical in APA

## File Structure

```
template_jsep/
├── jsep_template.tex    # Main template file
├── author_guidelines.md # Original JSEP guidelines
└── README.md           # This file
```

## Usage Instructions

### 1. Basic Setup
1. Copy `jsep_template.tex` to your working directory
2. Rename it to your paper's filename (e.g., `my_paper.tex`)
3. Open the file in your LaTeX editor

### 2. Customizing the Template

#### Title and Author Information
Replace the placeholder text in the center environment:
```latex
\begin{center}
    \textbf{Your Paper Title Here: A Descriptive Subtitle if Needed}
    
    \vspace{0.5em}
    
    \textbf{Author Name}\\
    Institution Name\\
    City, State/Country\\
    email@institution.edu
\end{center}
```

#### Abstract
Replace the abstract text:
```latex
\apaabstract{
    Your abstract text here. Should be 150-250 words.
}
```

#### Keywords
Update the keywords:
```latex
\apakeywords{keyword1, keyword2, keyword3, keyword4, keyword5}
```

### 3. Adding Content

#### Sections
The template includes standard research paper sections:
- Introduction
- Literature Review
- Methodology
- Results
- Discussion
- Conclusion
- References

#### Tables
Use the provided table format:
```latex
\begin{table}[H]
\centering
\caption{Your Table Caption}
\begin{tabular}{lccc}
\toprule
Header 1 & Header 2 & Header 3 & Header 4 \\
\midrule
Data 1 & Data 2 & Data 3 & Data 4 \\
\bottomrule
\end{tabular}
\end{table}
```

#### Figures
```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.8\textwidth]{figure_name.png}
\caption{Your figure caption}
\end{figure}
```

### 4. Citations

#### Manual Bibliography (Current Setup)
Add references manually in the `thebibliography` environment:
```latex
\bibitem{key}
Author, A. A., \& Author, B. B. (2023). Title. \textit{Journal}, \textit{Volume}(Issue), pages.
```

#### BibTeX (Alternative)
To use BibTeX, uncomment these lines and create a `.bib` file:
```latex
% \bibliographystyle{apacite}
% \bibliography{references}
```

### 5. Compilation

Compile the document using:
```bash
pdflatex jsep_template.tex
```

If using BibTeX:
```bash
pdflatex jsep_template.tex
bibtex jsep_template
pdflatex jsep_template.tex
pdflatex jsep_template.tex
```

## Required Packages

The template includes all necessary packages for APA formatting:
- `geometry`: Page margins
- `setspace`: Line spacing
- `titlesec`: Section formatting
- `booktabs`: Professional tables
- `graphicx`: Image inclusion
- `hyperref`: Hyperlinks
- `apacite`: APA citation style

## Important Notes

### Formatting Requirements
- **Font**: 12-point Times New Roman (default in LaTeX)
- **Spacing**: Single space throughout
- **Margins**: 1 inch on all sides
- **Page breaks**: Avoid between sections
- **Headers/Footers**: None (added by journal)

### Content Guidelines
- **Abstract**: 150-250 words
- **Keywords**: 3-5 keywords
- **Figures/Tables**: Place within text, not at end
- **Citations**: Use APA format
- **References**: APA style bibliography

### Submission Checklist
Before submitting, ensure:
- [ ] No separate title page
- [ ] No table of contents
- [ ] No page breaks between sections
- [ ] Single spacing throughout
- [ ] No headers or footers
- [ ] All figures and tables within text
- [ ] APA citation style used
- [ ] English language only

## Troubleshooting

### Common Issues

1. **Package not found**: Install missing LaTeX packages
2. **Compilation errors**: Check for syntax errors in citations
3. **Formatting issues**: Ensure all packages are loaded

### Getting Help

- Check LaTeX documentation for specific packages
- Consult APA Publication Manual for citation guidelines
- Review JSEP author guidelines for specific requirements

## Example Output

The template produces a professional-looking document with:
- Clean, readable formatting
- Proper APA structure
- Professional table and figure layouts
- Consistent citation style
- JSEP-compliant formatting

## License

This template is provided as-is for use with JSEP submissions. Modify as needed for your specific paper while maintaining compliance with JSEP guidelines.


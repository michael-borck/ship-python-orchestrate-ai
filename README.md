# Ship Python, Orchestrate AI

<!-- BADGES:START -->
[![continuous-integration](https://img.shields.io/badge/-continuous--integration-blue?style=flat-square)](https://github.com/topics/continuous-integration) [![dependency-management](https://img.shields.io/badge/-dependency--management-blue?style=flat-square)](https://github.com/topics/dependency-management) [![documentation](https://img.shields.io/badge/-documentation-blue?style=flat-square)](https://github.com/topics/documentation) [![github-pages](https://img.shields.io/badge/-github--pages-blue?style=flat-square)](https://github.com/topics/github-pages) [![packaging](https://img.shields.io/badge/-packaging-blue?style=flat-square)](https://github.com/topics/packaging) [![python](https://img.shields.io/badge/-python-3776ab?style=flat-square)](https://github.com/topics/python) [![software-development](https://img.shields.io/badge/-software--development-blue?style=flat-square)](https://github.com/topics/software-development) [![static-analysis](https://img.shields.io/badge/-static--analysis-blue?style=flat-square)](https://github.com/topics/static-analysis) [![testing](https://img.shields.io/badge/-testing-blue?style=flat-square)](https://github.com/topics/testing) [![tex](https://img.shields.io/badge/-tex-blue?style=flat-square)](https://github.com/topics/tex)
<!-- BADGES:END -->

This repository contains the source for the book "Ship Python, Orchestrate AI: Professional Python in the AI Era" - a comprehensive guide to professional Python development practices.

## About the Book

Modern Python development demands more than just writing functional code. This book presents a complete development pipeline that balances simplicity with professional practices, helping developers at all levels build maintainable, production-ready Python projects.

### Key Topics

- Setting up proper project structure and version control
- Managing dependencies effectively
- Using code quality tools (linting, formatting, static analysis)
- Implementing testing strategies with pytest
- Adding type checking to Python projects
- Creating effective documentation
- Implementing CI/CD pipelines
- Packaging and distribution

The book follows a "crawl-walk-run" approach, starting with essential practices and progressively introducing more advanced techniques.

## Book Website

The rendered book is available at: https://michael-borck.github.io/ship-python-orchestrate-ai

## Related Materials

This book is part of a 5-book series for mastering modern software development in the AI era:

### Foundational Methodology
- **[Converse Python, Partner AI: The Python Edition](https://michael-borck.github.io/converse-python-partner-ai)** - A methodology for effective AI collaboration

### Python Track
- **[Think Python, Direct AI: Computational Thinking for Beginners](https://michael-borck.github.io/think-python-direct-ai)** - Perfect for absolute beginners
- **[Code Python, Consult AI: Python Fundamentals for the AI Era](https://michael-borck.github.io/code-python-consult-ai)** - Focused introduction to Python fundamentals
- **[Ship Python, Orchestrate AI: Professional Python in the AI Era](https://michael-borck.github.io/ship-python-orchestrate-ai)** (this book) - Professional Python development practices

### Web Track
- **[Build Web, Guide AI: Business Web Development with AI](https://michael-borck.github.io/build-web-guide-ai)** - Modern web development with AI as your partner

## Related Resources

### Companion Repositories

- **[simplebot](https://github.com/michael-borck/simplebot)** - Case study project: A lightweight LLM wrapper for educational settings
- **[ship-python-cookiecutter](https://github.com/michael-borck/ship-python-cookiecutter)** - Cookiecutter template for multi-platform Python apps
- **[ship-python-template](https://github.com/michael-borck/ship-python-template)** - GitHub template for quick project starts
- **[ship-python-example](https://github.com/michael-borck/ship-python-example)** - Complete working example of the multi-platform architecture

## Building the Book Locally

This book is built using [Quarto](https://quarto.org/), a scientific and technical publishing system.

### Prerequisites

- Install [Quarto](https://quarto.org/docs/get-started/)
- (Optional) Install [TinyTeX](https://quarto.org/docs/output-formats/pdf-basics.html) for PDF rendering

### Commands

```bash
# Preview the book with live reloading
quarto preview

# Render the book to HTML, PDF, and EPUB
quarto render

# Publish to GitHub Pages
quarto publish gh-pages
```

## Contributing

While this book is primarily maintained by Michael Borck, suggestions and corrections are welcome:

1. File an issue describing the problem or enhancement
2. For minor corrections, feel free to submit a pull request

## License

This project uses a dual licensing approach:

- **Book Content**: Licensed under [Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE-CONTENT.md). You can freely share, adapt, and build upon the material for any purpose, even commercially, with attribution.

- **Code Examples**: Licensed under the [MIT License](LICENSE-CODE.md). You can use, modify, and distribute the code with minimal restrictions.

See the [LICENSE](LICENSE) file for complete details.

## About the Author

Michael Borck is [brief bio or link to personal site].

## Acknowledgments

- [Any people or organizations you'd like to thank]
## Repository Structure

This book is part of the [books.borck.education](https://books.borck.education) series. Publishing (PDF, EPUB, llm.txt, chatbot, cover generation) is handled by the [book-publisher](https://github.com/michael-borck/book-publisher) repo.

| Path | Purpose |
|---|---|
| `index.qmd` | Preface (landing page) |
| `_quarto.yml` | HTML-only Quarto config |
| `cover.png` | Cover image |
| `copyright-page.tex` | Copyright page for PDF |
| `pdf-header.tex` | LaTeX header for PDF |
| `epub-styles.css` | EPUB styles |
| `notes/` | Working notes, outlines, planning docs (not published) |
| `rag-documents/` | Generated RAG chunks for chatbot |
| `_book/` | Rendered output (gitignored) |
| `_print_source/` | Generated print source (gitignored) |

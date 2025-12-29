python
code-analysis
code-quality
cli-tool
open-source
# 📊 Code Complexity Analyzer

A Python CLI tool that analyzes Python code quality and provides detailed complexity metrics. Perfect for developers who want to maintain clean, maintainable code.

## ✨ Features

- **Line Analysis**: Count total lines, code lines, blank lines, and comments
- **Structure Analysis**: Identify classes, functions, and imports
- **Complexity Scoring**: Calculate cyclomatic complexity approximation
- **Quality Grading**: Get A-D grades based on code complexity
- **Smart Recommendations**: Receive actionable suggestions for improvement
- **Batch Analysis**: Analyze entire directories at once

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/YASWANTH1976/code-complexity-analyzer.git
cd code-complexity-analyzer

# No dependencies needed - uses Python standard library only!
```

### Usage

**Analyze a single file:**
```bash
python analyzer.py my_script.py
```

**Analyze an entire directory:**
```bash
python analyzer.py ./my_project/
```

## 📋 Example Output

```
╔═══════════════════════════════════════════════════════════╗
║        CODE COMPLEXITY ANALYZER v1.0                      ║
║        Analyze Python Code Quality Metrics                ║
╚═══════════════════════════════════════════════════════════╝

============================================================
CODE COMPLEXITY ANALYSIS REPORT
============================================================
File: example.py
============================================================

📊 LINE METRICS:
  Total Lines:          145
  Code Lines:           98
  Blank Lines:          32
  Comment Lines:        15

🏗️  STRUCTURE METRICS:
  Classes:              3
  Functions:            12
  Imports:              5

📈 COMPLEXITY ANALYSIS:
  Complexity Score:     15
  Quality Grade:        B
  Assessment:           👍 Good - Moderate complexity

============================================================
RECOMMENDATIONS:
============================================================
• Code looks good! Keep up the quality standards.
============================================================
```

## 🎯 Metrics Explained

### Complexity Score
- **1-10 (Grade A)**: ✅ Excellent - Low complexity
- **11-20 (Grade B)**: 👍 Good - Moderate complexity  
- **21-30 (Grade C)**: ⚠️ Fair - Consider refactoring
- **31+ (Grade D)**: ❌ High complexity - Needs refactoring

### What It Analyzes
- **Decision Points**: If/else statements, loops, exception handlers
- **Function Count**: Total number of function definitions
- **Class Structure**: Object-oriented design patterns
- **Documentation**: Comment and docstring coverage

## 🛠️ Technical Details

- **Language**: Python 3.6+
- **Dependencies**: None (uses only standard library)
- **Key Libraries**: `ast`, `pathlib`, `os`

## 💡 Use Cases

- **Code Reviews**: Quick quality assessment before commits
- **Learning**: Understand complexity in your practice projects
- **Refactoring**: Identify areas that need improvement
- **Open Source**: Maintain quality standards in contributions

## 🤝 Contributing

Contributions are welcome! This is a learning project built as part of GSoC 2026 preparation.

### Ideas for Enhancement
- Add support for other languages
- Integrate with CI/CD pipelines
- Generate HTML reports
- Add test coverage metrics
- Create configuration file support

## 📄 License

MIT License - feel free to use and modify!

## 👤 Author

**Yaswanth**
- GitHub: [@YASWANTH1976](https://github.com/YASWANTH1976)
- Building open-source skills for GSoC 2026

---

⭐ If you find this useful, please star the repository!

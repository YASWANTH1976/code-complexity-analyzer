#!/usr/bin/env python3
"""
Code Complexity Analyzer
A tool to analyze Python code quality and complexity metrics.

Author: YASWANTH1976
GitHub: https://github.com/YASWANTH1976
"""

import ast
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class ComplexityAnalyzer:
    """Analyzes Python code for various complexity metrics."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.tree = None
        self.metrics = {
            'total_lines': 0,
            'code_lines': 0,
            'blank_lines': 0,
            'comment_lines': 0,
            'functions': 0,
            'classes': 0,
            'imports': 0,
            'complexity_score': 0
        }
        
    def analyze(self) -> Dict:
        """Main analysis method that orchestrates all checks."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")
        
        # Read file content
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Analyze line types
        self._analyze_lines(lines)
        
        # Parse AST for structural analysis
        try:
            self.tree = ast.parse(content)
            self._analyze_structure()
            self._calculate_complexity()
        except SyntaxError as e:
            print(f"⚠️  Syntax error in file: {e}")
            return self.metrics
        
        return self.metrics
    
    def _analyze_lines(self, lines: List[str]):
        """Analyze different types of lines in the code."""
        self.metrics['total_lines'] = len(lines)
        
        for line in lines:
            stripped = line.strip()
            
            if not stripped:
                self.metrics['blank_lines'] += 1
            elif stripped.startswith('#'):
                self.metrics['comment_lines'] += 1
            else:
                self.metrics['code_lines'] += 1
    
    def _analyze_structure(self):
        """Analyze code structure using AST."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                self.metrics['functions'] += 1
            elif isinstance(node, ast.ClassDef):
                self.metrics['classes'] += 1
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                self.metrics['imports'] += 1
    
    def _calculate_complexity(self):
        """Calculate a simple complexity score based on various factors."""
        # Cyclomatic complexity approximation
        decision_points = 0
        
        for node in ast.walk(self.tree):
            # Count decision points (if, for, while, except, etc.)
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                decision_points += 1
            elif isinstance(node, ast.BoolOp):
                decision_points += len(node.values) - 1
        
        # Simple complexity formula
        # Base complexity + decision points + functions/10
        self.metrics['complexity_score'] = (
            1 + decision_points + (self.metrics['functions'] // 10)
        )
    
    def get_quality_grade(self) -> Tuple[str, str]:
        """Return a quality grade based on complexity score."""
        score = self.metrics['complexity_score']
        
        if score <= 10:
            return 'A', '✅ Excellent - Low complexity'
        elif score <= 20:
            return 'B', '👍 Good - Moderate complexity'
        elif score <= 30:
            return 'C', '⚠️  Fair - Consider refactoring'
        else:
            return 'D', '❌ High complexity - Needs refactoring'
    
    def generate_report(self) -> str:
        """Generate a formatted analysis report."""
        grade, message = self.get_quality_grade()
        
        report = f"""
{'='*60}
CODE COMPLEXITY ANALYSIS REPORT
{'='*60}
File: {self.filepath}
{'='*60}

📊 LINE METRICS:
  Total Lines:       {self.metrics['total_lines']:>6}
  Code Lines:        {self.metrics['code_lines']:>6}
  Blank Lines:       {self.metrics['blank_lines']:>6}
  Comment Lines:     {self.metrics['comment_lines']:>6}

🏗️  STRUCTURE METRICS:
  Classes:           {self.metrics['classes']:>6}
  Functions:         {self.metrics['functions']:>6}
  Imports:           {self.metrics['imports']:>6}

📈 COMPLEXITY ANALYSIS:
  Complexity Score:  {self.metrics['complexity_score']:>6}
  Quality Grade:     {grade:>6}
  Assessment:        {message}

{'='*60}
RECOMMENDATIONS:
{'='*60}
"""
        
        # Add specific recommendations
        recommendations = []
        
        if self.metrics['complexity_score'] > 20:
            recommendations.append("• Consider breaking down complex functions into smaller ones")
        
        if self.metrics['functions'] > 30:
            recommendations.append("• High number of functions - consider organizing into classes")
        
        if self.metrics['comment_lines'] < (self.metrics['code_lines'] * 0.1):
            recommendations.append("• Add more comments/docstrings for better documentation")
        
        if self.metrics['classes'] == 0 and self.metrics['functions'] > 10:
            recommendations.append("• Consider using classes for better code organization")
        
        if not recommendations:
            recommendations.append("• Code looks good! Keep up the quality standards.")
        
        report += '\n'.join(recommendations)
        report += '\n' + '='*60 + '\n'
        
        return report


def analyze_directory(directory: str):
    """Analyze all Python files in a directory."""
    print(f"\n🔍 Scanning directory: {directory}\n")
    
    python_files = list(Path(directory).rglob('*.py'))
    
    if not python_files:
        print("❌ No Python files found in directory.")
        return
    
    print(f"Found {len(python_files)} Python file(s)\n")
    
    for filepath in python_files:
        print(f"\n{'─'*60}")
        print(f"Analyzing: {filepath.name}")
        print(f"{'─'*60}")
        
        try:
            analyzer = ComplexityAnalyzer(str(filepath))
            analyzer.analyze()
            print(analyzer.generate_report())
        except Exception as e:
            print(f"❌ Error analyzing {filepath.name}: {e}\n")


def main():
    """Main entry point for the CLI tool."""
    print("""
╔═══════════════════════════════════════════════════════════╗
║        CODE COMPLEXITY ANALYZER v1.0                      ║
║        Analyze Python Code Quality Metrics                ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file:  python analyzer.py <filepath.py>")
        print("  Directory:    python analyzer.py <directory_path>")
        print("\nExample:")
        print("  python analyzer.py my_script.py")
        print("  python analyzer.py ./my_project/")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if os.path.isfile(target):
        # Analyze single file
        try:
            analyzer = ComplexityAnalyzer(target)
            analyzer.analyze()
            print(analyzer.generate_report())
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    
    elif os.path.isdir(target):
        # Analyze directory
        analyze_directory(target)
    
    else:
        print(f"❌ Error: '{target}' is not a valid file or directory")
        sys.exit(1)


if __name__ == '__main__':
    main()
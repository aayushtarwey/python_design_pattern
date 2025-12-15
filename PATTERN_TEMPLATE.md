# Design Pattern Template

This is a template structure for adding new design patterns to the repository.

## 📁 How to Use This Template

For each design pattern you implement, follow this structure:

```
pattern_name/
├── README.md              (Overview and quick reference)
├── src/
│   └── pattern_name.py    (Implementation)
└── docs/
    ├── PATTERN_GUIDE.md   (Detailed documentation)
    └── PATTERN_GUIDE.pdf  (PDF for offline reading)
```

### Steps to Add a New Pattern:

1. **Create the folder structure:**
   ```bash
   mkdir -p category_name/pattern_name/{src,docs}
   ```

2. **Add implementation:**
   - Create `src/pattern_name.py` with clean, commented code
   - Include docstrings and examples

3. **Create documentation:**
   - Create `docs/PATTERN_GUIDE.md` with:
     - Definition and purpose
     - Detailed explanation
     - Real-world examples
     - Interview Q&A
     - Key takeaways
   
4. **Generate PDF:**
   ```bash
   # Run from root: python html_to_pdf_chrome.py
   # (Adjust script as needed)
   ```

5. **Create README.md:**
   - Use `singleton/README.md` as template
   - Customize for your pattern

6. **Commit to git:**
   ```bash
   git add category_name/pattern_name/
   git commit -m "Add pattern_name pattern"
   ```

---

## 📋 README.md Template

Your README should include:

- ✅ Pattern name and type
- ✅ Difficulty level
- ✅ Interview rating
- ✅ Quick overview
- ✅ Folder structure
- ✅ Quick start instructions
- ✅ Real-world use cases
- ✅ Key characteristics
- ✅ Common interview questions
- ✅ When to use/not use
- ✅ Alternative approaches
- ✅ File references

---

## 📖 PATTERN_GUIDE.md Template

Your documentation should include:

1. **Table of Contents**
   - Links to all sections

2. **Quick Definition**
   - One-sentence explanation
   - Key point

3. **Conceptual Explanation**
   - Detailed explanation
   - Analogies
   - Why it's useful

4. **Pattern Details**
   - Step-by-step breakdown
   - Visual diagrams (if applicable)

5. **Code Walkthrough**
   - Implementation explanation
   - Code examples

6. **Real-World Examples**
   - 3-5 practical examples
   - Use cases

7. **Interview Q&A**
   - 10-15 common questions
   - Detailed answers

8. **Key Takeaways**
   - Important points
   - Common mistakes
   - Interview tips

9. **Quick Reference**
   - Code templates
   - Usage examples

---

## 📊 Pattern Categories

### Creational Patterns (5)
Deal with object creation mechanisms

1. Singleton ✅
2. Factory Method
3. Abstract Factory
4. Builder
5. Prototype

### Structural Patterns (7)
Deal with object composition and relationships

1. Adapter
2. Bridge
3. Composite
4. Decorator
5. Facade
6. Flyweight
7. Proxy

### Behavioral Patterns (11)
Deal with communication between objects

1. Chain of Responsibility
2. Command
3. Interpreter
4. Iterator
5. Mediator
6. Memento
7. Observer
8. State
9. Strategy
10. Template Method
11. Visitor

---

## ✅ Checklist Before Committing

- [ ] Folder structure created correctly
- [ ] Implementation code is clean and commented
- [ ] Markdown documentation is comprehensive
- [ ] PDF generated successfully
- [ ] README.md created for the pattern
- [ ] Code runs without errors
- [ ] All examples tested
- [ ] Interview Q&A included
- [ ] Files organized in src/ and docs/
- [ ] Commit message is descriptive

---

## 📝 Example Commit Messages

```bash
# For a new pattern
git commit -m "Add Factory Method pattern with complete documentation"

# For improvements
git commit -m "Update Singleton pattern documentation with more examples"

# For bug fixes
git commit -m "Fix thread-safety example in Singleton pattern"
```

---

## 🎯 Quick Checklist for Each Pattern

### Before Starting
- [ ] Research the pattern thoroughly
- [ ] Understand use cases and benefits
- [ ] Know common interview questions

### During Implementation
- [ ] Write clean, readable code
- [ ] Add detailed comments
- [ ] Include working examples
- [ ] Test the implementation

### During Documentation
- [ ] Explain concept clearly
- [ ] Use analogies for clarity
- [ ] Provide multiple examples
- [ ] Include Q&A section
- [ ] Mention pros and cons

### Before Committing
- [ ] Verify file structure
- [ ] Test all code examples
- [ ] Review documentation
- [ ] Generate PDF
- [ ] Update main README.md

---

## 🚀 Getting Started

To add your first pattern after Singleton:

1. Copy this template folder structure
2. Implement the pattern
3. Write comprehensive documentation
4. Generate PDF
5. Create README.md
6. Commit to git

---

**Good luck with your next design pattern! 🎓**

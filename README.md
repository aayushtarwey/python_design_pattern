# Python Design Patterns Learning Repository

A comprehensive guide to learning all 23 Gang of Four (GoF) design patterns in Python with detailed explanations, code examples, and real-world use cases.

**Author:** Aayush Tarwey  
**Last Updated:** December 15, 2025

---

## 📚 Overview

This repository contains implementations and documentation for all design patterns organized into three categories:

1. **Creational Patterns** - Deal with object creation mechanisms
2. **Structural Patterns** - Deal with object composition and relationships
3. **Behavioral Patterns** - Deal with communication between objects

---

## 📁 Repository Structure

```
python_design_pattern/
├── README.md (this file)
├── creational_patterns/
│   ├── singleton/
│   │   ├── naiveSingleton.py          (Implementation)
│   │   ├── SINGLETON_GUIDE.md         (Markdown Documentation)
│   │   └── SINGLETON_GUIDE.pdf        (PDF Guide for offline reading)
│   ├── factory_method/                (Coming soon)
│   ├── abstract_factory/              (Coming soon)
│   ├── builder/                       (Coming soon)
│   └── prototype/                     (Coming soon)
├── structural_patterns/
│   ├── adapter/                       (Coming soon)
│   ├── bridge/                        (Coming soon)
│   ├── composite/                     (Coming soon)
│   ├── decorator/                     (Coming soon)
│   ├── facade/                        (Coming soon)
│   ├── flyweight/                     (Coming soon)
│   └── proxy/                         (Coming soon)
└── behavioral_patterns/
    ├── chain_of_responsibility/       (Coming soon)
    ├── command/                       (Coming soon)
    ├── interpreter/                   (Coming soon)
    ├── iterator/                      (Coming soon)
    ├── mediator/                      (Coming soon)
    ├── memento/                       (Coming soon)
    ├── observer/                      (Coming soon)
    ├── state/                         (Coming soon)
    ├── strategy/                      (Coming soon)
    ├── template_method/               (Coming soon)
    ├── visitor/                       (Coming soon)
    └── null_object/                   (Coming soon)
```

---

## 🎯 Design Patterns Covered

### ✅ Completed

#### Creational Patterns
- [x] **Singleton** - Ensures a class has only one instance
  - Location: `creational_patterns/singleton/`
  - Files: `naiveSingleton.py`, `SINGLETON_GUIDE.md`, `SINGLETON_GUIDE.pdf`
  - Status: ✅ Complete with documentation

### 🔄 In Progress
- [ ] Factory Method
- [ ] Abstract Factory
- [ ] Builder
- [ ] Prototype

### 📋 Planned
- All Structural Patterns (7 patterns)
- All Behavioral Patterns (11 patterns)

---

## 🚀 Quick Start

### Running the Singleton Example

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the singleton implementation
python creational_patterns/singleton/naiveSingleton.py
```

### Reading the Documentation

**Markdown Format (for GitHub/IDE):**
```bash
open creational_patterns/singleton/SINGLETON_GUIDE.md
```

**PDF Format (for offline reading):**
```bash
open creational_patterns/singleton/SINGLETON_GUIDE.pdf
```

---

## 📖 Each Pattern Includes

For every design pattern you'll find:

1. **Implementation File** (`.py`)
   - Clean, well-commented code
   - Production-ready examples

2. **Markdown Guide** (`.md`)
   - Comprehensive explanation
   - Real-world use cases
   - Step-by-step walkthrough
   - Advantages and disadvantages

3. **PDF Documentation** (`.pdf`)
   - Professional formatted guide
   - Easy to read offline
   - Printable format

---

## 💡 Learning Path

### Recommended Order:

**Phase 1: Creational Patterns** (Object Creation)
1. Singleton - Single instance
2. Factory Method - Object creation
3. Abstract Factory - Family of objects
4. Builder - Complex object construction
5. Prototype - Object cloning

**Phase 2: Structural Patterns** (Object Composition)
1. Adapter - Interface compatibility
2. Decorator - Dynamic enhancement
3. Facade - Simplified interface
4. Proxy - Controlled access
5. Bridge - Abstraction decoupling
6. Composite - Tree structures
7. Flyweight - Memory optimization

**Phase 3: Behavioral Patterns** (Object Interaction)
1. Observer - Publish/Subscribe
2. Strategy - Algorithm switching
3. Command - Action encapsulation
4. State - State-dependent behavior
5. Template Method - Algorithm skeleton
6. Iterator - Sequence traversal
7. Chain of Responsibility - Handler chain
8. Visitor - Element operations
9. Interpreter - Grammar rules
10. Mediator - Object communication
11. Memento - State snapshots

---

## 🎓 How to Learn

### For Each Pattern:

1. **Read the Markdown Guide** (PATTERN_GUIDE.md)
   - Understand the concept
   - Review the examples

2. **Study the Code** (pattern_name.py)
   - Read the implementation
   - Understand how it works
   - Try running it

3. **Save the PDF** (PATTERN_GUIDE.pdf)
   - For offline reference
   - For interview preparation
   - For future review

4. **Practice**
   - Modify the code
   - Create your own examples
   - Apply to real-world problems

---

## 🎯 Interview Preparation

### Quick Lookup Guide

Each pattern documentation includes:

✅ Definition and purpose  
✅ Real-world use cases  
✅ Advantages and disadvantages  
✅ Implementation details  
✅ Common interview questions  
✅ Code examples  
✅ Best practices  

### Using PDFs for Interview Prep

1. Download all PDFs
2. Read during commute/breaks
3. Use as reference during practice
4. Review before interviews

---

## 📊 Statistics

| Category | Patterns | Completed | Status |
|----------|----------|-----------|--------|
| Creational | 5 | 1 | 20% |
| Structural | 7 | 0 | 0% |
| Behavioral | 11 | 0 | 0% |
| **Total** | **23** | **1** | **4%** |

---

## 🔧 Technical Stack

- **Language:** Python 3.12+
- **Environment:** Virtual Environment (.venv)
- **Documentation:** Markdown + PDF
- **Version Control:** Git

---

## 📝 Notes for Each Pattern

### Singleton
- **Type:** Creational
- **Difficulty:** Beginner
- **Real-world Use:** Database connections, Loggers, Configuration managers
- **Key Concept:** Only one instance ever exists
- **Interview Rating:** ⭐⭐⭐ Very Common

---

## 🎯 Learning Goals

By completing this repository, you will:

✅ Understand all 23 GoF design patterns  
✅ Know when and where to use each pattern  
✅ Be able to implement patterns in Python  
✅ Be ready for design pattern interview questions  
✅ Write more maintainable and scalable code  
✅ Recognize patterns in existing code  

---

## 📚 Resources

### Official References
- Gang of Four (GoF) Design Patterns Book
- Head First Design Patterns
- Refactoring.Guru Design Patterns

### Python-Specific
- Python Design Patterns Documentation
- PEP 8 - Style Guide for Python Code
- Real Python Design Patterns Articles

---

## 🤝 Contributing

To add a new pattern:

1. Create a folder: `category/pattern_name/`
2. Add implementation: `pattern_name.py`
3. Create guide: `PATTERN_GUIDE.md`
4. Generate PDF: `PATTERN_GUIDE.pdf`
5. Update main README.md

---

## 📞 Contact & Support

For questions or clarifications about any pattern:
- Review the markdown guide
- Check the code comments
- Refer to the Q&A section in the guide

---

## 📄 License

This learning repository is for educational purposes.

---

## 🎉 Next Steps

1. ✅ Explore the Singleton pattern
2. ⏳ Review Creational patterns
3. ⏳ Learn Structural patterns
4. ⏳ Master Behavioral patterns
5. ⏳ Practice all patterns
6. ⏳ Use in real projects

---

**Happy Learning! 🚀**

Keep this repository updated as you learn each new pattern!

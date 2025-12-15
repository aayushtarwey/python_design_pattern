# Singleton Design Pattern

## 📁 Folder Structure

```
singleton/
├── README.md              (This file - Overview)
├── src/
│   └── naiveSingleton.py  (Implementation)
└── docs/
    ├── SINGLETON_GUIDE.md (Markdown documentation)
    └── SINGLETON_GUIDE.pdf (PDF for offline reading)
```

## 🎯 Quick Overview

**Pattern Name:** Singleton  
**Type:** Creational Pattern  
**Difficulty:** Beginner ⭐  
**Interview Rating:** ⭐⭐⭐ Very Common

### What is Singleton?
A creational design pattern that ensures a class has only ONE instance and provides a global point of access to that instance.

### Key Concept
No matter how many times you try to create an object of that class, you'll always get the SAME object back!

---

## 📚 Documentation

### For Beginners: Start Here
1. Read `docs/SINGLETON_GUIDE.md` (detailed explanation with examples)
2. Run `src/naiveSingleton.py` to see it in action
3. Review the code and comments

### For Reference
- `docs/SINGLETON_GUIDE.pdf` - Professional PDF guide for offline reading

### For Interview Prep
- Q&A section in `docs/SINGLETON_GUIDE.md`
- Real-world examples in documentation
- Common mistakes to avoid

---

## 🚀 Quick Start

### Run the Implementation
```bash
cd /Users/aayushtarwey/python_design_pattern
python creational_patterns/singleton/src/naiveSingleton.py
```

### Expected Output
```
All instances are the same. Singleton pattern works!
```

---

## 💡 Real-World Use Cases

1. **Database Connections** - Single connection pool for entire app
2. **Logger Objects** - One logger instance across all modules
3. **Configuration Manager** - One global config object
4. **Thread Pools** - Single thread pool
5. **Caches** - One cache for entire application
6. **Session Manager** - One session manager

---

## 📖 Reading Guide

### Start with: `docs/SINGLETON_GUIDE.md`
Contains:
- ✅ Quick definition
- ✅ Detailed explanation of metaclass and type()
- ✅ How singleton works (step-by-step)
- ✅ Real-world examples (3 complete examples)
- ✅ 12 Interview Q&A
- ✅ Key takeaways
- ✅ Common mistakes
- ✅ Interview tips

### For Offline Reading: `docs/SINGLETON_GUIDE.pdf`
Same content as markdown, professionally formatted for printing/reading

---

## 🔍 Code Walkthrough

### File: `src/naiveSingleton.py`

**Key Components:**

1. **Singleton Metaclass**
   ```python
   class Singleton(type):
       _instance = {}
       def __call__(self, *args, **kwds):
           # Returns same instance every time
   ```

2. **Using the Metaclass**
   ```python
   class NetworkDriver(metaclass=Singleton):
       # Only one instance will ever exist
   ```

3. **Testing**
   ```python
   driver1 = NetworkDriver()
   driver2 = NetworkDriver()
   assert driver1 is driver2  # True!
   ```

---

## ✅ What You'll Learn

By studying this pattern, you'll understand:

✅ What is a metaclass in Python  
✅ How type() works as a metaclass  
✅ How to control instance creation  
✅ Real-world applications  
✅ When to use singleton (and when NOT to)  
✅ Thread-safe considerations  
✅ Interview questions about singleton  

---

## 📊 Pattern Characteristics

| Aspect | Details |
|--------|---------|
| **Pattern Type** | Creational |
| **Scope** | Class |
| **Complexity** | Easy |
| **Use Frequency** | Very High |
| **Thread-Safe** | No (needs locks) |
| **Memory Impact** | Low (single instance) |

---

## 🎯 Interview Questions

### Top 3 Questions

**Q1: What is the Singleton pattern?**
> A creational design pattern that ensures only one instance of a class exists with a global access point.

**Q2: Why use Singleton?**
> To control instance creation, save memory, and provide global access to a shared resource.

**Q3: Is this implementation thread-safe?**
> No. Use locks for multi-threaded environments.

*See `docs/SINGLETON_GUIDE.md` for 12 complete Q&A*

---

## 🚨 Important Notes

### Thread Safety ⚠️
This implementation is **NOT thread-safe**. In multi-threaded environments, use locks:
```python
import threading
class ThreadSafeSingleton(type):
    _lock = threading.Lock()
    # ... with locking logic
```

### When NOT to Use
- When you need multiple instances
- When inheritance is complex
- For testing (hard to mock)
- In multithreaded scenarios (without locks)

### Alternatives
1. Module-level instance
2. Decorator approach
3. Using __new__ method

---

## 📞 How to Use This Folder

### For Learning
1. Start: Read `docs/SINGLETON_GUIDE.md`
2. Study: Examine `src/naiveSingleton.py`
3. Practice: Modify the code, try variations
4. Review: Use `docs/SINGLETON_GUIDE.pdf` for revision

### For Reference
- Quick lookup: Check README.md (this file)
- Detailed info: See SINGLETON_GUIDE.md
- Visual reference: Open SINGLETON_GUIDE.pdf

### For Interviews
- Review Q&A in documentation
- Practice explaining the pattern
- Know the pros and cons
- Be ready to code it

---

## 🎓 Learning Outcomes

After studying this pattern, you should be able to:

✅ Explain what Singleton is in simple terms  
✅ Understand metaclasses in Python  
✅ Implement a Singleton in Python  
✅ Identify real-world use cases  
✅ Discuss advantages and disadvantages  
✅ Answer interview questions  
✅ Know when to use and when not to use  
✅ Understand thread-safety concerns  

---

## 📝 Files Reference

| File | Purpose | Best For |
|------|---------|----------|
| `naiveSingleton.py` | Working implementation | Understanding & running |
| `SINGLETON_GUIDE.md` | Comprehensive guide | Detailed learning |
| `SINGLETON_GUIDE.pdf` | Professional documentation | Offline reading & interviews |
| `README.md` | Quick reference | Quick lookup |

---

## 🔗 Related Patterns

**Often Used With:**
- Factory Method (create singletons)
- Observer (singleton manages observers)
- Facade (singleton provides simplified interface)

**Similar To:**
- Module-level instances
- Dependency injection
- Service locator

---

## 💬 Common Questions

**Q: Can I have multiple singletons?**
> Yes! Each class with Singleton metaclass gets its own single instance.

**Q: Is it hard to test code with singletons?**
> Yes, mocking singletons is difficult. Consider alternatives for highly testable code.

**Q: What's the difference between Singleton and static class?**
> Singleton is an object instance, static class is just namespace. Objects can have state.

*More Q&A in documentation*

---

## 🚀 Next Steps

1. ✅ Read this README
2. ⏳ Study `SINGLETON_GUIDE.md`
3. ⏳ Run `naiveSingleton.py`
4. ⏳ Review `SINGLETON_GUIDE.pdf`
5. ⏳ Practice implementing variations
6. ⏳ Explain it to someone else
7. ⏳ Move to next design pattern

---

**Happy Learning! 🎯**

For more design patterns, return to the main README.md in the project root.

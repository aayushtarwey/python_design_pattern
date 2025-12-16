# Factory Method Design Pattern

## 📁 Folder Structure

```
factory_method/
├── README.md              (This file - Overview)
├── src/
│   └── factory_method.py  (Fully commented implementation)
└── docs/
    ├── FACTORY_METHOD_GUIDE.md (Comprehensive documentation)
    └── FACTORY_METHOD_GUIDE.pdf (PDF for offline reading)
```

## 🎯 Quick Overview

**Pattern Name:** Factory Method  
**Type:** Creational Pattern  
**Difficulty:** Intermediate ⭐⭐  
**Interview Rating:** ⭐⭐⭐⭐ Very Common

### What is Factory Method?
A design pattern that defines an interface for creating objects, but lets subclasses decide which class to instantiate.

### Key Concept
Create objects WITHOUT specifying their exact classes!

### Real-World Analogy
Think of a factory that produces different types of currency:
- **Fiat Currency Factory** produces: USD, EUR, JPY
- **Virtual Currency Factory** produces: Bitcoin, Ethereum, Dogecoin

---

## 📚 Documentation

### For Beginners: Start Here
1. Read `docs/FACTORY_METHOD_GUIDE.md` (comprehensive guide with analogies)
2. Run `src/factory_method.py` to see it in action
3. Review the code with detailed comments

### For Reference
- `docs/FACTORY_METHOD_GUIDE.md` - Complete guide with examples
- `docs/FACTORY_METHOD_GUIDE.pdf` - Professional PDF for offline reading

### For Interview Prep
- Q&A section in `docs/FACTORY_METHOD_GUIDE.md`
- Real-world examples throughout documentation
- Code walkthrough and explanations

---

## 🚀 Quick Start

### Run the Implementation
```bash
cd /Users/aayushtarwey/python_design_pattern
python creational_patterns/factory_method/src/factory_method.py
```

### Expected Output
```
============================================================
FIAT CURRENCY FACTORY OUTPUT:
============================================================
USD
EUR
JPY

============================================================
VIRTUAL CURRENCY FACTORY OUTPUT:
============================================================
Bitcoin
Ethereum
Dogecoin

============================================================
KEY BENEFITS OF THIS PATTERN:
============================================================
✅ Easy to add new currency types
✅ Easy to add new countries
✅ Creation logic is centralized
✅ Client code doesn't know HOW objects are created
✅ Easy to maintain and modify
```

---

## 💡 Real-World Use Cases

1. **Database Drivers** - MySQLFactory, PostgreSQLFactory, MongoDBFactory
2. **UI Elements** - WindowsButtonFactory, MacButtonFactory, LinuxButtonFactory
3. **Payment Systems** - CreditCardFactory, PayPalFactory, CryptoFactory
4. **Document Formats** - PDFFactory, ExcelFactory, WordFactory
5. **File Readers** - CSVReaderFactory, JSONReaderFactory, XMLReaderFactory

---

## 📖 Reading Guide

### Start with: `docs/FACTORY_METHOD_GUIDE.md`
Contains:
- ✅ Quick definition
- ✅ Real-world analogy (currency exchange)
- ✅ Pattern components breakdown
- ✅ Detailed explanation with diagrams
- ✅ Code walkthrough
- ✅ Comparison with other patterns
- ✅ 3+ Real-world examples
- ✅ 12 Interview Q&A
- ✅ Key takeaways
- ✅ Common mistakes
- ✅ Interview tips

### For Offline Reading: `docs/FACTORY_METHOD_GUIDE.pdf`
Same content as markdown, professionally formatted for printing/reading

---

## 🔍 Code Structure

### File: `src/factory_method.py`

**Key Components:**

1. **Abstract Factory (Interface)**
   ```python
   class CountryFactory(ABC):
       @abstractmethod
       def create_country(self, country):
           pass
   ```

2. **Concrete Factory 1**
   ```python
   class FiatCurrencyFactory(CountryFactory):
       def create_country(self, country):
           # Returns fiat currencies
   ```

3. **Concrete Factory 2**
   ```python
   class VirtualCurrencyFactory(CountryFactory):
       def create_country(self, country):
           # Returns virtual currencies
   ```

4. **Usage**
   ```python
   fiat = FiatCurrencyFactory()
   virtual = VirtualCurrencyFactory()
   
   fiat.create_country("USA")      # USD
   virtual.create_country("USA")   # Bitcoin
   ```

---

## ✅ What You'll Learn

By studying this pattern, you'll understand:

✅ How to decouple object creation from usage  
✅ How to create multiple types of objects through factories  
✅ How to follow the Open/Closed Principle  
✅ How to make code easily extensible  
✅ Real-world applications of Factory Method  
✅ When to use Factory Method (and when NOT to)  
✅ Interview questions about factory patterns  

---

## 📊 Pattern Characteristics

| Aspect | Details |
|--------|---------|
| **Pattern Type** | Creational |
| **Scope** | Class |
| **Complexity** | Medium |
| **Use Frequency** | Very High |
| **Thread-Safe** | Yes (with proper implementation) |
| **Memory Impact** | Low |

---

## 🎯 Interview Questions (Top 5)

**Q1: What is Factory Method?**
> Defines an interface for creating objects, but lets subclasses decide which class to instantiate.

**Q2: Why use Factory Method instead of new operator?**
> Provides flexibility, loose coupling, and easy extensibility.

**Q3: How is it different from Simple Factory?**
> Factory Method uses inheritance; Simple Factory uses a single method.

**Q4: What are real-world examples?**
> Database drivers, UI elements, payment systems, document formats.

**Q5: When should you use it?**
> When you have multiple object types and want to decouple creation from usage.

*See `docs/FACTORY_METHOD_GUIDE.md` for 12 complete Q&A*

---

## ✨ Key Benefits

✅ **Flexibility** - Easy to add new factory types  
✅ **Maintainability** - Creation logic centralized  
✅ **Loose Coupling** - Client doesn't know concrete classes  
✅ **Extensibility** - Add new types without modifying existing code  
✅ **Clean Code** - Follows SOLID principles  

---

## ⚠️ When NOT to Use

- When you have only one object type
- For very simple object creation
- When it adds unnecessary complexity
- When creation logic is trivial

---

## 🔗 Comparison with Other Patterns

### Factory Method vs Simple Factory
- **Factory Method:** Extensible, uses inheritance
- **Simple Factory:** Single method, not extensible

### Factory Method vs Abstract Factory
- **Factory Method:** Creates one product
- **Abstract Factory:** Creates family of products

### Factory Method vs Singleton
- **Factory Method:** Creates different objects
- **Singleton:** Only one instance of a class

---

## 📞 How to Use This Folder

### For Learning
1. Start: Read `docs/FACTORY_METHOD_GUIDE.md`
2. Study: Examine `src/factory_method.py`
3. Practice: Modify the code, create new factories
4. Review: Use PDF for revision

### For Reference
- Quick lookup: Check this README
- Detailed info: See FACTORY_METHOD_GUIDE.md
- Visual reference: Open FACTORY_METHOD_GUIDE.pdf

### For Interviews
- Review Q&A in documentation
- Practice explaining with analogies
- Know the pros and cons
- Be ready to extend the code

---

## 🎓 Learning Outcomes

After studying this pattern, you should be able to:

✅ Explain Factory Method in simple terms  
✅ Understand when and why to use it  
✅ Implement Factory Method in Python  
✅ Identify real-world use cases  
✅ Discuss advantages and disadvantages  
✅ Answer interview questions confidently  
✅ Extend existing code with new factories  
✅ Recognize Factory Method in existing code  

---

## 📝 Files Reference

| File | Purpose | Best For |
|------|---------|----------|
| `factory_method.py` | Implementation | Understanding & running |
| `FACTORY_METHOD_GUIDE.md` | Complete guide | Detailed learning |
| `FACTORY_METHOD_GUIDE.pdf` | Documentation | Offline reading & interviews |
| `README.md` | Quick reference | Quick lookup |

---

## 🔗 Related Patterns

**Often Used With:**
- Abstract Factory (create families of objects)
- Singleton (single factory instance)
- Strategy (different algorithms)

**Similar To:**
- Simple Factory
- Abstract Factory
- Builder (complex object creation)

---

## 💬 Common Questions

**Q: Can I have multiple concrete factories for the same product?**
> Yes! That's the beauty of Factory Method - different factories can create related products.

**Q: How do I add a new currency type?**
> Just create a new concrete factory - no changes to existing code!

**Q: Is Factory Method used in real libraries?**
> Yes! Django ORM, Pillow, SQLAlchemy, and many others use it.

*More Q&A in documentation*

---

## 🚀 Next Steps

1. ✅ Read this README
2. ⏳ Study `FACTORY_METHOD_GUIDE.md`
3. ⏳ Run `factory_method.py`
4. ⏳ Review `FACTORY_METHOD_GUIDE.pdf`
5. ⏳ Create your own factory examples
6. ⏳ Explain it to someone else
7. ⏳ Move to next design pattern

---

**Happy Learning! 🎯**

For more design patterns, return to the main README.md in the project root.

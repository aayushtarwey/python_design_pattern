"""
Factory Method Design Pattern - Currency Factory Example

PATTERN: Creational Pattern
PURPOSE: Create objects without specifying their exact classes
BENEFIT: Decouples object creation from usage

ANALOGY: Think of a factory that produces different types of currency
         You don't need to know how to create USD, EUR, or Bitcoin
         You just ask the factory to create it for you
"""

from abc import ABC, abstractmethod


# ============================================================================
# STEP 1: DEFINE THE PRODUCT (What we want to create)
# ============================================================================

class Country:
    """
    Base class representing a Country
    This is our PRODUCT that the factory will create
    """
    pass


# ============================================================================
# STEP 2: DEFINE CONCRETE PRODUCTS (Different types of countries)
# ============================================================================

class USA(Country):
    """Concrete product: USA"""
    pass


class Spain(Country):
    """Concrete product: Spain"""
    pass


class Japan(Country):
    """Concrete product: Japan"""
    pass


# ============================================================================
# STEP 3: DEFINE THE ABSTRACT FACTORY (Blueprint for all factories)
# ============================================================================

class CountryFactory(ABC):
    """
    Abstract Factory - Defines the interface that all concrete factories must follow
    
    WHY ABSTRACT?
    - Forces all subclasses to implement the create_country method
    - Ensures consistency across different factory implementations
    - Defines a contract that subclasses MUST follow
    """
    
    @abstractmethod
    def create_country(self) -> Country:
        """
        Abstract method that MUST be implemented by subclasses
        This ensures every factory knows how to create a country
        """
        pass


# ============================================================================
# STEP 4: DEFINE CONCRETE FACTORIES (Actual factory implementations)
# ============================================================================

class FiatCurrencyFactory(CountryFactory):
    """
    Concrete Factory #1: Fiat Currency Factory
    
    Responsibility: Create fiat currencies (government-backed money)
    Examples: USD, EUR, JPY, etc.
    
    This factory IMPLEMENTS the create_country method from the abstract class
    """
    
    def create_country(self, country) -> str:
        """
        Creates a fiat currency based on the country name
        
        Args:
            country (str): Name of the country (USA, Spain, Japan, etc.)
        
        Returns:
            str: The corresponding fiat currency code
        
        HOW IT WORKS:
        1. Takes country name as input
        2. Returns the corresponding fiat currency
        3. If country not recognized, returns "Unknown Country"
        """
        
        # Check which country and return its fiat currency
        if country == "USA":
            return "USD"  # United States Dollar
        elif country == "Spain":
            return "EUR"  # Euro (used in Spain)
        elif country == "Japan":
            return "JPY"  # Japanese Yen
        else:
            return "Unknown Country"


class VirtualCurrencyFactory(CountryFactory):
    """
    Concrete Factory #2: Virtual Currency Factory
    
    Responsibility: Create virtual/crypto currencies
    Examples: Bitcoin, Ethereum, Dogecoin, etc.
    
    This factory ALSO IMPLEMENTS the create_country method from the abstract class
    Notice: Different implementation but SAME INTERFACE as FiatCurrencyFactory
    """
    
    def create_country(self, country) -> str:
        """
        Creates a virtual currency based on the country name
        
        Args:
            country (str): Name of the country (USA, Spain, Japan, etc.)
        
        Returns:
            str: The corresponding virtual currency name
        
        HOW IT WORKS:
        1. Takes country name as input
        2. Returns the corresponding virtual currency
        3. If country not recognized, returns "Unknown Country"
        
        IMPORTANT: Same interface as FiatCurrencyFactory but different output!
        This is the power of Factory Pattern - same method, different results
        """
        
        # Check which country and return its virtual currency
        if country == "USA":
            return "Bitcoin"  # Popular in USA
        elif country == "Spain":
            return "Ethereum"  # Popular in Europe
        elif country == "Japan":
            return "Dogecoin"  # Popular in Japan
        else:
            return "Unknown Country"

        
# ============================================================================
# STEP 5: DEMONSTRATE THE FACTORY PATTERN
# ============================================================================

if __name__ == "__main__":
    """
    EXECUTION FLOW:
    
    The beauty of Factory Pattern is that we don't need to know HOW to create
    currencies. We just ask the factory and it handles the creation.
    """
    
    # Step 1: Create instances of our two different factories
    fiat_factory = FiatCurrencyFactory()        # Factory for fiat currencies
    virtual_factory = VirtualCurrencyFactory()  # Factory for virtual currencies
    
    print("=" * 60)
    print("FIAT CURRENCY FACTORY OUTPUT:")
    print("=" * 60)
    
    # Step 2: Use the fiat factory to create fiat currencies
    # Notice: We don't create objects, the factory does it for us
    print(fiat_factory.create_country("USA"))        # Output: USD
    print(fiat_factory.create_country("Spain"))      # Output: EUR
    print(fiat_factory.create_country("Japan"))      # Output: JPY
    
    print("\n" + "=" * 60)
    print("VIRTUAL CURRENCY FACTORY OUTPUT:")
    print("=" * 60)
    
    # Step 3: Use the virtual factory to create virtual currencies
    # Same input (country names), but DIFFERENT output!
    # This shows the power of having different factory implementations
    print(virtual_factory.create_country("USA"))     # Output: Bitcoin
    print(virtual_factory.create_country("Spain"))   # Output: Ethereum
    print(virtual_factory.create_country("Japan"))   # Output: Dogecoin
    
    print("\n" + "=" * 60)
    print("KEY BENEFITS OF THIS PATTERN:")
    print("=" * 60)
    print("✅ Easy to add new currency types (just create new factory)")
    print("✅ Easy to add new countries (just add elif in method)")
    print("✅ Creation logic is centralized in factories")
    print("✅ Client code doesn't know HOW objects are created")
    print("✅ Easy to maintain and modify")

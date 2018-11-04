def make_pizza(size,*toppings):
    """Making a pizza"""
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

import random

def main():
    """Generate and print multiple random sentences."""
    for _ in range(6):  # Generate 6 example sentences
        print(make_sentence())

def make_sentence():
    """Create a simple sentence with a determiner, noun, and verb."""
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    return f"{determiner} {noun} {verb}."

def get_determiner():
    """Return a randomly chosen determiner."""
    determiners = ["A", "One", "The", "Some", "Many"]
    return random.choice(determiners)

def get_noun():
    """Return a randomly chosen noun."""
    nouns = ["cat", "dog", "man", "woman", "girl", "boy", "bird", "child", "teacher", "student"]
    return random.choice(nouns)

def get_verb():
    """Return a randomly chosen verb."""
    verbs = ["laughed", "eats", "thinks", "thought", "runs", "writes", "sings", "jumps", "talks", "reads"]
    return random.choice(verbs)

if __name__ == "__main__":
    main()

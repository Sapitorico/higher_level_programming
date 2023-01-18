#!/usr/bin/python3
print(f"{random.randint(-10, 10)} is {"positive" if random.randint(-10, 10) > 0 else "negative" if random.randint(-10, 10) < 0 else "zero"}")

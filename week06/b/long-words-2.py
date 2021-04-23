#!/usr/bin/env python3

#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "unicorns", "", "elephant", "mouse"]

i = 0
while i < len(a):
    if len(a[i]) >= 6:
        print(a[i])
        i = len(a)
    i = i + 1

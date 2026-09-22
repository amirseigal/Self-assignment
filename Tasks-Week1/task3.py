# Task 3 - Data Type Conversion

if __name__ == '__main__':
    i = 7
    f = float(i)
    print(f"int {i} -> float {f}  (type: {type(f).__name__})")

    f2 = 9.8
    i2 = int(f2)
    print(f"float {f2} -> int {i2}  (type: {type(i2).__name__})")

    i3 = 42
    s3 = str(i3)
    print(f"int {i3} -> str '{s3}'  (type: {type(s3).__name__})")

    s4 = "123"
    i4 = int(s4)
    print(f"str '{s4}' -> int {i4}  (type: {type(i4).__name__})")

    i5 = 0
    b5 = bool(i5)
    print(f"int {i5} -> bool {b5}  (type: {type(b5).__name__})")

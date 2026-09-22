def digit_sum_and_average(s1):
    digits = [int(ch) for ch in s1 if ch.isdigit()]
    total = sum(digits)
    average = total / len(digits) if digits else 0
    return total, average


if __name__ == '__main__':
    s1 = input("Enter a string: ")
    total, average = digit_sum_and_average(s1)
    print("Sum:", total)
    print("Average:", average)

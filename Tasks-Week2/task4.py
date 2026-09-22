def strings_to_lists(strings):
    return list(map(list, strings))


if __name__ == '__main__':
    words = ['cat', 'dog', 'bird']
    print(strings_to_lists(words))

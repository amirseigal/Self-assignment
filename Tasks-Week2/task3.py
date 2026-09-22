def sort_dicts(dicts):
    return sorted(dicts, key=lambda d: d['color'])


if __name__ == '__main__':
    cars = [
        {'make': ' Google ', 'model': 216, 'color': 'Black'},
        {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
    ]
    print(sort_dicts(cars))

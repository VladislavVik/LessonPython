my_list = [(-5 + 0j)], 2, 3.4, None, True, \
          [5, 4], (4, 3, 4.3), {7: 'seven', 8: 'eight'}, \
          frozenset(), range(11), b'twelwe', bytearray(b'thirteen'), \
          zip(*[(17, 18), (19, 20), ('a', 'b')])

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")
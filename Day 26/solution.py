return_date = list(map(int, input().split()))
expected_date = list(map(int, input().split()))


if expected_date[2] > return_date[2]:
    print('0')
elif return_date[0] <= expected_date[0] and return_date[1] <= expected_date[1] and return_date[2] == expected_date[2]:
    print('0')
elif return_date[0] > expected_date[0] and return_date[1] == expected_date[1] and return_date[2] == expected_date[2]:
    print(15 * (return_date[0] - expected_date[0]))
elif return_date[1] > expected_date[1] and return_date[2] == expected_date[2]:
    print(500 * (return_date[1] - expected_date[1]))
else:
    print('10000')

def identify_min_and_max(data:list):
    minimum_value = data[0]
    maximum_value = data[0]

    for i in data:
        if i > maximum_value:
            maximum_value = i
        if i < minimum_value:
            minimum_value = i

    return (minimum_value, maximum_value)

print('This program will return min and max value as a tuple.')
start = int(input('Enter a starting value'))
end = int(input('Enter the value above higher bound. This value will be excluded.'))

print(identify_min_and_max(range(start, end)))
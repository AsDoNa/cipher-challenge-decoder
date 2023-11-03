def chi_squared(dataset:list,expected:list):
    if len(dataset) != len(expected):
        raise ValueError("INVALID DATASETS TO COMPARE")

    result = 0
    for i in range(len(dataset)):
        result += ((float(dataset[i])-float(expected[i]))**2 / float(expected[i]))

    return result

if __name__ == '__main__':
    # print(chi_squared([1.1,2.9,7.3], [1,3,7]))
    pass
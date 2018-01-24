def most_frequent(s):
    data = s.split()
    data_u = list(set(data))
    word_time = {}
    for item in data_u:
        word_time[item] = data.count(item)
    inv_dict = {}
    for key, val in word_time.items():
        inv_dict[val] = inv_dict.get(val, [])
        inv_dict[val].append(key)
    max_time = max(inv_dict.keys())
    result = min(inv_dict[max_time])
    return result


s = "I scream you scream we all scream for ice cream"
s2 = "cat bat mat cat bat cat bat"
s3 = "betty bought a bit of butter but the butter was bitter"


print(most_frequent(s3))

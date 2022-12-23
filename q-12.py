
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print("The orginal dictionary is:"+ str(sample_dict))
temp = min(sample_dict.values())
res = [key for key in sample_dict if sample_dict[key]== temp]
print("keys with minimum values are :" + str(res))
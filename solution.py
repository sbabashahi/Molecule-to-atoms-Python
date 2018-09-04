import re
  
def parse_molecule (formula):
    pattern = r'[A-Z][a-z]?'
    pattern2 = r'\d+'
    map_dict = {'(': ')', '{': '}', '[': ']'}
    i = 0 
    temp_dict = {}
    while i < len(formula):
        ss = re.match(pattern, formula[i:])
        if ss is not None:
            if ss.group(0).isalpha():
                i += len(ss.group(0))
                ss2 = re.match(pattern2, formula[i:])
                if ss2 is not None:
                    if ss2.group(0).isdigit():
                        i += len(ss2.group(0))
                        temp_dict[ss.group(0)] = int(ss2.group(0)) + temp_dict.get(ss.group(0), 0)
                    else:
                        temp_dict[ss.group(0)] = 1 + temp_dict.get(ss.group(0), 0)
                else:       
                    temp_dict[ss.group(0)] = 1 + temp_dict.get(ss.group(0), 0)
        elif formula[i] in map_dict:
            index = formula[i:].index(map_dict[formula[i]])
            temp_dict2 = parse_molecule(formula[i+1:i+index])
            i += index + 1 
            ss2 = re.match(pattern2, formula[i:])
            if ss2 is not None:
                if ss2.group(0).isdigit():
                    i += len(ss2.group(0))
                    for item in temp_dict2:
                        temp_dict2[item] *= int(ss2.group(0))
            for item in temp_dict2:
                temp_dict[item] = temp_dict2[item] + temp_dict.get(item, 0)
    return temp_dict

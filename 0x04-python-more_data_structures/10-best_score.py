#!/usr/bin/python3
def best_score(a_dict):
    if a_dict and len(a_dict):
        highest = list(a_dict.keys())[0]
        for key in a_dict:
            if a_dict[key] > a_dict[highest]:
                highest = key
        return highest
    return None

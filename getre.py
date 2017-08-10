import re

def get(reg,data):
    pagre = re.compile(reg)
    result = re.findall(pagre,data)
    return(result)
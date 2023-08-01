# PyDiscrd | Functions > Conversions






#Functions
def detectNone(item) -> bool:
    return item in [None, 'None']



def stringToBool(text: str) -> bool:
    if detectNone(text): return None
    return {'true' : True, 't' : True, 'false' : False, 'f' : False}.get(text.lower())



def stringToInteger(text: str) -> int:
    if detectNone(text): return None
    return int(text)
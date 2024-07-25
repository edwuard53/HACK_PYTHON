"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""
def mayuscula(palabra):
    result = palabra.upper()
    return result  

def conv(palabra):
    palabra = palabra.replace('o','0')
    palabra = palabra.replace('i','1')
    palabra = palabra.replace('a','@')
    return palabra  

def fn_hack_10():
    result = "fooziman"
    result = list(result)
    result = map(conv, result)
    result = list(result)
    result = map(mayuscula, result)
    result = list(result)
    return result

print(fn_hack_10())
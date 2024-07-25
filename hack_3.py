"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    result = "fooziman"
    result = result.title()
    return result

print (fn_hack_3())
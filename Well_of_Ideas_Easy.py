# For every good kata idea there seem to be quite a few bad ones!

# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or
# two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas,
# as is often the case, return 'Fail!'.
# def well(x):
#     if x.count('good') == 1 or x.count('good') == 2:
#         return "Publish!"
#     elif x.count('good') > 2:
#         return 'I smell a series!'
#     else:
#         return 'Fail!'

def well(x):
    x = ['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']
    tmp = [i for i in x if i == "good"]
    if len(tmp) == 1 or len(tmp) == 2:
        return 'Publish!'
    elif len(tmp) > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'

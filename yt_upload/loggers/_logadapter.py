def logadapter(*args, **kwargs):
    data = {}
    
    for item in args:
        data.update(item)
    
    for key, value in kwargs.items():
        data.update({key: value})
    
    return data 

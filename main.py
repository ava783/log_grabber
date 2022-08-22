def open_file(file):
    with open (file, 'r') as a:
        text=a.read()
    return(text)

def minute(log):
    sp=" ".join(log.split()).split(' ')
    minute=int(sp[1].split(':')[1])
    return(minute)

def value(log):
    sp=" ".join(log.split()).split(' ')
    value=str(sp[2])
    return(value)

def construct_dict(text):
    result=set()
    dictionary={}
    for z in text.replace('\n\n', '\n').split('\n'):
        result.add(minute(z))
    for i in result:
        dictionary[i]=0
    return(dictionary)

def main(file):
    text=open_file(file)
    dict=construct_dict(text)
    for z in text.replace('\n\n', '\n').split('\n'):
        if 'NOK' in value(z):
            dict[minute(z)]+=1
    print(dict)

if __name__ == '__main__':
    main('events.log')

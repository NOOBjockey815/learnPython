l = [1,2,'aasf','1','123',123]
def filter_list(l):
    a = []
    for i in l:
        try:
            if i == int(i):
                a.append(i)
        except:
            continue
    print(a)

filter_list(l)

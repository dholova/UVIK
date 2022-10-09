def read_csv():
    with open('data.csv') as file:
        w, e, r, u = [], [], [], []

        a = file.readline().split(',')

        b = [[j.strip() for j in i.split(',')] for i in file]
        
        w = [i[0] for i in b if i[0] not in w]

        for i in w:
            for j in b:
                if j[0] == i:
                    e.append(j[1])
            r.append(e)
            e = []
        for i in r:
            t = dict(zip(['people'], [i]))
            o = dict(zip(['count'], str(len(i))))
            p = t | o
            u.append(p)
        s = dict(zip(w, u))

        print(s)


read_csv()

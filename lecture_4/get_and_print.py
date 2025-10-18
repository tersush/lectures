a: list = [1,2,3,4,3,3,3] #меняется
a.append(23) #insert 23
a.pop(1) #delete value from index 1
a.remove(3) #deletes first left 3
print(a)



b: tuple = (3,4,10, 'super')
c1: set = {'how','now','never','che'}
d1: dict = {1: 'got', 2:'top', 3:'sup'}
d2:  dict = {'perviy': '1', 'vtoroy': 2}

c2: set = {'lalala','bla bla','how','now'}

a[-1]= 11
print(a)

#b[2]['super']='ne super'
print(b)

print(len(a),
      sum(a),
      sorted(a))

print(c1.intersection(c2))
print(c1.difference(c2))
print(c2.difference(c1))
print(c1 | c2)
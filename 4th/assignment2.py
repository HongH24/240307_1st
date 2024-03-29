#%% Q3
print('[ assignment2-Q3 ]')
def plus(v1,v2,v3):
    result = 0
    result = v1+v2+v3
    return result
    
hap = plus(100,200,300)
print(hap)
print('\n')

## (1) v1,v2,v3  (2) return result

#%% Q4
print('[ assignment2-Q4 ]')
def f1():
    print(var)
def f2():
    var=10
    print(var)
var=100
f1()
f2()

## guess : 100, 10
## answer : 100, 10
print('\n')

#%% Q11
print('[ assignment2-Q11 ]')
def addNumber(num):
    snum=0
    for i in range(1,num+1):
        snum += i
    print(snum)
print(addNumber(100))
print('\n')

## answer >> def complete the blank


#%% Q8
print('[ assignment1-Q8 ]')
def myFunc(p1=1,p2=2,p3=3):
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 ==> ", myFunc())
print("매개변수 1개로 호출 ==> ", myFunc(1))
print("매개변수 2개로 호출 ==> ", myFunc(1,2))
print("매개변수 3개로 호출 ==> ", myFunc(1,2,3))

## answer >> p1=1,p2=2,p3=3

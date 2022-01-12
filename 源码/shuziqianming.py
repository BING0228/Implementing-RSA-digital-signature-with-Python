import random
import math
import zhiyao as zy
#确定素数
def isPrime(num):
    if (num < 2):
        return False
    else:
        i = 2
        flag=True
        while i < num:
            # 如果num能被i整除，说明num不是质数
            if num % i == 0:
                # 只要num不是质数，将flag的值修改为 False
                flag = False
            i += 1
        return  flag
#大质数生成
def randPrime(n):
    rangeStart = 10 ** (n-1) #10**4
    rangeEnd = (10 ** n) - 1  #10**5-1
    while True:
        num = random.randint(rangeStart, rangeEnd)  #返回rangestart到rangeend任意一个数
        if isPrime(num): #判断是否是质数，如果是则生成
            return num
#扩展欧几里得算法，求逆元
def liyuan(a, n):
    x1, x2, x3 = 1, 0, n
    y1, y2, y3 = 0, 1, a
    while y3 != 1 and y3 != 0 and y3 > 0:
        Q = math.floor(x3 / y3)
        t1, t2, t3 = x1 - Q * y1, x2 - Q * y2, x3 - Q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if y3 == 0:
        return 0
    if y3 == 1:
        if y2 >0:
            return y2
        else:
            return n+y2

#寻找与f互质整数e
def randGcd1(b):
    rangeStart = 2
    rangeEnd = b - 1
    while True:
        num = random.randint(rangeStart, rangeEnd)
        if oujilide(num, b) == 1: #利用欧几里算法，如果值等于1，那么这个两个数互质
            return num
#欧几里得算法
def oujilide(a,b):
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    while True:
        if y == 0:
            return x
        else:
            r = x % y
            x = y
            y = r
#从数字幂快速搜索模块
def power(x, n, mod):  #x**n mod mod
    if n == 0:
        return 1
    elif n % 2 == 0:
        p = power(x, n / 2, mod)
        return (p * p) % mod
    else:
        return (x * power(x, n - 1, mod)) % mod
#D、E和N的密钥生成
def generatePublicAndSecretKeys(size = 5):
    p, q = randPrime(size), randPrime(size) #生成一对不相等且足够大的质数
    N = p * q #计算p、q的乘积
    f = (p - 1) * (q - 1) #计算n的欧拉函数
    e = randGcd1(f) #选出一个与f互质的整数e
    d = liyuan(e, f)#计算出e对于f的模反元素d  de mod f =1
    keys = {'d' :  d, 'e' : e, 'n' : N} #得出公钥与私钥
    return keys
#SHA256算法得到消息摘要
def hashing(M, size = 5):
    aa=zy.Sha256sum(M) #得到哈希值
    cc=int(aa, 16) % 10 ** (size * 2 - 2)#将哈希值转化为整型
    return cc
#将消息摘要进行签名
def signMessage(M, d, N):
    s = power(M, d, N) #使用私钥签名 hashM**d mod N 得到签名内容
    return s
#将得到
def verifySign(s, e,n):
    w = power(s, e, n)
    return w

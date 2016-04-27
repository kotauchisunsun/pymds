#coding:utf-8
import numpy as np
"""
よくわかる解説
http://yuki-koyama.hatenablog.com/entry/2015/07/13/015736
"""

def mds(s,dim):
    n = len(s)
    h = np.eye(n, dtype=float) - 1.0 / n

    b = - 1.0 / 2.0 * h.dot(s).dot(h)
    la,v =  np.linalg.eig(b)
    d = (((la * (la > 0 ))**0.5) * np.eye(n)).dot(v.T)
    idx = range(n)
    idx.sort(key=lambda i:(la[i] > 0) * -la[i].real)

    #print la
    #print idx

    pos = []
    for i in range(dim):
        pos.append(d[idx[i]].real)

    return np.array(pos).T

if __name__=="__main__":
    #pos = np.array([ 1 , 2, 3 ])
    #pos = np.array(range(1001))
    pos = np.random.random_sample( (5,10001))

    #距離は常に２乗で持つ
    s = np.array(
       [
           [
               np.linalg.norm(i-j) ** 2
               for j
               in pos
           ]
           for i
           in pos
       ]
    )

    print s

    print mds(s,2)


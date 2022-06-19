import pdb
def intersection(start1,end1,start2,end2):
    k1 = (end1[1]-end1[0])/(start1[1]-start1[0])
    k2 = (end2[1]-end2[0])/(start2[1]-start2[0])
    p1_x =max(start1[0],start2[0])
    p2_x =min(start1[1],start2[1])
    def a_line(x,k,x0,y0):
        return k*(x-x0) + y0
    if p1_x - p2_x > 1:
        return []
    if k1 == k2:
        if end2[0] == a_line(start2[0],k1,start1[0],end1[0]):
            return [p1_x,a_line(p1_x,k1,start1[0],end1[0])]
        else:
            return []
    elif k1 != k2:
        xx = (k2*start2[0]-k1*start1[0]+end1[0]-end2[0])/(k2-k1)
        if xx >= p1_x and xx <= p2_x:
            return [xx,a_line(xx,k1,start1[0],end1[0])]
        else:
            return []



if __name__ == "__main__":
    start1 = [0,1]
    end1 = [0,0]
    start2 = [0,1]
    end2 = [-1,1]
    print(intersection(start1,end1,start2,end2))


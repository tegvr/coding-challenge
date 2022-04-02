# import resource
import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)


def cellCheck(wilayah,visited,cekFaksi,xj,yk,row,col): #x=M (char) y=N(lines)
    if (xj < 0 or xj >= row):
        return
    # if (yj < 0 or yj >= row):
        return
    if (yk < 0 or yk >= col):
        return
    # if (xk < 0 or xk >= col):
    #     return

    # if visited[xk][yj] == True:
    #     return
    # visited[xk][yj] = True

    if visited[xj][yk] == True:
        return
    visited[xj][yk] = True
    
    if wilayah[xj][yk] == "#":
        # print("Ketemu #")
        return

    if wilayah[xj][yk] != ".":
        cekFaksi.append(wilayah[xj][yk])
        # print("Xnemu ")
        # return
    # elif wilayah[xj][yk] == ".": print("ketemu titik")
    
    #movement
    # print("move down")
    cellCheck(wilayah,visited,cekFaksi,xj,yk+1,row,col) #right
    # print("move up")
    cellCheck(wilayah,visited,cekFaksi,xj,yk-1,row,col) #left
    # print("move right")
    cellCheck(wilayah,visited,cekFaksi,xj+1,yk,row,col) #up
    # print("move left")
    cellCheck(wilayah,visited,cekFaksi,xj-1,yk,row,col) #down

    return

if __name__ == '__main__':
    faksi = {}
    cekFaksi = []

    T = int(input(""))
    for xt in range(T):
        faksi.clear()
        N = int(input("")) #lines
        M = int(input("")) #characters
        
        wilayah = [[0 for xx in range(M)] for yy in range(N)]
        visited = [[0 for xx in range(M)] for yy in range(N)]

        for xrow in range(N):
            user_input_txt = input("")
            if len(user_input_txt) == M:
                for j in range(M):
                    wilayah[xrow][j] = user_input_txt[j]
                    visited[xrow][j] = False

        constraints = (1<=T<=100 and 1<=N<=100 and 1<=M<=100)

        if constraints :
            contested = 0
            # print(cekFaksi)
            for j in range(N) :
                # print(cekFaksi)
                for k in range(M):
                    cekFaksi.clear()
                    # print("attem j k = {0}-{1}-{2}".format(j+1,k+1,visited[j][k]))
                    cellCheck(wilayah,visited,cekFaksi,j,k,N,M)
                    
                    # print(cekFaksi)
                    cekFaksiStr = ''.join(cekFaksi)
                    if len(cekFaksi) > 1 :
                        if(len(set(cekFaksi)) == 1):
                            cekFaksiDouble = ''.join(cekFaksi[0])
                            if cekFaksiDouble in faksi:
                                faksi[cekFaksiDouble] +=1
                            else :
                                key = cekFaksiStr[0]
                                faksi[key] = 1
                        else:
                            contested+=1
                        # print("Contested is? {0}".format(cekFaksiStr))
                    elif len(cekFaksi) == 1:
                        if faksi :
                            if cekFaksiStr in faksi:
                                # print("2.Update faksi {0}".format(cekFaksiStr))
                                faksi[cekFaksiStr] +=1
                        
                            else :
                                # print("1.1 add faksi {0}".format(cekFaksiStr))
                                faksi[cekFaksiStr] = 1
                        else :
                            # print("1.add faksi {0}".format(cekFaksiStr))
                            faksi[cekFaksiStr] = 1
                    

        numberCase = xt +1
        print("Case {0}:".format(numberCase))
        sortedFaksi = dict(sorted(faksi.items()))
        for x,y in sortedFaksi.items():
            print("{0} {1}".format(x,y))
        
        print("contested {0}".format(contested))
        # print(visited)
        
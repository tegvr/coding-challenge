# import resource
import sys
# print(sys.getrecursionlimit())
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10000)


def cellCheck(wilayah,visited,cekFaksi,xk,yj,row,col): #x=M (char) y=N(lines)
    
    cekMove(wilayah,visited,cekFaksi,xk+1,yj,row,col)
    cekMove(wilayah,visited,cekFaksi,xk-1,yj,row,col)
    cekMove(wilayah,visited,cekFaksi,xk,yj+1,row,col)
    cekMove(wilayah,visited,cekFaksi,xk,yj-1,row,col)


def cekMove(wilayah,visited,cekFaksi,xk,yj,row,col):
    if (xk < 0 or xk >= row):
        return
    if (yj < 0 or yj >= col):
        return
    
    if visited[xk][yj] == True:
        return
    visited[xk][yj] = True
    if wilayah[xk][yj] == "#":
        return
    if wilayah[xk][yj] != ".":
        # print("Wilayah {0} added".format(wilayah[xk][yj]))
        cekFaksi.append(wilayah[xk][yj])
        # return cekFaksi


if __name__ == '__main__':
    faksi = {}
    cekFaksi = []

    T = int(input(""))
    for xt in range(T): #xt : cases
        # print("Start no. {0}".format(xt+1))
        faksi.clear()
        N = int(input("")) #lines
        M = int(input("")) #characters
        
        wilayah = [[0 for xx in range(M)] for yy in range(N)]
        visited = [[0 for xx in range(M)] for yy in range(N)]

        for x in range(N):
            user_input_txt = input("")
            if len(user_input_txt) == M:
                for j in range(M):
                    wilayah[x][j] = user_input_txt[j]
                    visited[x][j] = False
            
            # else:
            #     break
        # print("CHECKING T {0}".format(T))
        # constraints = (1<=T<=100 and 1<=N<=100 and 1<=M<=100)
        constraints = 1
        if constraints :
            contested = 0
            
            for j in range(N) :
                # print("j {0}".format(faksi))
                for k in range(M):
                    cekFaksi.clear()

                    cellCheck(wilayah,visited,cekFaksi,k,j,N,M)
                    
                    cekFaksiStr = ''.join(cekFaksi)
                    # print("cekfaksi")
                    # print(cekFaksi)
                    if len(cekFaksi) > 1 :
                        # print("Contested bertambah {0}".format(contested+1))
                        contested+=1
                    elif len(cekFaksi) == 1:
                        # print("Add/update faksi")
                        # print(cekFaksiStr)
                        if faksi :
                            if cekFaksiStr in faksi:
                                # print("2.update faksi {0}".format(cekFaksiStr))
                                faksi[cekFaksiStr] +=1
                            # print("faksiada")
                            else :
                                # print("1.1.add faksi {0}".format(cekFaksiStr))
                                faksi[cekFaksiStr] = 1
                        else :
                            # print("1.add faksi {0}".format(cekFaksiStr))
                            faksi[cekFaksiStr] = 1
                    # print(faksi)
                        

        # else: break
        numberCase = xt +1
        print("Case {0}:".format(numberCase))
        sortedFaksi = dict(sorted(faksi.items()))
        # sortedFaksi = faksi
        for x,y in sortedFaksi.items():
            # x.strip()
            
            print("{0} {1}".format(x,y))
            # print("cek faksi {0}".format(cekFaksi))
        
        # print(cekFaksi)
        print("contested {0}".format(contested))
        # print("this is no. {0}".format(xt+1))
        
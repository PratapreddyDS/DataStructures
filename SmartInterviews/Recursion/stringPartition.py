# Enter your code here. Read input from STDIN. Print output to STDOUT



def partition(orgnl, sbstr, start, idx, grp, result, final):
    print("first",start,result)

    if ''.join(result) == orgnl:
        print(result)
        final.append(result)
        return
    
    if idx == len(orgnl):
        return

        
    for j in range(start,len(orgnl)):
        sbstr = orgnl[start:j+1]
        # print("second",sbstr,start,j)
        idx += 1
        if sbstr in grp:
            result.append(sbstr)
            print('third',result)
            partition(orgnl, sbstr, j+1, idx, grp, result, final)
            print("check",result)
            ele = result.pop()
            # partition(orgnl, sbstr, j+1-(len(ele)), idx, grp, result, final)



            # print('After pop', result)
            # partition(orgnl, sbstr, j+1, idx, grp, result, final)
        # else:
        #     if idx == len(orgnl):
        #         if result:
        #             result.pop()



orgnl = "smartinterviews"
grp = ['smart', 'inter', 'sm', 'art', 's', 'mart', 'view', 'views', 'int']
result = []
final = []
sbstr = ''
    
partition(orgnl, sbstr, 0, 0, grp, result, final)

        


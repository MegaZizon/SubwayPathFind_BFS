import csv

def addVer(adj, st, dest):   #인접리스트에 역을 추가한다

    stPass=True
    destPass=True
    for i in range(len(adj[st])): # 해당역 처리
        if(adj[st][i]==dest):  #dest 값이 해당 인접리스트에 이미 있을 경우
            stPass=False       #False로 처리해서 추가하지 못하도록 설정
    if(stPass==True):          #dest 값이 해당 인접리스트에 없다면
        adj[st].append(dest)   #인접리스트에 추가

    for i in range(len(adj[dest])): # 인접역 자동 인접처리
        if(adj[dest][i]==st):  #st 값이 해당 인접리스트에 이미 있을 경우
            destPass=False      #dest 값이 해당 인접리스트에 이미 있을 경우
    if(destPass==True):         #dest 값이 해당 인접리스트에 없다면
        adj[dest].append(st)   #인접리스트에 추가


def BFS(adj, start, dest, v, prev): #너비 우선 탐색

    queue = []                          #큐를 대신할 리스트queue 선언
    visited = [False for i in range(v)] #방문노드 처리

    for i in range(v):                  #거리에 무한, 선행자역 리스트에  -1값 입력  
        prev[i] = -1

    visited[start] = True;            #시작역 방문처리
    queue.append(start);              #큐에 추가

    while (len(queue) != 0):        #큐안에 아무것도 없을때까지
        u = queue[0];               #큐를 pop에서 해당역을 u에 저장
        queue.pop(0);               #큐 pop 처리 
        for i in range(len(adj[u])): #정점(역) u 의 모든 인접리스트를 방문 처리하기 위해 반복문 선언
            
            if (visited[adj[u][i]] == False): #u가 현재 방문한 정점(역,i) 이 방문하지 않은 정점(역)이라면 
                visited[adj[u][i]] = True     #u가 현재 방문한 정점(역,i) 방문처리
                prev[adj[u][i]] = u           #u가 현재 방문한 정점(역,i)을 방문한 노드는 u로 설정
                queue.append(adj[u][i]);      #u가 현재 방문한 정점(역,i)을 큐에 추가
                
                if (adj[u][i] == dest):       #u가 현재 방문한 정점(역,i)이 목적지 라면
                    return                    #탐색 종료
    return

def printStation(adj, start, dest, v):
    prev=[0 for i in range(v)]  #역을 호출한 선행 역의 값을 저장
    
    BFS(adj, start, dest, v, prev) #너비 우선 탐색 시작
        
    path = []                   #BFS탐색을 하면서 목적지를 찾기 전까지 그 역을 직전에 호출한 선행 역들의 값들을 담기 위한 리스트
    dest2 = dest
    path.append(dest2)           #목적지를 리스트[path]에 추가
    while (prev[dest2] != -1):   #BFS 탐색을 하면서 저장해두었던 선행 역이 -1이 아닐 동안
        path.append(prev[dest2]) #해당 역의 을 호출한 선행역 값 리스트[path]에 추가
        dest2 = prev[dest2]      #선행역의 인덱스로 변수 재설정

    count=0
    isStart=0
    queue1=[]
    queue2=[]
    queue3=[]
    queue4=[]
    cnt=0
    
    for i in range(len(path)-1, -1, -1): #출발역부터 도착역까지 반복 path의 출발역은 마지막인덱스,
                                         #마지막역은 첫번째 인덱스이기 때문에 -1씩 감소연산
                        
        TempAr=station[path[i]].split('/')  #현재 역 출력을 위한 연산
        TempAr2=TempAr[len(TempAr)-1].split(',')
        
                                           ####환승 처리 부분####
        if(isStart==0):                   #처음 실행했을때 주변역 정보 Queue1에 추가
            for j in range(len(TempAr2)):
                queue1.append(TempAr2[j]) #Queue1 - 이전역의 주변역정보 Queue2 - 현재역의 주변역정보
                                          #Queue3 - Queue1과 2를 바탕으로 이전노선에서 현재로올때 탑승한 노선 정보
            isStart+=1
            
        elif(isStart==1):                 #두번 실행됐을때 Queue1과 Queue2 바탕으로 현재역까지 타고온 노선Queue3에 저장
            queue2=TempAr2
            for j in range(len(queue1)):
                for k in range(len(queue2)):
                    if(queue1[j]==queue2[k]):
                        queue3.append(queue1[j])
                        if(queue1[j] == 'A'):
                            print(" - [탑승] 2호선외부순환선\n")
                        else:
                            print(" - [탑승] {}호선\n".format(queue1[j]))                                                            
            queue1=[]   
            queue1=queue2
            isStart+=1
            
        else:       #세번이상(역 3개를 거침) 실행됐을때 환승이라면
                    #Queue1과 Queue2 바탕으로 현재역까지 타고온 노선을
                    #Queue4에 저장하고 Queue3에있는값과 비교
            queue2=[]
            queue2=TempAr2
            twobreak=False
            
            for j in range(len(queue1)):
                for k in range(len(queue2)):
                    if(queue1[j]==queue2[k]):
                        queue4.append(queue1[j])
                            
            for j in range(len(queue3)):
                for k in range(len(queue4)):
                    if(queue3[j]!=queue4[k]):   #쭉 타고온 노선과 현재 노선이 다르다면 Queue3 pop 후 Queue3에 값 추가
                        if(queue3[j] == 'A'):
                            print("               [환승] 2호선외부순환선→{}호선".format(queue4[k]))
                        elif(queue4[k] == 'A'):
                            print("               [환승] {}호선→2호선외부순환선".format(queue3[j]))
                        else:
                            print("               [환승] {}호선→{}호선".format(queue3[j],queue4[k]))           
                        queue3=[]
                        queue3.append(queue4[k])
                        twobreak=True
                        queue4=[]
                        cnt +=1
                        break
                if (twobreak==True):
                    break;
                
            queue1=[]   
            queue1=queue2
            isStart+=1
        ###역 출력###
        if(count==0):
            print("\n###################################\n\n출발:{}".format(TempAr[0]),end="")
            
        elif(count==len(path)-1):
            print("{}번째 정거장 : {} ".format(count,TempAr[0]))
            print("\n도착:{}".format(TempAr[0]))
            print()
        else:
            print("{}번째 정거장 : {} ".format(count,TempAr[0]),end="")                     
            print()
        count+=1
    print("{}개역 환승{}회\n###################################".format(count-1,cnt))

        
        
def findVertex(vertex):         #String 문자열 역 정점의 인덱스를 찾는 함수
    for i in range (0,v):
        if vertex in station[i]:
            TempArr3=station[i].split('/')
            if(TempArr3[0]==vertex):
                return i
            
    return 9999
#########################################################Main Funtion########################################################
                
f = open('Station_List.csv','r') #csv 파일을 불러온다 
rdr = csv.reader(f)
station=[]
for line in rdr:
    station.append(line[0]) #리스트[station] 에 파일내용을 저장한다.
                            #[staion] 열의 의미!!!
                            #슬래시("/") 로 나누어져있으며
                            #맨 처음 슬래시가 나오기 전의 내용은 하나의 역 이름
                            #맨 뒤에 슬래시가 나오기 전의 내용은 해당 역과 연결되어있는 역
                            #맨 뒤에 슬래시 이후 마지막 내용은 해당역의 노선 느낌표는 환승역 ex)1 - 1호선, ex)! - 환승역
                            #Example) 건대입구/뚝섬유원지/구의/어린이대공원/성수/!
                            #         ┖정점   ┖   인   접   리   스   트   ┛  ┖ 환승역 
                            #Example) 뚝섬유원지/건대입구/청담/2
                            #         ┖정점   ┖인접리스트┛  ┖ 뚝섬유원지의 노선
                            #한번 인접해있다고 선언하면 인접역은 자동으로 연결처리됨
                            #Example) 뚝섬유원지/건대입구/청담/2 → 건대입구와 청담은 프로그램에서 자동으로 인접처리 그러나 
                            #                                       역 선언은 해야함 Example)청담/2 하면
                            #                                       자동으로 청담/뚝섬유원지/2 처리
f.close()

v = len(station)              #v는 정점의 개수

adj = [[] for i in range(v)]; #정점의 개수만큼 인접리스트 배열 [adj] 생성

for i in range (0,v):
    TempArr=station[i].split('/')           #리스트[station] 에 i번째줄을 슬래시로 나누어 TempArr배열에 저장 
    for j in range (0,v):
        if TempArr[0] in station[j]:        #리스트[station] 에 해당 역(슬래시의 이전의 가장 첫 내용=TempArr[0])이 쓰여진 String이 있다면
            TempArr2=station[j].split('/')  #리스트[stationn 의 j번째 인덱스를 다시 TempArr2에 슬래시로 나누어 저장 이유는 4행아래에 기술
            for k in range(0,len(TempArr2)):
                if(TempArr[0]==TempArr2[k]):#TempArr2 내용중 TempArr의 역이 나온다면
                    addVer(adj, i,j)        #간선에 추가
                    break                   #"동인천" 과 "인천" 역이 있을떄 인천역으로 간선에 추가한다면 동인천도 같이 간선이
                                            #추가되기때문에 리스트[station]을 다시 쪼개어서 완벽하게 문자열이 일치해야 추가되도록 하기 위함


adj[303]=[159,303]          #특이한 역 정점 수동처리(6호선 연신내 부분)
adj[304]=[158,304]
adj[305]=[302, 305]
adj[158]=[157, 158, 159, 305]
adj[159]=[158, 159, 160, 304]

while(True):
    print("\n**************MENU*****************"
          +"\n1.지하철경로탐색 \n2.종료\n**************MENU*****************\n")
    print("메뉴 입력:",end="")
    menu=input()
    
    if(menu=="2"):
        print("종료합니다.")
        break
    elif(menu=="1"):
        print("\n출발역을 입력하세요.\n")
        print("출발역 입력:",end="")
        START=input()
        if(9999==findVertex(START)):
            print("해당역이 없습니다.\n")
            continue
        print("\n도착역을 입력하세요.\n")
        print("도착역 입력:",end="")
        DESTINATION=input()
        if(9999==findVertex(DESTINATION)):
            print("해당역이 없습니다.\n")
            continue
        start=findVertex(START)
        finish=findVertex(DESTINATION)
        printStation(adj, start, finish, v);
    else:
        print("잘못된 입력입니다.")




                    
        

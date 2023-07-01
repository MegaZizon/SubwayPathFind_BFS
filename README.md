# SubwayPathFind_BFS
지하철 최단경로 찾기 (BFS)


## 🖥️ 프로젝트 소개
지하철 노선도 최단거리를 찾는 프로그램 입니다.
<br>

### ⚙️ 개발 환경
- `Python3`

## 📌 주요 기능
#### 출발역과 도착역 입력시 사이구간 역과 환승노선 출력

<br>

## 🗝️ 사용 기술 
<details><summary><h4>BFS 알고리즘을 이용하여 최단경로 찾기</h4> </summary>

<!-- summary 아래 한칸 공백 두어야함 -->
```
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
```
</details>
<details><summary><h4>환승이 필요한 경우 환승노선 출력</h4> </summary>

<!-- summary 아래 한칸 공백 두어야함 -->
```
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
```
</details>

</details>
<details><summary><h4> <a href="https://data.seoul.go.kr/index.do">서울열린데이터광장<a>에서 제공하는 서울교통공사_노선별 지하철역 정보 CSV 파일 사용</h4> </summary>

<!-- summary 아래 한칸 공백 두어야함 -->
```
import csv
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
```
</details>

## 🚩 구현 결과

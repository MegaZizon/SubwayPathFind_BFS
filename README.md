# SubwayPathFind_BFS
지하철 최단경로 찾기 (BFS)


## 🖥️ 프로젝트 소개
지하철 노선도 최단거리를 찾는 프로그램 입니다.
<br>

### ⚙️ 개발 환경
- `Python3`

## 📌 주요 기능
#### 출발역과 도착역 입력 
<details>
  <summary><h4>BFS 알고리즘을 이용하여 최단경로 찾기</h1> </summary>

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



#### 환승이 필요한 경우 - <a href="https://github.com/chaehyuenwoo/SpringBoot-Project-MEGABOX/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(Member)" >상세보기 - WIKI 이동</a>
- 주소 API 연동
- 회원정보 변경

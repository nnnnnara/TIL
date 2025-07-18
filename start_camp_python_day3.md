### Git / Git Hub 복습
1. 조장은 홈 디렉토리에 word-ralay 폴더 생성
2. 조장은 github에 word-relay 원격 저장소 생성 및 로컬 저장소와 연결
3. 조장은 로컬 저장소에 README.md 파일과 .gitignore파일을 생성하고 push
4. 조장은 원격 저장소의 collaborator로 조원을 초대하기
    (조장: github 해당 repository -> setting -> collaborators -> add people -> 각 조원들 email or username 입력 후 초대)
    (조원: 각자 이메일에 들어가 조장의 초대를 승낙하기)
5. 조원들은 해당 레포 clone 하기
---
5번까지 각 팀원들도 모두 진행

---

1. 조장과 조원은 add, commit, push, pull을 이용해서 끝말잇기를 진행
2. 규칙)
   1. 순서는 팀 내에서 알아서 정하기
   2. 자신이 끝말잇기 작성 후 push, push 완료 후 완료한 사실을 팀원에게 공유 (README.md에 작성한다.)
   3. 전체 6바퀴 돌면 상황 종료
   4. 전체 6바퀴가 돈 이후에도 연습을 한다면, 순서를 뺏거나 데이터를 섞어서 conflict를 유발하면서 여러가지 실험을 하는 것도 추천!

처음 생성
```[python]
cd ~
mkdir word-relay
cd word-relay
git init
touch README.md
touch .gitignore
git add README.md
git commit -m "first"
git remote add origin #주소
git push origin master
```
조원이 처음 받을 때 (clone)
```[python]
git clone #주소
git add origin
git commit -m "second"
git push origin master
```
주고 받을 때 (push & pull)
```[python]
git pull origin master
git add README.md
git commit -m "third"
git push origin master
```

# 1.  ChatGPT
### Generative AI
오디오, 비디오, 이미지, 텍스트, 코드, 시뮬레이션 등의 새로운 콘텐츠르 생성하는 인공지능 모델
-> 최근 언어 및 이미지 분석에서 큰 파급력을 보임


# 2. API

# 3. Prompt Engineering

# 4. Vibe Coding
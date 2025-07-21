# Start Camp Day2. Python
### 지난 시간
- CLI
- MarkDown
- Git : 분산 버전 관리 시스템
  - git add, git commit, git status, git log

CLI 복습하기
1. 홈 디렉토리로 이동하기
   ```[python]
   cd ~
   ```
2. Practice 디렉토리 생성하기
    ```[python]
    mkdir practice
    ```
3.  Practice 안에 Practice_Folder 디렉토리 생성하기
    ```[python]
    cd practice
    
    mkdir Practice_Folder
    ```
4. Practice 디렉토리 안의 디렉토리 및 파일 출력하기
    ```[python]
    ls
    ```
5. Practice 디렉토리에서 practice_file.txt파일 생성하기
    ```[python]
    touch practice_file.txt
    ```
6. practice_file.txt를 copy_practice_file.txt로 복사하기
    ```[python]
    cp -r practice_file.txt copy_practice_file.txt
    ```
7. copy_practice_file.txt를 PracticeFolder로 위치를 변경하고, 이 때 이름을 moved_practice_file.txt로 변경하기
    ```[python]
    mv copy_practice_file.txt Practice_Folder/moved_practice_file.txt```
8.  Practice 디렉토리의 practice_file.txt 파일 삭제하기
    ```[python]
    rm practice_file.txt
    ```
9. Practice_Folder 디렉토리 삭제하기
    ```[python]
    rm -r Practice_Folder
    ```
10. Practice 디렉토리 삭제하기
    ```[python]
    cd ..
    rm -r Practice
    ```

GIT 연습하기 : Git Status, Log, Add, Commit 연습하기
1. myFolder 라는 디렉토리를 만들고, Git 초기화 진행
    ```[python]
    mkdir myFolder
    git init
    ```
2. myFolder 디렉토리로 이동 후, test.py 파일을 만드세요
    ```[python]
    cd myFolder
    touch test.py
    ```
3. test.py 를 staging area로 추가하세요
    ```[python]
    git add test.py
    ```
4. first commit이라는 커밋명으로 커밋을 추가하세요
   ```[python]
   git commit -m "first commit"
   ```
5. InnerFolder라는 디렉토리를 만들고 디렉토리 내부에 test2.py와 test3.py, test4.py 파일을 생성하세요
   ```[python]
   mkdir InnerFolder
   cd InnerFolder
   touch test2.py test3.py test4.py
   ```
6. InnerFolder 안의 test2.py를 staging area로 추가한 뒤 second commit이라는 커밋을 추가하세요
   ```[python]
   git add test2.py
   git commit -m "second commit"
   ```
7. InnerFolder 안에서 커밋에 추가되지 않은 나머지 파일을 third commit으로 커밋을 추가하세요
   ```[python]
   git add test3.py test4.py
   git commit -m "third commit"
   ```
위 과정을 실행한 후 git status, git log 실행
```[python]
$ git status
On branch master
nothing to commit, working tree clean
```
```[python]
$ git log
commit 142787f5180b4ca38d6bf9d6ec026ee86e926e57 (HEAD -> master)
Auther: nara <snls369527@gmail.com>
Date:   Thu Jul 17 11:29:45 2025 +0900

    third commit

commit 6fa79c823a074a375a1b7f7da1d094ed5085909e
Auther: nara <snls369527@gmail.com>
Date:   Thu Jul 17 11:29:08 2025 +0900

    second commit

commit 2a028b1552d08d7020cbaa383235b1517beaa02
Auther: nara <snls369527@gmail.com>
Date:   Thu Jul 17 11:27:25 2025 +0900

    first commit

```

- 잘못 만든 git 초기화(원상복귀)
    ```[python]
    rm -rf .git
    ```

### 오늘 수업
  git commit 실습

1. 바탕화면에 git_commit 폴더를 만들고 git 저장소 생성
```[python]
mkdir git_commit
cd git_commit
git init
```
2. 해당 폴더 안에 a.txt라는 텍스트 파일을 만들고, "add a.txt"라는 커밋 메세지로 커밋 생성
```[pythod]
touch a.txt
git add a.txt
git commit -m "add a.txt"
```
3. 이번에는 b.txt라는 텍스트 파일을 만들고, "add b.txt"라는 커밋 메세지로 커밋 생성
   ```
   touch b.txt
   git add b.txt
   git commit -m "add b.txt"
   ```
4. a.txt파일을 수정하고, "update a.txt"라는 커밋 메세지로 커밋 생성
   ```
   git add a.txt
   git commit -m "update a.txt"
   ```
5. 커밋 목록 확인하기
    ```
    $ git log
    commit ~ (HEAD -> master)
    Auther: nara <snls369527@gmail.com>
    Date:   Thu Jul 17 11:51:46 2025 +0900

        update a.txt

    commit ~ 
    Auther: nara <snls369527@gmail.com>
    Date:   Thu Jul 17 11:49:30 2025 +0900ㄴ

        add b.txt

    commit ~ 
    Auther: nara <snls369527@gmail.com>
    Date:   Thu Jul 17 11:48:55 2025 +0900

        add a.txt
    
    ```

- git 기타 명령어
  - git status : 현재 로컬 저장소의 파일 상태 보기
  - git log : commit history 보기
  - git log --oneline : commit 목록 한 줄로 보기
  - git config --global -l : git global 설정 정보 보기

- git init 주의사항
  - git 로컬 저장소 내에 또 다른 git 로컬 저장소를 만들지 말 것

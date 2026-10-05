# 📚 ROKEY1151_Bootcamp_Study
> **ROKEY 부트캠프 11기 5반-1조** 스터디용 Repository입니다.

---

## 📌 ROKEY 스터디 Git 가이드 및 제출 규칙

### 1. Git 가져오기 (Clone)
`rokey/py_work` 디렉토리에서 원격 저장소를 로컬로 가져옵니다.

```bash
cd C:/rokey/py_work
git clone [https://github.com/jhc1000/ROKEY1151_Bootcamp_Study.git](https://github.com/jhc1000/ROKEY1151_Bootcamp_Study.git)
```

### 2. 추가/변경 후 git에 올리기
```bash
# ROKEY1151_Bootcamp_Study 폴더로 이동
cd ./ROKEY1151_Bootcamp_Study
git init

# 모든 변경점 스테이징
git add .

# 커밋 및 원격 저장소 업로드
git commit -m "add changes into master"
git push origin master
```

### 3. 수업자료 연습문제 / 과제 코드 올리기
code_review/python 폴더에 주차별 폴더가 존재합니다.
week04 폴더에 예시가 있으니 참고하세요.

- 수업자료 연습문제 올리기
해당차시(ex. ch13) 폴더에 "이름_해당차시.py" (ex. hyungchan_ch13.py) 로 파일을 만든 후 코드를 올려주세요.

해당차시과제(ex. hw13) 폴더에 "이름_해당차시과제.py" (ex. hyungchan_hw13.py) 로 파일을 만든 후 코드를 올려주세요.

- 주차별 과제 올리기
주차별 폴더에 주차별과제(ex. weektest04) 폴더가 있습니다. 
"이름_해당주차별과제.py" (ex. hyungchan_weektest04.py) 로 파일을 만든 후 코드를 올려주세요.


4. (선택) 코딩 테스트 코드 올리기
coding_test_review 폴더에 각 스터디 날짜별 폴더가 있습니다.
코딩 테스트 링크를 마크다운에 적어놨으니 링크로 들어가셔서 풀어보시고
"이름_코딩테스트번호.py" (ex. hyungchan_coding_test_01.py) 로 파일을 만든 후 코드를 올려주세요.
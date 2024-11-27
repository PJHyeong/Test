import random # 랜덤함수 불러오기
guesses = ' ' # 추측한 단어
turns = 20    # 20턴으로 설정

infile = open("./words.txt", "r") # 단어를 불러오기 할 메모장의 경로 설정
lines = infile.read().split()     # 단어들을 lines라는 이름의 배열에 추가
word = random.choice(lines)       # word라는 이름으로 lines 내에서 단어 하나를 랜덤으로 선택

while turns > 0:            # 0턴이 될 때까지 반복
  failed = 0                # 실패횟수
  for char in word:         # 
    if char in guesses:     # 
      print(char, end = "") # 입력한 문자를 출력
    else:
      print("_", end = "")  # 아니면 _를 출력a
      failed += 1           #
  if failed == 0:           # 실패가 0일 경우
    print("사용자 승리")    # "사용자의 승리"를 출력
    break
  print("")
  guess = input("단어를 추측하시오: ")    # 추측할 단어를 입력할 input
  guesses += guess                        # 추측한 단어들을 계속 더해줌
  if guess not in word:                   # 만약 추측한 단어가 문자에 해당한 것이 없을 때
    turns -= 1                            # 턴을 -1을 취함
    print("틀렸음!")                      # 그리고 "틀렸음!"을 출력
    print(str(turns) + "기회가 남았음!")  # "n턴 기회가 남았음"을 출력
    if turns == 0:                        # 턴이 0이 되었을 때
      print("사용자 패배 정답은" + word)  # "사용자 패배 정답은 word"를 출력한다
infile.close()
    

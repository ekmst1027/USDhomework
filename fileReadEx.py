# 파일 입출력 예제

# 정석적인 방법
# my_file = open("ihaveadream.txt", "r")
# contents = my_file.read()
# print(type(contents), contents)
# my_file.close()

# with 구문 사용(close가 필요 없음)
# with open("ihaveadream.txt", "r") as my_file:
#     contents = my_file.read()
#     print(type(contents), contents)

# # 한 줄씩 읽어 List Type으로 반환함
# with open("ihaveadream.txt", "r") as my_file:
#     content_list = my_file.readlines()  # 파일 전체를 list로 반환
#     print(type(content_list))   # Type 확인
#     print(content_list) # 리스트 값 출력

# 실행 시 마다 한 줄 씩 읽어오기
# with open("ihaveadream.txt", "r") as my_file:
#     i = 0
#     while 1:
#         line = my_file.readline()
#         if line.strip() != "":
#             print(str(i) + " === " + line.strip())
#         if not line: 
#             break
#         i += 1

# 단어 통계 정보 산출
with open("ihaveadream.txt", "r") as my_file:
    contents = my_file.read()
    word_list = contents.split(" ")    # 빈 칸 기준으로 단어를 분리 리스트
    line_list = contents.split("\n")    # 한줄씩 분리하여 리스트
    

print("Total Number of Characters : ", len(contents))
print("Total Number of Words : ", len(word_list))
print("Total Number of Lines : ", len(line_list))
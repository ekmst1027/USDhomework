# 파일 쓰기 예제

# 기본 예제
# f = open("count_log.txt", "w", encoding="utf8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# 붙여 쓰기
FILE_NAME = "count_log.txt"
with open(FILE_NAME, "a", encoding="utf8") as f:
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)


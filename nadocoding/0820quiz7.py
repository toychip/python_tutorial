
# for
# with open("주차 보고서", "w", encoding="utf8") as nweek_report:
#     nweek_report.write("= x 주차 주간 보고\
#         부서 :\
#         이름 :\
#         업무 요약 : \
#             ")

for i in range(1, 5):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as nweek_report:
        nweek_report.write("- {0}주차 주간 보고 -".format(i))
        nweek_report.write("\n부서 :")
        nweek_report.write("\n이름 :")
        nweek_report.write("\n업무 요약 :")

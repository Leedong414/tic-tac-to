#원본은 입력 받은 것을 바로 print문으로 직접 문자열을 출력하지만 변수에 할당된 문자열을 출력하는 방법으로 바꾸었고 어떤 번호를 눌러야 어디서 입력되는지 계속 보여주게함
#두번 나오는 오류 수정
ttt_list = [" " for _ in range(9)] + ["O", "X", 0]
while not any([not ttt_list[int(check_index[0]) - 1] == " " and ttt_list[int(check_index[0]) - 1] == ttt_list[int(check_index[1]) - 1] and ttt_list[int(check_index[1]) - 1] == ttt_list[int(check_index[2]) - 1] for check_index in ["123", "456", "789", "147", "258", "369", "159", "357"]]):
    print("\n{}\nI 1 I 2 I 3 I\n{}\nI 4 I 5 I 6 I\n{}\nI 7 I 8 I 9 I\n\n".format("-" * 14, "-" * 14, "-" * 14))
    print("".join(["\n{}\nI {} I {} I {} I".format("-" * 14, ttt_list[line * 3], ttt_list[line * 3 + 1], ttt_list[line * 3 + 2]) for line in range(3)]))
    ttt_list[int(input(("\nChoose player {} number 1 ~ 9 >>> ".format(ttt_list[9 + ttt_list[-1] % 2])))) - 1] = ttt_list[9 + ttt_list[-1] % 2]
    print("\n\nPlayer {} Win!".format(ttt_list[9 + ttt_list[-1] % 2]) if any([not ttt_list[int(check_index[0]) - 1] == " " and ttt_list[int(check_index[0]) - 1] == ttt_list[int(check_index[1]) - 1] and ttt_list[int(check_index[1]) - 1] == ttt_list[int(check_index[2]) - 1] for check_index in ["123", "456", "789", "147", "258", "369", "159", "357"]]) else "")
    ttt_list[-1] += 1
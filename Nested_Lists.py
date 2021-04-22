if __name__ == '__main__':
    list = []
    second_list = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        list.append([name,score])
    second_lowest_score = sorted(scores)[1]
    for i,j in list:
        if(j==second_lowest_score):
            second_list.append(i)
    for name in sorted(second_list):
        print(name)


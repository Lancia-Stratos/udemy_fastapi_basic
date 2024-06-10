# インプットなし、アウトプットもなし
def test():
    print("テスト")

test()

# インプットあり、アウトプットなし
def get_comment(string):
    print(string)

get_comment("コメント")
get_comment("コメント123")

# インプットなし、アウトプットあり
def get_number_of_comment():
    return 5

# アウトプット(戻り値) 変数に入れてあげる
comment_number = get_number_of_comment()
print(comment_number)

# インプット2つ、アウトプットあり
def sum_price(int1, int2):
    #int3 = int1 + int2
    return int1 + int2

total = sum_price(3, 5)
print(total)
global_variable = "グローバル"

def global_test():
    print(global_variable)

def local_test():
    local_variable = "ローカル"
    print(local_variable)

global_test()
local_test()
# print(local_variable)
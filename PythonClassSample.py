#初期化メソッド
class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self_operation = "+"
#計算を実行するメソッド
    def do_operation(self):
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            self.result = self.first_term - self.second_term
        elif self.operation == "*":
            self.result = self.first_term * self.second_term
        elif self.operation == "/":
            self.result = self.first_term / self.second_term
#ここからメイン
#オブジェクトの生成
dentaku = Dentaku()
while True:
    f = int(input("First term"))
    dentaku.first_term = f
    o = input("Operation")
    dentaku.operation = o
    s = int(input("Second term"))
    dentaku.second_term = s
    dentaku.do_operation()
    r = dentaku.result
    print("Result",r)
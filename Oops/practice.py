# class A:
#     def level1(self):
#         print("Level1 Accessed !!")
#     def score(self):
#         print("Score : 100")
#
# class B(A):
#     def level2(self):
#         # super().level1()
#         self.level1()
#         print("Level2 Accessed !!")
#
#     # Extend functionailty
#     def score(self):
#             # super().score()
#             print("Perfect Score !!")
#
#
#
# obj = B()
# # obj.level2()
# obj.score()

class A:
    def user1(self):
        print("User from the Class-A")
class B(A):
    def user1(self):
        super().user1()
        print("User1 is from Brazil")
    def user2(self):
        print("User from the Class-B")

class C(B):
    def user1(self):
        super().user1()
        print("User1 is from -- South America --")
    def user2(self):
        self.user1()
        super().user1()
        print("User from the Class-C")

obj = C()
obj.user1()
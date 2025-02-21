class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")

    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()

# Test cases
def test_student():
    student = Student()
    assert student.hello() is None  # Ensuring no errors occur
    assert student.raise_hand() is None

def test_chatty_student():
    chatty_student = ChattyStudent()
    assert chatty_student.hello() is None  # Ensuring no errors occur
    assert chatty_student.raise_hand() is None

if __name__ == "__main__":
    test_student()
    test_chatty_student()
    print("All tests passed successfully!")

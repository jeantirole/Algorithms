# Problem --------------------------------------------------

1700. Number of Students Unable to Eat Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]


# Solution 1 --------------------------------------------------
runtime : 44ms (top 70%)

#- cnt 풀이에서, 제약에서 주어진 숫자에 max cnt 를 어림짐작했음. 
# 밑의 풀이에서 확인할 수 있듯이 ,, len(students) > cnt 로 while 제약해주는게 맞음. 하나의 sandwich 에 대해서 전체 학생의 경우의 수 대입 횟수가 넘어가면 stop. 

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = 0
        while True:
            a = students.pop(0)
            
            s0 = sandwiches.pop(0)

            if a == s0:
                cnt +=1 
                pass

            elif a != s0:
                cnt +=1 
                students.append(a)
                sandwiches.insert(0,s0)
            
            if len(students) == 0 or cnt == 400:
                break

        return len(students)
# Solution 2 ------------------------------------------------------

class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        cnt = 0
        while len(students) > cnt:
            a = students.pop(0)
            
            s0 = sandwiches.pop(0)

            if a == s0:
                cnt = 0 
                pass
                
            
            elif a != s0:
                cnt +=1 
                students.append(a)
                sandwiches.insert(0,s0)
          

        return len(students)

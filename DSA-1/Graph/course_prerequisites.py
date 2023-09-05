# There are a total of A courses you have to take, labeled from 1 to A.
# Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].
# The pairs are given as two arrays B and C, where [B[i], C[i]] form a pair.

def solve(A, B, C):
    prereq_courses = {}
    child = {}
    for i in range(len(B)):
        if C[i] in prereq_courses:
            prereq_courses[C[i]].add(B[i])
        else:
            prereq_courses[C[i]] = set([B[i]])
        if B[i] in child:
            child[B[i]].add(C[i])
        else:
            child[B[i]] = set([C[i]])
    course_taken = set()
    open_courses = []

    for i in range(1, A + 1):
        if i not in prereq_courses:
            open_courses.append(i)

    while len(open_courses) > 0:
        curr_course = open_courses.pop(0)
        course_taken.add(curr_course)
        if curr_course in child:
            for child_course in child[curr_course]:
                prereq_courses[child_course].discard(curr_course)
                if len(prereq_courses[child_course]) == 0:
                    open_courses.append(child_course)

    return 1 if len(course_taken) == A else 0

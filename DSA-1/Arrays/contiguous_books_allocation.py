def cbaHelper(books, max_pages_per_student):
    total_students = 1
    pagesPerStudent = 0
    for i in range(len(books)):
        if pagesPerStudent + books[i] <= max_pages_per_student:
            pagesPerStudent += books[i]
        else:
            total_students += 1
            pagesPerStudent = books[i]
    return total_students


# contigusous books allocation
def cba(books, total_students):
    if total_students > len(books):
        return -1
    min_pages = max(books)
    max_pages = sum(books)
    while min_pages <= max_pages:
        avg = (min_pages + max_pages) // 2
        no_of_students = cbaHelper(books, avg)
        if no_of_students > total_students:
            min_pages = avg + 1
        else:
            max_pages = avg - 1
    return min_pages


books = [33, 20, 42, 68, 70, 10]
total_students = 2

print(cba(books, total_students))

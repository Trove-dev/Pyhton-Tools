courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Art", "Education"]



#courses.insert(0, "Art")
#print(courses[:4])

#courses.insert(0, courses_2)

#print(courses)

courses.extend(courses_2)

courses.remove("Math")

courses.sort()

print(courses)

nums = [1, 5, 3, 2]
nums.sort(reverse=True)
print(nums)

sorted_courses = sorted(courses)
print(sorted_courses)

minimun = min(nums)
thesum = sum(nums)

print(thesum)


print(courses.index("Physics"))


print("Art" in courses)

for index, course in enumerate(courses, start=1):
    print(index, course)


course_str = " - ".join(courses)

new_list = course_str.split(' - ')

print(course_str)
print(new_list)


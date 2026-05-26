def first_n_characters(s: str, n: int) -> str:
    first = ""
    for i in range(n):
        first+=s[i]
    return first

def last_n_characters(s: str, n: int) -> str:
    last = ""
    for i in range(len(s) - n, len(s)):
        last+=s[i]
    return last


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))

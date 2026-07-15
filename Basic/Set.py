s = { 2,3,4}
print(type(s))

st= set()

st.add(3)
st.add(4)
st.add(1)
st.add(8)
st.add(0)
print((st))

st.remove(1)
print(st)

st.pop()
print(st)

st.clear()
print(st)

s1 = {1,2,3}
s2 = {3,4,5}

print(s1.union(s2))
print(s1.intersection(s2))
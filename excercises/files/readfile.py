# Use absolute path
test_file = open(file='/Users/bluejays/Documents/projects/jsu216/learn_python/README.md')
text = test_file.read()
print(text)

# Use relative path
test_file = open(file='../../README.md')
text = test_file.read()
print(text)

# Use relative path
test_file = open('myfile2.txt', 'w')
test_file.write('this is my second text file line #1!')

# Use absolute path
test_file = open('/Users/bluejays/Documents/projects/jsu216/learn_python/excercises/files/myfile2.txt', 'a')
test_file.write('\nthis is my second text file line #2!')

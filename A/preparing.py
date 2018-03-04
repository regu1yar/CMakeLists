f = open('index.h', 'w')
f.write('''#include <iostream>
void indexFoo() { std::cout << "index" << std::endl; }
''')
f.close()

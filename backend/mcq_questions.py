"""Career Intelligence Python MCQ bank: 40 foundational questions."""

MCQ_QUESTION_BANK = {
    "python": [
        {
            "id": "python_001",
            "skill": "Python",
            "topic": 'Syntax and functions',
            "question": 'Which keyword begins a function definition in Python?',
            "options": ['function', 'def', 'fun', 'define'],
            "correct_answer": 'def',
            "explanation": 'Python function definitions begin with the def keyword.'
        },
        {
            "id": "python_002",
            "skill": "Python",
            "topic": 'Data types',
            "question": 'Which built-in type represents either True or False?',
            "options": ['str', 'bool', 'float', 'bytes'],
            "correct_answer": 'bool',
            "explanation": 'The bool type has two values: True and False.'
        },
        {
            "id": "python_003",
            "skill": "Python",
            "topic": 'Comments',
            "question": 'Which character starts a single-line comment in ordinary Python code?',
            "options": ['#', '//', '/*', '--'],
            "correct_answer": '#',
            "explanation": 'Python uses # for a single-line comment.'
        },
        {
            "id": "python_004",
            "skill": "Python",
            "topic": 'Collections',
            "question": 'Which built-in collection stores key-value pairs?',
            "options": ['list', 'tuple', 'dict', 'set'],
            "correct_answer": 'dict',
            "explanation": 'A dictionary maps keys to values.'
        },
        {
            "id": "python_005",
            "skill": "Python",
            "topic": 'Built-in functions',
            "question": 'What does len([10, 20, 30]) return?',
            "options": ['2', '3', '10', '30'],
            "correct_answer": '3',
            "explanation": 'The list contains three elements, so len returns 3.'
        },
        {
            "id": "python_006",
            "skill": "Python",
            "topic": 'Strings',
            "question": "Given s = 'Python', what does s[0] return?",
            "options": ['P', 'y', 'Python', 'An IndexError'],
            "correct_answer": 'P',
            "explanation": 'Python sequences use zero-based indexing, so index 0 is the first character.'
        },
        {
            "id": "python_007",
            "skill": "Python",
            "topic": 'Slicing',
            "question": 'Given nums = [0, 1, 2, 3, 4], what does nums[1:4] return?',
            "options": ['[0, 1, 2, 3]', '[1, 2, 3]', '[1, 2, 3, 4]', '[2, 3, 4]'],
            "correct_answer": '[1, 2, 3]',
            "explanation": 'A slice includes the start index and excludes the stop index.'
        },
        {
            "id": "python_008",
            "skill": "Python",
            "topic": 'Mutability',
            "question": 'Which of these built-in types is immutable?',
            "options": ['list', 'dict', 'set', 'tuple'],
            "correct_answer": 'tuple',
            "explanation": "A tuple's element references cannot be reassigned after the tuple is created."
        },
        {
            "id": "python_009",
            "skill": "Python",
            "topic": 'Operators',
            "question": 'What is the result of 7 // 2 in Python?',
            "options": ['3', '3.5', '4', '1'],
            "correct_answer": '3',
            "explanation": 'Floor division rounds the quotient down; here the result is 3.'
        },
        {
            "id": "python_010",
            "skill": "Python",
            "topic": 'Operators',
            "question": 'What is the result of 2 ** 3?',
            "options": ['6', '8', '9', '5'],
            "correct_answer": '8',
            "explanation": 'The ** operator raises 2 to the power of 3: 2 × 2 × 2 = 8.'
        },
        {
            "id": "python_011",
            "skill": "Python",
            "topic": 'Conditionals',
            "question": 'Which keyword checks another condition after an if condition is false?',
            "options": ['elseif', 'elif', 'else if', 'then'],
            "correct_answer": 'elif',
            "explanation": 'Python uses elif for an additional conditional branch.'
        },
        {
            "id": "python_012",
            "skill": "Python",
            "topic": 'Loops',
            "question": 'What values does range(3) produce when iterated over?',
            "options": ['1, 2, 3', '0, 1, 2', '0, 1, 2, 3', '3 only'],
            "correct_answer": '0, 1, 2',
            "explanation": 'With one argument, range starts at 0 and stops before 3.'
        },
        {
            "id": "python_013",
            "skill": "Python",
            "topic": 'Loop control',
            "question": 'What does break do inside a loop?',
            "options": ['Skips only the current iteration', 'Ends the nearest enclosing loop', 'Restarts the loop', 'Pauses the program permanently'],
            "correct_answer": 'Ends the nearest enclosing loop',
            "explanation": 'break exits the nearest enclosing for or while loop.'
        },
        {
            "id": "python_014",
            "skill": "Python",
            "topic": 'Loop control',
            "question": 'What does continue do inside a loop?',
            "options": ['Ends the whole program', 'Exits the loop immediately', 'Skips to the next iteration', 'Repeats the current statement forever'],
            "correct_answer": 'Skips to the next iteration',
            "explanation": 'continue skips the remaining statements in the current iteration and proceeds to the next one.'
        },
        {
            "id": "python_015",
            "skill": "Python",
            "topic": 'Functions and return',
            "question": 'What does a Python function return if it reaches the end without a return statement?',
            "options": ['0', 'False', 'None', 'An empty string'],
            "correct_answer": 'None',
            "explanation": 'A function that does not explicitly return a value returns None.'
        },
        {
            "id": "python_016",
            "skill": "Python",
            "topic": 'Default arguments',
            "question": "In def greet(name='Guest'): what is the default value of name?",
            "options": ['None', 'Guest', 'name', 'An empty string'],
            "correct_answer": 'Guest',
            "explanation": 'The default argument is the value assigned in the function definition.'
        },
        {
            "id": "python_017",
            "skill": "Python",
            "topic": 'Scope',
            "question": 'Inside a function, which keyword lets you assign to a module-level global variable?',
            "options": ['public', 'global', 'outer', 'static'],
            "correct_answer": 'global',
            "explanation": 'The global statement declares that an assignment refers to a module-level global variable.'
        },
        {
            "id": "python_018",
            "skill": "Python",
            "topic": 'Comprehensions',
            "question": 'What does [x * 2 for x in [1, 2, 3]] produce?',
            "options": ['[1, 2, 3, 2]', '[2, 4, 6]', '[1, 4, 9]', '[3, 2, 1]'],
            "correct_answer": '[2, 4, 6]',
            "explanation": 'The list comprehension doubles each item in the original list.'
        },
        {
            "id": "python_019",
            "skill": "Python",
            "topic": 'Dictionaries',
            "question": "For d = {'a': 1}, what does d.get('b', 0) return?",
            "options": ['None', 'KeyError', '0', '1'],
            "correct_answer": '0',
            "explanation": 'dict.get returns the supplied default when the key is absent.'
        },
        {
            "id": "python_020",
            "skill": "Python",
            "topic": 'Sets',
            "question": 'What is a key property of a Python set?',
            "options": ['It preserves duplicate elements', 'It stores only key-value pairs', 'It contains unique elements', 'It can only contain strings'],
            "correct_answer": 'It contains unique elements',
            "explanation": 'A set stores distinct hashable elements, so duplicates are removed.'
        },
        {
            "id": "python_021",
            "skill": "Python",
            "topic": 'Exceptions',
            "question": 'Which block is used to handle an exception raised in a try block?',
            "options": ['catch', 'except', 'rescue', 'handle'],
            "correct_answer": 'except',
            "explanation": 'Python uses except clauses to catch and handle specified exceptions.'
        },
        {
            "id": "python_022",
            "skill": "Python",
            "topic": 'Exceptions',
            "question": "Which exception is raised by int('hello')?",
            "options": ['TypeError', 'ValueError', 'KeyError', 'IndexError'],
            "correct_answer": 'ValueError',
            "explanation": 'The string has an invalid value format for integer conversion, so int raises ValueError.'
        },
        {
            "id": "python_023",
            "skill": "Python",
            "topic": 'File handling',
            "question": 'Which file mode opens a file for reading text without requesting write access?',
            "options": ["'w'", "'a'", "'r'", "'x'"],
            "correct_answer": "'r'",
            "explanation": 'The r mode opens a file for reading and is the default mode.'
        },
        {
            "id": "python_024",
            "skill": "Python",
            "topic": 'File handling',
            "question": 'Why is `with open(path) as file:` commonly preferred?',
            "options": ['It automatically sorts file contents', 'It closes the file when the block exits', 'It makes every file read-only', 'It prevents all file errors'],
            "correct_answer": 'It closes the file when the block exits',
            "explanation": 'The context manager closes the file when the with block finishes, including if an exception occurs.'
        },
        {
            "id": "python_025",
            "skill": "Python",
            "topic": 'Modules',
            "question": "Which statement imports Python's standard math module?",
            "options": ['include math', 'using math', 'import math', "require('math')"],
            "correct_answer": 'import math',
            "explanation": 'Python modules are commonly imported with the import statement.'
        },
        {
            "id": "python_026",
            "skill": "Python",
            "topic": 'Main guard',
            "question": "What is the purpose of `if __name__ == '__main__':`?",
            "options": ['It prevents the module from being imported', 'It runs guarded code when the file is executed as the main program', 'It declares a class', 'It installs dependencies'],
            "correct_answer": 'It runs guarded code when the file is executed as the main program',
            "explanation": "When run directly, a file's __name__ is '__main__'; when imported, it usually has its module name."
        },
        {
            "id": "python_027",
            "skill": "Python",
            "topic": 'Object-oriented programming',
            "question": 'Which keyword is used to define a class in Python?',
            "options": ['object', 'class', 'struct', 'typeclass'],
            "correct_answer": 'class',
            "explanation": 'A class definition begins with the class keyword.'
        },
        {
            "id": "python_028",
            "skill": "Python",
            "topic": 'Object-oriented programming',
            "question": 'In an ordinary instance method, what does the first parameter self refer to?',
            "options": ['The parent class', 'The current instance', 'The module', "The method's return value"],
            "correct_answer": 'The current instance',
            "explanation": 'By convention, self refers to the instance on which the method is called.'
        },
        {
            "id": "python_029",
            "skill": "Python",
            "topic": 'Inheritance',
            "question": 'What does inheritance allow a class to do?',
            "options": ['Reuse and extend behavior from a base class', 'Automatically convert every object to a string', 'Prevent all methods from being overridden', 'Make every attribute private'],
            "correct_answer": 'Reuse and extend behavior from a base class',
            "explanation": 'A derived class can inherit attributes and methods and can add or override behavior.'
        },
        {
            "id": "python_030",
            "skill": "Python",
            "topic": 'Iterators',
            "question": 'What does next(iterator) normally do?',
            "options": ['Returns the last item', 'Returns the next item from an iterator', 'Sorts the iterator', 'Creates a list from the iterator'],
            "correct_answer": 'Returns the next item from an iterator',
            "explanation": 'next requests the next value and raises StopIteration when exhausted unless a default is provided.'
        },
        {
            "id": "python_031",
            "skill": "Python",
            "topic": 'Generators',
            "question": 'Which keyword makes a function produce a value and suspend so it can resume later?',
            "options": ['return', 'yield', 'pause', 'emit'],
            "correct_answer": 'yield',
            "explanation": 'yield produces a value from a generator and suspends the function until it is resumed.'
        },
        {
            "id": "python_032",
            "skill": "Python",
            "topic": 'Lambda functions',
            "question": 'What kind of object does `lambda x: x + 1` create?',
            "options": ['A class', 'An anonymous function', 'A generator object immediately', 'A dictionary'],
            "correct_answer": 'An anonymous function',
            "explanation": 'lambda creates a small anonymous function expression.'
        },
        {
            "id": "python_033",
            "skill": "Python",
            "topic": 'Sorting',
            "question": 'Which built-in function returns a new sorted list from an iterable?',
            "options": ['sort()', 'sorted()', 'order()', 'arrange()'],
            "correct_answer": 'sorted()',
            "explanation": 'sorted(iterable) returns a new list in sorted order, leaving the original iterable unchanged.'
        },
        {
            "id": "python_034",
            "skill": "Python",
            "topic": 'Sorting',
            "question": 'For a list named values, what is true of values.sort()?',
            "options": ['It returns a new sorted list and keeps values unchanged', 'It sorts the list in place and returns None', 'It converts the list to a tuple', 'It sorts only strings'],
            "correct_answer": 'It sorts the list in place and returns None',
            "explanation": 'list.sort() modifies the existing list and returns None.'
        },
        {
            "id": "python_035",
            "skill": "Python",
            "topic": 'Identity and equality',
            "question": 'What does the == operator normally check between two objects?',
            "options": ['Whether they are the same object in memory', 'Whether their values are equal', 'Whether both variables have the same name', 'Whether both objects are mutable'],
            "correct_answer": 'Whether their values are equal',
            "explanation": '== tests equality as defined by the objects; is tests object identity.'
        },
        {
            "id": "python_036",
            "skill": "Python",
            "topic": 'Truthiness',
            "question": 'Which value is falsey in a Python conditional?',
            "options": ["'0'", '[0]', '1', '[]'],
            "correct_answer": '[]',
            "explanation": 'An empty list is falsey; the other listed values are truthy.'
        },
        {
            "id": "python_037",
            "skill": "Python",
            "topic": 'Type conversion',
            "question": "What does float('3.5') return?",
            "options": ["The string '3.5'", 'The integer 3', 'The floating-point number 3.5', 'A ValueError'],
            "correct_answer": 'The floating-point number 3.5',
            "explanation": 'float converts a valid numeric string into a floating-point value.'
        },
        {
            "id": "python_038",
            "skill": "Python",
            "topic": 'Argument unpacking',
            "question": 'In a function call, what does **settings do when settings is a dictionary?',
            "options": ['Passes keys as positional arguments', 'Unpacks entries as keyword arguments', 'Multiplies every value by two', 'Creates a copy but passes no arguments'],
            "correct_answer": 'Unpacks entries as keyword arguments',
            "explanation": 'In a call, ** unpacks a mapping into keyword arguments.'
        },
        {
            "id": "python_039",
            "skill": "Python",
            "topic": 'Virtual environments',
            "question": 'What is the main purpose of a Python virtual environment?',
            "options": ['Run Python without an interpreter', 'Isolate project dependencies from other environments', 'Automatically fix syntax errors', 'Convert Python into JavaScript'],
            "correct_answer": 'Isolate project dependencies from other environments',
            "explanation": "A virtual environment keeps a project's installed packages separate from other projects."
        },
        {
            "id": "python_040",
            "skill": "Python",
            "topic": 'Testing',
            "question": 'In a typical unit test, what is an assertion used for?',
            "options": ['Install a package', 'Check that an expected condition or result is true', 'Start a web server', 'Declare a loop'],
            "correct_answer": 'Check that an expected condition or result is true',
            "explanation": 'An assertion verifies an expected condition; a failed assertion causes the test to fail.'
        }
    ],
    "java": [
        {
            "id": "java_001",
            "skill": "Java",
            "topic": "JVM and execution",
            "question": "What is the main role of the JVM when running a Java program?",
            "options": [
                "It converts Java source code directly into HTML",
                "It executes Java bytecode and manages runtime operations",
                "It replaces the Java compiler",
                "It converts every Java program into JavaScript"
            ],
            "correct_answer": "It executes Java bytecode and manages runtime operations",
            "explanation": "The JVM executes bytecode and provides runtime services such as memory management and garbage collection."
        },
        {
            "id": "java_002",
            "skill": "Java",
            "topic": "Java execution",
            "question": "Which command normally compiles a Java source file named Main.java?",
            "options": [
                "java Main.java",
                "javac Main.java",
                "compile Main.java",
                "jvm Main.java"
            ],
            "correct_answer": "javac Main.java",
            "explanation": "The javac compiler compiles Java source code into bytecode."
        },
        {
            "id": "java_003",
            "skill": "Java",
            "topic": "Data types",
            "question": "What is the value of x after this code executes? int x = 7 / 2;",
            "options": [
                "3",
                "3.5",
                "4",
                "Compilation error"
            ],
            "correct_answer": "3",
            "explanation": "Both operands are integers, so integer division discards the fractional part."
        },
        {
            "id": "java_004",
            "skill": "Java",
            "topic": "Type conversion",
            "question": "Which statement correctly converts the double value 9.8 into an int?",
            "options": [
                "int x = 9.8;",
                "int x = (int) 9.8;",
                "int x = double(9.8);",
                "int x = convert(9.8);"
            ],
            "correct_answer": "int x = (int) 9.8;",
            "explanation": "An explicit cast converts the value to int, truncating the fractional part to produce 9."
        },
        {
            "id": "java_005",
            "skill": "Java",
            "topic": "Strings",
            "question": "What is printed by this code? String s = \"Java\"; s.concat(\" SE\"); System.out.println(s);",
            "options": [
                "Java SE",
                "Java",
                "SE",
                "Compilation error"
            ],
            "correct_answer": "Java",
            "explanation": "Strings are immutable. concat returns a new String, and the result is not assigned back to s."
        },
        {
            "id": "java_006",
            "skill": "Java",
            "topic": "String comparison",
            "question": "Which method should normally be used to compare the contents of two String objects?",
            "options": [
                "==",
                "equals()",
                "compareReference()",
                "sameObject()"
            ],
            "correct_answer": "equals()",
            "explanation": "equals compares String contents, while == checks whether references point to the same object."
        },
        {
            "id": "java_007",
            "skill": "Java",
            "topic": "Operators",
            "question": "What is the value of result? int a = 5; int result = a++ + ++a;",
            "options": [
                "10",
                "11",
                "12",
                "13"
            ],
            "correct_answer": "12",
            "explanation": "The first a++ contributes 5 and then increments a to 6. ++a increments it to 7 before contributing, so the sum is 12."
        },
        {
            "id": "java_008",
            "skill": "Java",
            "topic": "Control flow",
            "question": "What does the break statement do inside a loop?",
            "options": [
                "Skips only the current iteration",
                "Terminates the nearest enclosing loop or switch",
                "Restarts the loop from the beginning",
                "Terminates the entire Java application in every case"
            ],
            "correct_answer": "Terminates the nearest enclosing loop or switch",
            "explanation": "break exits the nearest enclosing loop or switch statement."
        },
        {
            "id": "java_009",
            "skill": "Java",
            "topic": "Control flow",
            "question": "What is printed? for (int i = 0; i < 5; i++) { if (i == 2) continue; System.out.print(i); }",
            "options": [
                "01234",
                "0134",
                "012",
                "134"
            ],
            "correct_answer": "0134",
            "explanation": "When i is 2, continue skips the print statement for that iteration."
        },
        {
            "id": "java_010",
            "skill": "Java",
            "topic": "Arrays",
            "question": "What happens when code accesses arr[3] in an array created as int[] arr = new int[3];?",
            "options": [
                "It returns 0",
                "It returns null",
                "It throws ArrayIndexOutOfBoundsException",
                "It automatically expands the array"
            ],
            "correct_answer": "It throws ArrayIndexOutOfBoundsException",
            "explanation": "An array of length 3 has valid indices 0, 1, and 2."
        },
        {
            "id": "java_011",
            "skill": "Java",
            "topic": "Methods",
            "question": "Which statement about Java method overloading is correct?",
            "options": [
                "Methods must have different return types only",
                "Methods must have the same parameter list",
                "Methods must differ in their parameter lists",
                "Overloaded methods must belong to different classes"
            ],
            "correct_answer": "Methods must differ in their parameter lists",
            "explanation": "Overloaded methods have the same name but different parameter lists; return type alone cannot distinguish overloads."
        },
        {
            "id": "java_012",
            "skill": "Java",
            "topic": "Constructors",
            "question": "Which statement about a Java constructor is correct?",
            "options": [
                "It must declare a return type",
                "Its name must match the class name and it has no return type",
                "It must always be private",
                "It can be called only once in the entire program"
            ],
            "correct_answer": "Its name must match the class name and it has no return type",
            "explanation": "A constructor has the same name as its class and does not declare a return type, not even void."
        },
        {
            "id": "java_013",
            "skill": "Java",
            "topic": "Static members",
            "question": "A static method cannot directly access which of the following without an object reference?",
            "options": [
                "Another static field",
                "Another static method",
                "An instance field",
                "A local variable declared inside it"
            ],
            "correct_answer": "An instance field",
            "explanation": "An instance field belongs to an object, while a static method belongs to the class and has no implicit this reference."
        },
        {
            "id": "java_014",
            "skill": "Java",
            "topic": "Encapsulation",
            "question": "Which design best demonstrates encapsulation?",
            "options": [
                "Making every field public",
                "Making fields private and exposing controlled access through methods",
                "Putting all methods in a single static class",
                "Avoiding constructors in every class"
            ],
            "correct_answer": "Making fields private and exposing controlled access through methods",
            "explanation": "Encapsulation hides internal state and allows controlled access through a class's public methods."
        },
        {
            "id": "java_015",
            "skill": "Java",
            "topic": "Inheritance",
            "question": "Which keyword allows a subclass constructor to invoke its superclass constructor?",
            "options": [
                "this",
                "super",
                "parent",
                "extends"
            ],
            "correct_answer": "super",
            "explanation": "super() invokes a superclass constructor and, when used explicitly, must be the first statement in the constructor."
        },
        {
            "id": "java_016",
            "skill": "Java",
            "topic": "Polymorphism",
            "question": "A superclass reference points to a subclass object. Which implementation is called for an overridden instance method?",
            "options": [
                "Always the superclass implementation",
                "The implementation belonging to the actual object's class",
                "The implementation with the shortest method name",
                "Both implementations run automatically"
            ],
            "correct_answer": "The implementation belonging to the actual object's class",
            "explanation": "Overridden instance methods use runtime dynamic dispatch based on the actual object's class."
        },
        {
            "id": "java_017",
            "skill": "Java",
            "topic": "Abstraction",
            "question": "Which statement about an abstract Java class is correct?",
            "options": [
                "It cannot contain implemented methods",
                "It can contain both abstract and concrete methods",
                "It must contain only static methods",
                "It can always be instantiated directly"
            ],
            "correct_answer": "It can contain both abstract and concrete methods",
            "explanation": "Abstract classes can contain abstract methods, implemented methods, fields, and constructors, but cannot be instantiated directly."
        },
        {
            "id": "java_018",
            "skill": "Java",
            "topic": "Interfaces",
            "question": "Which statement about Java interfaces is correct?",
            "options": [
                "A class can implement multiple interfaces",
                "A class can implement exactly one interface",
                "Interfaces cannot declare methods",
                "An interface can always be instantiated directly"
            ],
            "correct_answer": "A class can implement multiple interfaces",
            "explanation": "Java supports implementing multiple interfaces, allowing a class to follow multiple contracts."
        },
        {
            "id": "java_019",
            "skill": "Java",
            "topic": "Access modifiers",
            "question": "Which access modifier allows access from anywhere, provided the containing class itself is accessible?",
            "options": [
                "private",
                "protected",
                "public",
                "default"
            ],
            "correct_answer": "public",
            "explanation": "A public member can be accessed from any location where its containing type is accessible."
        },
        {
            "id": "java_020",
            "skill": "Java",
            "topic": "Final keyword",
            "question": "What does declaring a variable as final generally prevent?",
            "options": [
                "Reading the variable",
                "Assigning a value to it more than once",
                "Using it inside a method",
                "Using it as a method argument"
            ],
            "correct_answer": "Assigning a value to it more than once",
            "explanation": "A final variable can be assigned only once. If it holds an object reference, the reference cannot be reassigned, although the object's state may still change."
        },
        {
            "id": "java_021",
            "skill": "Java",
            "topic": "Exception handling",
            "question": "What is the purpose of a finally block in Java?",
            "options": [
                "It executes only when an exception occurs",
                "It normally runs after try/catch processing, whether or not an exception occurred",
                "It catches every exception automatically",
                "It replaces the return statement"
            ],
            "correct_answer": "It normally runs after try/catch processing, whether or not an exception occurred",
            "explanation": "A finally block normally runs whether or not an exception occurs, though abrupt JVM termination and certain other situations can prevent it."
        },
        {
            "id": "java_022",
            "skill": "Java",
            "topic": "Checked exceptions",
            "question": "Which of these is a checked exception that generally must be caught or declared?",
            "options": [
                "NullPointerException",
                "ArithmeticException",
                "IOException",
                "ArrayIndexOutOfBoundsException"
            ],
            "correct_answer": "IOException",
            "explanation": "IOException is a checked exception. The other listed exceptions are unchecked runtime exceptions."
        },
        {
            "id": "java_023",
            "skill": "Java",
            "topic": "Exception propagation",
            "question": "What happens if a method throws a checked exception and neither catches it nor declares it with throws?",
            "options": [
                "The compiler normally reports an error",
                "The exception is always ignored",
                "The JVM converts it to null",
                "The method runs twice"
            ],
            "correct_answer": "The compiler normally reports an error",
            "explanation": "Checked exceptions must be caught or declared in the method's throws clause."
        },
        {
            "id": "java_024",
            "skill": "Java",
            "topic": "Try-with-resources",
            "question": "What is a key benefit of Java's try-with-resources statement?",
            "options": [
                "It automatically retries failed operations",
                "It automatically closes eligible resources when the statement finishes",
                "It prevents all exceptions",
                "It makes every object immutable"
            ],
            "correct_answer": "It automatically closes eligible resources when the statement finishes",
            "explanation": "Resources implementing AutoCloseable are automatically closed when the try-with-resources statement exits."
        },
        {
            "id": "java_025",
            "skill": "Java",
            "topic": "Collections",
            "question": "Which collection is generally suitable when you need a resizable list that preserves element order and allows duplicates?",
            "options": [
                "ArrayList",
                "HashSet",
                "TreeSet",
                "HashMap"
            ],
            "correct_answer": "ArrayList",
            "explanation": "ArrayList is a resizable list that preserves positional order and permits duplicate elements."
        },
        {
            "id": "java_026",
            "skill": "Java",
            "topic": "Sets",
            "question": "Which statement best describes a HashSet?",
            "options": [
                "It stores key-value pairs",
                "It prevents duplicate elements and does not guarantee iteration order",
                "It always sorts elements alphabetically",
                "It allows duplicates but sorts them automatically"
            ],
            "correct_answer": "It prevents duplicate elements and does not guarantee iteration order",
            "explanation": "HashSet stores unique elements and does not guarantee a particular iteration order."
        },
        {
            "id": "java_027",
            "skill": "Java",
            "topic": "Maps",
            "question": "How does a HashMap normally handle a second put operation using an existing key?",
            "options": [
                "It always creates a duplicate key entry",
                "It replaces the value associated with that key",
                "It deletes the entire map",
                "It throws an exception in every case"
            ],
            "correct_answer": "It replaces the value associated with that key",
            "explanation": "Map keys are unique; putting a value for an existing key replaces its associated value."
        },
        {
            "id": "java_028",
            "skill": "Java",
            "topic": "Generics",
            "question": "What is the main benefit of using List<String> instead of a raw List?",
            "options": [
                "It makes the list automatically sorted",
                "It provides compile-time type checking for String elements",
                "It allows only one element",
                "It guarantees that no null value can be stored"
            ],
            "correct_answer": "It provides compile-time type checking for String elements",
            "explanation": "Generics provide stronger type checking and reduce the need for manual casts when retrieving elements."
        },
        {
            "id": "java_029",
            "skill": "Java",
            "topic": "Equality and hash codes",
            "question": "When a class overrides equals() for logical equality, which additional method should generally be overridden consistently?",
            "options": [
                "toString()",
                "hashCode()",
                "finalize()",
                "wait()"
            ],
            "correct_answer": "hashCode()",
            "explanation": "Equal objects must have equal hash codes, which is essential for correct behavior in hash-based collections."
        },
        {
            "id": "java_030",
            "skill": "Java",
            "topic": "Object class",
            "question": "Which method is commonly overridden to provide a readable textual representation of an object?",
            "options": [
                "main()",
                "toString()",
                "cloneAll()",
                "getClassName()"
            ],
            "correct_answer": "toString()",
            "explanation": "Overriding toString() lets a class provide a meaningful text representation of its objects."
        },
        {
            "id": "java_031",
            "skill": "Java",
            "topic": "Memory management",
            "question": "What does Java garbage collection primarily do?",
            "options": [
                "Deletes every object when a method ends",
                "Reclaims memory occupied by objects that are no longer reachable",
                "Removes all local variables before execution",
                "Guarantees immediate memory release when an object becomes unused"
            ],
            "correct_answer": "Reclaims memory occupied by objects that are no longer reachable",
            "explanation": "Garbage collection reclaims memory from unreachable objects, but collection timing is not guaranteed to be immediate."
        },
        {
            "id": "java_032",
            "skill": "Java",
            "topic": "References and null",
            "question": "What happens when an instance method is invoked through a reference whose value is null?",
            "options": [
                "The JVM creates an object automatically",
                "A NullPointerException is thrown",
                "The method runs as a static method",
                "The reference becomes a valid object"
            ],
            "correct_answer": "A NullPointerException is thrown",
            "explanation": "Calling an instance method through a null reference causes a NullPointerException."
        },
        {
            "id": "java_033",
            "skill": "Java",
            "topic": "Recursion",
            "question": "What is essential for a recursive method to terminate normally for a valid input?",
            "options": [
                "A static variable in every method",
                "A base case that stops further recursive calls",
                "A constructor call on every iteration",
                "A finally block in every call"
            ],
            "correct_answer": "A base case that stops further recursive calls",
            "explanation": "A base case stops recursion. Without a reachable stopping condition, calls may continue until a StackOverflowError occurs."
        },
        {
            "id": "java_034",
            "skill": "Java",
            "topic": "Pass by value",
            "question": "When an object reference is passed to a Java method, what is actually passed?",
            "options": [
                "The object is always copied completely",
                "A copy of the reference value",
                "The object's memory address as a directly editable variable",
                "The class definition itself"
            ],
            "correct_answer": "A copy of the reference value",
            "explanation": "Java is pass-by-value. The method receives a copy of the reference, so it can modify the object but cannot reassign the caller's reference."
        },
        {
            "id": "java_035",
            "skill": "Java",
            "topic": "Lambdas",
            "question": "A Java lambda expression can directly implement which type of interface?",
            "options": [
                "Any class",
                "A functional interface with one abstract method",
                "An interface with no methods only",
                "Every interface regardless of its abstract method count"
            ],
            "correct_answer": "A functional interface with one abstract method",
            "explanation": "A lambda expression provides an implementation of a functional interface, which has exactly one abstract method."
        },
        {
            "id": "java_036",
            "skill": "Java",
            "topic": "Streams",
            "question": "In Java Streams, which operation is typically used to transform each element into another value?",
            "options": [
                "filter()",
                "map()",
                "count()",
                "findFirst()"
            ],
            "correct_answer": "map()",
            "explanation": "map transforms each stream element. filter selects elements that satisfy a condition."
        },
        {
            "id": "java_037",
            "skill": "Java",
            "topic": "Concurrency",
            "question": "What is a key difference between calling start() and calling run() directly on a Thread object?",
            "options": [
                "run() always creates two threads",
                "start() initiates a new thread of execution, while direct run() executes like a normal method call",
                "start() runs only on the main thread",
                "There is no difference in execution behavior"
            ],
            "correct_answer": "start() initiates a new thread of execution, while direct run() executes like a normal method call",
            "explanation": "start() schedules a new thread to execute run(); calling run() directly does not start a new thread."
        },
        {
            "id": "java_038",
            "skill": "Java",
            "topic": "Synchronization",
            "question": "What is the primary purpose of synchronized when used to protect a shared object's method?",
            "options": [
                "To make the method execute faster in every situation",
                "To coordinate access using the object's monitor lock",
                "To prevent the method from returning values",
                "To convert the method into a static method"
            ],
            "correct_answer": "To coordinate access using the object's monitor lock",
            "explanation": "Synchronization uses a monitor lock to coordinate access between threads and helps prevent certain race conditions."
        },
        {
            "id": "java_039",
            "skill": "Java",
            "topic": "Immutability",
            "question": "Which design choice helps make a Java class immutable?",
            "options": [
                "Expose all fields as public and mutable",
                "Prevent state changes after construction and avoid exposing mutable internal state",
                "Provide setters for every field",
                "Allow subclasses to change all internal fields"
            ],
            "correct_answer": "Prevent state changes after construction and avoid exposing mutable internal state",
            "explanation": "An immutable class prevents changes to its state after construction and protects mutable internal objects from outside modification."
        },
        {
            "id": "java_040",
            "skill": "Java",
            "topic": "Design and type safety",
            "question": "Why is composition often preferred over inheritance when one class only needs to use another class's functionality?",
            "options": [
                "Composition always uses less memory",
                "Composition can reduce tight coupling and avoid an unnecessary inheritance relationship",
                "Inheritance is not supported in Java",
                "Composition prevents objects from calling methods"
            ],
            "correct_answer": "Composition can reduce tight coupling and avoid an unnecessary inheritance relationship",
            "explanation": "Composition lets a class delegate work to another object without creating an inheritance relationship that may be unnecessary or restrictive."
        }
    ],
    
    "javascript": [
        {
            "id": "javascript_001",
            "skill": "JavaScript",
            "topic": "Scope",
            "question": "What does let provide that var does not provide in a typical block statement?",
            "options": [
                "Block scope",
                "Automatic JSON conversion",
                "Class inheritance",
                "Asynchronous execution"
            ],
            "correct_answer": "Block scope",
            "explanation": "let is block-scoped, while var is scoped to the nearest function or global scope."
        },
        {
            "id": "javascript_002",
            "skill": "JavaScript",
            "topic": "Hoisting",
            "question": "What happens when this code runs? console.log(x); var x = 5;",
            "options": [
                "It prints 5",
                "It prints undefined",
                "It throws a ReferenceError",
                "It throws a SyntaxError"
            ],
            "correct_answer": "It prints undefined",
            "explanation": "The var declaration is hoisted and initialized to undefined before the assignment executes."
        },
        {
            "id": "javascript_003",
            "skill": "JavaScript",
            "topic": "Temporal dead zone",
            "question": "What happens when console.log(x) runs before let x = 10 within the same block?",
            "options": [
                "It prints undefined",
                "It prints null",
                "It throws a ReferenceError",
                "It automatically declares x as global"
            ],
            "correct_answer": "It throws a ReferenceError",
            "explanation": "A let binding cannot be accessed before its declaration is evaluated; this period is called the temporal dead zone."
        },
        {
            "id": "javascript_004",
            "skill": "JavaScript",
            "topic": "Equality",
            "question": "What does the expression 0 == false evaluate to in JavaScript?",
            "options": [
                "true",
                "false",
                "undefined",
                "A SyntaxError"
            ],
            "correct_answer": "true",
            "explanation": "Loose equality performs type coercion, so 0 == false evaluates to true."
        },
        {
            "id": "javascript_005",
            "skill": "JavaScript",
            "topic": "Strict equality",
            "question": "What does 0 === false evaluate to?",
            "options": [
                "true",
                "false",
                "null",
                "A TypeError"
            ],
            "correct_answer": "false",
            "explanation": "Strict equality does not convert operands to the same type; number 0 and boolean false differ in type."
        },
        {
            "id": "javascript_006",
            "skill": "JavaScript",
            "topic": "Closures",
            "question": "What is a closure in JavaScript?",
            "options": [
                "A function together with access to its surrounding lexical environment",
                "A loop that always executes once",
                "An object that cannot have properties",
                "A method that automatically closes browser tabs"
            ],
            "correct_answer": "A function together with access to its surrounding lexical environment",
            "explanation": "A closure allows a function to retain access to variables from its lexical scope even after the outer function has returned."
        },
        {
            "id": "javascript_007",
            "skill": "JavaScript",
            "topic": "Closures",
            "question": "What does this return? function makeCounter() { let n = 0; return () => ++n; } const c = makeCounter(); c(); c();",
            "options": [
                "1",
                "2",
                "0",
                "undefined"
            ],
            "correct_answer": "2",
            "explanation": "The returned function closes over n. The two calls increment it from 0 to 1 and then to 2; the final expression evaluates to 2."
        },
        {
            "id": "javascript_008",
            "skill": "JavaScript",
            "topic": "Function declarations",
            "question": "Which statement about a function declaration is correct?",
            "options": [
                "It can generally be called before its declaration in the same scope",
                "It can only be called after the last line of the file",
                "It must always be assigned to a const variable",
                "It cannot accept parameters"
            ],
            "correct_answer": "It can generally be called before its declaration in the same scope",
            "explanation": "Function declarations are hoisted with their function definitions, allowing calls before the declaration in the same scope."
        },
        {
            "id": "javascript_009",
            "skill": "JavaScript",
            "topic": "Arrow functions",
            "question": "What is a key difference between an arrow function and a regular function regarding this?",
            "options": [
                "An arrow function has its own dynamically bound this",
                "An arrow function captures this from its surrounding lexical context",
                "An arrow function always binds this to window",
                "An arrow function cannot access object properties"
            ],
            "correct_answer": "An arrow function captures this from its surrounding lexical context",
            "explanation": "Arrow functions do not create their own this binding; they use the surrounding lexical this value."
        },
        {
            "id": "javascript_010",
            "skill": "JavaScript",
            "topic": "Array methods",
            "question": "Which array method creates a new array containing elements that pass a test?",
            "options": [
                "filter()",
                "findIndex()",
                "forEach()",
                "push()"
            ],
            "correct_answer": "filter()",
            "explanation": "filter returns a new array containing elements for which the callback returns a truthy value."
        },
        {
            "id": "javascript_011",
            "skill": "JavaScript",
            "topic": "Array methods",
            "question": "What is returned by [1, 2, 3].map(n => n * 2)?",
            "options": [
                "[1, 2, 3]",
                "[2, 4, 6]",
                "[1, 4, 9]",
                "6"
            ],
            "correct_answer": "[2, 4, 6]",
            "explanation": "map applies the callback to every element and creates a new array with the transformed values."
        },
        {
            "id": "javascript_012",
            "skill": "JavaScript",
            "topic": "Array methods",
            "question": "What is the result of [1, 2, 3].reduce((sum, n) => sum + n, 0)?",
            "options": [
                "3",
                "5",
                "6",
                "[1, 2, 3]"
            ],
            "correct_answer": "6",
            "explanation": "reduce accumulates the values: 0 + 1 + 2 + 3 equals 6."
        },
        {
            "id": "javascript_013",
            "skill": "JavaScript",
            "topic": "Array mutation",
            "question": "Which statement about sort() on a JavaScript array is correct?",
            "options": [
                "It always returns a sorted copy without changing the original",
                "It sorts the array in place by default using string-based ordering",
                "It only sorts numeric arrays correctly without a comparator",
                "It converts the array into a Set"
            ],
            "correct_answer": "It sorts the array in place by default using string-based ordering",
            "explanation": "sort mutates the original array. Its default ordering compares string representations, so numeric arrays often need a comparator."
        },
        {
            "id": "javascript_014",
            "skill": "JavaScript",
            "topic": "Spread syntax",
            "question": "What does [...[1, 2], 3] produce?",
            "options": [
                "[[1, 2], 3]",
                "[1, 2, 3]",
                "[3, [1, 2]]",
                "[1, [2, 3]]"
            ],
            "correct_answer": "[1, 2, 3]",
            "explanation": "Array spread expands the iterable elements into the new array."
        },
        {
            "id": "javascript_015",
            "skill": "JavaScript",
            "topic": "Destructuring",
            "question": "Given const [a, , b] = [10, 20, 30], what are the values of a and b?",
            "options": [
                "a = 10, b = 20",
                "a = 20, b = 30",
                "a = 10, b = 30",
                "a = 30, b = 10"
            ],
            "correct_answer": "a = 10, b = 30",
            "explanation": "The empty position skips the second array element, so b receives the third element, 30."
        },
        {
            "id": "javascript_016",
            "skill": "JavaScript",
            "topic": "Objects",
            "question": "What happens when a property is added to an object declared with const?",
            "options": [
                "It always throws a TypeError",
                "It is allowed unless the object itself is otherwise restricted",
                "It changes the object into a primitive",
                "It automatically freezes the object"
            ],
            "correct_answer": "It is allowed unless the object itself is otherwise restricted",
            "explanation": "const prevents reassignment of the binding, not modification of the referenced object's properties."
        },
        {
            "id": "javascript_017",
            "skill": "JavaScript",
            "topic": "Object references",
            "question": "What is printed? const a = {x: 1}; const b = a; b.x = 5; console.log(a.x);",
            "options": [
                "1",
                "5",
                "undefined",
                "A ReferenceError"
            ],
            "correct_answer": "5",
            "explanation": "Both variables refer to the same object, so changing its x property through b is visible through a."
        },
        {
            "id": "javascript_018",
            "skill": "JavaScript",
            "topic": "Shallow copying",
            "question": "What is an important limitation of using {...original} to copy an object?",
            "options": [
                "It cannot copy top-level string properties",
                "Nested objects are still shared references",
                "It always removes every property",
                "It converts all values to strings"
            ],
            "correct_answer": "Nested objects are still shared references",
            "explanation": "Object spread makes a shallow copy, so nested objects are not recursively cloned."
        },
        {
            "id": "javascript_019",
            "skill": "JavaScript",
            "topic": "Promises",
            "question": "Which three states can a Promise have?",
            "options": [
                "Created, running, deleted",
                "Pending, fulfilled, rejected",
                "Open, closed, paused",
                "True, false, undefined"
            ],
            "correct_answer": "Pending, fulfilled, rejected",
            "explanation": "A Promise begins pending and eventually settles as fulfilled or rejected."
        },
        {
            "id": "javascript_020",
            "skill": "JavaScript",
            "topic": "Promise chaining",
            "question": "What happens when a .then() callback returns a normal value rather than a Promise?",
            "options": [
                "The next Promise in the chain fulfills with that value",
                "The chain always rejects",
                "The next callback is skipped",
                "The returned value is discarded in every case"
            ],
            "correct_answer": "The next Promise in the chain fulfills with that value",
            "explanation": "Promise chaining adopts the callback's returned value, fulfilling the next Promise with it unless an error or rejected Promise is returned."
        },
        {
            "id": "javascript_021",
            "skill": "JavaScript",
            "topic": "Async and await",
            "question": "What does an async function return?",
            "options": [
                "Always a plain string",
                "A Promise",
                "Only undefined",
                "A generator object in every case"
            ],
            "correct_answer": "A Promise",
            "explanation": "An async function returns a Promise; a returned value fulfills it, while a thrown error rejects it."
        },
        {
            "id": "javascript_022",
            "skill": "JavaScript",
            "topic": "Async error handling",
            "question": "How can an error from an awaited rejected Promise be handled inside an async function?",
            "options": [
                "Only with a switch statement",
                "With try/catch around the await expression",
                "Only by calling JSON.stringify()",
                "By using break outside a loop"
            ],
            "correct_answer": "With try/catch around the await expression",
            "explanation": "A rejection encountered by await throws into the surrounding control flow and can be handled with try/catch."
        },
        {
            "id": "javascript_023",
            "skill": "JavaScript",
            "topic": "Event loop",
            "question": "What is the output order? console.log('A'); setTimeout(() => console.log('B'), 0); Promise.resolve().then(() => console.log('C')); console.log('D');",
            "options": [
                "A B C D",
                "A D C B",
                "A C D B",
                "D A B C"
            ],
            "correct_answer": "A D C B",
            "explanation": "Synchronous logs A and D run first, Promise callbacks run as microtasks, and the timer callback runs afterward."
        },
        {
            "id": "javascript_024",
            "skill": "JavaScript",
            "topic": "Promise.all",
            "question": "What happens when one input Promise rejects in Promise.all([...])?",
            "options": [
                "The returned Promise rejects with that rejection",
                "The returned Promise always fulfills with all successful values",
                "All input Promises are cancelled immediately",
                "The returned Promise ignores the rejection"
            ],
            "correct_answer": "The returned Promise rejects with that rejection",
            "explanation": "Promise.all rejects when an input rejects, although the other operations are not automatically cancelled."
        },
        {
            "id": "javascript_025",
            "skill": "JavaScript",
            "topic": "DOM selection",
            "question": "Which method returns the first element matching a CSS selector?",
            "options": [
                "document.querySelector()",
                "document.querySelectorAll()",
                "document.getElementsByClassName()",
                "document.createElement()"
            ],
            "correct_answer": "document.querySelector()",
            "explanation": "querySelector returns the first matching element or null if there is no match."
        },
        {
            "id": "javascript_026",
            "skill": "JavaScript",
            "topic": "DOM collections",
            "question": "What does document.querySelectorAll('.item') return?",
            "options": [
                "A single element only",
                "A static NodeList of matching elements",
                "A new HTML document",
                "A Promise containing matching elements"
            ],
            "correct_answer": "A static NodeList of matching elements",
            "explanation": "querySelectorAll returns a static NodeList containing elements that match the selector at query time."
        },
        {
            "id": "javascript_027",
            "skill": "JavaScript",
            "topic": "Event handling",
            "question": "What is the purpose of event.preventDefault() in a browser event handler?",
            "options": [
                "It stops every event listener from running",
                "It prevents the browser's default action when the event is cancelable",
                "It removes the event target from the DOM",
                "It automatically reloads the page"
            ],
            "correct_answer": "It prevents the browser's default action when the event is cancelable",
            "explanation": "preventDefault cancels a cancelable event's default browser action, such as a form's normal submission."
        },
        {
            "id": "javascript_028",
            "skill": "JavaScript",
            "topic": "Event propagation",
            "question": "What does event.stopPropagation() do?",
            "options": [
                "It prevents an event from propagating further through the event path",
                "It always prevents the default browser action",
                "It deletes all registered listeners",
                "It prevents JavaScript from running again"
            ],
            "correct_answer": "It prevents an event from propagating further through the event path",
            "explanation": "stopPropagation stops further propagation but does not, by itself, cancel the default action."
        },
        {
            "id": "javascript_029",
            "skill": "JavaScript",
            "topic": "Event delegation",
            "question": "Why can event delegation be useful for a list containing many child elements?",
            "options": [
                "It requires a separate listener on every child",
                "A parent listener can handle matching events from descendants through bubbling",
                "It disables event bubbling",
                "It prevents new children from being added"
            ],
            "correct_answer": "A parent listener can handle matching events from descendants through bubbling",
            "explanation": "Event delegation uses bubbling so a common ancestor can handle events from many child elements."
        },
        {
            "id": "javascript_030",
            "skill": "JavaScript",
            "topic": "JSON",
            "question": "Which statement correctly describes JSON.stringify()?",
            "options": [
                "It parses a JSON string into an object",
                "It converts a JavaScript value into a JSON string when serializable",
                "It validates every business rule in an object",
                "It creates a deep copy of every possible JavaScript value"
            ],
            "correct_answer": "It converts a JavaScript value into a JSON string when serializable",
            "explanation": "JSON.stringify serializes supported JavaScript values into JSON text; it does not support every JavaScript value or preserve all object details."
        },
        {
            "id": "javascript_031",
            "skill": "JavaScript",
            "topic": "JSON parsing",
            "question": "What happens when JSON.parse() receives malformed JSON text?",
            "options": [
                "It always returns an empty object",
                "It throws a SyntaxError",
                "It automatically repairs every error",
                "It returns the original text as an object"
            ],
            "correct_answer": "It throws a SyntaxError",
            "explanation": "JSON.parse throws a SyntaxError when the input string is not valid JSON."
        },
        {
            "id": "javascript_032",
            "skill": "JavaScript",
            "topic": "Error handling",
            "question": "Which statement about a finally block in JavaScript is correct?",
            "options": [
                "It runs only when catch handles an error",
                "It normally runs after try/catch processing whether an error occurred or not",
                "It automatically retries the try block",
                "It converts all errors into strings"
            ],
            "correct_answer": "It normally runs after try/catch processing whether an error occurred or not",
            "explanation": "finally is used for cleanup and normally executes after try/catch, including when control leaves through a return statement."
        },
        {
            "id": "javascript_033",
            "skill": "JavaScript",
            "topic": "Modules",
            "question": "In an ES module, which keyword is used to make a binding available to other modules?",
            "options": [
                "export",
                "expose",
                "publish",
                "global"
            ],
            "correct_answer": "export",
            "explanation": "ES modules use export to make functions, variables, classes, or other supported bindings available for import."
        },
        {
            "id": "javascript_034",
            "skill": "JavaScript",
            "topic": "Modules",
            "question": "What does a named import require?",
            "options": [
                "The imported binding must match an exported name unless aliased",
                "Every import must use the name default",
                "The source module must be a JSON file",
                "The imported value must always be a function"
            ],
            "correct_answer": "The imported binding must match an exported name unless aliased",
            "explanation": "Named imports refer to exported names and can use an alias with the as keyword."
        },
        {
            "id": "javascript_035",
            "skill": "JavaScript",
            "topic": "Prototypes",
            "question": "How does JavaScript normally find a property that is not an own property of an object?",
            "options": [
                "It searches the object's prototype chain",
                "It searches every variable in every browser tab",
                "It converts the object to JSON first",
                "It creates the property automatically in all cases"
            ],
            "correct_answer": "It searches the object's prototype chain",
            "explanation": "Property lookup can continue through the prototype chain until a matching property is found or the chain ends."
        },
        {
            "id": "javascript_036",
            "skill": "JavaScript",
            "topic": "Classes",
            "question": "What does the extends keyword indicate in a JavaScript class declaration?",
            "options": [
                "The class inherits from another class or constructor",
                "The class becomes a JSON document",
                "The class cannot have methods",
                "The class is converted into a Promise"
            ],
            "correct_answer": "The class inherits from another class or constructor",
            "explanation": "extends establishes an inheritance relationship, allowing the subclass to inherit behavior from its base class."
        },
        {
            "id": "javascript_037",
            "skill": "JavaScript",
            "topic": "Map and Set",
            "question": "Which statement correctly describes a JavaScript Map?",
            "options": [
                "It stores unique values only and has no keys",
                "It stores key-value pairs and can use objects as keys",
                "It only accepts string keys",
                "It automatically converts every value to JSON"
            ],
            "correct_answer": "It stores key-value pairs and can use objects as keys",
            "explanation": "Map stores key-value pairs and allows keys of any value type, including objects."
        },
        {
            "id": "javascript_038",
            "skill": "JavaScript",
            "topic": "Optional chaining",
            "question": "What does user.profile?.name evaluate to if user.profile is null?",
            "options": [
                "It throws a TypeError",
                "undefined",
                "null.profile.name",
                "false"
            ],
            "correct_answer": "undefined",
            "explanation": "Optional chaining stops property access when the value immediately before ?. is null or undefined and returns undefined."
        },
        {
            "id": "javascript_039",
            "skill": "JavaScript",
            "topic": "Nullish coalescing",
            "question": "What is the result of 0 ?? 10?",
            "options": [
                "0",
                "10",
                "null",
                "undefined"
            ],
            "correct_answer": "0",
            "explanation": "The nullish coalescing operator uses its right operand only when the left operand is null or undefined. Zero is preserved."
        },
        {
            "id": "javascript_040",
            "skill": "JavaScript",
            "topic": "Debouncing",
            "question": "Why is debouncing commonly used for a search input that triggers requests while a user types?",
            "options": [
                "To send a request after every keystroke without delay",
                "To wait for a quiet period before running the operation",
                "To sort search results automatically",
                "To guarantee that network requests never fail"
            ],
            "correct_answer": "To wait for a quiet period before running the operation",
            "explanation": "Debouncing delays an operation until a specified period passes without another triggering event, reducing unnecessary repeated work."
        }
    ],
    
    "c": [
        {
            "id": "c_001",
            "skill": "C",
            "topic": "Pointers",
            "question": "What is printed by this code? int x = 10; int *p = &x; *p = 25; printf(\"%d\", x);",
            "options": ["10", "25", "Address of x", "Compilation error"],
            "correct_answer": "25",
            "explanation": "The pointer p stores the address of x. Assigning 25 through *p changes x to 25."
        },
        {
            "id": "c_002",
            "skill": "C",
            "topic": "Pointer arithmetic",
            "question": "If int a[5] = {10, 20, 30, 40, 50}; and int *p = a;, what does *(p + 2) return?",
            "options": ["10", "20", "30", "40"],
            "correct_answer": "30",
            "explanation": "Array indexing and pointer arithmetic are related: *(p + 2) accesses the third element, a[2]."
        },
        {
            "id": "c_003",
            "skill": "C",
            "topic": "Arrays",
            "question": "What is the value of sizeof(a) / sizeof(a[0]) in the same scope where int a[8] is declared?",
            "options": ["1", "4", "8", "The number of bytes in a pointer"],
            "correct_answer": "8",
            "explanation": "For an actual array in the same scope, sizeof(a) gives the whole array size and sizeof(a[0]) gives one element's size. Their ratio is 8."
        },
        {
            "id": "c_004",
            "skill": "C",
            "topic": "Array parameters",
            "question": "When an array is passed to a function as an int parameter written int a[], what does the parameter effectively become?",
            "options": ["A complete copy of the array", "A pointer to the first element", "A structure containing the array", "A pointer to the last element"],
            "correct_answer": "A pointer to the first element",
            "explanation": "In a function parameter declaration, int a[] is adjusted to int *a. The array length is not carried automatically."
        },
        {
            "id": "c_005",
            "skill": "C",
            "topic": "Strings",
            "question": "What is the size of char s[] = \"Hello\"; including the terminating null character?",
            "options": ["5 bytes", "6 bytes", "7 bytes", "Depends on the pointer size"],
            "correct_answer": "6 bytes",
            "explanation": "The five visible characters are followed by the terminating '\\0', making six char elements."
        },
        {
            "id": "c_006",
            "skill": "C",
            "topic": "String functions",
            "question": "What does strcmp(\"cat\", \"cat\") return?",
            "options": ["1", "-1", "0", "The string length"],
            "correct_answer": "0",
            "explanation": "strcmp returns zero when the two strings are equal."
        },
        {
            "id": "c_007",
            "skill": "C",
            "topic": "Dynamic memory",
            "question": "Which function allocates a block of memory and initializes all its bytes to zero?",
            "options": ["malloc()", "calloc()", "realloc()", "free()"],
            "correct_answer": "calloc()",
            "explanation": "calloc allocates space for multiple elements and initializes all allocated bytes to zero."
        },
        {
            "id": "c_008",
            "skill": "C",
            "topic": "Dynamic memory",
            "question": "What is the purpose of free(ptr) when ptr refers to a dynamically allocated block that has not already been freed?",
            "options": ["It sets every program variable to zero", "It releases the allocated block for reuse", "It deletes the pointer variable itself", "It permanently removes the memory from the computer"],
            "correct_answer": "It releases the allocated block for reuse",
            "explanation": "free releases dynamically allocated storage. The pointer variable itself remains, so using it to access the released block is invalid."
        },
        {
            "id": "c_009",
            "skill": "C",
            "topic": "Dynamic memory",
            "question": "What should a program do if malloc() fails to allocate the requested memory?",
            "options": ["Assume the returned pointer is valid", "Check whether the returned pointer is NULL", "Call free() on every program variable", "Increase the pointer address manually"],
            "correct_answer": "Check whether the returned pointer is NULL",
            "explanation": "malloc returns NULL when allocation fails, so the program should check the result before accessing the memory."
        },
        {
            "id": "c_010",
            "skill": "C",
            "topic": "Dangling pointers",
            "question": "Which situation creates a dangling pointer?",
            "options": ["A pointer refers to a valid local variable while it is alive", "A pointer is used after the object it referred to has ceased to exist", "A pointer is initialized to NULL", "A pointer refers to the first element of a valid array"],
            "correct_answer": "A pointer is used after the object it referred to has ceased to exist",
            "explanation": "A dangling pointer refers to storage whose lifetime has ended or which has been released."
        },
        {
            "id": "c_011",
            "skill": "C",
            "topic": "Function pointers",
            "question": "What can a function pointer be used for in C?",
            "options": ["Storing a function's address for indirect calls", "Automatically allocating arrays", "Changing a function's return type at runtime", "Creating a new data type without a declaration"],
            "correct_answer": "Storing a function's address for indirect calls",
            "explanation": "A function pointer can refer to a compatible function and allow the program to call it indirectly."
        },
        {
            "id": "c_012",
            "skill": "C",
            "topic": "Recursion",
            "question": "What is the main purpose of a base case in a recursive function?",
            "options": ["To allocate more memory on every call", "To stop recursion when a condition is reached", "To guarantee constant execution time", "To convert recursion into a pointer"],
            "correct_answer": "To stop recursion when a condition is reached",
            "explanation": "A base case ends further recursive calls for the relevant input, preventing endless recursion."
        },
        {
            "id": "c_013",
            "skill": "C",
            "topic": "Storage classes",
            "question": "What is a key property of a local variable declared with static inside a function?",
            "options": ["It is recreated and reset on every call", "It retains its value between function calls", "It is automatically visible in every source file", "It must be allocated dynamically"],
            "correct_answer": "It retains its value between function calls",
            "explanation": "A block-scope static variable has static storage duration and retains its stored value between calls."
        },
        {
            "id": "c_014",
            "skill": "C",
            "topic": "Scope",
            "question": "What does the extern keyword commonly indicate in a variable declaration?",
            "options": ["The variable must be a local variable", "The declaration refers to an object defined elsewhere or declared later", "The variable is always stored on the heap", "The variable cannot be accessed by another function"],
            "correct_answer": "The declaration refers to an object defined elsewhere or declared later",
            "explanation": "extern commonly declares an object with external linkage that is defined elsewhere, or refers to a compatible declaration."
        },
        {
            "id": "c_015",
            "skill": "C",
            "topic": "Preprocessor",
            "question": "Why can a function-like macro such as #define SQUARE(x) ((x) * (x)) be dangerous when called as SQUARE(i++)?",
            "options": ["Macros cannot accept arguments", "The argument expression may be evaluated more than once", "The preprocessor automatically allocates memory", "The macro always returns a pointer"],
            "correct_answer": "The argument expression may be evaluated more than once",
            "explanation": "The macro substitutes its argument in two places, so i++ appears twice and can cause undefined behavior because of unsequenced modifications."
        },
        {
            "id": "c_016",
            "skill": "C",
            "topic": "Operator precedence",
            "question": "What is the value of x after int x = 2 + 3 * 4;?",
            "options": ["20", "14", "24", "11"],
            "correct_answer": "14",
            "explanation": "Multiplication has higher precedence than addition, so the expression evaluates as 2 + 12."
        },
        {
            "id": "c_017",
            "skill": "C",
            "topic": "Integer division",
            "question": "What is the value of 7 / 2 when both operands have type int?",
            "options": ["3", "3.5", "4", "A compilation error"],
            "correct_answer": "3",
            "explanation": "Integer division of two integers discards the fractional part of the result."
        },
        {
            "id": "c_018",
            "skill": "C",
            "topic": "Bitwise operators",
            "question": "What is the result of 5 & 3 using the bitwise AND operator?",
            "options": ["1", "2", "6", "7"],
            "correct_answer": "1",
            "explanation": "Binary 5 is 0101 and binary 3 is 0011. Their bitwise AND is 0001, which equals 1."
        },
        {
            "id": "c_019",
            "skill": "C",
            "topic": "Bitwise operators",
            "question": "For a nonnegative int x, what does x << 1 do when the result is representable in int?",
            "options": ["Shifts the bits one position to the right", "Shifts the bits one position to the left", "Sets every bit to zero", "Reverses the bit order"],
            "correct_answer": "Shifts the bits one position to the left",
            "explanation": "The left-shift operator moves the bit pattern left by one position. For nonnegative x with a representable result, this corresponds to multiplying by two."
        },
        {
            "id": "c_020",
            "skill": "C",
            "topic": "Undefined behavior",
            "question": "What is the most accurate statement about evaluating i = i++ + 1 in standard C?",
            "options": ["It always assigns i plus two", "It always assigns i plus one", "It has undefined behavior because i is modified without the required sequencing", "It always assigns zero"],
            "correct_answer": "It has undefined behavior because i is modified without the required sequencing",
            "explanation": "The expression modifies i through both the postfix increment and assignment without the sequencing required by C."
        },
        {
            "id": "c_021",
            "skill": "C",
            "topic": "Structures",
            "question": "What is a key difference between a C structure and a C union?",
            "options": ["A structure cannot contain integers", "Structure members have separate storage, while union members share storage", "A union can only contain pointers", "Structure members must all have the same type"],
            "correct_answer": "Structure members have separate storage, while union members share storage",
            "explanation": "A structure allocates storage for its members separately, whereas union members overlap the same storage region."
        },
        {
            "id": "c_022",
            "skill": "C",
            "topic": "Typedef",
            "question": "What is the main purpose of typedef in C?",
            "options": ["To define an alias for an existing type", "To allocate memory dynamically", "To execute a function automatically", "To make all variables constant"],
            "correct_answer": "To define an alias for an existing type",
            "explanation": "typedef introduces an alternative type name, which can make declarations clearer."
        },
        {
            "id": "c_023",
            "skill": "C",
            "topic": "Enumerations",
            "question": "If enum Color { RED, GREEN, BLUE }; uses the default enumerator values, what is the value of GREEN?",
            "options": ["0", "1", "2", "3"],
            "correct_answer": "1",
            "explanation": "By default, enumeration constants start at zero and increase by one, making RED 0, GREEN 1, and BLUE 2."
        },
        {
            "id": "c_024",
            "skill": "C",
            "topic": "Const correctness",
            "question": "What does const int *p mean?",
            "options": ["p cannot point to another object", "The int value accessed through p cannot be modified through p", "The pointer and every object are always immutable", "p must be initialized to NULL"],
            "correct_answer": "The int value accessed through p cannot be modified through p",
            "explanation": "const int *p is a pointer to const int. The pointer can be reassigned, but the pointed-to value cannot be modified through that pointer."
        },
        {
            "id": "c_025",
            "skill": "C",
            "topic": "Pointer declarations",
            "question": "In the declaration int *p, *q;, what are the types of p and q?",
            "options": ["Both are int variables", "Both are pointers to int", "p is a pointer and q is an int variable", "p is an int and q is a pointer"],
            "correct_answer": "Both are pointers to int",
            "explanation": "The asterisk applies separately to each declarator, so both p and q are pointers to int."
        },
        {
            "id": "c_026",
            "skill": "C",
            "topic": "Command-line arguments",
            "question": "In int main(int argc, char *argv[]), what does argc represent?",
            "options": ["The number of command-line arguments including the program name", "The number of characters in the first argument", "The number of functions in the program", "The address of the argument array"],
            "correct_answer": "The number of command-line arguments including the program name",
            "explanation": "argc gives the count of argument strings supplied through argv, including the program name when provided by the host environment."
        },
        {
            "id": "c_027",
            "skill": "C",
            "topic": "File handling",
            "question": "Why should a program check whether fopen() returns NULL?",
            "options": ["Because fopen always returns NULL", "Because opening a file can fail", "Because NULL indicates the file was successfully closed", "Because fopen returns the file contents directly"],
            "correct_answer": "Because opening a file can fail",
            "explanation": "fopen returns NULL if it cannot open the requested file, so the program must check for failure before using the FILE pointer."
        },
        {
            "id": "c_028",
            "skill": "C",
            "topic": "File handling",
            "question": "What does fclose(fp) do when fp refers to an open stream?",
            "options": ["Deletes the file from the filesystem", "Closes the stream and flushes buffered output as required", "Resets the file contents to zero", "Converts the file to read-only mode"],
            "correct_answer": "Closes the stream and flushes buffered output as required",
            "explanation": "fclose closes the stream and handles buffered output before releasing associated stream resources."
        },
        {
            "id": "c_029",
            "skill": "C",
            "topic": "Input handling",
            "question": "Why is scanf(\"%s\", buffer) risky when buffer has a fixed size and no field width is specified?",
            "options": ["It always reads the entire file", "It can write beyond the buffer if the input word is too long", "It cannot read strings", "It automatically frees the buffer"],
            "correct_answer": "It can write beyond the buffer if the input word is too long",
            "explanation": "Without a width limit, %s can store more characters than the buffer can hold, causing a buffer overflow."
        },
        {
            "id": "c_030",
            "skill": "C",
            "topic": "Input handling",
            "question": "What is a useful property of fgets(buffer, sizeof buffer, stdin) compared with an unbounded %s conversion?",
            "options": ["It limits the number of characters read to the buffer capacity", "It always reads only one character", "It removes every newline from the input automatically", "It allocates an unlimited buffer"],
            "correct_answer": "It limits the number of characters read to the buffer capacity",
            "explanation": "fgets reads at most one fewer character than the buffer size and then adds a terminating null character when it reads successfully."
        },
        {
            "id": "c_031",
            "skill": "C",
            "topic": "Header files",
            "question": "What is the purpose of include guards in a C header file?",
            "options": ["To prevent the header's contents from being processed more than once in a translation unit", "To encrypt the header file", "To stop every other header from being included", "To automatically link all libraries"],
            "correct_answer": "To prevent the header's contents from being processed more than once in a translation unit",
            "explanation": "Include guards use preprocessor conditions to prevent repeated inclusion of the same header's contents within one translation unit."
        },
        {
            "id": "c_032",
            "skill": "C",
            "topic": "Compilation",
            "question": "Which stage normally resolves references between separately compiled object files and libraries?",
            "options": ["Preprocessing", "Linking", "Lexical analysis", "Runtime input"],
            "correct_answer": "Linking",
            "explanation": "The linker combines object files and libraries and resolves external symbol references."
        },
        {
            "id": "c_033",
            "skill": "C",
            "topic": "Function arguments",
            "question": "How does C normally pass an ordinary int argument to a function?",
            "options": ["By value", "By reference automatically", "By copying the entire process memory", "By passing the variable's name"],
            "correct_answer": "By value",
            "explanation": "C passes arguments by value. A function that needs to modify a caller's variable can receive a pointer to it."
        },
        {
            "id": "c_034",
            "skill": "C",
            "topic": "Return values",
            "question": "What is the purpose of returning a pointer from a function when the pointer refers to dynamically allocated memory?",
            "options": ["To let the caller access the allocated object and later release it", "To make the allocated object disappear immediately", "To turn the pointer into an integer automatically", "To prevent the caller from accessing the memory"],
            "correct_answer": "To let the caller access the allocated object and later release it",
            "explanation": "Dynamically allocated storage remains allocated until it is released, so returning its pointer can let the caller use and eventually free it."
        },
        {
            "id": "c_035",
            "skill": "C",
            "topic": "Memory layout",
            "question": "Which storage duration does an ordinary non-static local variable have?",
            "options": ["Static storage duration", "Automatic storage duration", "Thread storage duration in every case", "Dynamic storage duration"],
            "correct_answer": "Automatic storage duration",
            "explanation": "An ordinary local variable generally has automatic storage duration, lasting for its enclosing block execution."
        },
        {
            "id": "c_036",
            "skill": "C",
            "topic": "Volatile",
            "question": "What does the volatile type qualifier primarily tell the compiler?",
            "options": ["The object is always thread-safe", "Accesses to the object have observable behavior that must be respected by the implementation", "The object is stored permanently on disk", "The object can never change"],
            "correct_answer": "Accesses to the object have observable behavior that must be respected by the implementation",
            "explanation": "volatile is useful for objects that can change outside ordinary program flow, but it does not provide general thread synchronization or atomicity."
        },
        {
            "id": "c_037",
            "skill": "C",
            "topic": "Macros and parentheses",
            "question": "Why should a macro such as #define DOUBLE(x) (2 * (x)) use parentheses around its parameter?",
            "options": ["To help preserve the intended expression grouping when an expression is passed", "To allocate memory for x", "To make the macro recursive", "To prevent the macro from accepting integers"],
            "correct_answer": "To help preserve the intended expression grouping when an expression is passed",
            "explanation": "Parenthesizing a macro parameter reduces precedence-related surprises when the argument is an expression."
        },
        {
            "id": "c_038",
            "skill": "C",
            "topic": "Linked lists",
            "question": "In a singly linked list, what information does a typical node contain?",
            "options": ["Only a pointer to the previous node", "Data and a pointer to the next node", "A complete copy of the whole list", "Only an array index"],
            "correct_answer": "Data and a pointer to the next node",
            "explanation": "A typical singly linked-list node stores its data and a link to the next node, with the final node pointing to NULL."
        },
        {
            "id": "c_039",
            "skill": "C",
            "topic": "Time complexity",
            "question": "What is the time complexity of binary search on a sorted array of n elements?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n squared)"],
            "correct_answer": "O(log n)",
            "explanation": "Binary search repeatedly halves the remaining search interval, resulting in logarithmic time complexity."
        },
        {
            "id": "c_040",
            "skill": "C",
            "topic": "Memory safety",
            "question": "Which action is undefined behavior in C?",
            "options": ["Reading an initialized int variable", "Accessing an array element within its bounds", "Dereferencing a null pointer", "Comparing two valid integer values"],
            "correct_answer": "Dereferencing a null pointer",
            "explanation": "Dereferencing a null pointer is undefined behavior because it does not refer to a valid object."
        }
    ],
    
    "c++": [
        {
            "id": "cpp_001",
            "skill": "C++",
            "topic": "Classes and objects",
            "question": "What is the main difference between a class and an object in C++?",
            "options": [
                "A class defines a type, while an object is an instance of that type",
                "A class is always stored on the heap, while an object is always stored on the stack",
                "An object defines a type, while a class is an instance",
                "Classes can contain functions, but objects cannot call them"
            ],
            "correct_answer": "A class defines a type, while an object is an instance of that type",
            "explanation": "A class defines members and behavior. An object is an instance created from that class."
        },
        {
            "id": "cpp_002",
            "skill": "C++",
            "topic": "Access control",
            "question": "What is the default access level for members of a C++ class?",
            "options": ["public", "protected", "private", "internal"],
            "correct_answer": "private",
            "explanation": "Members of a class are private by default. Members of a struct are public by default."
        },
        {
            "id": "cpp_003",
            "skill": "C++",
            "topic": "Constructors",
            "question": "When is a constructor normally called for an object?",
            "options": [
                "When the object is initialized",
                "Only when the program ends",
                "Whenever any member function is called",
                "Only when the object is deleted"
            ],
            "correct_answer": "When the object is initialized",
            "explanation": "A constructor initializes an object as it is created."
        },
        {
            "id": "cpp_004",
            "skill": "C++",
            "topic": "Destructors",
            "question": "What is the purpose of a destructor in C++?",
            "options": [
                "To initialize every object with default values",
                "To perform cleanup when an object's lifetime ends",
                "To overload arithmetic operators automatically",
                "To create a copy of an object"
            ],
            "correct_answer": "To perform cleanup when an object's lifetime ends",
            "explanation": "A destructor can release resources owned by an object when its lifetime ends."
        },
        {
            "id": "cpp_005",
            "skill": "C++",
            "topic": "Function overloading",
            "question": "Which change can create a valid overloaded function in C++?",
            "options": [
                "Changing only the return type",
                "Changing the number or types of parameters",
                "Changing only the function body",
                "Changing only the parameter names"
            ],
            "correct_answer": "Changing the number or types of parameters",
            "explanation": "Overloaded functions must have distinguishable parameter lists; return type alone is insufficient."
        },
        {
            "id": "cpp_006",
            "skill": "C++",
            "topic": "References",
            "question": "Which statement about an ordinary C++ reference is correct?",
            "options": [
                "It must be initialized when declared",
                "It always stores a null value initially",
                "It can be reseated to refer to another object later",
                "It must be allocated using new"
            ],
            "correct_answer": "It must be initialized when declared",
            "explanation": "An ordinary reference must be initialized to refer to an object or function and cannot later be reseated."
        },
        {
            "id": "cpp_007",
            "skill": "C++",
            "topic": "Pointers",
            "question": "What is the effect of *p = 15 when p is a valid int pointer to x?",
            "options": [
                "It changes the pointer's address to 15",
                "It assigns 15 to the pointed-to integer",
                "It deletes the pointed-to object",
                "It creates a new integer automatically"
            ],
            "correct_answer": "It assigns 15 to the pointed-to integer",
            "explanation": "The unary * operator dereferences the pointer, allowing access to the object it points to."
        },
        {
            "id": "cpp_008",
            "skill": "C++",
            "topic": "Const references",
            "question": "Why is a parameter such as const std::string& name often useful?",
            "options": [
                "It avoids copying the string and prevents modification through that reference",
                "It always creates a new copy of the string",
                "It makes the original string permanently immutable",
                "It guarantees that the string is stored on the heap"
            ],
            "correct_answer": "It avoids copying the string and prevents modification through that reference",
            "explanation": "A const reference can avoid copying an existing string and prevents changes through that parameter, though other references may still modify the object."
        },
        {
            "id": "cpp_009",
            "skill": "C++",
            "topic": "Inheritance",
            "question": "What does public inheritance normally preserve for the public and protected members of a base class?",
            "options": [
                "Public members become private and protected members become public",
                "Public members remain public and protected members remain protected in the derived class",
                "All base members become public",
                "All base members become inaccessible"
            ],
            "correct_answer": "Public members remain public and protected members remain protected in the derived class",
            "explanation": "With public inheritance, public and protected access levels are preserved in the derived class; private base members are not directly accessible there."
        },
        {
            "id": "cpp_010",
            "skill": "C++",
            "topic": "Runtime polymorphism",
            "question": "Which feature enables runtime dispatch to a derived-class implementation through a base-class pointer?",
            "options": [
                "A virtual function",
                "A static local variable",
                "A function-like macro",
                "A typedef declaration"
            ],
            "correct_answer": "A virtual function",
            "explanation": "Virtual functions support dynamic dispatch when called through a base pointer or reference."
        },
        {
            "id": "cpp_011",
            "skill": "C++",
            "topic": "Virtual destructors",
            "question": "Why should a polymorphic base class generally have a virtual destructor when objects may be deleted through base pointers?",
            "options": [
                "To allow the appropriate derived destructor to run during deletion",
                "To prevent all derived classes from declaring destructors",
                "To make the base class abstract automatically",
                "To make object allocation faster in every case"
            ],
            "correct_answer": "To allow the appropriate derived destructor to run during deletion",
            "explanation": "Deleting a derived object through a base pointer requires a virtual base destructor for defined behavior and correct derived-object cleanup."
        },
        {
            "id": "cpp_012",
            "skill": "C++",
            "topic": "Abstract classes",
            "question": "What makes a C++ class abstract?",
            "options": [
                "It contains at least one pure virtual function that remains unimplemented in that class",
                "It contains only private data members",
                "It has a constructor with no parameters",
                "It contains at least one static function"
            ],
            "correct_answer": "It contains at least one pure virtual function that remains unimplemented in that class",
            "explanation": "A class with a pure virtual function that is not overridden to provide an implementation in that class is abstract and cannot be instantiated directly."
        },
        {
            "id": "cpp_013",
            "skill": "C++",
            "topic": "Operator overloading",
            "question": "Which statement about operator overloading in C++ is correct?",
            "options": [
                "It can change the precedence of an operator",
                "It can define operator behavior for user-defined types, subject to language rules",
                "It allows every operator to be overloaded",
                "It changes the meaning of operators for all built-in types"
            ],
            "correct_answer": "It can define operator behavior for user-defined types, subject to language rules",
            "explanation": "Operator overloading customizes eligible operators for user-defined types but cannot change precedence or overload every operator."
        },
        {
            "id": "cpp_014",
            "skill": "C++",
            "topic": "Copy constructors",
            "question": "What is the main purpose of a copy constructor?",
            "options": [
                "To initialize an object from another object of the same class",
                "To destroy an existing object",
                "To convert every object into an integer",
                "To allocate global variables"
            ],
            "correct_answer": "To initialize an object from another object of the same class",
            "explanation": "A copy constructor initializes a new object using an existing object of the same class."
        },
        {
            "id": "cpp_015",
            "skill": "C++",
            "topic": "Move semantics",
            "question": "What is a primary benefit of move semantics for a type that owns a large dynamic resource?",
            "options": [
                "It can transfer resource ownership instead of copying the resource contents",
                "It guarantees that every operation becomes constant time",
                "It prevents objects from being destroyed",
                "It converts all pointers into references"
            ],
            "correct_answer": "It can transfer resource ownership instead of copying the resource contents",
            "explanation": "Move operations can transfer resources from an object rather than performing an expensive deep copy."
        },
        {
            "id": "cpp_016",
            "skill": "C++",
            "topic": "RAII",
            "question": "What is the central idea of RAII in C++?",
            "options": [
                "Manage resource lifetime through object lifetime",
                "Allocate every resource globally",
                "Manually release every resource at the end of main only",
                "Avoid constructors and destructors"
            ],
            "correct_answer": "Manage resource lifetime through object lifetime",
            "explanation": "RAII ties resource acquisition and release to an object's lifetime, usually through constructors and destructors."
        },
        {
            "id": "cpp_017",
            "skill": "C++",
            "topic": "Smart pointers",
            "question": "Which smart pointer type represents exclusive ownership of a dynamically managed object?",
            "options": [
                "std::unique_ptr",
                "std::weak_ptr",
                "std::string",
                "std::initializer_list"
            ],
            "correct_answer": "std::unique_ptr",
            "explanation": "std::unique_ptr has exclusive ownership and is not copyable, though it can transfer ownership through moves."
        },
        {
            "id": "cpp_018",
            "skill": "C++",
            "topic": "Shared ownership",
            "question": "How does std::shared_ptr normally determine when its managed object can be destroyed?",
            "options": [
                "When its reference count reaches zero",
                "Immediately after the first copy",
                "Only when the operating system shuts down",
                "Whenever any shared_ptr is assigned a new value"
            ],
            "correct_answer": "When its reference count reaches zero",
            "explanation": "The managed object is released when the last shared owner relinquishes ownership, so the shared ownership count reaches zero."
        },
        {
            "id": "cpp_019",
            "skill": "C++",
            "topic": "Memory safety",
            "question": "What is a use-after-free error?",
            "options": [
                "Using an object after its storage has been released",
                "Reading an initialized local integer",
                "Calling a valid constructor",
                "Copying a standard string"
            ],
            "correct_answer": "Using an object after its storage has been released",
            "explanation": "Accessing an object after its lifetime or allocated storage has ended is invalid and can cause undefined behavior."
        },
        {
            "id": "cpp_020",
            "skill": "C++",
            "topic": "STL containers",
            "question": "Which standard container provides fast random access by index and stores elements contiguously?",
            "options": [
                "std::vector",
                "std::list",
                "std::map",
                "std::set"
            ],
            "correct_answer": "std::vector",
            "explanation": "std::vector stores its elements contiguously and provides constant-time random access by index."
        },
        {
            "id": "cpp_021",
            "skill": "C++",
            "topic": "Associative containers",
            "question": "Which property distinguishes std::map from std::unordered_map?",
            "options": [
                "std::map maintains keys in sorted order",
                "std::map permits only integer keys",
                "std::map always provides average constant-time lookup",
                "std::map cannot store mapped values"
            ],
            "correct_answer": "std::map maintains keys in sorted order",
            "explanation": "std::map orders keys according to its comparison object, while std::unordered_map uses hashing and does not guarantee sorted iteration."
        },
        {
            "id": "cpp_022",
            "skill": "C++",
            "topic": "Sets",
            "question": "What happens when the same key is inserted twice into a std::set?",
            "options": [
                "The set stores two copies",
                "The set maintains only one equivalent key",
                "The program must always terminate",
                "The set automatically changes into a vector"
            ],
            "correct_answer": "The set maintains only one equivalent key",
            "explanation": "std::set stores unique keys according to its comparison relation, so equivalent keys are not duplicated."
        },
        {
            "id": "cpp_023",
            "skill": "C++",
            "topic": "Iterators",
            "question": "What does std::sort(first, last) normally sort?",
            "options": [
                "The elements in the half-open range [first, last)",
                "Only the element at first",
                "The elements before first",
                "Every element in every container in the program"
            ],
            "correct_answer": "The elements in the half-open range [first, last)",
            "explanation": "std::sort orders the elements from first up to, but not including, last and requires random-access iterators."
        },
        {
            "id": "cpp_024",
            "skill": "C++",
            "topic": "Complexity",
            "question": "What is the average time complexity of searching for a key in a well-behaved std::unordered_map?",
            "options": [
                "O(1)",
                "O(log n)",
                "O(n log n)",
                "O(n squared) in every case"
            ],
            "correct_answer": "O(1)",
            "explanation": "Hash-table lookup in std::unordered_map is average constant time, although worst-case lookup can be linear."
        },
        {
            "id": "cpp_025",
            "skill": "C++",
            "topic": "Templates",
            "question": "What is the primary purpose of a function template in C++?",
            "options": [
                "To write a function pattern that can work with multiple types",
                "To execute a function before compilation",
                "To force every argument to be a string",
                "To prevent compiler type checking"
            ],
            "correct_answer": "To write a function pattern that can work with multiple types",
            "explanation": "Templates allow generic code to be instantiated for compatible types at compile time."
        },
        {
            "id": "cpp_026",
            "skill": "C++",
            "topic": "Template deduction",
            "question": "For template<class T> T add(T a, T b), why might add(2, 3.5) fail template argument deduction?",
            "options": [
                "The arguments suggest different types for the same T",
                "Templates cannot accept arithmetic types",
                "Function templates cannot return values",
                "The function must be declared virtual"
            ],
            "correct_answer": "The arguments suggest different types for the same T",
            "explanation": "Template argument deduction generally cannot deduce a single T from conflicting argument types in this signature without an explicit conversion or different template design."
        },
        {
            "id": "cpp_027",
            "skill": "C++",
            "topic": "Lambda expressions",
            "question": "What does [&] mean in a C++ lambda capture list?",
            "options": [
                "Capture odr-used local variables by reference when permitted",
                "Capture every variable by value",
                "Capture only global variables by reference",
                "Prevent the lambda from accessing local variables"
            ],
            "correct_answer": "Capture odr-used local variables by reference when permitted",
            "explanation": "A default reference capture lets a lambda capture eligible local variables it uses by reference; their lifetimes must be managed carefully."
        },
        {
            "id": "cpp_028",
            "skill": "C++",
            "topic": "Lambda expressions",
            "question": "What is a key effect of declaring a lambda with mutable when it captures a variable by value?",
            "options": [
                "It permits modification of the lambda's captured copy",
                "It modifies the original variable automatically",
                "It makes the lambda execute on another thread",
                "It converts all captures into references"
            ],
            "correct_answer": "It permits modification of the lambda's captured copy",
            "explanation": "mutable allows a lambda's call operator to modify its by-value captured state, without automatically changing the original variable."
        },
        {
            "id": "cpp_029",
            "skill": "C++",
            "topic": "Exception handling",
            "question": "When an exception is thrown in C++, what normally happens to fully constructed local automatic objects while the stack unwinds?",
            "options": [
                "Their destructors are called",
                "They are all intentionally leaked",
                "Their constructors run again",
                "Their member functions are all called twice"
            ],
            "correct_answer": "Their destructors are called",
            "explanation": "Stack unwinding destroys fully constructed automatic objects, which is an important part of RAII-based cleanup."
        },
        {
            "id": "cpp_030",
            "skill": "C++",
            "topic": "Exception specifications",
            "question": "What does noexcept communicate about a C++ function?",
            "options": [
                "The function is guaranteed to return an integer",
                "The function is specified not to let exceptions escape",
                "The function cannot call other functions",
                "The function always runs without allocating memory"
            ],
            "correct_answer": "The function is specified not to let exceptions escape",
            "explanation": "If an exception escapes a noexcept function, the runtime calls std::terminate."
        },
        {
            "id": "cpp_031",
            "skill": "C++",
            "topic": "Const member functions",
            "question": "What does the const qualifier at the end of a non-static member function declaration mean?",
            "options": [
                "The function cannot modify the object's non-mutable data members through this",
                "The function can never return a value",
                "The function can only be called from a constructor",
                "The function is automatically static"
            ],
            "correct_answer": "The function cannot modify the object's non-mutable data members through this",
            "explanation": "A const member function treats this as pointing to a const object, preventing modification of non-mutable data members through that access."
        },
        {
            "id": "cpp_032",
            "skill": "C++",
            "topic": "Static members",
            "question": "How many copies of a static data member normally exist for a class, regardless of how many ordinary instances are created?",
            "options": [
                "One shared class member",
                "One separate copy for every object",
                "Exactly two copies",
                "No storage is ever required"
            ],
            "correct_answer": "One shared class member",
            "explanation": "A static data member belongs to the class rather than to each individual object."
        },
        {
            "id": "cpp_033",
            "skill": "C++",
            "topic": "Initialization",
            "question": "What is a key advantage of using a constructor member initializer list?",
            "options": [
                "It initializes bases and members directly, including members that cannot be assigned later",
                "It guarantees that members initialize in the textual order of the list",
                "It allows const members to be assigned repeatedly",
                "It prevents base-class constructors from running"
            ],
            "correct_answer": "It initializes bases and members directly, including members that cannot be assigned later",
            "explanation": "Initializer lists directly initialize bases and members. Actual initialization order follows base and member declaration order, not list order."
        },
        {
            "id": "cpp_034",
            "skill": "C++",
            "topic": "Rule of three and five",
            "question": "When a class manually manages a resource and needs custom copy and destruction behavior, what does the Rule of Three advise considering?",
            "options": [
                "A destructor, copy constructor, and copy-assignment operator",
                "Three default constructors",
                "Three virtual functions in every class",
                "Three global variables for every resource"
            ],
            "correct_answer": "A destructor, copy constructor, and copy-assignment operator",
            "explanation": "The Rule of Three advises that if a class needs one of these resource-management operations, it may need all three to manage copying and cleanup safely."
        },
        {
            "id": "cpp_035",
            "skill": "C++",
            "topic": "Dynamic allocation",
            "question": "Which statement correctly contrasts new and delete in ordinary single-object allocation?",
            "options": [
                "new creates an object and delete releases its dynamically allocated storage",
                "new releases storage and delete creates an object",
                "new and delete are interchangeable with malloc and free in every respect",
                "delete can only be used with stack objects"
            ],
            "correct_answer": "new creates an object and delete releases its dynamically allocated storage",
            "explanation": "new allocates storage and initializes an object; delete destroys the object and releases its storage. Array allocations require matching delete[]."
        },
        {
            "id": "cpp_036",
            "skill": "C++",
            "topic": "Smart pointers",
            "question": "Why should cyclic ownership between std::shared_ptr objects be handled carefully?",
            "options": [
                "Their reference counts may never reach zero, causing a memory leak",
                "They automatically convert into unique_ptr objects",
                "They make all pointers invalid immediately",
                "They prevent destructors from being declared"
            ],
            "correct_answer": "Their reference counts may never reach zero, causing a memory leak",
            "explanation": "A cycle of shared ownership can keep reference counts above zero. std::weak_ptr can break such ownership cycles."
        },
        {
            "id": "cpp_037",
            "skill": "C++",
            "topic": "Move operations",
            "question": "Which standard utility is commonly used to cast an expression to an rvalue reference category for move-aware operations?",
            "options": [
                "std::move",
                "std::copy",
                "std::swap",
                "std::size"
            ],
            "correct_answer": "std::move",
            "explanation": "std::move enables move-aware overload resolution by casting to an rvalue expression; it does not itself move resources."
        },
        {
            "id": "cpp_038",
            "skill": "C++",
            "topic": "Namespaces",
            "question": "What is the main purpose of a namespace in C++?",
            "options": [
                "To group names and reduce naming conflicts",
                "To allocate all variables on the heap",
                "To make every function virtual",
                "To replace the type system"
            ],
            "correct_answer": "To group names and reduce naming conflicts",
            "explanation": "Namespaces organize declarations and help avoid naming collisions between libraries and program components."
        },
        {
            "id": "cpp_039",
            "skill": "C++",
            "topic": "Concurrency",
            "question": "What does std::lock_guard<std::mutex> normally do when constructed with a mutex reference?",
            "options": [
                "Locks the mutex and unlocks it when the guard's lifetime ends",
                "Creates a new operating-system process",
                "Permanently locks the mutex",
                "Automatically makes every shared variable atomic"
            ],
            "correct_answer": "Locks the mutex and unlocks it when the guard's lifetime ends",
            "explanation": "std::lock_guard uses RAII to acquire a mutex on construction and release it when the guard is destroyed."
        },
        {
            "id": "cpp_040",
            "skill": "C++",
            "topic": "Undefined behavior",
            "question": "What is the main risk of using an iterator after a vector operation has invalidated it?",
            "options": [
                "The iterator is guaranteed to point to the first element",
                "Using the invalidated iterator can cause undefined behavior",
                "The vector automatically restores the iterator",
                "The iterator always becomes a valid end iterator"
            ],
            "correct_answer": "Using the invalidated iterator can cause undefined behavior",
            "explanation": "Operations such as vector reallocation can invalidate iterators, pointers, and references to its elements. Using invalidated handles is unsafe."
        }
    ],
    
    "html": [
        {
            "id": "html_001",
            "skill": "HTML",
            "topic": "Document structure",
            "question": "Why is <!DOCTYPE html> placed at the beginning of a modern HTML document?",
            "options": ["To load CSS files", "To tell the browser to use standards mode", "To declare the page language", "To execute JavaScript"],
            "correct_answer": "To tell the browser to use standards mode",
            "explanation": "The HTML doctype tells browsers to render the document using standards mode."
        },
        {
            "id": "html_002",
            "skill": "HTML",
            "topic": "Semantic HTML",
            "question": "Which element is most appropriate for the main, unique content of a webpage?",
            "options": ["<section>", "<main>", "<aside>", "<footer>"],
            "correct_answer": "<main>",
            "explanation": "The main element identifies the dominant content of the document."
        },
        {
            "id": "html_003",
            "skill": "HTML",
            "topic": "Semantic HTML",
            "question": "Which element is most appropriate for a self-contained blog post that could be distributed independently?",
            "options": ["<article>", "<span>", "<nav>", "<strong>"],
            "correct_answer": "<article>",
            "explanation": "An article represents self-contained content such as a blog post or news story."
        },
        {
            "id": "html_004",
            "skill": "HTML",
            "topic": "Semantic HTML",
            "question": "What is the primary purpose of the <nav> element?",
            "options": ["To display images", "To identify a major navigation section", "To create a form submission", "To define a table row"],
            "correct_answer": "To identify a major navigation section",
            "explanation": "The nav element identifies a section containing important navigation links."
        },
        {
            "id": "html_005",
            "skill": "HTML",
            "topic": "Accessibility",
            "question": "Which is the best way to provide a text alternative for an informative image?",
            "options": ["Add a title to the page", "Provide meaningful alt text on the img element", "Place the image inside a div", "Set the image width"],
            "correct_answer": "Provide meaningful alt text on the img element",
            "explanation": "Useful alt text communicates the image's relevant information to people who cannot see it."
        },
        {
            "id": "html_006",
            "skill": "HTML",
            "topic": "Accessibility",
            "question": "Why should a form control normally have an associated label?",
            "options": ["To increase the file size", "To identify the control and improve accessible interaction", "To make every field required", "To submit the form automatically"],
            "correct_answer": "To identify the control and improve accessible interaction",
            "explanation": "An associated label provides an accessible name and can let users activate the control by clicking the label."
        },
        {
            "id": "html_007",
            "skill": "HTML",
            "topic": "Forms",
            "question": "Which attribute connects a label to an input whose id is email?",
            "options": ["name=\"email\"", "for=\"email\"", "target=\"email\"", "action=\"email\""],
            "correct_answer": "for=\"email\"",
            "explanation": "The label's for value matches the associated control's id."
        },
        {
            "id": "html_008",
            "skill": "HTML",
            "topic": "Forms",
            "question": "What is the default type of a button inside a form when no type attribute is specified?",
            "options": ["button", "submit", "reset", "menu"],
            "correct_answer": "submit",
            "explanation": "A button inside a form defaults to submit unless its type is specified otherwise."
        },
        {
            "id": "html_009",
            "skill": "HTML",
            "topic": "Forms",
            "question": "Which input type provides built-in validation for a typical email address format?",
            "options": ["type=\"text\"", "type=\"email\"", "type=\"password\"", "type=\"search\""],
            "correct_answer": "type=\"email\"",
            "explanation": "The email input type provides browser-level validation for an email-like value, but does not verify that the address exists."
        },
        {
            "id": "html_010",
            "skill": "HTML",
            "topic": "Forms",
            "question": "What does the required attribute do on a supported form control?",
            "options": ["Makes the control read-only", "Prevents normal form submission when the control is empty or otherwise invalid", "Automatically fills the control", "Hides the control"],
            "correct_answer": "Prevents normal form submission when the control is empty or otherwise invalid",
            "explanation": "Browser constraint validation checks required controls before normal form submission."
        },
        {
            "id": "html_011",
            "skill": "HTML",
            "topic": "Forms",
            "question": "What is the difference between readonly and disabled on a form control?",
            "options": ["They are identical in every respect", "Readonly controls are generally submitted, while disabled controls are not submitted", "Disabled controls are always editable", "Readonly controls are always hidden"],
            "correct_answer": "Readonly controls are generally submitted, while disabled controls are not submitted",
            "explanation": "Readonly supported controls remain focusable and are generally submitted; disabled controls are normally excluded from form submission."
        },
        {
            "id": "html_012",
            "skill": "HTML",
            "topic": "Form submission",
            "question": "What is the purpose of the name attribute on a successful form control?",
            "options": ["It defines the CSS color", "It provides the key used to submit that control's value", "It sets the browser window title", "It automatically makes the value unique"],
            "correct_answer": "It provides the key used to submit that control's value",
            "explanation": "Form data is submitted as name-value pairs for successful controls."
        },
        {
            "id": "html_013",
            "skill": "HTML",
            "topic": "Form submission",
            "question": "What does the action attribute of a form specify?",
            "options": ["The destination that processes the submitted form data", "The color of the submit button", "The required field count", "The browser's default font"],
            "correct_answer": "The destination that processes the submitted form data",
            "explanation": "The action attribute specifies the URL to which the form submission is directed."
        },
        {
            "id": "html_014",
            "skill": "HTML",
            "topic": "Form submission",
            "question": "What is the usual difference between GET and POST when submitting a form?",
            "options": ["GET generally places form data in the URL, while POST sends it in the request body", "GET encrypts all data automatically", "POST cannot send text values", "GET is always suitable for passwords"],
            "correct_answer": "GET generally places form data in the URL, while POST sends it in the request body",
            "explanation": "GET commonly encodes form data in the URL; POST normally sends it in the body. HTTPS is still needed to protect data in transit."
        },
        {
            "id": "html_015",
            "skill": "HTML",
            "topic": "Tables",
            "question": "Which table element groups header cells and data cells into a row?",
            "options": ["<tr>", "<td>", "<caption>", "<colgroup>"],
            "correct_answer": "<tr>",
            "explanation": "The tr element defines a table row containing cells."
        },
        {
            "id": "html_016",
            "skill": "HTML",
            "topic": "Tables",
            "question": "Which attribute allows a table cell to span multiple columns?",
            "options": ["rowspan", "colspan", "scope", "headers"],
            "correct_answer": "colspan",
            "explanation": "colspan specifies how many columns a table cell spans."
        },
        {
            "id": "html_017",
            "skill": "HTML",
            "topic": "Links",
            "question": "Which attribute specifies the destination of a hyperlink?",
            "options": ["src", "href", "action", "rel"],
            "correct_answer": "href",
            "explanation": "The href attribute specifies the linked resource's URL."
        },
        {
            "id": "html_018",
            "skill": "HTML",
            "topic": "Links and security",
            "question": "When using target=\"_blank\" for an external link, which practice helps explicitly prevent access through the opened page's opener reference?",
            "options": ["Add rel=\"noopener\"", "Add type=\"submit\"", "Add method=\"post\"", "Add autoplay"],
            "correct_answer": "Add rel=\"noopener\"",
            "explanation": "noopener prevents the newly opened browsing context from receiving a usable window.opener reference."
        },
        {
            "id": "html_019",
            "skill": "HTML",
            "topic": "Media",
            "question": "Which element is designed to provide alternative media sources and fallback content for video?",
            "options": ["<video>", "<picture>", "<canvas>", "<meter>"],
            "correct_answer": "<video>",
            "explanation": "The video element supports embedded video, source elements, and fallback content."
        },
        {
            "id": "html_020",
            "skill": "HTML",
            "topic": "Responsive images",
            "question": "Which element can provide different image sources based on media conditions?",
            "options": ["<picture>", "<audio>", "<progress>", "<output>"],
            "correct_answer": "<picture>",
            "explanation": "The picture element can contain source elements with media conditions and a fallback img element."
        },
        {
            "id": "html_021",
            "skill": "HTML",
            "topic": "Script loading",
            "question": "For a classic external script, what does the defer attribute generally do?",
            "options": ["Executes the script immediately before parsing continues", "Downloads the script while parsing continues and executes it after parsing", "Prevents the script from executing", "Runs the script only after a button is clicked"],
            "correct_answer": "Downloads the script while parsing continues and executes it after parsing",
            "explanation": "For classic external scripts, defer allows downloading during parsing and executes the script after document parsing, preserving deferred-script order."
        },
        {
            "id": "html_022",
            "skill": "HTML",
            "topic": "Script loading",
            "question": "How does async generally differ from defer for a classic external script?",
            "options": ["async executes as soon as it is ready and does not guarantee document order", "async always waits for all images to load", "async guarantees scripts execute in document order", "async prevents the browser from downloading the script"],
            "correct_answer": "async executes as soon as it is ready and does not guarantee document order",
            "explanation": "An async script executes when available, so its execution may interrupt parsing and its order relative to other async scripts is not guaranteed."
        },
        {
            "id": "html_023",
            "skill": "HTML",
            "topic": "Metadata",
            "question": "Which meta tag is important for making a page use the device's layout viewport on mobile browsers?",
            "options": ["<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">", "<meta name=\"image\" content=\"mobile\">", "<meta name=\"script\" content=\"responsive\">", "<meta name=\"table\" content=\"width\">"],
            "correct_answer": "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
            "explanation": "The viewport meta tag helps mobile browsers set the layout viewport to the device width."
        },
        {
            "id": "html_024",
            "skill": "HTML",
            "topic": "Metadata",
            "question": "Where is the document's title, character encoding declaration, and linked stylesheet normally placed?",
            "options": ["Inside <head>", "Inside <footer>", "Inside <main>", "Inside <tbody>"],
            "correct_answer": "Inside <head>",
            "explanation": "The head element contains document metadata and references to resources such as stylesheets."
        },
        {
            "id": "html_025",
            "skill": "HTML",
            "topic": "Character encoding",
            "question": "Why is <meta charset=\"UTF-8\"> commonly included in an HTML document?",
            "options": ["To specify the document's character encoding", "To set the page's background color", "To load a JavaScript library", "To make every input required"],
            "correct_answer": "To specify the document's character encoding",
            "explanation": "UTF-8 defines how text characters are encoded and decoded in the document."
        },
        {
            "id": "html_026",
            "skill": "HTML",
            "topic": "Global attributes",
            "question": "What is the purpose of the data-* attributes in HTML?",
            "options": ["To store custom data on an element for scripts to access", "To automatically encrypt user information", "To define table borders", "To load external CSS without a link element"],
            "correct_answer": "To store custom data on an element for scripts to access",
            "explanation": "Custom data attributes expose element-specific data through the DOM, commonly via element.dataset."
        },
        {
            "id": "html_027",
            "skill": "HTML",
            "topic": "Accessibility",
            "question": "Why should heading levels generally follow a logical hierarchy?",
            "options": ["To communicate the content structure and help navigation", "To make every heading bold automatically in all designs", "To prevent CSS from loading", "To ensure the page contains exactly six sections"],
            "correct_answer": "To communicate the content structure and help navigation",
            "explanation": "A logical heading hierarchy helps users and assistive technologies understand and navigate the page structure."
        },
        {
            "id": "html_028",
            "skill": "HTML",
            "topic": "Accessibility",
            "question": "When is a native HTML button generally preferable to a clickable div?",
            "options": ["When the control performs an action and needs built-in keyboard and accessibility behavior", "Only when the control contains an image", "When no interaction is required", "When the page has no CSS"],
            "correct_answer": "When the control performs an action and needs built-in keyboard and accessibility behavior",
            "explanation": "Native buttons provide built-in keyboard interaction, focus behavior, and semantics that a generic div would require extra work to reproduce."
        },
        {
            "id": "html_029",
            "skill": "HTML",
            "topic": "Accessibility",
            "question": "What is the purpose of aria-label on an element when used appropriately?",
            "options": ["To provide an accessible name", "To change the element's visual font size", "To submit a form", "To create a CSS media query"],
            "correct_answer": "To provide an accessible name",
            "explanation": "aria-label supplies an accessible name for elements when a suitable visible label is not otherwise available."
        },
        {
            "id": "html_030",
            "skill": "HTML",
            "topic": "HTML semantics",
            "question": "Which element is intended for a disclosure widget that users can expand or collapse?",
            "options": ["<details>", "<summary>", "<dialogue>", "<fieldset>"],
            "correct_answer": "<details>",
            "explanation": "The details element creates a disclosure widget; summary supplies its visible label."
        },
        {
            "id": "html_031",
            "skill": "HTML",
            "topic": "HTML semantics",
            "question": "What is the role of the <summary> element inside <details>?",
            "options": ["It provides the visible label for the disclosure widget", "It creates a page footer", "It submits form data", "It defines an image source"],
            "correct_answer": "It provides the visible label for the disclosure widget",
            "explanation": "The summary element labels the details disclosure control and is normally its first child."
        },
        {
            "id": "html_032",
            "skill": "HTML",
            "topic": "Embedded content",
            "question": "Which attribute on an iframe can help restrict the capabilities available to embedded content?",
            "options": ["sandbox", "colspan", "placeholder", "download"],
            "correct_answer": "sandbox",
            "explanation": "The iframe sandbox attribute applies restrictions to embedded content, with selected capabilities available through specific tokens."
        },
        {
            "id": "html_033",
            "skill": "HTML",
            "topic": "Security",
            "question": "Why should user-provided text generally not be inserted directly into the page using an unsafe HTML-parsing API?",
            "options": ["It can introduce cross-site scripting if the input contains malicious markup", "It always breaks CSS Grid", "It automatically removes all scripts", "It prevents the page from using links"],
            "correct_answer": "It can introduce cross-site scripting if the input contains malicious markup",
            "explanation": "Parsing untrusted input as HTML can execute attacker-controlled markup or scripts. Safe text insertion and appropriate sanitization reduce this risk."
        },
        {
            "id": "html_034",
            "skill": "HTML",
            "topic": "HTML validation",
            "question": "What is the main benefit of using a semantic element instead of a generic div when suitable?",
            "options": ["It communicates meaning and can improve accessibility and maintainability", "It automatically replaces all JavaScript", "It guarantees a perfect visual design", "It prevents the element from being styled"],
            "correct_answer": "It communicates meaning and can improve accessibility and maintainability",
            "explanation": "Semantic HTML gives browsers, assistive technologies, and developers more meaningful structure."
        },
        {
            "id": "html_035",
            "skill": "HTML",
            "topic": "Form validation",
            "question": "What does the pattern attribute do on a supported input?",
            "options": ["Checks the value against a regular-expression pattern during constraint validation", "Changes the input's background image", "Automatically encrypts the value", "Sets the input's database column"],
            "correct_answer": "Checks the value against a regular-expression pattern during constraint validation",
            "explanation": "pattern provides a regular expression used for client-side constraint validation on supported input types."
        },
        {
            "id": "html_036",
            "skill": "HTML",
            "topic": "Forms",
            "question": "What is the purpose of the autocomplete attribute on a form control?",
            "options": ["It guides the browser's autofill behavior", "It forces the form to submit immediately", "It prevents the control from receiving focus", "It automatically validates the server's database"],
            "correct_answer": "It guides the browser's autofill behavior",
            "explanation": "autocomplete indicates whether and how the browser may offer autofill suggestions for a control."
        },
        {
            "id": "html_037",
            "skill": "HTML",
            "topic": "Images",
            "question": "Which attribute provides an intrinsic width hint for an img element?",
            "options": ["width", "alt", "loading", "usemap"],
            "correct_answer": "width",
            "explanation": "The width attribute provides the image's displayed width in CSS pixels and helps browsers determine layout space."
        },
        {
            "id": "html_038",
            "skill": "HTML",
            "topic": "Resource loading",
            "question": "What is the purpose of loading=\"lazy\" on a supported image or iframe?",
            "options": ["To defer loading until the resource is nearer the viewport", "To guarantee that the resource never loads", "To increase image resolution", "To disable caching"],
            "correct_answer": "To defer loading until the resource is nearer the viewport",
            "explanation": "Lazy loading can delay off-screen resource loading until it is closer to becoming visible."
        },
        {
            "id": "html_039",
            "skill": "HTML",
            "topic": "Web components",
            "question": "Which HTML API allows a page to define custom elements with reusable behavior?",
            "options": ["Custom Elements", "CSS selectors", "The table element", "The viewport meta tag"],
            "correct_answer": "Custom Elements",
            "explanation": "The Custom Elements API allows developers to define reusable HTML elements with custom behavior."
        },
        {
            "id": "html_040",
            "skill": "HTML",
            "topic": "HTML debugging",
            "question": "A form field appears correctly but its value is missing from submitted form data. Which attribute should you check first?",
            "options": ["name", "class", "style", "title"],
            "correct_answer": "name",
            "explanation": "Successful form controls generally need a name to contribute a name-value pair to submitted form data."
        }
    ],

    "css": [
        {
            "id": "css_001",
            "skill": "CSS",
            "topic": "Cascade and specificity",
            "question": "Which selector generally has the highest specificity?",
            "options": ["p", ".content", "#main", "*"],
            "correct_answer": "#main",
            "explanation": "An ID selector has greater specificity than a class, type, or universal selector."
        },
        {
            "id": "css_002",
            "skill": "CSS",
            "topic": "Cascade",
            "question": "When two applicable declarations have equal origin, importance, and specificity, which generally decides the winner?",
            "options": ["The declaration that appears later in source order", "The declaration with the shorter property name", "The declaration inside the smaller element", "The declaration with more spaces"],
            "correct_answer": "The declaration that appears later in source order",
            "explanation": "When the relevant cascade criteria tie, later source order generally wins."
        },
        {
            "id": "css_003",
            "skill": "CSS",
            "topic": "Box model",
            "question": "With the default content-box model, width: 200px; padding: 10px; border: 2px solid; what is the total outer width?",
            "options": ["200px", "220px", "224px", "244px"],
            "correct_answer": "224px",
            "explanation": "The total is 200 + 10 + 10 + 2 + 2 = 224px."
        },
        {
            "id": "css_004",
            "skill": "CSS",
            "topic": "Box model",
            "question": "What does box-sizing: border-box do to an element's declared width?",
            "options": ["Includes content, padding, and border within the specified width", "Includes only the content area", "Removes all padding", "Makes every element position absolute"],
            "correct_answer": "Includes content, padding, and border within the specified width",
            "explanation": "With border-box, the declared width includes the content, padding, and border."
        },
        {
            "id": "css_005",
            "skill": "CSS",
            "topic": "Display",
            "question": "Which display value allows an element to flow inline while also accepting width and height like a block-level box?",
            "options": ["inline", "inline-block", "none", "contents"],
            "correct_answer": "inline-block",
            "explanation": "inline-block participates in inline flow but supports width, height, and box-model dimensions."
        },
        {
            "id": "css_006",
            "skill": "CSS",
            "topic": "Flexbox",
            "question": "In a flex container with flex-direction: row, which property aligns items along the main axis?",
            "options": ["align-items", "justify-content", "align-content", "vertical-align"],
            "correct_answer": "justify-content",
            "explanation": "For a row flex container, justify-content distributes items along the horizontal main axis."
        },
        {
            "id": "css_007",
            "skill": "CSS",
            "topic": "Flexbox",
            "question": "In a row flex container, which property normally aligns items along the cross axis?",
            "options": ["justify-content", "align-items", "flex-basis", "order"],
            "correct_answer": "align-items",
            "explanation": "align-items controls cross-axis alignment for items in a flex line."
        },
        {
            "id": "css_008",
            "skill": "CSS",
            "topic": "Flexbox",
            "question": "What does flex-wrap: wrap allow in a flex container?",
            "options": ["Items can move onto additional flex lines when needed", "Items must all remain on one line", "Items become absolutely positioned", "The container stops displaying its children"],
            "correct_answer": "Items can move onto additional flex lines when needed",
            "explanation": "flex-wrap permits flex items to wrap onto multiple lines when space is insufficient."
        },
        {
            "id": "css_009",
            "skill": "CSS",
            "topic": "Flexbox",
            "question": "What is the main role of flex: 1 on a flex item in a typical layout?",
            "options": ["It lets the item grow and share available space", "It fixes the item at one pixel wide", "It removes the item from document flow", "It sets the item's z-index to 1"],
            "correct_answer": "It lets the item grow and share available space",
            "explanation": "flex: 1 commonly lets an item grow to occupy available space, subject to flex sizing and constraints."
        },
        {
            "id": "css_010",
            "skill": "CSS",
            "topic": "CSS Grid",
            "question": "Which declaration creates three equal flexible columns in a CSS Grid container?",
            "options": ["grid-template-columns: repeat(3, 1fr);", "grid-template-rows: repeat(3, 1fr);", "display: inline;", "column-count: 3;"],
            "correct_answer": "grid-template-columns: repeat(3, 1fr);",
            "explanation": "repeat(3, 1fr) creates three grid columns with equal fractional sizing."
        },
        {
            "id": "css_011",
            "skill": "CSS",
            "topic": "CSS Grid",
            "question": "What does the fr unit represent in CSS Grid track sizing?",
            "options": ["A fraction of the available grid space", "A fixed font size", "A percentage of the viewport height only", "A duration in seconds"],
            "correct_answer": "A fraction of the available grid space",
            "explanation": "The fr unit distributes a share of available grid space among flexible tracks."
        },
        {
            "id": "css_012",
            "skill": "CSS",
            "topic": "CSS Grid",
            "question": "What does grid-column: 1 / 3 mean for a grid item?",
            "options": ["It spans from grid line 1 to grid line 3", "It occupies exactly three complete columns", "It creates three separate grid containers", "It sets the item to three pixels wide"],
            "correct_answer": "It spans from grid line 1 to grid line 3",
            "explanation": "Grid placement uses line numbers; from line 1 to line 3 the item spans two grid tracks."
        },
        {
            "id": "css_013",
            "skill": "CSS",
            "topic": "Positioning",
            "question": "Relative to which containing block is an absolutely positioned element normally positioned?",
            "options": ["The nearest ancestor that establishes its absolute-positioning containing block", "Always the viewport", "Always the body element", "The nearest sibling element"],
            "correct_answer": "The nearest ancestor that establishes its absolute-positioning containing block",
            "explanation": "An absolutely positioned element uses its established containing block, often created by a positioned ancestor."
        },
        {
            "id": "css_014",
            "skill": "CSS",
            "topic": "Positioning",
            "question": "What is a common effect of position: fixed on an element?",
            "options": ["It is positioned relative to the viewport in the usual case", "It always stays inside normal document flow", "It automatically becomes a flex container", "It cannot overlap other elements"],
            "correct_answer": "It is positioned relative to the viewport in the usual case",
            "explanation": "Fixed elements are typically positioned relative to the viewport, though certain ancestors can establish a different containing block."
        },
        {
            "id": "css_015",
            "skill": "CSS",
            "topic": "Positioning",
            "question": "How does position: sticky generally behave?",
            "options": ["It behaves in normal flow until a scroll threshold is reached, then sticks within its containing area", "It is always removed from document flow", "It always stays fixed at the top of the browser", "It prevents the page from scrolling"],
            "correct_answer": "It behaves in normal flow until a scroll threshold is reached, then sticks within its containing area",
            "explanation": "Sticky positioning combines normal-flow placement with a scroll-dependent sticking behavior subject to its container and inset settings."
        },
        {
            "id": "css_016",
            "skill": "CSS",
            "topic": "Stacking contexts",
            "question": "Why might increasing z-index on an element fail to place it above an element in another stacking context?",
            "options": ["Stacking contexts are layered as groups, so a child cannot escape its parent's stacking order", "z-index works only on images", "z-index accepts only negative values", "The browser ignores every z-index value"],
            "correct_answer": "Stacking contexts are layered as groups, so a child cannot escape its parent's stacking order",
            "explanation": "A descendant is ordered within its own stacking context and cannot outrank a separate context above its parent context merely by increasing its z-index."
        },
        {
            "id": "css_017",
            "skill": "CSS",
            "topic": "Responsive design",
            "question": "What is the purpose of a CSS media query?",
            "options": ["To apply styles conditionally based on media features", "To retrieve data from a database", "To create HTML elements automatically", "To replace every CSS selector"],
            "correct_answer": "To apply styles conditionally based on media features",
            "explanation": "Media queries apply CSS rules depending on conditions such as viewport width or user display preferences."
        },
        {
            "id": "css_018",
            "skill": "CSS",
            "topic": "Responsive design",
            "question": "What does a mobile-first responsive design approach usually mean?",
            "options": ["Start with small-screen styles and add enhancements for larger screens", "Design only for mobile devices", "Use fixed pixel widths for every screen", "Disable all media queries"],
            "correct_answer": "Start with small-screen styles and add enhancements for larger screens",
            "explanation": "Mobile-first design establishes a useful small-screen baseline and progressively enhances layouts for larger viewports."
        },
        {
            "id": "css_019",
            "skill": "CSS",
            "topic": "CSS units",
            "question": "What is the main difference between em and rem for font sizing?",
            "options": ["em is relative to the relevant element's font-size context, while rem is relative to the root element's font size", "em always means pixels and rem always means percentages", "rem is relative to the viewport width", "They are both fixed physical units"],
            "correct_answer": "em is relative to the relevant element's font-size context, while rem is relative to the root element's font size",
            "explanation": "em sizing depends on the relevant element's font-size context; rem is based on the root element's font size."
        },
        {
            "id": "css_020",
            "skill": "CSS",
            "topic": "CSS units",
            "question": "What does width: 80vw mean?",
            "options": ["80 percent of the viewport width", "80 percent of the parent's font size", "80 pixels", "80 percent of the viewport height"],
            "correct_answer": "80 percent of the viewport width",
            "explanation": "The vw unit represents one percent of the viewport width."
        },
        {
            "id": "css_021",
            "skill": "CSS",
            "topic": "Pseudo-classes",
            "question": "Which selector targets an input when it currently has keyboard focus?",
            "options": ["input:hover", "input:focus", "input::before", "input:visited"],
            "correct_answer": "input:focus",
            "explanation": "The :focus pseudo-class matches an element that currently has focus."
        },
        {
            "id": "css_022",
            "skill": "CSS",
            "topic": "Pseudo-elements",
            "question": "What is the primary distinction between ::before and :hover?",
            "options": ["::before is a pseudo-element, while :hover is a pseudo-class", "::before is an HTML tag, while :hover is an attribute", "Both are HTML elements", "Both create a new document"],
            "correct_answer": "::before is a pseudo-element, while :hover is a pseudo-class",
            "explanation": "Pseudo-elements style a particular part or generated content, while pseudo-classes match an element's state or relationship."
        },
        {
            "id": "css_023",
            "skill": "CSS",
            "topic": "Selectors",
            "question": "What does the selector .card > p target?",
            "options": ["Every paragraph anywhere inside .card", "Paragraphs that are direct children of .card", "Only paragraphs immediately after .card", "Every element with the id card"],
            "correct_answer": "Paragraphs that are direct children of .card",
            "explanation": "The child combinator > matches elements that are direct children of the preceding selector."
        },
        {
            "id": "css_024",
            "skill": "CSS",
            "topic": "Selectors",
            "question": "What does the selector h2 + p match?",
            "options": ["Any paragraph inside an h2", "A paragraph immediately following an h2 with the same parent", "Every paragraph after any heading anywhere on the page", "An h2 immediately following a paragraph"],
            "correct_answer": "A paragraph immediately following an h2 with the same parent",
            "explanation": "The adjacent-sibling combinator + selects the next sibling that matches the second selector."
        },
        {
            "id": "css_025",
            "skill": "CSS",
            "topic": "Custom properties",
            "question": "Where are CSS custom properties declared to make them commonly available throughout a document?",
            "options": [":root { --brand-color: blue; }", "root { brand-color: blue; }", "body { @variable: blue; }", "html { var(--brand-color): blue; }"],
            "correct_answer": ":root { --brand-color: blue; }",
            "explanation": "Custom properties use names beginning with -- and can be declared on :root for broad availability."
        },
        {
            "id": "css_026",
            "skill": "CSS",
            "topic": "Custom properties",
            "question": "How can a custom property use a fallback value if --accent is unavailable?",
            "options": ["var(--accent, blue)", "fallback(--accent, blue)", "value(--accent = blue)", "default: --accent blue"],
            "correct_answer": "var(--accent, blue)",
            "explanation": "The second argument to var() provides a fallback when the custom property cannot be resolved."
        },
        {
            "id": "css_027",
            "skill": "CSS",
            "topic": "Overflow",
            "question": "What does overflow: auto generally do when content exceeds an element's available box?",
            "options": ["Provides scrolling when needed", "Always hides overflowing content", "Always makes all content visible without scrolling", "Removes the element from layout"],
            "correct_answer": "Provides scrolling when needed",
            "explanation": "overflow: auto allows scrolling when the content overflows and scrolling is applicable."
        },
        {
            "id": "css_028",
            "skill": "CSS",
            "topic": "Visibility",
            "question": "What is the main layout difference between display: none and visibility: hidden?",
            "options": ["Both always preserve the same layout space", "display: none removes the element's box from layout, while visibility: hidden normally preserves its space", "visibility: hidden removes the element from layout", "display: none only hides text but not the element"],
            "correct_answer": "display: none removes the element's box from layout, while visibility: hidden normally preserves its space",
            "explanation": "display: none removes the element from layout, whereas visibility: hidden keeps its layout space."
        },
        {
            "id": "css_029",
            "skill": "CSS",
            "topic": "Transitions",
            "question": "What is required for a CSS transition to visibly animate between two property values?",
            "options": ["The property's value must change and the property must support the transition", "Every property must be declared !important", "The element must use position: fixed", "The page must contain a form"],
            "correct_answer": "The property's value must change and the property must support the transition",
            "explanation": "A transition animates eligible property changes over time according to the specified transition settings."
        },
        {
            "id": "css_030",
            "skill": "CSS",
            "topic": "Animations",
            "question": "Which CSS feature defines intermediate stages of an animation?",
            "options": ["@keyframes", "@media only", "::selection", "box-sizing"],
            "correct_answer": "@keyframes",
            "explanation": "@keyframes defines the stages an animation progresses through."
        },
        {
            "id": "css_031",
            "skill": "CSS",
            "topic": "Transforms",
            "question": "What does transform: translateX(20px) do?",
            "options": ["Moves the rendered element 20px along the horizontal axis", "Adds 20px of padding", "Changes the element's font size to 20px", "Moves every sibling by 20px"],
            "correct_answer": "Moves the rendered element 20px along the horizontal axis",
            "explanation": "translateX applies a horizontal visual transform without changing normal-flow space as margin or padding would."
        },
        {
            "id": "css_032",
            "skill": "CSS",
            "topic": "Object fitting",
            "question": "For an image inside a fixed-size box, what does object-fit: cover generally do?",
            "options": ["Scales the image to cover the box, potentially cropping it", "Always stretches the image without preserving its aspect ratio", "Makes the image transparent", "Changes the box into a CSS Grid"],
            "correct_answer": "Scales the image to cover the box, potentially cropping it",
            "explanation": "cover preserves the image's aspect ratio while filling the box, so some content may be cropped."
        },
        {
            "id": "css_033",
            "skill": "CSS",
            "topic": "Typography",
            "question": "What does line-height primarily control for text?",
            "options": ["The height of the line box used for text layout", "The width of each character", "The thickness of a border", "The distance between grid columns only"],
            "correct_answer": "The height of the line box used for text layout",
            "explanation": "line-height sets the height of a line box and influences vertical spacing between lines of text."
        },
        {
            "id": "css_034",
            "skill": "CSS",
            "topic": "Margin collapsing",
            "question": "In normal block layout, what can happen when two adjacent vertical margins collapse?",
            "options": ["Their effective separation can be the larger margin rather than their sum", "They always add together", "Both margins become zero in every case", "The elements automatically become flex items"],
            "correct_answer": "Their effective separation can be the larger margin rather than their sum",
            "explanation": "Collapsing positive vertical margins generally produce a separation equal to the larger margin, subject to the margin-collapsing rules."
        },
        {
            "id": "css_035",
            "skill": "CSS",
            "topic": "Responsive layout",
            "question": "Which CSS function is useful for defining a responsive size with a preferred value and minimum and maximum limits?",
            "options": ["clamp()", "repeat()", "counter()", "attr()"],
            "correct_answer": "clamp()",
            "explanation": "clamp(minimum, preferred, maximum) constrains a value between lower and upper limits."
        },
        {
            "id": "css_036",
            "skill": "CSS",
            "topic": "Responsive layout",
            "question": "What does minmax(200px, 1fr) mean when used for a CSS Grid track?",
            "options": ["The track has a minimum of 200px and can grow to a flexible fraction", "The track is always exactly 1px wide", "The track has a maximum of 200px and cannot grow", "The track becomes a fixed-height row"],
            "correct_answer": "The track has a minimum of 200px and can grow to a flexible fraction",
            "explanation": "minmax specifies a minimum and maximum track sizing function; 1fr permits flexible growth."
        },
        {
            "id": "css_037",
            "skill": "CSS",
            "topic": "Accessibility",
            "question": "Which media query can detect a user preference for reduced motion?",
            "options": ["@media (prefers-reduced-motion: reduce)", "@media (motion: disabled)", "@media (animation: none)", "@media (screen: static)"],
            "correct_answer": "@media (prefers-reduced-motion: reduce)",
            "explanation": "This media feature lets authors reduce nonessential motion for users who request reduced motion in their system settings."
        },
        {
            "id": "css_038",
            "skill": "CSS",
            "topic": "CSS architecture",
            "question": "What is a practical advantage of using CSS classes rather than repeating inline styles across many elements?",
            "options": ["Styles can be reused and maintained centrally", "Classes automatically validate server responses", "Classes eliminate the cascade entirely", "Classes prevent responsive styling"],
            "correct_answer": "Styles can be reused and maintained centrally",
            "explanation": "Reusable classes reduce duplication and make visual changes easier to maintain consistently."
        },
        {
            "id": "css_039",
            "skill": "CSS",
            "topic": "Specificity",
            "question": "Why is !important generally best avoided unless there is a clear need?",
            "options": ["It can make cascade conflicts harder to reason about and override", "It makes the browser ignore the declaration entirely", "It converts the selector into an HTML element", "It prevents the declaration from applying on mobile"],
            "correct_answer": "It can make cascade conflicts harder to reason about and override",
            "explanation": "!important changes cascade priority and can make styles harder to override and maintain."
        },
        {
            "id": "css_040",
            "skill": "CSS",
            "topic": "Debugging",
            "question": "A CSS rule appears in a stylesheet but does not affect an element. What is a useful first debugging step?",
            "options": ["Inspect the element's computed styles and matched rules in developer tools", "Delete every stylesheet", "Rewrite the page in JavaScript", "Change all values to !important immediately"],
            "correct_answer": "Inspect the element's computed styles and matched rules in developer tools",
            "explanation": "Developer tools reveal selector matches, cascade conflicts, inherited values, and overridden declarations."
        }
    ],
    
    "react.js": [
        {
            "id": "react_001",
            "skill": "React.js",
            "topic": "Fundamentals",
            "question": "What is React primarily used for?",
            "options": ["Building user interfaces", "Managing databases", "Configuring servers", "Writing SQL queries"],
            "correct_answer": "Building user interfaces",
            "explanation": "React is a JavaScript library for building user interfaces."
        },
        {
            "id": "react_002",
            "skill": "React.js",
            "topic": "JSX",
            "question": "What is JSX?",
            "options": ["A syntax extension for JavaScript", "A database language", "A CSS framework", "A server protocol"],
            "correct_answer": "A syntax extension for JavaScript",
            "explanation": "JSX lets developers describe UI elements using HTML-like syntax in JavaScript."
        },
        {
            "id": "react_003",
            "skill": "Components",
            "topic": "Components",
            "question": "Which statement about React function components is correct?",
            "options": ["They are JavaScript functions that return React elements", "They must extend React.Component", "They can never receive props", "They must directly modify the DOM"],
            "correct_answer": "They are JavaScript functions that return React elements",
            "explanation": "Function components commonly return JSX that React renders."
        },
        {
            "id": "react_004",
            "skill": "React.js",
            "topic": "Props",
            "question": "What are props used for?",
            "options": ["Passing data from a parent to a child component", "Directly updating the browser DOM", "Storing server passwords", "Replacing JavaScript functions"],
            "correct_answer": "Passing data from a parent to a child component",
            "explanation": "Props allow parent components to configure child components."
        },
        {
            "id": "react_005",
            "skill": "React.js",
            "topic": "State",
            "question": "What is state used for in a React component?",
            "options": ["Storing data that can change over time", "Defining database tables", "Replacing all props", "Loading CSS files only"],
            "correct_answer": "Storing data that can change over time",
            "explanation": "Updating state can cause React to render the component again."
        },
        {
            "id": "react_006",
            "skill": "React.js",
            "topic": "Hooks",
            "question": "Which hook is commonly used to manage local component state?",
            "options": ["useState", "useRoute", "useClass", "useHTML"],
            "correct_answer": "useState",
            "explanation": "useState returns the current state value and a setter function."
        },
        {
            "id": "react_007",
            "skill": "React.js",
            "topic": "Hooks",
            "question": "What does useEffect commonly handle?",
            "options": ["Synchronizing with external systems", "Declaring HTML tags", "Creating database schemas", "Replacing JSX"],
            "correct_answer": "Synchronizing with external systems",
            "explanation": "Effects are commonly used for subscriptions, timers, and synchronization with external systems."
        },
        {
            "id": "react_008",
            "skill": "React.js",
            "topic": "Hooks",
            "question": "What does an empty dependency array in useEffect generally indicate?",
            "options": ["The effect has no reactive dependencies", "The effect runs after every render", "The component never renders", "The effect runs only when a button is clicked"],
            "correct_answer": "The effect has no reactive dependencies",
            "explanation": "An effect with an empty dependency array normally runs after the initial commit, with development Strict Mode potentially running an extra setup cycle."
        },
        {
            "id": "react_009",
            "skill": "React.js",
            "topic": "Rendering",
            "question": "How can a React component render a list of items?",
            "options": ["Using map() to produce elements", "Using SQL SELECT inside JSX", "Using document.write() for every item", "Using a CSS media query"],
            "correct_answer": "Using map() to produce elements",
            "explanation": "Array map() is commonly used to transform data into rendered elements."
        },
        {
            "id": "react_010",
            "skill": "React.js",
            "topic": "Keys",
            "question": "Why should list elements have stable keys?",
            "options": ["To help React identify items between renders", "To encrypt the list", "To add CSS automatically", "To prevent all component updates"],
            "correct_answer": "To help React identify items between renders",
            "explanation": "Stable keys help React track list items when items are inserted, removed, or reordered."
        },
        {
            "id": "react_011",
            "skill": "React.js",
            "topic": "Events",
            "question": "Which is the correct way to handle a click in JSX?",
            "options": ["onClick={handleClick}", "onclick=\"handleClick()\"", "click={handleClick}", "on-click=\"handleClick\""],
            "correct_answer": "onClick={handleClick}",
            "explanation": "React event handlers use camelCase event names and receive a function."
        },
        {
            "id": "react_012",
            "skill": "React.js",
            "topic": "Forms",
            "question": "What makes an input controlled in React?",
            "options": ["Its value is driven by React state and updated through an event handler", "It has no value property", "It uses only CSS", "It cannot receive user input"],
            "correct_answer": "Its value is driven by React state and updated through an event handler",
            "explanation": "A controlled input uses React state as its source of truth."
        },
        {
            "id": "react_013",
            "skill": "React.js",
            "topic": "Conditional Rendering",
            "question": "Which operator is commonly used for inline conditional rendering?",
            "options": ["Ternary operator", "Bitwise NOT only", "SQL UNION", "Assignment operator only"],
            "correct_answer": "Ternary operator",
            "explanation": "The condition ? valueA : valueB expression selects between two render results."
        },
        {
            "id": "react_014",
            "skill": "React.js",
            "topic": "Conditional Rendering",
            "question": "What does the expression {isLoggedIn && <Dashboard />} do?",
            "options": ["Renders Dashboard when isLoggedIn is truthy", "Always renders Dashboard", "Deletes Dashboard", "Changes the URL automatically"],
            "correct_answer": "Renders Dashboard when isLoggedIn is truthy",
            "explanation": "Logical AND can conditionally include an element in JSX."
        },
        {
            "id": "react_015",
            "skill": "React.js",
            "topic": "Props",
            "question": "Can a child component directly change its parent's state using a state setter it does not receive?",
            "options": ["No, it needs an appropriate callback or shared state mechanism", "Yes, every component shares all state automatically", "Yes, by changing its CSS", "No, React has no state"],
            "correct_answer": "No, it needs an appropriate callback or shared state mechanism",
            "explanation": "A parent can pass a callback to let a child request a state update."
        },
        {
            "id": "react_016",
            "skill": "React.js",
            "topic": "Hooks",
            "question": "What is a core rule of React Hooks?",
            "options": ["Call Hooks at the top level of components or custom Hooks", "Call Hooks inside every loop iteration", "Call Hooks only inside if statements", "Call Hooks only from class methods"],
            "correct_answer": "Call Hooks at the top level of components or custom Hooks",
            "explanation": "Consistent Hook call order allows React to associate Hook state correctly."
        },
        {
            "id": "react_017",
            "skill": "React.js",
            "topic": "Hooks",
            "question": "What is useRef commonly used for?",
            "options": ["Keeping a mutable value or referencing a DOM element", "Automatically fetching every API", "Replacing all component props", "Defining CSS selectors"],
            "correct_answer": "Keeping a mutable value or referencing a DOM element",
            "explanation": "Changing a ref does not itself trigger a re-render."
        },
        {
            "id": "react_018",
            "skill": "React.js",
            "topic": "Hooks",
            "question": "What is useMemo intended to do?",
            "options": ["Cache a calculated value between renders when dependencies are unchanged", "Persist data permanently on a server", "Replace useState in every case", "Automatically memoize every component"],
            "correct_answer": "Cache a calculated value between renders when dependencies are unchanged",
            "explanation": "useMemo is a performance optimization for calculations."
        },
        {
            "id": "react_019",
            "skill": "React.js",
            "topic": "Hooks",
            "question": "What does useCallback cache?",
            "options": ["A function definition between renders when dependencies are unchanged", "An API response permanently", "A CSS stylesheet", "A database connection"],
            "correct_answer": "A function definition between renders when dependencies are unchanged",
            "explanation": "useCallback can help preserve function identity for memoized children or other dependencies."
        },
        {
            "id": "react_020",
            "skill": "React.js",
            "topic": "Context",
            "question": "What problem does React Context help solve?",
            "options": ["Passing shared values through a component tree without manually forwarding props at every level", "Replacing every API endpoint", "Creating SQL indexes", "Styling all elements automatically"],
            "correct_answer": "Passing shared values through a component tree without manually forwarding props at every level",
            "explanation": "Context provides values to descendant components that consume that context."
        },
        {
            "id": "react_021",
            "skill": "React.js",
            "topic": "Performance",
            "question": "What does React.memo commonly help avoid?",
            "options": ["Some re-renders when props have not changed", "All network requests", "All state updates", "Every render under every condition"],
            "correct_answer": "Some re-renders when props have not changed",
            "explanation": "React.memo can skip rendering when props compare equal, but it is not a guarantee against every render."
        },
        {
            "id": "react_022",
            "skill": "React.js",
            "topic": "State Updates",
            "question": "When should a functional state update be preferred?",
            "options": ["When the next state depends on the previous state", "Whenever declaring a CSS class", "Only when making an HTTP request", "When returning a static image"],
            "correct_answer": "When the next state depends on the previous state",
            "explanation": "A setter such as setCount(previous => previous + 1) uses the previous queued state."
        },
        {
            "id": "react_023",
            "skill": "React.js",
            "topic": "State Updates",
            "question": "What is a safe way to update an object stored in React state?",
            "options": ["Create a new object with the changed properties", "Mutate the existing object without notifying React", "Change the object's CSS selector", "Reload the entire computer"],
            "correct_answer": "Create a new object with the changed properties",
            "explanation": "Immutable updates create a new reference that React can recognize."
        },
        {
            "id": "react_024",
            "skill": "React.js",
            "topic": "Forms",
            "question": "Which React event is commonly used to respond as a text input changes?",
            "options": ["onChange", "onHoverOnly", "onCompile", "onDatabase"],
            "correct_answer": "onChange",
            "explanation": "onChange is commonly used to update controlled form input state."
        },
        {
            "id": "react_025",
            "skill": "React.js",
            "topic": "Fragments",
            "question": "What is the purpose of React Fragment?",
            "options": ["Group elements without adding an extra DOM wrapper", "Create a new browser window", "Store global CSS", "Fetch server data automatically"],
            "correct_answer": "Group elements without adding an extra DOM wrapper",
            "explanation": "Fragments group multiple elements without introducing an extra DOM node."
        },
        {
            "id": "react_026",
            "skill": "React.js",
            "topic": "Portals",
            "question": "What is a React portal used for?",
            "options": ["Rendering children into a different DOM node", "Sending data to a database", "Replacing a component's props", "Creating a package.json file"],
            "correct_answer": "Rendering children into a different DOM node",
            "explanation": "Portals are useful for overlays such as dialogs while preserving React-tree behavior."
        },
        {
            "id": "react_027",
            "skill": "React.js",
            "topic": "Error Handling",
            "question": "What do React error boundaries primarily catch?",
            "options": ["Errors during rendering and related lifecycle work in descendant components", "Every error in every event handler", "All server database failures automatically", "All CSS warnings"],
            "correct_answer": "Errors during rendering and related lifecycle work in descendant components",
            "explanation": "Error boundaries do not automatically catch errors from event handlers or arbitrary asynchronous callbacks."
        },
        {
            "id": "react_028",
            "skill": "React.js",
            "topic": "Lifecycle",
            "question": "What does the cleanup function returned by useEffect commonly do?",
            "options": ["Remove subscriptions, listeners, or timers created by the effect", "Delete the component source file", "Clear all browser cookies automatically", "Reset every component in the application"],
            "correct_answer": "Remove subscriptions, listeners, or timers created by the effect",
            "explanation": "Cleanup prevents stale subscriptions and resource leaks."
        },
        {
            "id": "react_029",
            "skill": "React.js",
            "topic": "Data Fetching",
            "question": "What should a component usually track when loading data asynchronously?",
            "options": ["Loading, success, and error states", "Only the button's color", "Only the browser width", "The user's operating system password"],
            "correct_answer": "Loading, success, and error states",
            "explanation": "These states let the UI represent pending requests and failures clearly."
        },
        {
            "id": "react_030",
            "skill": "React.js",
            "topic": "Security",
            "question": "What is a safer approach when displaying user-provided text in React?",
            "options": ["Render it as ordinary text rather than injecting raw HTML", "Always use dangerouslySetInnerHTML", "Convert it into executable JavaScript", "Disable all escaping"],
            "correct_answer": "Render it as ordinary text rather than injecting raw HTML",
            "explanation": "React escapes ordinary text content; raw HTML injection requires careful sanitization."
        },
        {
            "id": "react_031",
            "skill": "React.js",
            "topic": "Architecture",
            "question": "What is a custom Hook?",
            "options": ["A JavaScript function that reuses stateful React logic using Hooks", "A browser extension", "A special HTML element", "A database trigger"],
            "correct_answer": "A JavaScript function that reuses stateful React logic using Hooks",
            "explanation": "Custom Hooks share logic between components without sharing one state instance automatically."
        },
        {
            "id": "react_032",
            "skill": "React.js",
            "topic": "Routing",
            "question": "What is a client-side routing library commonly used for in a React SPA?",
            "options": ["Mapping URL paths to rendered views without full page loads for every navigation", "Compiling SQL queries", "Replacing HTTP entirely", "Creating image files"],
            "correct_answer": "Mapping URL paths to rendered views without full page loads for every navigation",
            "explanation": "Client-side routers manage navigation and rendered views within a single-page application."
        },
        {
            "id": "react_033",
            "skill": "React.js",
            "topic": "Accessibility",
            "question": "Which approach improves accessibility for a clickable action?",
            "options": ["Use a semantic button element", "Use a div with no keyboard behavior", "Use color alone to convey its purpose", "Remove the accessible name"],
            "correct_answer": "Use a semantic button element",
            "explanation": "Buttons provide built-in keyboard interaction and semantics."
        },
        {
            "id": "react_034",
            "skill": "React.js",
            "topic": "Testing",
            "question": "What should a React component test generally verify?",
            "options": ["Observable behavior and rendered output for given inputs", "Only the component file's line count", "The color of the developer's editor", "The number of folders in the repository"],
            "correct_answer": "Observable behavior and rendered output for given inputs",
            "explanation": "Behavior-focused tests check what users can observe and interact with."
        },
        {
            "id": "react_035",
            "skill": "React.js",
            "topic": "Reconciliation",
            "question": "What can changing a component's key intentionally cause?",
            "options": ["React to treat it as a different component and reset its state", "React to encrypt its state", "The browser to restart", "The component to become a CSS file"],
            "correct_answer": "React to treat it as a different component and reset its state",
            "explanation": "A changed key can reset component identity and its local state."
        },
        {
            "id": "react_036",
            "skill": "React.js",
            "topic": "Rendering",
            "question": "What does hydration mean in a server-rendered React application?",
            "options": ["Attaching React behavior to HTML rendered on the server", "Compressing an image", "Converting CSS to SQL", "Deleting server-rendered HTML"],
            "correct_answer": "Attaching React behavior to HTML rendered on the server",
            "explanation": "Hydration connects the client React application to existing server-rendered markup."
        },
        {
            "id": "react_037",
            "skill": "React.js",
            "topic": "Performance",
            "question": "Why can unstable object props reduce memoization benefits?",
            "options": ["A new object reference may be created on each render", "Objects cannot be passed as props", "React automatically converts objects into CSS", "Objects always prevent rendering"],
            "correct_answer": "A new object reference may be created on each render",
            "explanation": "Shallow comparisons see newly created objects as different references."
        },
        {
            "id": "react_038",
            "skill": "React.js",
            "topic": "State Management",
            "question": "When is useReducer often useful?",
            "options": ["When state transitions involve multiple related actions or complex logic", "Only for displaying static text", "Only for loading CSS", "When no state is required"],
            "correct_answer": "When state transitions involve multiple related actions or complex logic",
            "explanation": "A reducer centralizes state transitions based on dispatched actions."
        },
        {
            "id": "react_039",
            "skill": "React.js",
            "topic": "Performance",
            "question": "What is code splitting used for in a React application?",
            "options": ["Loading parts of the application only when needed", "Combining all CSS into database rows", "Disabling JavaScript", "Removing all components"],
            "correct_answer": "Loading parts of the application only when needed",
            "explanation": "Code splitting can reduce the initial JavaScript bundle size."
        },
        {
            "id": "react_040",
            "skill": "React.js",
            "topic": "Architecture",
            "question": "Which practice generally improves React component maintainability?",
            "options": ["Keep components focused and separate reusable logic", "Place all application logic in one huge component", "Mutate props directly", "Duplicate the same logic everywhere"],
            "correct_answer": "Keep components focused and separate reusable logic",
            "explanation": "Focused components are easier to test, reuse, and maintain."
        }
    ],
    "next.js": [
        {
            "id": "nextjs_001",
            "skill": "Next.js",
            "topic": "Fundamentals",
            "question": "What is Next.js?",
            "options": ["A React framework for building web applications", "A relational database", "A CSS-only language", "A Python package manager"],
            "correct_answer": "A React framework for building web applications",
            "explanation": "Next.js adds routing, rendering options, and other application features to React."
        },
        {
            "id": "nextjs_002",
            "skill": "Next.js",
            "topic": "Routing",
            "question": "In the App Router, what does app/about/page.js normally represent?",
            "options": ["The /about route", "The /page/about route", "A global stylesheet only", "An API endpoint automatically"],
            "correct_answer": "The /about route",
            "explanation": "A page.js file inside app/about defines the route at /about."
        },
        {
            "id": "nextjs_003",
            "skill": "Next.js",
            "topic": "Routing",
            "question": "What is the purpose of layout.js in the App Router?",
            "options": ["Define shared UI around pages and nested routes", "Define SQL database tables", "Replace every page.js file", "Store environment variables"],
            "correct_answer": "Define shared UI around pages and nested routes",
            "explanation": "Layouts can preserve shared UI such as navigation across route changes."
        },
        {
            "id": "nextjs_004",
            "skill": "Next.js",
            "topic": "Server Components",
            "question": "What is the default component type in the App Router?",
            "options": ["Server Component", "Client Component", "Web Worker", "Service Worker"],
            "correct_answer": "Server Component",
            "explanation": "Components in the App Router are Server Components by default unless marked otherwise."
        },
        {
            "id": "nextjs_005",
            "skill": "Next.js",
            "topic": "Client Components",
            "question": "What does the 'use client' directive indicate?",
            "options": ["The module belongs to the client component boundary", "The page must be stored in SQL", "The component runs only as a database process", "The route is automatically private"],
            "correct_answer": "The module belongs to the client component boundary",
            "explanation": "It enables client-side features such as state, effects, and browser event handlers."
        },
        {
            "id": "nextjs_006",
            "skill": "Next.js",
            "topic": "Client Components",
            "question": "Where should 'use client' normally appear?",
            "options": ["At the top of the module before imports", "Inside a CSS selector", "At the bottom of package.json", "Inside every JSX element"],
            "correct_answer": "At the top of the module before imports",
            "explanation": "The directive must precede imports to mark the module as a client entry point."
        },
        {
            "id": "nextjs_007",
            "skill": "Next.js",
            "topic": "Navigation",
            "question": "Which component is commonly used for internal navigation in Next.js?",
            "options": ["Link from next/link", "Table from next/table", "SQLLink", "BrowserWindow"],
            "correct_answer": "Link from next/link",
            "explanation": "The Link component enables client-side navigation between application routes."
        },
        {
            "id": "nextjs_008",
            "skill": "Next.js",
            "topic": "Dynamic Routes",
            "question": "What does app/products/[id]/page.js represent?",
            "options": ["A dynamic product route such as /products/42", "Only the /products route", "A static CSS file", "A database migration"],
            "correct_answer": "A dynamic product route such as /products/42",
            "explanation": "Square brackets define a dynamic route segment."
        },
        {
            "id": "nextjs_009",
            "skill": "Next.js",
            "topic": "Route Handlers",
            "question": "Where is an App Router route handler commonly defined?",
            "options": ["In a route.js file inside the route directory", "In layout.css", "In package-lock.json", "In next.config.css"],
            "correct_answer": "In a route.js file inside the route directory",
            "explanation": "Route handlers define HTTP methods such as GET and POST in route.js or route.ts."
        },
        {
            "id": "nextjs_010",
            "skill": "Next.js",
            "topic": "Data Fetching",
            "question": "Where can server-side data fetching be performed in a Server Component?",
            "options": ["Directly in an async Server Component", "Only inside useEffect", "Only in a browser click handler", "Only in CSS"],
            "correct_answer": "Directly in an async Server Component",
            "explanation": "Server Components can await supported data-fetching operations on the server."
        },
        {
            "id": "nextjs_011",
            "skill": "Next.js",
            "topic": "Data Fetching",
            "question": "Why is fetching private API data in a Server Component sometimes useful?",
            "options": ["It can keep secret credentials on the server", "It exposes every secret to the browser", "It removes the need for authentication", "It disables all network requests"],
            "correct_answer": "It can keep secret credentials on the server",
            "explanation": "Server-only credentials can remain outside the client bundle when used correctly."
        },
        {
            "id": "nextjs_012",
            "skill": "Next.js",
            "topic": "Rendering",
            "question": "What is static rendering?",
            "options": ["Generating a page ahead of a request when possible", "Rendering only after every mouse click", "Saving all pages as database tables", "Disabling HTML output"],
            "correct_answer": "Generating a page ahead of a request when possible",
            "explanation": "Static output can be served efficiently when page data and configuration allow it."
        },
        {
            "id": "nextjs_013",
            "skill": "Next.js",
            "topic": "Rendering",
            "question": "What is dynamic rendering?",
            "options": ["Rendering a route at request time when its data or configuration requires it", "Rendering only static images", "Compiling CSS during every click", "Creating routes without URLs"],
            "correct_answer": "Rendering a route at request time when its data or configuration requires it",
            "explanation": "Dynamic rendering can support request-dependent data and behavior."
        },
        {
            "id": "nextjs_014",
            "skill": "Next.js",
            "topic": "Loading UI",
            "question": "What is loading.js used for in the App Router?",
            "options": ["Providing a loading UI while route content loads", "Installing npm packages", "Creating database indexes", "Defining a permanent redirect only"],
            "correct_answer": "Providing a loading UI while route content loads",
            "explanation": "Next.js can use loading.js to display a loading state for a route segment."
        },
        {
            "id": "nextjs_015",
            "skill": "Next.js",
            "topic": "Error Handling",
            "question": "What is error.js commonly used for?",
            "options": ["Providing an error boundary UI for a route segment", "Logging every error to a database automatically", "Replacing the root layout in every case", "Creating API credentials"],
            "correct_answer": "Providing an error boundary UI for a route segment",
            "explanation": "error.js provides a segment-level error UI and recovery mechanism."
        },
        {
            "id": "nextjs_016",
            "skill": "Next.js",
            "topic": "Metadata",
            "question": "How can a page define metadata in the App Router?",
            "options": ["Export metadata or generateMetadata from a supported server module", "Add metadata only inside a click handler", "Create a file named database.sql", "Use a CSS media query"],
            "correct_answer": "Export metadata or generateMetadata from a supported server module",
            "explanation": "Next.js uses these exports to generate page metadata such as titles and descriptions."
        },
        {
            "id": "nextjs_017",
            "skill": "Next.js",
            "topic": "Images",
            "question": "What is a key benefit of next/image?",
            "options": ["Image optimization and support for responsive image loading", "Automatic SQL query optimization", "Replacing every HTML form", "Encrypting all user uploads"],
            "correct_answer": "Image optimization and support for responsive image loading",
            "explanation": "The Image component provides image optimization features when configured and used appropriately."
        },
        {
            "id": "nextjs_018",
            "skill": "Next.js",
            "topic": "Fonts",
            "question": "What does next/font help with?",
            "options": ["Loading and optimizing fonts as part of the application build", "Managing database users", "Replacing React state", "Creating API routes automatically"],
            "correct_answer": "Loading and optimizing fonts as part of the application build",
            "explanation": "next/font helps reduce external font requests and supports optimized font loading."
        },
        {
            "id": "nextjs_019",
            "skill": "Next.js",
            "topic": "Environment Variables",
            "question": "Which environment variable prefix exposes a variable to browser-side code?",
            "options": ["NEXT_PUBLIC_", "SERVER_ONLY_", "PRIVATE_BROWSER_", "DATABASE_PUBLIC_ONLY_"],
            "correct_answer": "NEXT_PUBLIC_",
            "explanation": "NEXT_PUBLIC_ variables can be included in client-side bundles, so they must not contain secrets."
        },
        {
            "id": "nextjs_020",
            "skill": "Next.js",
            "topic": "Security",
            "question": "Where should a database password normally be used?",
            "options": ["In server-only code using a private environment variable", "In a NEXT_PUBLIC_ variable", "Inside visible JSX text", "In a public GitHub README"],
            "correct_answer": "In server-only code using a private environment variable",
            "explanation": "Private credentials must not be exposed in client bundles or public source."
        },
        {
            "id": "nextjs_021",
            "skill": "Next.js",
            "topic": "Middleware",
            "question": "What is the common purpose of Next.js middleware or proxy logic?",
            "options": ["Run request-time logic such as redirects or request checks before a route completes", "Replace every React component", "Store permanent user passwords in the browser", "Generate SQL tables from CSS"],
            "correct_answer": "Run request-time logic such as redirects or request checks before a route completes",
            "explanation": "This layer can intercept requests for supported routing and request-processing tasks; naming and runtime details depend on the Next.js version."
        },
        {
            "id": "nextjs_022",
            "skill": "Next.js",
            "topic": "API Integration",
            "question": "How can a Next.js application communicate with an external backend API?",
            "options": ["Use fetch or another HTTP client from an appropriate server or client context", "Only import the backend's database file", "Use CSS variables", "Use JSX tags as network protocols"],
            "correct_answer": "Use fetch or another HTTP client from an appropriate server or client context",
            "explanation": "HTTP requests can be made from server or client code, depending on security and interaction needs."
        },
        {
            "id": "nextjs_023",
            "skill": "Next.js",
            "topic": "Forms",
            "question": "What are Server Actions designed to support?",
            "options": ["Server-side functions that can be invoked by supported form or client interactions", "Only CSS animations", "Database queries directly from every browser without security checks", "Replacing all URL routes"],
            "correct_answer": "Server-side functions that can be invoked by supported form or client interactions",
            "explanation": "Server Actions support server-side mutations and still require validation and authorization."
        },
        {
            "id": "nextjs_024",
            "skill": "Next.js",
            "topic": "Caching",
            "question": "Why should developers understand Next.js caching behavior?",
            "options": ["It affects data freshness, performance, and when requests are repeated", "It controls the monitor brightness", "It replaces authentication", "It prevents all server errors"],
            "correct_answer": "It affects data freshness, performance, and when requests are repeated",
            "explanation": "Caching defaults and controls vary by Next.js version and the specific data-fetching approach."
        },
        {
            "id": "nextjs_025",
            "skill": "Next.js",
            "topic": "Revalidation",
            "question": "What is revalidation used for?",
            "options": ["Refreshing cached data or rendered output according to a chosen strategy", "Removing all routes", "Resetting the user's operating system", "Replacing HTML with SQL"],
            "correct_answer": "Refreshing cached data or rendered output according to a chosen strategy",
            "explanation": "Revalidation supports updating cached content without requiring a complete application rebuild for every change."
        },
        {
            "id": "nextjs_026",
            "skill": "Next.js",
            "topic": "Routing",
            "question": "What is a route group such as app/(dashboard)/settings/page.js used for?",
            "options": ["Organizing routes without adding the group name to the URL", "Adding dashboard to every URL automatically", "Creating a database schema", "Defining a global JavaScript variable"],
            "correct_answer": "Organizing routes without adding the group name to the URL",
            "explanation": "Parenthesized route groups organize route structure without affecting the URL path."
        },
        {
            "id": "nextjs_027",
            "skill": "Next.js",
            "topic": "Layouts",
            "question": "What is a benefit of nested layouts?",
            "options": ["Different route sections can share their own UI structure", "Every route must have identical content", "They remove all navigation", "They force every page to be a client component"],
            "correct_answer": "Different route sections can share their own UI structure",
            "explanation": "Nested layouts let sections maintain shared navigation or other UI."
        },
        {
            "id": "nextjs_028",
            "skill": "Next.js",
            "topic": "Dynamic Routes",
            "question": "What is the purpose of a catch-all segment such as [...slug]?",
            "options": ["Match one or more remaining path segments", "Match only a CSS class", "Disable routing", "Always match the home page only"],
            "correct_answer": "Match one or more remaining path segments",
            "explanation": "Catch-all segments collect multiple path parts into an array; optional catch-all segments use double brackets."
        },
        {
            "id": "nextjs_029",
            "skill": "Next.js",
            "topic": "Navigation",
            "question": "What is useRouter from next/navigation commonly used for in a Client Component?",
            "options": ["Programmatic navigation and related router actions", "Creating server environment variables", "Styling a grid", "Opening a database transaction directly"],
            "correct_answer": "Programmatic navigation and related router actions",
            "explanation": "The App Router's useRouter supports actions such as push, replace, and refresh."
        },
        {
            "id": "nextjs_030",
            "skill": "Next.js",
            "topic": "Search Parameters",
            "question": "What do URL search parameters commonly represent?",
            "options": ["Query-string values such as ?page=2", "Only dynamic folder names", "CSS animation frames", "Environment variables automatically"],
            "correct_answer": "Query-string values such as ?page=2",
            "explanation": "Search parameters can represent filters, pagination, and other URL-encoded state."
        },
        {
            "id": "nextjs_031",
            "skill": "Next.js",
            "topic": "Deployment",
            "question": "What does running npm run build commonly do in a Next.js project?",
            "options": ["Builds the application for production", "Starts an interactive database shell", "Deletes the source code", "Publishes the app to every hosting provider automatically"],
            "correct_answer": "Builds the application for production",
            "explanation": "The build command prepares the application for production; deployment is a separate step."
        },
        {
            "id": "nextjs_032",
            "skill": "Next.js",
            "topic": "Development",
            "question": "Which command commonly starts the Next.js development server in a project with the default scripts?",
            "options": ["npm run dev", "npm run database", "python start-next", "git deploy-everywhere"],
            "correct_answer": "npm run dev",
            "explanation": "The dev script normally starts the local development server."
        },
        {
            "id": "nextjs_033",
            "skill": "Next.js",
            "topic": "Styling",
            "question": "Which approach can be used to style Next.js components?",
            "options": ["CSS Modules, global CSS, or supported styling libraries", "Only inline SQL", "Only server environment variables", "Only image metadata"],
            "correct_answer": "CSS Modules, global CSS, or supported styling libraries",
            "explanation": "Next.js supports multiple styling approaches, including CSS Modules and global stylesheets."
        },
        {
            "id": "nextjs_034",
            "skill": "Next.js",
            "topic": "Static Assets",
            "question": "Where are files commonly placed to serve them directly from the site root?",
            "options": ["The public directory", "The node_modules directory", "The .git directory", "The app/layout.js file"],
            "correct_answer": "The public directory",
            "explanation": "A file such as public/logo.png can be referenced as /logo.png."
        },
        {
            "id": "nextjs_035",
            "skill": "Next.js",
            "topic": "Rendering",
            "question": "Why can Server Components reduce client-side JavaScript?",
            "options": ["Their implementation does not need to be shipped as client component JavaScript", "They disable all HTML output", "They force every library into the browser", "They replace the need for a server"],
            "correct_answer": "Their implementation does not need to be shipped as client component JavaScript",
            "explanation": "Server Components can keep server-only code out of the client bundle."
        },
        {
            "id": "nextjs_036",
            "skill": "Next.js",
            "topic": "Hydration",
            "question": "What can cause a hydration mismatch?",
            "options": ["Server-rendered HTML differs from the initial client-rendered output", "The page contains a valid title", "A route uses a layout", "A CSS file has a newline"],
            "correct_answer": "Server-rendered HTML differs from the initial client-rendered output",
            "explanation": "Non-deterministic values or environment-dependent rendering can cause markup differences."
        },
        {
            "id": "nextjs_037",
            "skill": "Next.js",
            "topic": "Authentication",
            "question": "What should a protected server-side operation do before returning private data?",
            "options": ["Verify authentication and authorize the requested action", "Trust any hidden button in the UI", "Expose the database password to the browser", "Skip all input checks"],
            "correct_answer": "Verify authentication and authorize the requested action",
            "explanation": "UI restrictions alone are not security controls; server-side operations must enforce access rules."
        },
        {
            "id": "nextjs_038",
            "skill": "Next.js",
            "topic": "Error Handling",
            "question": "What is notFound() from next/navigation used for?",
            "options": ["Triggering the not-found handling for a route segment", "Creating a new database", "Starting the development server", "Defining a client state hook"],
            "correct_answer": "Triggering the not-found handling for a route segment",
            "explanation": "Calling notFound() ends the current route segment's rendering path and displays its not-found UI."
        },
        {
            "id": "nextjs_039",
            "skill": "Next.js",
            "topic": "Internationalization",
            "question": "How can a Next.js application commonly organize language-specific routes?",
            "options": ["Use a locale segment such as app/[lang]/page.js", "Use a CSS color named locale", "Create a separate package.json for every sentence", "Store every translation in the URL fragment only"],
            "correct_answer": "Use a locale segment such as app/[lang]/page.js",
            "explanation": "A dynamic locale segment can help route users to language-specific content."
        },
        {
            "id": "nextjs_040",
            "skill": "Next.js",
            "topic": "Architecture",
            "question": "Which is a sound way to choose between Server and Client Components?",
            "options": ["Prefer Server Components by default and use Client Components when browser interactivity or client-only APIs are needed", "Make every component a Client Component regardless of need", "Never use Server Components", "Use Client Components to store private server secrets"],
            "correct_answer": "Prefer Server Components by default and use Client Components when browser interactivity or client-only APIs are needed",
            "explanation": "This approach can limit client JavaScript while preserving interactive features where required."
        }
    ],
    
    "typescript": [
        {
            "id": "typescript_001",
            "skill": "TypeScript",
            "topic": "Fundamentals",
            "question": "What is TypeScript?",
            "options": ["JavaScript with static type checking", "A relational database", "A CSS framework", "A replacement for HTML"],
            "correct_answer": "JavaScript with static type checking",
            "explanation": "TypeScript adds a type system to JavaScript and is commonly compiled to JavaScript."
        },
        {
            "id": "typescript_002",
            "skill": "Types",
            "topic": "Types",
            "question": "Which keyword explicitly declares a variable's type in TypeScript?",
            "options": ["let age: number", "let age := number", "number age := let", "type age = let"],
            "correct_answer": "let age: number",
            "explanation": "A colon followed by a type annotation declares the expected type."
        },
        {
            "id": "typescript_003",
            "skill": "TypeScript",
            "topic": "Type Inference",
            "question": "What is type inference?",
            "options": ["The compiler determines a type from the available context", "The programmer must annotate every value", "The browser converts CSS into JavaScript", "The database assigns a password"],
            "correct_answer": "The compiler determines a type from the available context",
            "explanation": "TypeScript can infer types from initial values and surrounding context."
        },
        {
            "id": "typescript_004",
            "skill": "TypeScript",
            "topic": "Primitive Types",
            "question": "Which type represents a true or false value?",
            "options": ["boolean", "string", "number", "object"],
            "correct_answer": "boolean",
            "explanation": "The boolean type represents true or false."
        },
        {
            "id": "typescript_005",
            "skill": "TypeScript",
            "topic": "Arrays",
            "question": "Which declaration represents an array of numbers?",
            "options": ["let scores: number[]", "let scores: number", "let scores: boolean[]", "let scores: string"],
            "correct_answer": "let scores: number[]",
            "explanation": "The number[] syntax represents an array whose elements are numbers."
        },
        {
            "id": "typescript_006",
            "skill": "TypeScript",
            "topic": "Functions",
            "question": "How do you specify that a function returns a string?",
            "options": ["function greet(): string", "function greet() -> string", "string function greet()", "function string: greet()"],
            "correct_answer": "function greet(): string",
            "explanation": "The return type appears after the parameter list, following a colon."
        },
        {
            "id": "typescript_007",
            "skill": "TypeScript",
            "topic": "Interfaces",
            "question": "What is an interface commonly used for?",
            "options": ["Describing the expected structure of an object", "Executing SQL queries", "Creating browser windows", "Installing packages"],
            "correct_answer": "Describing the expected structure of an object",
            "explanation": "Interfaces describe object shapes and can be used to check whether values match them."
        },
        {
            "id": "typescript_008",
            "skill": "TypeScript",
            "topic": "Type Aliases",
            "question": "Which keyword creates a type alias?",
            "options": ["type", "alias", "typedefine", "interfaceonly"],
            "correct_answer": "type",
            "explanation": "The type keyword creates a named alias for a type expression."
        },
        {
            "id": "typescript_009",
            "skill": "TypeScript",
            "topic": "Union Types",
            "question": "What does string | number mean?",
            "options": ["The value may be a string or a number", "The value must be both types simultaneously", "The value must be a boolean", "The value is always null"],
            "correct_answer": "The value may be a string or a number",
            "explanation": "A union type allows a value to match one of its listed alternatives."
        },
        {
            "id": "typescript_010",
            "skill": "TypeScript",
            "topic": "Literal Types",
            "question": "What does the type 'success' | 'error' allow?",
            "options": ["Only the literal values success or error", "Any string without restriction", "Only numeric values", "Only arrays"],
            "correct_answer": "Only the literal values success or error",
            "explanation": "String literal unions restrict values to the specified strings."
        },
        {
            "id": "typescript_011",
            "skill": "TypeScript",
            "topic": "Optional Properties",
            "question": "What does the question mark mean in `name?: string`?",
            "options": ["The property is optional", "The property must be null", "The property is private", "The property is always numeric"],
            "correct_answer": "The property is optional",
            "explanation": "An optional property may be absent from the object."
        },
        {
            "id": "typescript_012",
            "skill": "TypeScript",
            "topic": "Interfaces",
            "question": "Can a TypeScript interface describe an optional property?",
            "options": ["Yes, using a question mark after the property name", "No, interfaces only describe functions", "Only when using JavaScript files", "Only for numeric properties"],
            "correct_answer": "Yes, using a question mark after the property name",
            "explanation": "An interface can declare optional properties such as email?: string."
        },
        {
            "id": "typescript_013",
            "skill": "TypeScript",
            "topic": "Generics",
            "question": "What is the main purpose of generics?",
            "options": ["Create reusable code that works with different types while preserving type information", "Force every value to be a string", "Replace functions with classes", "Run code only in a browser"],
            "correct_answer": "Create reusable code that works with different types while preserving type information",
            "explanation": "Generics allow types to be supplied as parameters to reusable functions, classes, and interfaces."
        },
        {
            "id": "typescript_014",
            "skill": "TypeScript",
            "topic": "Generics",
            "question": "In `function identity<T>(value: T): T`, what does T represent?",
            "options": ["A generic type parameter", "A required text value", "A database table", "A runtime loop"],
            "correct_answer": "A generic type parameter",
            "explanation": "T represents a type selected when the function is used or inferred."
        },
        {
            "id": "typescript_015",
            "skill": "TypeScript",
            "topic": "Type Narrowing",
            "question": "What is type narrowing?",
            "options": ["Reducing a broad type to a more specific type using checks", "Removing all type information", "Converting every value to a string", "Making a function private"],
            "correct_answer": "Reducing a broad type to a more specific type using checks",
            "explanation": "Checks such as typeof can help TypeScript determine a more specific type in a code branch."
        },
        {
            "id": "typescript_016",
            "skill": "TypeScript",
            "topic": "Type Guards",
            "question": "Which check can narrow a value typed as string | number?",
            "options": ["typeof value === 'string'", "value.css === true", "value.sql()", "document.type(value)"],
            "correct_answer": "typeof value === 'string'",
            "explanation": "The typeof check narrows the value to string in the matching branch."
        },
        {
            "id": "typescript_017",
            "skill": "TypeScript",
            "topic": "Enums",
            "question": "What are enums used for in TypeScript?",
            "options": ["Defining a named set of related constants", "Creating HTML elements", "Connecting directly to every database", "Replacing the compiler"],
            "correct_answer": "Defining a named set of related constants",
            "explanation": "Enums provide named constants, though literal unions are also a common alternative."
        },
        {
            "id": "typescript_018",
            "skill": "TypeScript",
            "topic": "Type Assertions",
            "question": "What does a type assertion do?",
            "options": ["Tells the compiler to treat a value as a specified type", "Validates every value at runtime automatically", "Converts every value into that type at runtime", "Creates an interface automatically"],
            "correct_answer": "Tells the compiler to treat a value as a specified type",
            "explanation": "Type assertions affect compile-time checking and do not perform runtime conversion or validation."
        },
        {
            "id": "typescript_019",
            "skill": "TypeScript",
            "topic": "Unknown Type",
            "question": "Why is unknown often safer than any?",
            "options": ["Values of type unknown must be checked before most operations", "unknown accepts only strings", "unknown automatically validates API data", "unknown disables type checking"],
            "correct_answer": "Values of type unknown must be checked before most operations",
            "explanation": "The unknown type requires narrowing or an assertion before using the value as a more specific type."
        },
        {
            "id": "typescript_020",
            "skill": "TypeScript",
            "topic": "Any Type",
            "question": "What is a major risk of using any extensively?",
            "options": ["It bypasses many useful type checks", "It prevents all JavaScript output", "It makes every value immutable", "It automatically checks data at runtime"],
            "correct_answer": "It bypasses many useful type checks",
            "explanation": "Excessive any usage reduces the errors TypeScript can catch during development."
        },
        {
            "id": "typescript_021",
            "skill": "TypeScript",
            "topic": "Utility Types",
            "question": "What does Partial<T> do?",
            "options": ["Makes the properties of T optional", "Makes every property private", "Converts T into a string", "Removes all properties from T"],
            "correct_answer": "Makes the properties of T optional",
            "explanation": "Partial is a built-in utility type that makes each property optional."
        },
        {
            "id": "typescript_022",
            "skill": "TypeScript",
            "topic": "Utility Types",
            "question": "What does Pick<T, K> do?",
            "options": ["Creates a type containing selected properties of T", "Deletes the selected runtime object properties", "Makes every property optional", "Converts T to a function"],
            "correct_answer": "Creates a type containing selected properties of T",
            "explanation": "Pick constructs a type using the chosen keys from another type."
        },
        {
            "id": "typescript_023",
            "skill": "TypeScript",
            "topic": "Utility Types",
            "question": "What does Omit<T, K> do?",
            "options": ["Creates a type excluding selected properties", "Deletes properties from an object at runtime", "Makes every property numeric", "Combines two arrays"],
            "correct_answer": "Creates a type excluding selected properties",
            "explanation": "Omit produces a type containing the properties of T except the specified keys."
        },
        {
            "id": "typescript_024",
            "skill": "TypeScript",
            "topic": "Readonly",
            "question": "What does Readonly<T> do?",
            "options": ["Marks properties as readonly in the resulting type", "Freezes an object at runtime automatically", "Makes all values strings", "Removes all methods"],
            "correct_answer": "Marks properties as readonly in the resulting type",
            "explanation": "Readonly is a compile-time type utility and does not itself freeze an object at runtime."
        },
        {
            "id": "typescript_025",
            "skill": "TypeScript",
            "topic": "Null Safety",
            "question": "What does strictNullChecks help detect?",
            "options": ["Potentially unsafe use of null and undefined", "Slow CSS animations", "Missing database indexes", "Incorrect image dimensions"],
            "correct_answer": "Potentially unsafe use of null and undefined",
            "explanation": "With strictNullChecks enabled, null and undefined are treated as distinct types."
        },
        {
            "id": "typescript_026",
            "skill": "TypeScript",
            "topic": "Optional Chaining",
            "question": "What does `user?.address` do?",
            "options": ["Safely accesses address when user is not null or undefined", "Always throws an error", "Creates an address object", "Converts user into an array"],
            "correct_answer": "Safely accesses address when user is not null or undefined",
            "explanation": "Optional chaining returns undefined if the value before ?. is null or undefined."
        },
        {
            "id": "typescript_027",
            "skill": "TypeScript",
            "topic": "Nullish Coalescing",
            "question": "What does `value ?? fallback` use fallback for?",
            "options": ["When value is null or undefined", "Whenever value is zero", "Whenever value is an empty string", "Whenever value is false"],
            "correct_answer": "When value is null or undefined",
            "explanation": "Nullish coalescing preserves values such as 0, false, and an empty string."
        },
        {
            "id": "typescript_028",
            "skill": "TypeScript",
            "topic": "Classes",
            "question": "Which keyword indicates that a class inherits from another class?",
            "options": ["extends", "inheritsFrom", "implementsOnly", "include"],
            "correct_answer": "extends",
            "explanation": "The extends keyword establishes class inheritance."
        },
        {
            "id": "typescript_029",
            "skill": "TypeScript",
            "topic": "Access Modifiers",
            "question": "What does the private access modifier generally mean in a TypeScript class?",
            "options": ["The member is restricted from ordinary access outside its class", "The member is automatically encrypted", "The member is available only through CSS", "The member is always static"],
            "correct_answer": "The member is restricted from ordinary access outside its class",
            "explanation": "TypeScript private provides compile-time access restrictions; JavaScript #private fields have runtime privacy."
        },
        {
            "id": "typescript_030",
            "skill": "TypeScript",
            "topic": "Interfaces",
            "question": "What does implements do in a class declaration?",
            "options": ["Checks that the class satisfies an interface or compatible type", "Creates a new database", "Imports a package automatically", "Makes every method asynchronous"],
            "correct_answer": "Checks that the class satisfies an interface or compatible type",
            "explanation": "implements checks structural compatibility at compile time."
        },
        {
            "id": "typescript_031",
            "skill": "TypeScript",
            "topic": "Modules",
            "question": "How can a value be made available to another module?",
            "options": ["Use export and import", "Use only console.log", "Use a CSS selector", "Use an HTML comment"],
            "correct_answer": "Use export and import",
            "explanation": "JavaScript module exports and imports share values between modules."
        },
        {
            "id": "typescript_032",
            "skill": "TypeScript",
            "topic": "Compiler",
            "question": "What is the purpose of tsconfig.json?",
            "options": ["Configure TypeScript compiler options and project files", "Store user login passwords", "Define a database schema only", "Configure HTML forms"],
            "correct_answer": "Configure TypeScript compiler options and project files",
            "explanation": "The TypeScript project configuration controls compiler behavior and related project settings."
        },
        {
            "id": "typescript_033",
            "skill": "TypeScript",
            "topic": "Compiler",
            "question": "Which command commonly compiles TypeScript using the TypeScript compiler?",
            "options": ["tsc", "npm-css", "python-ts", "git-types"],
            "correct_answer": "tsc",
            "explanation": "The tsc command runs the TypeScript compiler."
        },
        {
            "id": "typescript_034",
            "skill": "TypeScript",
            "topic": "Async Programming",
            "question": "What is the return type of an async function that returns a number?",
            "options": ["Promise<number>", "number[]", "void only", "string"],
            "correct_answer": "Promise<number>",
            "explanation": "An async function wraps its returned value in a Promise."
        },
        {
            "id": "typescript_035",
            "skill": "TypeScript",
            "topic": "Tuples",
            "question": "What is a tuple useful for?",
            "options": ["Representing an array with a known sequence of element types", "Storing only database tables", "Defining CSS layouts", "Running code without compilation"],
            "correct_answer": "Representing an array with a known sequence of element types",
            "explanation": "Tuples can describe fixed-position values with specific types."
        },
        {
            "id": "typescript_036",
            "skill": "TypeScript",
            "topic": "Discriminated Unions",
            "question": "How can a discriminated union commonly be narrowed?",
            "options": ["Check a shared literal-valued property", "Convert every variant to any", "Remove all object properties", "Compare CSS class names only"],
            "correct_answer": "Check a shared literal-valued property",
            "explanation": "A shared property such as status can distinguish union variants."
        },
        {
            "id": "typescript_037",
            "skill": "TypeScript",
            "topic": "Type Compatibility",
            "question": "What does structural typing primarily compare?",
            "options": ["The members and shape of types", "Only the names of classes", "Only source file names", "Only package versions"],
            "correct_answer": "The members and shape of types",
            "explanation": "TypeScript generally checks whether the required members are compatible."
        },
        {
            "id": "typescript_038",
            "skill": "TypeScript",
            "topic": "Declaration Files",
            "question": "What is a .d.ts file commonly used for?",
            "options": ["Providing type declarations for JavaScript code or libraries", "Storing images", "Defining SQL records", "Running a web server"],
            "correct_answer": "Providing type declarations for JavaScript code or libraries",
            "explanation": "Declaration files describe types without implementing the runtime behavior."
        },
        {
            "id": "typescript_039",
            "skill": "TypeScript",
            "topic": "Runtime Validation",
            "question": "Does a TypeScript interface automatically validate JSON received from an API at runtime?",
            "options": ["No, runtime validation requires additional checks", "Yes, every interface validates all incoming data", "Yes, but only in CSS", "No, because TypeScript cannot describe objects"],
            "correct_answer": "No, runtime validation requires additional checks",
            "explanation": "Type information is generally erased during compilation, so external data must be validated separately."
        },
        {
            "id": "typescript_040",
            "skill": "TypeScript",
            "topic": "Best Practices",
            "question": "Which practice improves TypeScript reliability?",
            "options": ["Use strict checking and validate untrusted external data", "Use any for every variable", "Assume API responses always match declared interfaces", "Disable all compiler diagnostics"],
            "correct_answer": "Use strict checking and validate untrusted external data",
            "explanation": "Static checks and runtime validation address different kinds of errors."
        }
    ],
    "node.js": [
        {
            "id": "nodejs_001",
            "skill": "Node.js",
            "topic": "Fundamentals",
            "question": "What is Node.js?",
            "options": ["A JavaScript runtime built on the V8 engine", "A database query language", "A CSS framework", "A browser-only JavaScript library"],
            "correct_answer": "A JavaScript runtime built on the V8 engine",
            "explanation": "Node.js executes JavaScript outside the browser."
        },
        {
            "id": "nodejs_002",
            "skill": "Node.js",
            "topic": "Runtime",
            "question": "Which engine executes JavaScript in Node.js?",
            "options": ["V8", "SQLite", "PostgreSQL", "Bootstrap"],
            "correct_answer": "V8",
            "explanation": "Node.js uses Google's V8 JavaScript engine."
        },
        {
            "id": "nodejs_003",
            "skill": "Node.js",
            "topic": "Modules",
            "question": "Which function is commonly used to load a module in CommonJS?",
            "options": ["require()", "includeCSS()", "loadSQL()", "importFileOnly()"],
            "correct_answer": "require()",
            "explanation": "CommonJS modules commonly use require() to load dependencies."
        },
        {
            "id": "nodejs_004",
            "skill": "Node.js",
            "topic": "Modules",
            "question": "Which syntax exports a value in CommonJS?",
            "options": ["module.exports = value", "document.exports = value", "css.exports = value", "server.return = value"],
            "correct_answer": "module.exports = value",
            "explanation": "module.exports defines the value exposed by a CommonJS module."
        },
        {
            "id": "nodejs_005",
            "skill": "Node.js",
            "topic": "Package Management",
            "question": "What is package.json used for?",
            "options": ["Recording project metadata, scripts, and dependencies", "Storing only HTML content", "Replacing the Node.js runtime", "Saving browser cookies exclusively"],
            "correct_answer": "Recording project metadata, scripts, and dependencies",
            "explanation": "package.json describes a Node.js project and its package configuration."
        },
        {
            "id": "nodejs_006",
            "skill": "Node.js",
            "topic": "Package Management",
            "question": "What does npm install commonly do when run in a project directory?",
            "options": ["Installs project dependencies", "Deletes all JavaScript files", "Starts a database server automatically", "Compiles every HTML page into CSS"],
            "correct_answer": "Installs project dependencies",
            "explanation": "npm install installs dependencies described by the project manifest and lockfile when available."
        },
        {
            "id": "nodejs_007",
            "skill": "Node.js",
            "topic": "Event Loop",
            "question": "What is the event loop responsible for?",
            "options": ["Coordinating callbacks and asynchronous work in the JavaScript runtime", "Creating HTML tags", "Designing database tables", "Styling application buttons"],
            "correct_answer": "Coordinating callbacks and asynchronous work in the JavaScript runtime",
            "explanation": "The event loop allows Node.js to handle asynchronous operations without blocking on every I/O task."
        },
        {
            "id": "nodejs_008",
            "skill": "Node.js",
            "topic": "Asynchronous Programming",
            "question": "Why can asynchronous I/O improve a Node.js server's scalability?",
            "options": ["It allows the process to handle other work while I/O is pending", "It makes every CPU operation parallel automatically", "It removes the need for memory", "It converts all requests into database queries"],
            "correct_answer": "It allows the process to handle other work while I/O is pending",
            "explanation": "While an I/O operation waits, Node.js can continue processing other events."
        },
        {
            "id": "nodejs_009",
            "skill": "Node.js",
            "topic": "Callbacks",
            "question": "What is a callback?",
            "options": ["A function passed to another function to be called later or at a defined point", "A database table", "A type of HTML attribute", "A CSS animation"],
            "correct_answer": "A function passed to another function to be called later or at a defined point",
            "explanation": "Callbacks are commonly used to handle events and asynchronous results."
        },
        {
            "id": "nodejs_010",
            "skill": "Node.js",
            "topic": "Promises",
            "question": "Which method handles a rejected Promise?",
            "options": [".catch()", ".style()", ".select()", ".renderCSS()"],
            "correct_answer": ".catch()",
            "explanation": "The catch method registers a rejection handler for a Promise chain."
        },
        {
            "id": "nodejs_011",
            "skill": "Node.js",
            "topic": "Async Programming",
            "question": "What does await do inside an async function?",
            "options": ["Pauses that function's progress until the awaited Promise settles", "Stops the entire operating system", "Automatically starts a new process", "Converts a Promise into a database"],
            "correct_answer": "Pauses that function's progress until the awaited Promise settles",
            "explanation": "await suspends the async function while allowing the runtime to process other work."
        },
        {
            "id": "nodejs_012",
            "skill": "Node.js",
            "topic": "File System",
            "question": "Which built-in module provides file-system operations?",
            "options": ["node:fs", "node:css", "node:html", "node:style"],
            "correct_answer": "node:fs",
            "explanation": "The fs module provides APIs for working with files and directories."
        },
        {
            "id": "nodejs_013",
            "skill": "Node.js",
            "topic": "File System",
            "question": "Why might fs.readFile() be preferred over fs.readFileSync() in a request handler?",
            "options": ["The asynchronous version avoids blocking the event loop while waiting for file I/O", "It always reads files in less memory", "It automatically encrypts files", "It requires no file path"],
            "correct_answer": "The asynchronous version avoids blocking the event loop while waiting for file I/O",
            "explanation": "Synchronous file operations block JavaScript execution until they complete."
        },
        {
            "id": "nodejs_014",
            "skill": "Node.js",
            "topic": "Path Module",
            "question": "What is the path module used for?",
            "options": ["Working with file and directory paths", "Creating HTTP response codes", "Validating passwords automatically", "Rendering React components"],
            "correct_answer": "Working with file and directory paths",
            "explanation": "The path module provides utilities for joining, resolving, and analyzing paths."
        },
        {
            "id": "nodejs_015",
            "skill": "Node.js",
            "topic": "HTTP",
            "question": "Which built-in module can create an HTTP server?",
            "options": ["node:http", "node:css", "node:images", "node:styles"],
            "correct_answer": "node:http",
            "explanation": "The http module supports creating HTTP servers and clients."
        },
        {
            "id": "nodejs_016",
            "skill": "Node.js",
            "topic": "HTTP",
            "question": "What does an HTTP server's request handler receive?",
            "options": ["Request and response objects", "Only a CSS stylesheet", "Only a database password", "A React component and a JSX file"],
            "correct_answer": "Request and response objects",
            "explanation": "The request describes the incoming request, and the response is used to send a reply."
        },
        {
            "id": "nodejs_017",
            "skill": "Node.js",
            "topic": "Environment Variables",
            "question": "How can a Node.js application read an environment variable?",
            "options": ["process.env.VARIABLE_NAME", "document.env.VARIABLE_NAME", "css.env.VARIABLE_NAME", "window.serverSecret"],
            "correct_answer": "process.env.VARIABLE_NAME",
            "explanation": "Environment variables are exposed through process.env."
        },
        {
            "id": "nodejs_018",
            "skill": "Node.js",
            "topic": "Process",
            "question": "What does process.argv contain?",
            "options": ["Command-line arguments supplied to the Node.js process", "All database records", "All files on the computer", "Only HTTP response headers"],
            "correct_answer": "Command-line arguments supplied to the Node.js process",
            "explanation": "process.argv is an array containing the executable path, script path, and supplied arguments."
        },
        {
            "id": "nodejs_019",
            "skill": "Node.js",
            "topic": "Buffers",
            "question": "What is a Buffer used for?",
            "options": ["Working with binary data", "Defining CSS colors", "Creating React routes", "Storing only JavaScript function names"],
            "correct_answer": "Working with binary data",
            "explanation": "Buffers represent sequences of bytes, useful for files, streams, and network data."
        },
        {
            "id": "nodejs_020",
            "skill": "Node.js",
            "topic": "Streams",
            "question": "Why are streams useful for large files?",
            "options": ["They allow data to be processed in chunks", "They require the entire file to fit in memory first", "They automatically compress every file", "They eliminate all file errors"],
            "correct_answer": "They allow data to be processed in chunks",
            "explanation": "Streaming can reduce memory usage compared with loading an entire large file at once."
        },
        {
            "id": "nodejs_021",
            "skill": "Node.js",
            "topic": "Streams",
            "question": "What is backpressure in streams?",
            "options": ["A mechanism that helps a slower consumer control the rate of incoming data", "A type of password encryption", "A way to style HTTP headers", "An automatic database backup"],
            "correct_answer": "A mechanism that helps a slower consumer control the rate of incoming data",
            "explanation": "Backpressure helps prevent a producer from overwhelming a consumer."
        },
        {
            "id": "nodejs_022",
            "skill": "Node.js",
            "topic": "Events",
            "question": "Which class is commonly used to create event emitters?",
            "options": ["EventEmitter from node:events", "HTMLElement from node:html", "DatabaseEmitter from node:sql", "CSSListener from node:style"],
            "correct_answer": "EventEmitter from node:events",
            "explanation": "EventEmitter supports emitting named events and registering listeners."
        },
        {
            "id": "nodejs_023",
            "skill": "Node.js",
            "topic": "Error Handling",
            "question": "How should a rejected Promise normally be handled?",
            "options": ["Use await with try/catch or attach a rejection handler", "Ignore it in every situation", "Convert it to CSS", "Restart the computer automatically"],
            "correct_answer": "Use await with try/catch or attach a rejection handler",
            "explanation": "Handling rejections makes failures easier to report and recover from."
        },
        {
            "id": "nodejs_024",
            "skill": "Node.js",
            "topic": "Security",
            "question": "What is a safer way to handle application secrets?",
            "options": ["Keep them in protected environment configuration and never commit them to source control", "Hard-code them in a public repository", "Return them in every API response", "Place them in public client-side JavaScript"],
            "correct_answer": "Keep them in protected environment configuration and never commit them to source control",
            "explanation": "Secrets should be restricted to authorized environments and kept out of public code."
        },
        {
            "id": "nodejs_025",
            "skill": "Node.js",
            "topic": "Security",
            "question": "Why should user input be validated on the server?",
            "options": ["Client-side checks can be bypassed", "Browsers always send valid data", "Validation replaces authentication", "Node.js cannot receive strings"],
            "correct_answer": "Client-side checks can be bypassed",
            "explanation": "Server-side validation is necessary because clients cannot be trusted to enforce rules."
        },
        {
            "id": "nodejs_026",
            "skill": "Node.js",
            "topic": "Child Processes",
            "question": "What is the child_process module used for?",
            "options": ["Creating and interacting with subprocesses", "Rendering HTML forms", "Defining JavaScript types", "Managing CSS layouts"],
            "correct_answer": "Creating and interacting with subprocesses",
            "explanation": "The module provides APIs for starting external programs and other processes."
        },
        {
            "id": "nodejs_027",
            "skill": "Node.js",
            "topic": "Child Processes",
            "question": "Why can execFile() be preferable to constructing a shell command with untrusted input?",
            "options": ["It can run an executable directly without a shell by default", "It automatically makes every program safe", "It removes the need for input validation", "It encrypts command-line arguments"],
            "correct_answer": "It can run an executable directly without a shell by default",
            "explanation": "Avoiding shell interpretation reduces shell-injection risk, though input validation and safe argument handling remain important."
        },
        {
            "id": "nodejs_028",
            "skill": "Node.js",
            "topic": "Worker Threads",
            "question": "When are worker threads especially useful?",
            "options": ["For CPU-intensive JavaScript work that should run off the main event loop", "For replacing every HTTP request", "For styling HTML elements", "For storing environment variables"],
            "correct_answer": "For CPU-intensive JavaScript work that should run off the main event loop",
            "explanation": "Worker threads can run CPU-intensive JavaScript in parallel threads."
        },
        {
            "id": "nodejs_029",
            "skill": "Node.js",
            "topic": "Performance",
            "question": "What can happen if a Node.js callback performs a very long CPU-bound loop?",
            "options": ["It can block the event loop and delay other requests", "It automatically creates many worker threads", "It makes all I/O complete instantly", "It disables JavaScript execution permanently"],
            "correct_answer": "It can block the event loop and delay other requests",
            "explanation": "Long synchronous tasks prevent the event loop from processing other callbacks until they finish."
        },
        {
            "id": "nodejs_030",
            "skill": "Node.js",
            "topic": "Timers",
            "question": "What does setTimeout(callback, delay) do?",
            "options": ["Schedules a callback to run after a minimum delay when the event loop can process it", "Guarantees execution at the exact millisecond", "Blocks the thread until the delay ends", "Runs the callback in a separate process automatically"],
            "correct_answer": "Schedules a callback to run after a minimum delay when the event loop can process it",
            "explanation": "The callback runs when the timer has expired and the event loop can execute it."
        },
        {
            "id": "nodejs_031",
            "skill": "Node.js",
            "topic": "Module Systems",
            "question": "Which file setting commonly enables ES module syntax in Node.js JavaScript files?",
            "options": ["Setting \"type\": \"module\" in package.json", "Setting \"type\": \"css\"", "Adding \"database\": true", "Creating index.html only"],
            "correct_answer": "Setting \"type\": \"module\" in package.json",
            "explanation": "The package type field can make .js files use the ES module system."
        },
        {
            "id": "nodejs_032",
            "skill": "Node.js",
            "topic": "Module Systems",
            "question": "What is a common distinction between CommonJS and ES modules?",
            "options": ["CommonJS commonly uses require/module.exports, while ES modules use import/export", "CommonJS uses CSS, while ES modules use SQL", "ES modules cannot export values", "CommonJS only runs inside browsers"],
            "correct_answer": "CommonJS commonly uses require/module.exports, while ES modules use import/export",
            "explanation": "These are two module systems supported by Node.js, with different syntax and loading semantics."
        },
        {
            "id": "nodejs_033",
            "skill": "Node.js",
            "topic": "Testing",
            "question": "What is the purpose of automated tests in a Node.js project?",
            "options": ["Check expected behavior and catch regressions", "Guarantee that software has no bugs", "Replace all documentation", "Automatically secure every server"],
            "correct_answer": "Check expected behavior and catch regressions",
            "explanation": "Tests help detect incorrect behavior but cannot guarantee the absence of every defect."
        },
        {
            "id": "nodejs_034",
            "skill": "Node.js",
            "topic": "Debugging",
            "question": "Which built-in capability can help debug a Node.js application?",
            "options": ["The Node.js inspector and debugger tools", "Only CSS media queries", "Only SQL indexes", "An HTML image tag"],
            "correct_answer": "The Node.js inspector and debugger tools",
            "explanation": "The inspector supports breakpoints, stepping through code, and examining runtime state."
        },
        {
            "id": "nodejs_035",
            "skill": "Node.js",
            "topic": "Database Integration",
            "question": "What is a good practice when querying a database from Node.js?",
            "options": ["Use parameterized queries or the database library's safe query interface", "Build SQL by directly concatenating untrusted input", "Expose database credentials to clients", "Skip access control for every query"],
            "correct_answer": "Use parameterized queries or the database library's safe query interface",
            "explanation": "Parameterized queries help prevent SQL injection."
        },
        {
            "id": "nodejs_036",
            "skill": "Node.js",
            "topic": "HTTP Clients",
            "question": "Which built-in API is available in modern Node.js versions for making HTTP requests?",
            "options": ["fetch()", "document.fetchCSS()", "sqlRequest()", "browserOnlyGet()"],
            "correct_answer": "fetch()",
            "explanation": "Modern Node.js includes a global fetch API; availability and behavior can depend on the runtime version."
        },
        {
            "id": "nodejs_037",
            "skill": "Node.js",
            "topic": "Memory Management",
            "question": "What can cause a memory leak in a long-running Node.js process?",
            "options": ["Keeping unnecessary references that prevent objects from being collected", "Using a const declaration", "Returning a string from a function", "Reading a small file once"],
            "correct_answer": "Keeping unnecessary references that prevent objects from being collected",
            "explanation": "Garbage collection cannot reclaim objects that remain reachable."
        },
        {
            "id": "nodejs_038",
            "skill": "Node.js",
            "topic": "Process Signals",
            "question": "Why might a server handle SIGTERM?",
            "options": ["To perform graceful shutdown when asked to terminate", "To create a new HTML element", "To install npm packages", "To change the CSS theme"],
            "correct_answer": "To perform graceful shutdown when asked to terminate",
            "explanation": "A server can handle SIGTERM to stop accepting work and close resources cleanly."
        },
        {
            "id": "nodejs_039",
            "skill": "Node.js",
            "topic": "Logging",
            "question": "What is a benefit of structured application logging?",
            "options": ["Logs can be searched and analyzed using consistent fields", "It guarantees there will be no runtime errors", "It automatically encrypts every network connection", "It replaces all monitoring"],
            "correct_answer": "Logs can be searched and analyzed using consistent fields",
            "explanation": "Structured logs make it easier to filter events by fields such as level, request ID, and timestamp."
        },
        {
            "id": "nodejs_040",
            "skill": "Node.js",
            "topic": "Architecture",
            "question": "Which practice helps make a Node.js service easier to maintain?",
            "options": ["Separate responsibilities and handle errors at appropriate boundaries", "Put all code in one giant callback", "Ignore rejected Promises", "Store every secret directly in source files"],
            "correct_answer": "Separate responsibilities and handle errors at appropriate boundaries",
            "explanation": "Modular code and clear error handling improve testability and maintainability."
        }
    ],
    
    "express.js": [
        {
            "id": "express_001",
            "skill": "Express.js",
            "topic": "Fundamentals",
            "question": "What is Express.js?",
            "options": ["A web framework for Node.js", "A relational database", "A programming language", "A CSS preprocessor"],
            "correct_answer": "A web framework for Node.js",
            "explanation": "Express provides tools for building web servers and APIs with Node.js."
        },
        {
            "id": "express_002",
            "skill": "Routing",
            "topic": "Routing",
            "question": "Which method defines a route that handles HTTP GET requests?",
            "options": ["app.get()", "app.read()", "app.fetchRoute()", "app.select()"],
            "correct_answer": "app.get()",
            "explanation": "app.get() registers a handler for GET requests at a specified path."
        },
        {
            "id": "express_003",
            "skill": "Express.js",
            "topic": "Routing",
            "question": "Which method commonly handles HTTP POST requests?",
            "options": ["app.post()", "app.createRoute()", "app.insert()", "app.sendPost()"],
            "correct_answer": "app.post()",
            "explanation": "POST routes are commonly used to receive submitted data or create resources."
        },
        {
            "id": "express_004",
            "skill": "Express.js",
            "topic": "Middleware",
            "question": "What is Express middleware?",
            "options": ["A function that can access the request, response, and next function", "A database table", "A CSS class", "A browser extension"],
            "correct_answer": "A function that can access the request, response, and next function",
            "explanation": "Middleware can run logic, modify request or response objects, end a response, or pass control onward."
        },
        {
            "id": "express_005",
            "skill": "Express.js",
            "topic": "Middleware",
            "question": "What does next() normally do in regular middleware?",
            "options": ["Passes control to the next middleware or route handler", "Restarts the server", "Deletes the current request", "Automatically sends JSON"],
            "correct_answer": "Passes control to the next middleware or route handler",
            "explanation": "Calling next() continues the request-processing chain."
        },
        {
            "id": "express_006",
            "skill": "Express.js",
            "topic": "Middleware",
            "question": "What can happen if middleware neither sends a response nor calls next()?",
            "options": ["The request may remain pending", "Express automatically sends a 200 response in every case", "The database always restarts", "The route is converted to GET"],
            "correct_answer": "The request may remain pending",
            "explanation": "A middleware function must continue processing or finish the response."
        },
        {
            "id": "express_007",
            "skill": "Express.js",
            "topic": "Request Data",
            "question": "Where are named route parameters stored?",
            "options": ["req.params", "req.body only", "res.params", "app.parameters"],
            "correct_answer": "req.params",
            "explanation": "A route such as /users/:id makes the id value available through req.params.id."
        },
        {
            "id": "express_008",
            "skill": "Express.js",
            "topic": "Request Data",
            "question": "Where are URL query-string parameters commonly available?",
            "options": ["req.query", "req.params only", "res.query", "app.queryString"],
            "correct_answer": "req.query",
            "explanation": "For a URL such as /search?q=python, the q parameter is available through req.query."
        },
        {
            "id": "express_009",
            "skill": "Express.js",
            "topic": "Request Data",
            "question": "Which middleware commonly parses incoming JSON request bodies?",
            "options": ["express.json()", "express.static()", "express.router()", "express.html()"],
            "correct_answer": "express.json()",
            "explanation": "express.json() parses supported JSON request bodies and populates req.body."
        },
        {
            "id": "express_010",
            "skill": "Express.js",
            "topic": "Request Data",
            "question": "What is req.body commonly used for?",
            "options": ["Accessing parsed data submitted in the request body", "Reading the response status", "Defining application routes", "Starting the HTTP server"],
            "correct_answer": "Accessing parsed data submitted in the request body",
            "explanation": "The available body data depends on the request content type and configured parsing middleware."
        },
        {
            "id": "express_011",
            "skill": "Express.js",
            "topic": "Responses",
            "question": "Which method sends a JSON response?",
            "options": ["res.json()", "req.json()", "app.jsonResponseOnly()", "next.json()"],
            "correct_answer": "res.json()",
            "explanation": "res.json() serializes a value as JSON and sends the response."
        },
        {
            "id": "express_012",
            "skill": "Express.js",
            "topic": "Responses",
            "question": "What does res.status(404).json({ error: 'Not found' }) do?",
            "options": ["Sends a JSON response with HTTP status 404", "Creates a new route automatically", "Changes the request method to POST", "Restarts Express"],
            "correct_answer": "Sends a JSON response with HTTP status 404",
            "explanation": "res.status() sets the status code, and res.json() sends the JSON body."
        },
        {
            "id": "express_013",
            "skill": "Express.js",
            "topic": "Routing",
            "question": "What is the purpose of express.Router()?",
            "options": ["Organizing related routes into a modular router", "Connecting automatically to every database", "Parsing CSS files", "Replacing all middleware"],
            "correct_answer": "Organizing related routes into a modular router",
            "explanation": "Routers help separate route definitions into manageable modules."
        },
        {
            "id": "express_014",
            "skill": "Express.js",
            "topic": "Routing",
            "question": "What does app.use('/api', router) commonly do?",
            "options": ["Mounts the router under the /api path prefix", "Creates a database named api", "Changes every request to POST", "Serves only CSS files"],
            "correct_answer": "Mounts the router under the /api path prefix",
            "explanation": "Routes defined in the router are reached under the mounted path prefix."
        },
        {
            "id": "express_015",
            "skill": "Express.js",
            "topic": "Middleware",
            "question": "Why does middleware registration order matter?",
            "options": ["Middleware generally executes in registration order when reached", "Express always sorts middleware alphabetically", "Only the last middleware can run", "Order affects CSS but not requests"],
            "correct_answer": "Middleware generally executes in registration order when reached",
            "explanation": "Earlier middleware can parse data or handle a request before later handlers run."
        },
        {
            "id": "express_016",
            "skill": "Express.js",
            "topic": "Error Handling",
            "question": "How is Express error-handling middleware commonly identified?",
            "options": ["It has four parameters: err, req, res, next", "It has only req and res", "It must be named error.js", "It uses only a CSS selector"],
            "correct_answer": "It has four parameters: err, req, res, next",
            "explanation": "The four-argument signature identifies error-handling middleware."
        },
        {
            "id": "express_017",
            "skill": "Express.js",
            "topic": "Error Handling",
            "question": "How can a synchronous route handler pass an error to Express?",
            "options": ["Throw an error or pass it to next(err)", "Call res.json() twice", "Change req.method manually", "Return a CSS class"],
            "correct_answer": "Throw an error or pass it to next(err)",
            "explanation": "Express can route synchronous errors to error-handling middleware; asynchronous handling depends on the handler and Express version."
        },
        {
            "id": "express_018",
            "skill": "Express.js",
            "topic": "Error Handling",
            "question": "What should an API error handler generally avoid?",
            "options": ["Exposing stack traces and internal secrets to clients", "Returning an appropriate error status", "Logging useful diagnostic details securely", "Providing a safe error message"],
            "correct_answer": "Exposing stack traces and internal secrets to clients",
            "explanation": "Detailed internal errors can expose implementation details and sensitive information."
        },
        {
            "id": "express_019",
            "skill": "Express.js",
            "topic": "Static Files",
            "question": "What does express.static() provide?",
            "options": ["Middleware for serving static files", "Automatic database backups", "User authentication by default", "Automatic API documentation"],
            "correct_answer": "Middleware for serving static files",
            "explanation": "It can serve files such as images, CSS, and client-side JavaScript."
        },
        {
            "id": "express_020",
            "skill": "Express.js",
            "topic": "HTTP",
            "question": "Which HTTP status code usually indicates successful resource creation?",
            "options": ["201", "404", "500", "301"],
            "correct_answer": "201",
            "explanation": "HTTP 201 Created indicates that a resource was created successfully."
        },
        {
            "id": "express_021",
            "skill": "Express.js",
            "topic": "HTTP",
            "question": "Which status code commonly indicates invalid request data?",
            "options": ["400", "200", "301", "204"],
            "correct_answer": "400",
            "explanation": "HTTP 400 Bad Request is commonly used when a request cannot be processed because of client-side input problems."
        },
        {
            "id": "express_022",
            "skill": "Express.js",
            "topic": "REST APIs",
            "question": "In a REST-style API, what does DELETE /users/12 usually represent?",
            "options": ["Requesting deletion of user 12", "Listing every user", "Creating user 12", "Updating the server's configuration"],
            "correct_answer": "Requesting deletion of user 12",
            "explanation": "DELETE is commonly used to request removal of the resource identified by the URL."
        },
        {
            "id": "express_023",
            "skill": "Express.js",
            "topic": "Security",
            "question": "Why should req.body be validated before use?",
            "options": ["Incoming data can be missing, malformed, or malicious", "Express guarantees every field is correct", "JSON parsing automatically authenticates users", "Validation is only needed for CSS"],
            "correct_answer": "Incoming data can be missing, malformed, or malicious",
            "explanation": "Request parsing does not guarantee that submitted data satisfies application rules."
        },
        {
            "id": "express_024",
            "skill": "Express.js",
            "topic": "Security",
            "question": "What is a common purpose of Helmet middleware?",
            "options": ["Setting various HTTP security headers", "Automatically fixing every application vulnerability", "Creating database tables", "Replacing route handlers"],
            "correct_answer": "Setting various HTTP security headers",
            "explanation": "Helmet helps configure security-related response headers but does not replace broader security practices."
        },
        {
            "id": "express_025",
            "skill": "Express.js",
            "topic": "Security",
            "question": "What is CORS primarily concerned with?",
            "options": ["Browser rules for cross-origin requests", "Encrypting database backups", "Compiling TypeScript", "Defining file-system paths"],
            "correct_answer": "Browser rules for cross-origin requests",
            "explanation": "Cross-Origin Resource Sharing controls how browsers permit web pages to access resources from other origins."
        },
        {
            "id": "express_026",
            "skill": "Express.js",
            "topic": "Security",
            "question": "Does enabling CORS authenticate users?",
            "options": ["No, CORS is not an authentication mechanism", "Yes, it verifies every password", "Yes, it grants administrator access", "No, because Express cannot send headers"],
            "correct_answer": "No, CORS is not an authentication mechanism",
            "explanation": "CORS controls browser cross-origin access; authentication and authorization must be implemented separately."
        },
        {
            "id": "express_027",
            "skill": "Express.js",
            "topic": "Security",
            "question": "Why might an API use rate limiting?",
            "options": ["To limit repeated requests and reduce abuse", "To make all requests anonymous", "To replace input validation", "To disable all HTTP methods"],
            "correct_answer": "To limit repeated requests and reduce abuse",
            "explanation": "Rate limits can help mitigate excessive requests and some denial-of-service or brute-force attempts."
        },
        {
            "id": "express_028",
            "skill": "Express.js",
            "topic": "Authentication",
            "question": "What is the difference between authentication and authorization?",
            "options": ["Authentication verifies identity; authorization checks permitted actions", "They are exactly the same", "Authentication checks CSS; authorization checks HTML", "Authorization always creates a new account"],
            "correct_answer": "Authentication verifies identity; authorization checks permitted actions",
            "explanation": "Applications need both identity verification and access-control checks."
        },
        {
            "id": "express_029",
            "skill": "Express.js",
            "topic": "Cookies",
            "question": "What is a common use of cookies in a web application?",
            "options": ["Storing small pieces of client-associated data such as a session identifier", "Storing unlimited server files", "Replacing all database tables", "Executing SQL automatically"],
            "correct_answer": "Storing small pieces of client-associated data such as a session identifier",
            "explanation": "Cookies can carry session identifiers or preferences; sensitive session cookies need appropriate security settings."
        },
        {
            "id": "express_030",
            "skill": "Express.js",
            "topic": "Sessions",
            "question": "What does session middleware commonly help manage?",
            "options": ["User session state across multiple HTTP requests", "The server's CSS animations", "Only file uploads", "The JavaScript compiler"],
            "correct_answer": "User session state across multiple HTTP requests",
            "explanation": "Sessions associate requests with stored session data, commonly through a session identifier."
        },
        {
            "id": "express_031",
            "skill": "Express.js",
            "topic": "File Uploads",
            "question": "What should an Express API check when accepting uploaded files?",
            "options": ["File type, size, authorization, and safe storage handling", "Only the original filename", "Nothing if the browser has a file picker", "Only the file's icon"],
            "correct_answer": "File type, size, authorization, and safe storage handling",
            "explanation": "Uploads should be validated and stored safely to reduce security and resource risks."
        },
        {
            "id": "express_032",
            "skill": "Express.js",
            "topic": "Configuration",
            "question": "Why are environment variables commonly used for deployment configuration?",
            "options": ["They allow configuration to vary by environment without hard-coding values", "They make all variables public automatically", "They replace HTTP requests", "They store all source code"],
            "correct_answer": "They allow configuration to vary by environment without hard-coding values",
            "explanation": "Environment variables can hold configuration such as port numbers and private connection settings."
        },
        {
            "id": "express_033",
            "skill": "Express.js",
            "topic": "Server",
            "question": "What does app.listen() commonly do?",
            "options": ["Starts the application listening for incoming connections on a port", "Defines a database model", "Parses request JSON automatically", "Creates a route without a path"],
            "correct_answer": "Starts the application listening for incoming connections on a port",
            "explanation": "app.listen() starts an HTTP server for the Express application."
        },
        {
            "id": "express_034",
            "skill": "Express.js",
            "topic": "Request Lifecycle",
            "question": "What happens if a route sends a response and then attempts to send another response?",
            "options": ["It can cause a headers-already-sent error", "Express combines both responses automatically", "The first response is always replaced", "The request changes into a WebSocket"],
            "correct_answer": "It can cause a headers-already-sent error",
            "explanation": "A response should normally be completed only once for a request."
        },
        {
            "id": "express_035",
            "skill": "Express.js",
            "topic": "API Design",
            "question": "Why is consistent API response formatting useful?",
            "options": ["Clients can handle results and errors more predictably", "It removes the need for HTTP status codes", "It automatically authenticates requests", "It prevents every network failure"],
            "correct_answer": "Clients can handle results and errors more predictably",
            "explanation": "Consistent response structures simplify frontend integration and error handling."
        },
        {
            "id": "express_036",
            "skill": "Express.js",
            "topic": "Testing",
            "question": "What can an HTTP testing tool such as Supertest help test?",
            "options": ["Express routes and their HTTP responses", "Only CSS animations", "The physical network cable", "Only database storage capacity"],
            "correct_answer": "Express routes and their HTTP responses",
            "explanation": "HTTP tests can check status codes, headers, and response bodies."
        },
        {
            "id": "express_037",
            "skill": "Express.js",
            "topic": "Architecture",
            "question": "What is a benefit of separating routes, controllers, and services?",
            "options": ["It separates request handling from application logic", "It guarantees zero bugs", "It makes validation unnecessary", "It forces all code into one file"],
            "correct_answer": "It separates request handling from application logic",
            "explanation": "Separation of concerns improves readability, testing, and maintenance."
        },
        {
            "id": "express_038",
            "skill": "Express.js",
            "topic": "Asynchronous Errors",
            "question": "What is a safe general practice for asynchronous route handlers?",
            "options": ["Ensure rejected operations reach appropriate error handling", "Ignore every rejected Promise", "Send success before checking the result", "Disable all middleware"],
            "correct_answer": "Ensure rejected operations reach appropriate error handling",
            "explanation": "Async error propagation depends on the Express version and handler pattern; errors must be handled or forwarded correctly."
        },
        {
            "id": "express_039",
            "skill": "Express.js",
            "topic": "Deployment",
            "question": "Why should an Express production server avoid exposing detailed internal error messages?",
            "options": ["They can reveal sensitive implementation details", "They increase the number of routes", "They prevent JSON parsing", "They automatically change the port"],
            "correct_answer": "They can reveal sensitive implementation details",
            "explanation": "Clients should receive safe error messages while detailed diagnostics are logged securely."
        },
        {
            "id": "express_040",
            "skill": "Express.js",
            "topic": "Best Practices",
            "question": "Which practice is best for a maintainable Express API?",
            "options": ["Validate inputs, use clear route structure, and centralize error handling", "Put every route in one giant callback", "Trust all incoming requests", "Ignore status codes"],
            "correct_answer": "Validate inputs, use clear route structure, and centralize error handling",
            "explanation": "These practices improve reliability, readability, and security."
        }
    ],
    "flask": [
        {
            "id": "flask_001",
            "skill": "Flask",
            "topic": "Fundamentals",
            "question": "What is Flask?",
            "options": ["A lightweight Python web framework", "A JavaScript runtime", "A relational database", "A CSS framework"],
            "correct_answer": "A lightweight Python web framework",
            "explanation": "Flask provides a flexible foundation for Python web applications and APIs."
        },
        {
            "id": "flask_002",
            "skill": "Flask",
            "topic": "Routing",
            "question": "Which decorator commonly defines a Flask route?",
            "options": ["@app.route()", "@app.database()", "@app.html()", "@app.style()"],
            "correct_answer": "@app.route()",
            "explanation": "The route decorator associates a URL rule with a view function."
        },
        {
            "id": "flask_003",
            "skill": "Flask",
            "topic": "Routing",
            "question": "What HTTP method does a basic Flask route allow by default?",
            "options": ["GET", "POST only", "DELETE only", "PATCH only"],
            "correct_answer": "GET",
            "explanation": "A basic route allows GET by default and typically also supports HEAD and OPTIONS as applicable."
        },
        {
            "id": "flask_004",
            "skill": "Flask",
            "topic": "Routing",
            "question": "How can a Flask route explicitly allow POST requests?",
            "options": ["Set methods=['POST'] in the route decorator", "Set css='POST'", "Use app.database('POST')", "Add POST only to the HTML title"],
            "correct_answer": "Set methods=['POST'] in the route decorator",
            "explanation": "The methods argument specifies which HTTP methods a route accepts."
        },
        {
            "id": "flask_005",
            "skill": "Flask",
            "topic": "Responses",
            "question": "What does Flask's jsonify() commonly do?",
            "options": ["Creates a JSON response from supported Python data", "Creates a database table", "Compiles Python into CSS", "Starts a background operating system"],
            "correct_answer": "Creates a JSON response from supported Python data",
            "explanation": "jsonify() serializes supported data into a Flask JSON response."
        },
        {
            "id": "flask_006",
            "skill": "Flask",
            "topic": "Request Data",
            "question": "Where can Flask access submitted JSON request data?",
            "options": ["request.get_json()", "response.json_input()", "app.json_body_only()", "flask.read_css()"],
            "correct_answer": "request.get_json()",
            "explanation": "request.get_json() parses JSON request data when the request is configured appropriately."
        },
        {
            "id": "flask_007",
            "skill": "Flask",
            "topic": "Request Data",
            "question": "Where are URL query parameters available in Flask?",
            "options": ["request.args", "request.path_only", "response.args", "app.query_data"],
            "correct_answer": "request.args",
            "explanation": "For a URL such as /search?q=python, the q value is available through request.args."
        },
        {
            "id": "flask_008",
            "skill": "Flask",
            "topic": "Request Data",
            "question": "Where can Flask access submitted HTML form fields?",
            "options": ["request.form", "request.styles", "response.form", "app.html_data"],
            "correct_answer": "request.form",
            "explanation": "request.form contains parsed form data submitted using supported form encodings."
        },
        {
            "id": "flask_009",
            "skill": "Flask",
            "topic": "Templates",
            "question": "Which function renders a Jinja template in Flask?",
            "options": ["render_template()", "render_database()", "compile_css()", "start_template_server()"],
            "correct_answer": "render_template()",
            "explanation": "render_template() loads and renders a template, usually from the templates directory."
        },
        {
            "id": "flask_010",
            "skill": "Flask",
            "topic": "Templates",
            "question": "Which template engine is commonly used by Flask?",
            "options": ["Jinja", "React", "Bootstrap", "PostgreSQL"],
            "correct_answer": "Jinja",
            "explanation": "Flask uses Jinja for template rendering by default."
        },
        {
            "id": "flask_011",
            "skill": "Flask",
            "topic": "Static Files",
            "question": "Where are static files commonly stored in a Flask project?",
            "options": ["The static directory", "The migrations directory only", "The database table directory", "The Python interpreter folder"],
            "correct_answer": "The static directory",
            "explanation": "The static directory commonly stores assets such as CSS, JavaScript, and images."
        },
        {
            "id": "flask_012",
            "skill": "Flask",
            "topic": "URL Building",
            "question": "What is url_for() commonly used for?",
            "options": ["Generating a URL for an endpoint", "Creating a database backup", "Parsing Python indentation", "Starting the development server"],
            "correct_answer": "Generating a URL for an endpoint",
            "explanation": "url_for() builds URLs using endpoint names and optional parameters."
        },
        {
            "id": "flask_013",
            "skill": "Flask",
            "topic": "Configuration",
            "question": "What is app.config used for?",
            "options": ["Storing application configuration settings", "Defining HTML elements", "Replacing Python imports", "Saving every HTTP response permanently"],
            "correct_answer": "Storing application configuration settings",
            "explanation": "Flask's configuration object stores settings such as debug options and secret keys."
        },
        {
            "id": "flask_014",
            "skill": "Flask",
            "topic": "Security",
            "question": "What is SECRET_KEY commonly used for in Flask?",
            "options": ["Signing session data and other security-related values", "Naming every URL route", "Replacing the database password automatically", "Serving static images"],
            "correct_answer": "Signing session data and other security-related values",
            "explanation": "The secret key protects signed data such as Flask's default session cookie; it should remain secret."
        },
        {
            "id": "flask_015",
            "skill": "Flask",
            "topic": "Sessions",
            "question": "Where does Flask's default session implementation store session data?",
            "options": ["In a signed cookie held by the client", "Only in a mandatory SQL table", "Inside the HTML stylesheet", "In a public image file"],
            "correct_answer": "In a signed cookie held by the client",
            "explanation": "The default session cookie is signed to detect tampering but is not encrypted by default."
        },
        {
            "id": "flask_016",
            "skill": "Flask",
            "topic": "Blueprints",
            "question": "What is a Flask Blueprint used for?",
            "options": ["Organizing related routes and application components into reusable groups", "Drawing UI wireframes", "Replacing the Python runtime", "Automatically encrypting all database records"],
            "correct_answer": "Organizing related routes and application components into reusable groups",
            "explanation": "Blueprints help structure larger Flask applications into modules."
        },
        {
            "id": "flask_017",
            "skill": "Flask",
            "topic": "Application Factory",
            "question": "What is the purpose of an application factory function?",
            "options": ["Creating and configuring a Flask application instance", "Creating HTML files automatically for every route", "Replacing the request object", "Starting a database without configuration"],
            "correct_answer": "Creating and configuring a Flask application instance",
            "explanation": "A factory function makes it easier to configure separate application instances for testing or different environments."
        },
        {
            "id": "flask_018",
            "skill": "Flask",
            "topic": "Error Handling",
            "question": "How can a Flask application define a handler for HTTP 404 errors?",
            "options": ["Use an error handler for status code 404", "Create a CSS class named 404", "Use request.form(404)", "Call app.database(404)"],
            "correct_answer": "Use an error handler for status code 404",
            "explanation": "Flask supports custom error handlers for HTTP status codes and exception types."
        },
        {
            "id": "flask_019",
            "skill": "Flask",
            "topic": "Responses",
            "question": "Which HTTP status code indicates that a request was successful?",
            "options": ["200", "404", "500", "401"],
            "correct_answer": "200",
            "explanation": "HTTP 200 OK indicates that a request succeeded."
        },
        {
            "id": "flask_020",
            "skill": "Flask",
            "topic": "Responses",
            "question": "Which status code is commonly used when a resource does not exist?",
            "options": ["404", "201", "204", "302"],
            "correct_answer": "404",
            "explanation": "HTTP 404 Not Found indicates that the requested resource could not be found."
        },
        {
            "id": "flask_021",
            "skill": "Flask",
            "topic": "REST APIs",
            "question": "What is a common way to return both JSON data and a status code from a Flask view?",
            "options": ["Return a JSON response together with the desired status code", "Return a CSS selector", "Use render_template() for every API response", "Change the request method after processing"],
            "correct_answer": "Return a JSON response together with the desired status code",
            "explanation": "A Flask view can return a response object or a supported response-and-status combination."
        },
        {
            "id": "flask_022",
            "skill": "Flask",
            "topic": "Security",
            "question": "Why should a Flask API validate incoming data?",
            "options": ["To reject malformed or disallowed values before processing them", "Because JSON parsing guarantees business rules", "To automatically grant user permissions", "Because validation creates database indexes"],
            "correct_answer": "To reject malformed or disallowed values before processing them",
            "explanation": "Parsing data does not guarantee that the data is safe or satisfies application requirements."
        },
        {
            "id": "flask_023",
            "skill": "Flask",
            "topic": "Security",
            "question": "Why should debug mode be disabled in production?",
            "options": ["Debug tools can expose sensitive information and create serious security risks", "It prevents Flask from serving HTML", "It disables all routes", "It makes JSON impossible"],
            "correct_answer": "Debug tools can expose sensitive information and create serious security risks",
            "explanation": "The interactive debugger is intended for development, not public production servers."
        },
        {
            "id": "flask_024",
            "skill": "Flask",
            "topic": "Deployment",
            "question": "Should Flask's built-in development server normally be used as the production server?",
            "options": ["No, use a suitable production WSGI server or deployment platform", "Yes, for every high-traffic application", "Only if debug mode is enabled", "No, because Flask cannot be deployed"],
            "correct_answer": "No, use a suitable production WSGI server or deployment platform",
            "explanation": "The development server is not designed to provide production deployment requirements."
        },
        {
            "id": "flask_025",
            "skill": "Flask",
            "topic": "Testing",
            "question": "What does Flask's test client help developers do?",
            "options": ["Test application routes without running a live external server", "Compile Python into JavaScript", "Create production credentials", "Install operating system updates"],
            "correct_answer": "Test application routes without running a live external server",
            "explanation": "The test client makes requests to the Flask application within tests."
        },
        {
            "id": "flask_026",
            "skill": "Flask",
            "topic": "Application Context",
            "question": "What does current_app refer to?",
            "options": ["The active Flask application in the current application context", "The user's browser tab", "The latest database row", "The current CSS file"],
            "correct_answer": "The active Flask application in the current application context",
            "explanation": "current_app provides access to the active Flask application without importing a specific global instance."
        },
        {
            "id": "flask_027",
            "skill": "Flask",
            "topic": "Request Context",
            "question": "What does the Flask request object represent?",
            "options": ["The current incoming HTTP request", "The application's database schema", "The response from every previous request", "The Python package installer"],
            "correct_answer": "The current incoming HTTP request",
            "explanation": "The request proxy provides access to data for the request being handled."
        },
        {
            "id": "flask_028",
            "skill": "Flask",
            "topic": "Request Lifecycle",
            "question": "Why should request-specific data not be stored in an ordinary global variable in a multi-user Flask app?",
            "options": ["Concurrent requests may interfere with shared mutable data", "Global variables are always encrypted", "Flask permits only one user", "Python does not support variables"],
            "correct_answer": "Concurrent requests may interfere with shared mutable data",
            "explanation": "Request-specific values should use appropriate context-local mechanisms rather than shared mutable globals."
        },
        {
            "id": "flask_029",
            "skill": "Flask",
            "topic": "Templates",
            "question": "How can a Python value be passed to a Jinja template?",
            "options": ["Pass it as a keyword argument to render_template()", "Place it only in a CSS file", "Use app.listen()", "Store it in request.method"],
            "correct_answer": "Pass it as a keyword argument to render_template()",
            "explanation": "Template context values can be supplied as keyword arguments."
        },
        {
            "id": "flask_030",
            "skill": "Flask",
            "topic": "Templates",
            "question": "What is a benefit of Jinja's default autoescaping for HTML templates?",
            "options": ["It helps prevent injected text from being interpreted as HTML markup", "It encrypts every template variable", "It validates database permissions", "It prevents every possible security vulnerability"],
            "correct_answer": "It helps prevent injected text from being interpreted as HTML markup",
            "explanation": "Autoescaping reduces some HTML injection risks, but does not eliminate every security issue."
        },
        {
            "id": "flask_031",
            "skill": "Flask",
            "topic": "URL Building",
            "question": "How can a Flask route generate a URL for another endpoint?",
            "options": ["Use url_for() with the endpoint name", "Use request.body()", "Use jsonify.route()", "Use app.static_url_only()"],
            "correct_answer": "Use url_for() with the endpoint name",
            "explanation": "url_for() creates URLs based on registered endpoint names and supplied parameters."
        },
        {
            "id": "flask_032",
            "skill": "Flask",
            "topic": "Database Integration",
            "question": "What is a good practice when executing SQL from a Flask application?",
            "options": ["Use parameterized queries instead of concatenating untrusted input", "Insert user input directly into SQL strings", "Expose database credentials in templates", "Disable database error handling"],
            "correct_answer": "Use parameterized queries instead of concatenating untrusted input",
            "explanation": "Parameterized queries help protect against SQL injection."
        },
        {
            "id": "flask_033",
            "skill": "Flask",
            "topic": "Authentication",
            "question": "What should a protected Flask endpoint do before returning private information?",
            "options": ["Verify authentication and check authorization", "Trust that the frontend hides the button", "Skip input validation", "Return the secret key in JSON"],
            "correct_answer": "Verify authentication and check authorization",
            "explanation": "Access controls must be enforced on the server for every protected operation."
        },
        {
            "id": "flask_034",
            "skill": "Flask",
            "topic": "Cross-Origin Requests",
            "question": "When might a Flask API need CORS configuration?",
            "options": ["When a browser frontend on another origin needs permitted access to the API", "Whenever Python imports a module", "Only when using HTML templates", "When creating a local variable"],
            "correct_answer": "When a browser frontend on another origin needs permitted access to the API",
            "explanation": "CORS controls browser cross-origin access; it does not replace authentication or authorization."
        },
        {
            "id": "flask_035",
            "skill": "Flask",
            "topic": "File Uploads",
            "question": "What should a Flask application do with uploaded files?",
            "options": ["Validate allowed types and sizes and store files safely", "Trust every filename and file type", "Execute uploaded files automatically", "Save every upload using an unrestricted original path"],
            "correct_answer": "Validate allowed types and sizes and store files safely",
            "explanation": "Safe upload handling reduces malicious file, path traversal, and resource-exhaustion risks."
        },
        {
            "id": "flask_036",
            "skill": "Flask",
            "topic": "Configuration",
            "question": "Why use separate configuration for development and production?",
            "options": ["The environments need different settings and security controls", "Python requires different syntax in production", "Routes cannot run in development", "It removes the need for testing"],
            "correct_answer": "The environments need different settings and security controls",
            "explanation": "Separate configurations help manage debug settings, credentials, and service endpoints safely."
        },
        {
            "id": "flask_037",
            "skill": "Flask",
            "topic": "Logging",
            "question": "What is application logging useful for?",
            "options": ["Recording events and diagnosing problems", "Replacing input validation", "Automatically fixing every error", "Storing passwords in plain text"],
            "correct_answer": "Recording events and diagnosing problems",
            "explanation": "Useful logs help developers investigate failures while sensitive data should be excluded."
        },
        {
            "id": "flask_038",
            "skill": "Flask",
            "topic": "Asynchronous Views",
            "question": "Does declaring a Flask view async automatically make every operation non-blocking?",
            "options": ["No, blocking operations can still block execution", "Yes, all Python operations become parallel", "Yes, the database becomes asynchronous automatically", "No, Flask cannot define routes"],
            "correct_answer": "No, blocking operations can still block execution",
            "explanation": "Async views can await compatible operations, but synchronous blocking work remains blocking."
        },
        {
            "id": "flask_039",
            "skill": "Flask",
            "topic": "API Design",
            "question": "Why should a Flask API return meaningful HTTP status codes?",
            "options": ["Clients can distinguish success, client errors, and server errors", "It automatically encrypts the response", "It eliminates network latency", "It replaces response bodies in every case"],
            "correct_answer": "Clients can distinguish success, client errors, and server errors",
            "explanation": "Appropriate status codes make API behavior clearer and easier to handle."
        },
        {
            "id": "flask_040",
            "skill": "Flask",
            "topic": "Best Practices",
            "question": "Which practice improves the maintainability of a larger Flask application?",
            "options": ["Use application factories, blueprints, validation, and tests where appropriate", "Put every feature in one giant route", "Ignore errors and invalid requests", "Store every secret in public source code"],
            "correct_answer": "Use application factories, blueprints, validation, and tests where appropriate",
            "explanation": "These practices support modular design, safer request handling, and reliable testing."
        }
    ],
    
    "django": [
        {
            "id": "django_001",
            "skill": "Django",
            "topic": "Fundamentals",
            "question": "What is Django?",
            "options": ["A Python web framework", "A JavaScript runtime", "A database language", "A CSS framework"],
            "correct_answer": "A Python web framework",
            "explanation": "Django provides tools for building Python web applications."
        },
        {
            "id": "django_002",
            "skill": "Django",
            "topic": "Architecture",
            "question": "What architectural pattern does Django commonly use?",
            "options": ["Model-Template-View (MTV)", "Model-View-Controller only", "Peer-to-peer architecture", "Microkernel architecture"],
            "correct_answer": "Model-Template-View (MTV)",
            "explanation": "Django's architecture is commonly described as Model-Template-View."
        },
        {
            "id": "django_003",
            "skill": "Django",
            "topic": "Models",
            "question": "What does a Django model usually represent?",
            "options": ["A data structure mapped to database storage", "A CSS layout", "A browser event", "An image file"],
            "correct_answer": "A data structure mapped to database storage",
            "explanation": "Models define application data and commonly map to database tables."
        },
        {
            "id": "django_004",
            "skill": "Django",
            "topic": "ORM",
            "question": "What is Django ORM used for?",
            "options": ["Working with database records through Python objects", "Styling HTML elements", "Compiling JavaScript", "Managing browser tabs"],
            "correct_answer": "Working with database records through Python objects",
            "explanation": "The Object-Relational Mapper lets developers query and update data using Python."
        },
        {
            "id": "django_005",
            "skill": "Django",
            "topic": "Migrations",
            "question": "What does python manage.py makemigrations do?",
            "options": ["Creates migration files from model changes", "Applies all migrations to the database", "Starts the production server", "Creates HTML templates"],
            "correct_answer": "Creates migration files from model changes",
            "explanation": "makemigrations generates migration instructions based on detected model changes."
        },
        {
            "id": "django_006",
            "skill": "Django",
            "topic": "Migrations",
            "question": "What does python manage.py migrate do?",
            "options": ["Applies database migrations", "Creates a new Python interpreter", "Collects browser cookies", "Generates CSS styles"],
            "correct_answer": "Applies database migrations",
            "explanation": "migrate applies pending migration operations to the configured database."
        },
        {
            "id": "django_007",
            "skill": "Django",
            "topic": "Views",
            "question": "What is a Django view responsible for?",
            "options": ["Processing a request and returning a response", "Only defining database columns", "Installing Python packages", "Compiling CSS"],
            "correct_answer": "Processing a request and returning a response",
            "explanation": "A view contains request-handling logic and returns an HTTP response."
        },
        {
            "id": "django_008",
            "skill": "Django",
            "topic": "URL Routing",
            "question": "Which function is commonly used to define a URL pattern in Django?",
            "options": ["path()", "route_css()", "url_table()", "request_path_only()"],
            "correct_answer": "path()",
            "explanation": "django.urls.path() maps URL patterns to views."
        },
        {
            "id": "django_009",
            "skill": "Django",
            "topic": "Templates",
            "question": "What is the purpose of a Django template?",
            "options": ["Generating dynamic output such as HTML", "Creating database indexes only", "Running operating system commands", "Defining network cables"],
            "correct_answer": "Generating dynamic output such as HTML",
            "explanation": "Templates combine presentation markup with context data."
        },
        {
            "id": "django_010",
            "skill": "Django",
            "topic": "Templates",
            "question": "Which syntax displays a variable in a Django template?",
            "options": ["{{ username }}", "[[ username ]]", "<% username %>", "(( username ))"],
            "correct_answer": "{{ username }}",
            "explanation": "Double curly braces display a variable's value in a Django template."
        },
        {
            "id": "django_011",
            "skill": "Django",
            "topic": "Admin",
            "question": "What is Django Admin mainly used for?",
            "options": ["Managing application data through an administrative interface", "Replacing all application views", "Compiling Python files", "Creating network protocols"],
            "correct_answer": "Managing application data through an administrative interface",
            "explanation": "The admin site provides a configurable interface for managing registered models."
        },
        {
            "id": "django_012",
            "skill": "Django",
            "topic": "Admin",
            "question": "What is commonly required before a model appears in Django Admin?",
            "options": ["Register the model with the admin site", "Rename it to index.html", "Add it to a CSS file", "Convert it into a JavaScript class"],
            "correct_answer": "Register the model with the admin site",
            "explanation": "Registering a model makes it available for management through the admin interface."
        },
        {
            "id": "django_013",
            "skill": "Django",
            "topic": "Authentication",
            "question": "What does Django's authentication system help manage?",
            "options": ["Users, passwords, and authentication checks", "CSS animations only", "Database server hardware", "Image compression exclusively"],
            "correct_answer": "Users, passwords, and authentication checks",
            "explanation": "Django includes built-in tools for user authentication and related functionality."
        },
        {
            "id": "django_014",
            "skill": "Django",
            "topic": "Authorization",
            "question": "What is Django's permission system used for?",
            "options": ["Controlling which actions users may perform", "Automatically styling templates", "Generating unique URLs only", "Compiling Python into HTML"],
            "correct_answer": "Controlling which actions users may perform",
            "explanation": "Permissions help restrict access to operations and resources."
        },
        {
            "id": "django_015",
            "skill": "Django",
            "topic": "Security",
            "question": "What does Django's CSRF protection help prevent?",
            "options": ["Forged requests made using a user's authenticated browser session", "All SQL errors", "Every server outage", "All incorrect Python types"],
            "correct_answer": "Forged requests made using a user's authenticated browser session",
            "explanation": "CSRF protection helps prevent unauthorized state-changing requests initiated from another site."
        },
        {
            "id": "django_016",
            "skill": "Django",
            "topic": "Security",
            "question": "Why should DEBUG normally be False in production?",
            "options": ["Debug pages can expose sensitive technical information", "Django cannot use databases with DEBUG disabled", "It prevents all routes from loading", "It disables authentication"],
            "correct_answer": "Debug pages can expose sensitive technical information",
            "explanation": "Production error pages should not expose detailed internal diagnostics."
        },
        {
            "id": "django_017",
            "skill": "Django",
            "topic": "Configuration",
            "question": "Where are many Django project settings defined?",
            "options": ["settings.py", "styles.css", "index.html", "package-lock.json"],
            "correct_answer": "settings.py",
            "explanation": "The settings module configures installed apps, middleware, databases, and other project behavior."
        },
        {
            "id": "django_018",
            "skill": "Django",
            "topic": "Middleware",
            "question": "What does Django middleware do?",
            "options": ["Processes requests and responses at defined stages", "Defines only database table names", "Replaces all URL patterns", "Creates CSS classes automatically"],
            "correct_answer": "Processes requests and responses at defined stages",
            "explanation": "Middleware can inspect or modify requests and responses across the request lifecycle."
        },
        {
            "id": "django_019",
            "skill": "Django",
            "topic": "Forms",
            "question": "What is a benefit of Django Forms?",
            "options": ["They help validate input and process form data", "They replace the database engine", "They automatically deploy applications", "They disable all HTML output"],
            "correct_answer": "They help validate input and process form data",
            "explanation": "Django Forms provide structured validation and form-processing tools."
        },
        {
            "id": "django_020",
            "skill": "Django",
            "topic": "Model Forms",
            "question": "What is a ModelForm designed to do?",
            "options": ["Build a form based on a Django model", "Create a model from a CSS selector", "Replace the URL configuration", "Start a web server automatically"],
            "correct_answer": "Build a form based on a Django model",
            "explanation": "ModelForm can generate form fields and validation based on model definitions."
        },
        {
            "id": "django_021",
            "skill": "Django",
            "topic": "QuerySets",
            "question": "What does Model.objects.filter() commonly return?",
            "options": ["A QuerySet containing matching records", "A CSS stylesheet", "A Python package", "An HTTP server"],
            "correct_answer": "A QuerySet containing matching records",
            "explanation": "filter() constructs a QuerySet representing objects that meet the conditions."
        },
        {
            "id": "django_022",
            "skill": "Django",
            "topic": "QuerySets",
            "question": "What does QuerySet.get() do when exactly one record matches?",
            "options": ["Returns the matching object", "Always returns a list", "Deletes the matching object", "Creates a new table"],
            "correct_answer": "Returns the matching object",
            "explanation": "get() returns one object and raises exceptions when no object or multiple objects match."
        },
        {
            "id": "django_023",
            "skill": "Django",
            "topic": "Relationships",
            "question": "Which model field represents a many-to-one relationship?",
            "options": ["ForeignKey", "CharField", "BooleanField", "TextField"],
            "correct_answer": "ForeignKey",
            "explanation": "ForeignKey commonly represents many records related to one record in another model."
        },
        {
            "id": "django_024",
            "skill": "Django",
            "topic": "Relationships",
            "question": "Which field represents a many-to-many relationship?",
            "options": ["ManyToManyField", "OneToOneOnly", "IntegerField", "FilePathField"],
            "correct_answer": "ManyToManyField",
            "explanation": "ManyToManyField models relationships where multiple records can be associated with multiple other records."
        },
        {
            "id": "django_025",
            "skill": "Django",
            "topic": "Query Optimization",
            "question": "What is select_related() commonly used for?",
            "options": ["Fetching related single-valued objects through SQL joins", "Creating HTML templates", "Deleting duplicate routes", "Enabling debug mode"],
            "correct_answer": "Fetching related single-valued objects through SQL joins",
            "explanation": "select_related() can reduce extra database queries for foreign-key and one-to-one relationships."
        },
        {
            "id": "django_026",
            "skill": "Django",
            "topic": "Query Optimization",
            "question": "What is prefetch_related() commonly used for?",
            "options": ["Fetching related collections using additional queries and joining results in Python", "Compiling templates into SQL", "Creating new user accounts", "Changing HTTP methods"],
            "correct_answer": "Fetching related collections using additional queries and joining results in Python",
            "explanation": "It can reduce repeated queries for many-to-many and reverse relationships."
        },
        {
            "id": "django_027",
            "skill": "Django",
            "topic": "Static Files",
            "question": "What is collectstatic used for?",
            "options": ["Collecting static files into the configured destination", "Deleting all model records", "Generating database migrations", "Creating a new Django app"],
            "correct_answer": "Collecting static files into the configured destination",
            "explanation": "The command gathers static assets for deployment according to the project's settings."
        },
        {
            "id": "django_028",
            "skill": "Django",
            "topic": "Application Structure",
            "question": "What does INSTALLED_APPS specify?",
            "options": ["Applications and components enabled in the Django project", "Only permitted URL query parameters", "The user's browser extensions", "Only database passwords"],
            "correct_answer": "Applications and components enabled in the Django project",
            "explanation": "Django uses INSTALLED_APPS to load project apps and installed packages."
        },
        {
            "id": "django_029",
            "skill": "Django",
            "topic": "Application Structure",
            "question": "What is the purpose of manage.py?",
            "options": ["Running Django management commands for a project", "Serving only static images", "Replacing the Python interpreter", "Storing database rows"],
            "correct_answer": "Running Django management commands for a project",
            "explanation": "manage.py provides a project-specific entry point for commands such as runserver and migrate."
        },
        {
            "id": "django_030",
            "skill": "Django",
            "topic": "Testing",
            "question": "What does Django's test framework help verify?",
            "options": ["Application behavior, views, and data handling", "That an application can never contain bugs", "Only the developer's screen resolution", "Only CSS colors"],
            "correct_answer": "Application behavior, views, and data handling",
            "explanation": "Automated tests help detect errors and prevent regressions."
        },
        {
            "id": "django_031",
            "skill": "Django",
            "topic": "Testing",
            "question": "What can Django's test client simulate?",
            "options": ["Requests to application URLs without a live external server", "Physical network cable failures", "Browser hardware upgrades", "Database server installation"],
            "correct_answer": "Requests to application URLs without a live external server",
            "explanation": "The test client allows views and responses to be tested within automated tests."
        },
        {
            "id": "django_032",
            "skill": "Django",
            "topic": "Signals",
            "question": "What are Django signals used for?",
            "options": ["Allowing components to be notified when certain events occur", "Sending electrical signals to hardware", "Replacing every model method", "Defining CSS animations"],
            "correct_answer": "Allowing components to be notified when certain events occur",
            "explanation": "Signals allow decoupled components to respond to events such as model saves."
        },
        {
            "id": "django_033",
            "skill": "Django",
            "topic": "Transactions",
            "question": "What is transaction.atomic() used for?",
            "options": ["Grouping database operations into a transaction", "Encrypting every model field", "Creating static files", "Starting the development server"],
            "correct_answer": "Grouping database operations into a transaction",
            "explanation": "Atomic blocks help ensure grouped database operations succeed or roll back together."
        },
        {
            "id": "django_034",
            "skill": "Django",
            "topic": "Caching",
            "question": "What is caching used for in Django?",
            "options": ["Reducing repeated work by reusing stored results", "Replacing all database records", "Disabling URL routing", "Automatically validating passwords"],
            "correct_answer": "Reducing repeated work by reusing stored results",
            "explanation": "Caching can improve performance for data or responses that do not need to be recomputed on every request."
        },
        {
            "id": "django_035",
            "skill": "Django",
            "topic": "Internationalization",
            "question": "What is Django's internationalization support designed to help with?",
            "options": ["Translating application text for different languages", "Encrypting database backups", "Creating network routes", "Compiling Python into machine code"],
            "correct_answer": "Translating application text for different languages",
            "explanation": "Internationalization and localization support multilingual applications."
        },
        {
            "id": "django_036",
            "skill": "Django",
            "topic": "File Uploads",
            "question": "What should a Django application do when handling uploaded files?",
            "options": ["Validate uploads and store them safely", "Trust every uploaded file automatically", "Execute uploaded files as Python", "Save every file to an unrestricted path"],
            "correct_answer": "Validate uploads and store them safely",
            "explanation": "Safe upload handling reduces malicious-file and resource-exhaustion risks."
        },
        {
            "id": "django_037",
            "skill": "Django",
            "topic": "Deployment",
            "question": "What is WSGI used for in a traditional Django deployment?",
            "options": ["Providing an interface between Python web applications and compatible web servers", "Styling HTML templates", "Creating SQL indexes", "Replacing application URLs"],
            "correct_answer": "Providing an interface between Python web applications and compatible web servers",
            "explanation": "WSGI is a standard interface used by many synchronous Python web deployments."
        },
        {
            "id": "django_038",
            "skill": "Django",
            "topic": "Deployment",
            "question": "Why should production secrets be kept outside public source code?",
            "options": ["To reduce the risk of exposing credentials", "To make database queries slower", "To prevent migrations from running", "To disable user authentication"],
            "correct_answer": "To reduce the risk of exposing credentials",
            "explanation": "Protected environment configuration or a secret manager helps keep credentials private."
        },
        {
            "id": "django_039",
            "skill": "Django",
            "topic": "REST Integration",
            "question": "Which package is commonly used to build REST APIs with Django?",
            "options": ["Django REST framework", "NumPy", "Matplotlib", "Pillow only"],
            "correct_answer": "Django REST framework",
            "explanation": "Django REST framework adds serializers, API views, authentication options, and other API tools."
        },
        {
            "id": "django_040",
            "skill": "Django",
            "topic": "Best Practices",
            "question": "Which practice improves maintainability in a larger Django project?",
            "options": ["Use modular apps, tests, validation, and clear separation of responsibilities", "Put every feature into one view", "Ignore invalid input", "Commit production secrets to source control"],
            "correct_answer": "Use modular apps, tests, validation, and clear separation of responsibilities",
            "explanation": "Modular design and testing make a project easier to maintain and safer to change."
        }
    ],
    "rest apis": [
        {
            "id": "rest_001",
            "skill": "REST APIs",
            "topic": "Fundamentals",
            "question": "What does REST stand for?",
            "options": ["Representational State Transfer", "Remote Execution Service Technology", "Request Encoding Standard Transfer", "Resource Execution Storage Table"],
            "correct_answer": "Representational State Transfer",
            "explanation": "REST is an architectural style for networked applications."
        },
        {
            "id": "rest_002",
            "skill": "REST APIs",
            "topic": "Resources",
            "question": "In a REST API, what does a resource commonly represent?",
            "options": ["An identifiable item such as a user or product", "Only a CSS file", "A programming language keyword", "A browser extension"],
            "correct_answer": "An identifiable item such as a user or product",
            "explanation": "Resources are commonly identified through URLs."
        },
        {
            "id": "rest_003",
            "skill": "REST APIs",
            "topic": "HTTP Methods",
            "question": "Which HTTP method is commonly used to retrieve a resource?",
            "options": ["GET", "DELETE", "PATCH", "CONNECT"],
            "correct_answer": "GET",
            "explanation": "GET requests representation data for a resource."
        },
        {
            "id": "rest_004",
            "skill": "REST APIs",
            "topic": "HTTP Methods",
            "question": "Which HTTP method is commonly used to create a resource?",
            "options": ["POST", "HEAD", "TRACE", "OPTIONS"],
            "correct_answer": "POST",
            "explanation": "POST commonly submits data that creates a resource or triggers processing."
        },
        {
            "id": "rest_005",
            "skill": "REST APIs",
            "topic": "HTTP Methods",
            "question": "What is PUT commonly used for?",
            "options": ["Replacing a resource representation or creating it at a known URI when supported", "Only retrieving a resource", "Only checking server headers", "Styling a web page"],
            "correct_answer": "Replacing a resource representation or creating it at a known URI when supported",
            "explanation": "PUT is generally defined as idempotent and often replaces the target resource."
        },
        {
            "id": "rest_006",
            "skill": "REST APIs",
            "topic": "HTTP Methods",
            "question": "What is PATCH commonly used for?",
            "options": ["Applying a partial modification to a resource", "Always deleting a resource", "Only retrieving a resource", "Restarting the API server"],
            "correct_answer": "Applying a partial modification to a resource",
            "explanation": "PATCH is intended for partial modifications rather than full replacement."
        },
        {
            "id": "rest_007",
            "skill": "REST APIs",
            "topic": "HTTP Methods",
            "question": "Which method is commonly used to remove a resource?",
            "options": ["DELETE", "GET", "HEAD", "OPTIONS"],
            "correct_answer": "DELETE",
            "explanation": "DELETE requests removal of the resource identified by the target URI."
        },
        {
            "id": "rest_008",
            "skill": "REST APIs",
            "topic": "Status Codes",
            "question": "What does HTTP 200 mean?",
            "options": ["The request succeeded", "The resource was not found", "Authentication is always required", "The server has failed"],
            "correct_answer": "The request succeeded",
            "explanation": "200 OK indicates a successful request."
        },
        {
            "id": "rest_009",
            "skill": "REST APIs",
            "topic": "Status Codes",
            "question": "Which status code usually indicates successful resource creation?",
            "options": ["201", "400", "404", "503"],
            "correct_answer": "201",
            "explanation": "201 Created indicates that the request created a resource."
        },
        {
            "id": "rest_010",
            "skill": "REST APIs",
            "topic": "Status Codes",
            "question": "What does HTTP 204 indicate?",
            "options": ["The request succeeded and there is no response content", "The request always failed", "The user is unauthenticated", "The resource was permanently moved"],
            "correct_answer": "The request succeeded and there is no response content",
            "explanation": "A 204 No Content response does not include a response body."
        },
        {
            "id": "rest_011",
            "skill": "REST APIs",
            "topic": "Status Codes",
            "question": "What does HTTP 400 usually indicate?",
            "options": ["The request is invalid or cannot be processed as submitted", "The request succeeded", "The resource was created", "The server is redirecting permanently"],
            "correct_answer": "The request is invalid or cannot be processed as submitted",
            "explanation": "400 Bad Request is commonly used for malformed or invalid client requests."
        },
        {
            "id": "rest_012",
            "skill": "REST APIs",
            "topic": "Status Codes",
            "question": "What is the usual distinction between HTTP 401 and 403?",
            "options": ["401 indicates missing or invalid authentication; 403 indicates the server refuses access", "401 means created; 403 means deleted", "Both always mean server failure", "401 is for images and 403 is for JSON"],
            "correct_answer": "401 indicates missing or invalid authentication; 403 indicates the server refuses access",
            "explanation": "401 concerns authentication, while 403 commonly indicates insufficient permission or refused access."
        },
        {
            "id": "rest_013",
            "skill": "REST APIs",
            "topic": "Status Codes",
            "question": "What does HTTP 404 mean?",
            "options": ["The requested resource was not found", "The request succeeded without content", "The server is temporarily unavailable", "The user has been created"],
            "correct_answer": "The requested resource was not found",
            "explanation": "404 Not Found indicates that the target resource could not be found."
        },
        {
            "id": "rest_014",
            "skill": "REST APIs",
            "topic": "Status Codes",
            "question": "What does HTTP 500 indicate?",
            "options": ["An internal server error", "A successful deletion", "An invalid URL query only", "A permanent redirect"],
            "correct_answer": "An internal server error",
            "explanation": "500 Internal Server Error indicates an unexpected server-side failure."
        },
        {
            "id": "rest_015",
            "skill": "REST APIs",
            "topic": "Status Codes",
            "question": "What does HTTP 503 commonly indicate?",
            "options": ["The service is temporarily unavailable", "The request was successfully created", "The resource was found", "The client sent a valid password"],
            "correct_answer": "The service is temporarily unavailable",
            "explanation": "503 Service Unavailable can indicate temporary overload or maintenance."
        },
        {
            "id": "rest_016",
            "skill": "REST APIs",
            "topic": "Idempotency",
            "question": "What does idempotency mean for an HTTP operation?",
            "options": ["Repeating the same request has the same intended effect as making it once", "The request must always return identical timestamps", "The request cannot fail", "The response must be XML"],
            "correct_answer": "Repeating the same request has the same intended effect as making it once",
            "explanation": "Idempotency concerns the intended effect, not necessarily identical responses."
        },
        {
            "id": "rest_017",
            "skill": "REST APIs",
            "topic": "Idempotency",
            "question": "Which pair of HTTP methods is generally defined as idempotent?",
            "options": ["GET and PUT", "POST and POST only", "POST and PATCH always", "CONNECT and POST"],
            "correct_answer": "GET and PUT",
            "explanation": "GET and PUT are defined as idempotent methods; DELETE is also defined as idempotent."
        },
        {
            "id": "rest_018",
            "skill": "REST APIs",
            "topic": "Headers",
            "question": "What does the Content-Type header describe?",
            "options": ["The media type of the message body", "The user's password", "The API's database schema", "The browser's screen resolution"],
            "correct_answer": "The media type of the message body",
            "explanation": "Content-Type identifies the format of the request or response body."
        },
        {
            "id": "rest_019",
            "skill": "REST APIs",
            "topic": "Headers",
            "question": "What does the Accept header commonly tell a server?",
            "options": ["Which response media types the client can accept", "Which database the server must install", "The client's password", "The server's file-system path"],
            "correct_answer": "Which response media types the client can accept",
            "explanation": "Accept communicates the response media types preferred or supported by the client."
        },
        {
            "id": "rest_020",
            "skill": "REST APIs",
            "topic": "JSON",
            "question": "Why is JSON commonly used in REST APIs?",
            "options": ["It provides a lightweight, structured data format supported by many languages", "It encrypts data automatically", "It replaces HTTP", "It guarantees valid business data"],
            "correct_answer": "It provides a lightweight, structured data format supported by many languages",
            "explanation": "JSON is widely supported for exchanging structured data, but it does not provide encryption or validation by itself."
        },
        {
            "id": "rest_021",
            "skill": "REST APIs",
            "topic": "Authentication",
            "question": "How is a bearer access token commonly sent in an HTTP request?",
            "options": ["In the Authorization header using the Bearer scheme", "In the CSS stylesheet name", "Only as a database table name", "In the HTTP status code"],
            "correct_answer": "In the Authorization header using the Bearer scheme",
            "explanation": "A common format is Authorization: Bearer followed by the access token."
        },
        {
            "id": "rest_022",
            "skill": "REST APIs",
            "topic": "Authentication",
            "question": "What is the main purpose of an API access token?",
            "options": ["To provide credentials used to authorize API access", "To compress every response", "To define URL routes", "To replace all status codes"],
            "correct_answer": "To provide credentials used to authorize API access",
            "explanation": "Tokens are credentials that a server validates according to its authentication design."
        },
        {
            "id": "rest_023",
            "skill": "REST APIs",
            "topic": "Authorization",
            "question": "Why must a server check authorization even if a user is authenticated?",
            "options": ["An authenticated user may not have permission to access every resource", "Authentication automatically grants administrator access", "The browser cannot send headers", "REST APIs do not support permissions"],
            "correct_answer": "An authenticated user may not have permission to access every resource",
            "explanation": "Authorization enforces what an authenticated identity is allowed to do."
        },
        {
            "id": "rest_024",
            "skill": "REST APIs",
            "topic": "Pagination",
            "question": "Why do APIs often support pagination?",
            "options": ["To return large result sets in manageable portions", "To encrypt passwords", "To replace HTTP methods", "To eliminate database queries"],
            "correct_answer": "To return large result sets in manageable portions",
            "explanation": "Pagination can reduce response size and improve performance."
        },
        {
            "id": "rest_025",
            "skill": "REST APIs",
            "topic": "Filtering",
            "question": "Where are filtering options commonly provided in a GET request?",
            "options": ["In URL query parameters", "Only in the response status code", "In the HTML title", "In the TLS certificate name"],
            "correct_answer": "In URL query parameters",
            "explanation": "Query parameters commonly represent filters, sorting, and pagination settings."
        },
        {
            "id": "rest_026",
            "skill": "REST APIs",
            "topic": "Versioning",
            "question": "Why might an API use versioning?",
            "options": ["To introduce changes while managing compatibility for existing clients", "To automatically encrypt all traffic", "To remove the need for documentation", "To guarantee zero downtime"],
            "correct_answer": "To introduce changes while managing compatibility for existing clients",
            "explanation": "Versioning helps APIs evolve while giving clients a known contract."
        },
        {
            "id": "rest_027",
            "skill": "REST APIs",
            "topic": "Caching",
            "question": "What is a benefit of HTTP caching for suitable API responses?",
            "options": ["It can reduce repeated requests and improve performance", "It guarantees that all data is always current", "It authenticates every user", "It removes all network delays"],
            "correct_answer": "It can reduce repeated requests and improve performance",
            "explanation": "Caching can save bandwidth and processing, but freshness rules must be configured appropriately."
        },
        {
            "id": "rest_028",
            "skill": "REST APIs",
            "topic": "Caching",
            "question": "What is the purpose of an ETag response header?",
            "options": ["Providing a validator for a particular representation", "Defining the API password", "Naming a database table", "Selecting the HTTP method"],
            "correct_answer": "Providing a validator for a particular representation",
            "explanation": "ETags can support conditional requests and cache validation."
        },
        {
            "id": "rest_029",
            "skill": "REST APIs",
            "topic": "Rate Limiting",
            "question": "What is the purpose of API rate limiting?",
            "options": ["Restricting how frequently clients can make requests", "Increasing every response's size", "Replacing authentication", "Automatically validating all input"],
            "correct_answer": "Restricting how frequently clients can make requests",
            "explanation": "Rate limiting helps control excessive usage and protect service availability."
        },
        {
            "id": "rest_030",
            "skill": "REST APIs",
            "topic": "Security",
            "question": "Why should APIs use HTTPS in production?",
            "options": ["It protects data in transit using TLS", "It validates all application rules automatically", "It replaces authorization checks", "It guarantees the server has no bugs"],
            "correct_answer": "It protects data in transit using TLS",
            "explanation": "HTTPS helps protect confidentiality and integrity during network transmission."
        },
        {
            "id": "rest_031",
            "skill": "REST APIs",
            "topic": "Input Validation",
            "question": "Why should an API validate request fields and data types?",
            "options": ["To reject malformed or disallowed input before processing", "Because JSON guarantees business correctness", "To automatically create user accounts", "To eliminate the need for authentication"],
            "correct_answer": "To reject malformed or disallowed input before processing",
            "explanation": "Input validation helps protect application logic and data integrity."
        },
        {
            "id": "rest_032",
            "skill": "REST APIs",
            "topic": "Error Responses",
            "question": "What makes a useful API error response?",
            "options": ["A suitable status code and a clear, safe error description", "A full server stack trace sent to every client", "Only an unrelated HTML page", "A database password"],
            "correct_answer": "A suitable status code and a clear, safe error description",
            "explanation": "Clear error responses help clients recover without exposing sensitive internal details."
        },
        {
            "id": "rest_033",
            "skill": "REST APIs",
            "topic": "OpenAPI",
            "question": "What is OpenAPI commonly used for?",
            "options": ["Describing an HTTP API in a machine-readable specification", "Encrypting API responses", "Creating database indexes", "Replacing the HTTP protocol"],
            "correct_answer": "Describing an HTTP API in a machine-readable specification",
            "explanation": "OpenAPI descriptions can support documentation, client generation, and tooling."
        },
        {
            "id": "rest_034",
            "skill": "REST APIs",
            "topic": "Testing",
            "question": "What should API tests commonly verify?",
            "options": ["Status codes, response data, validation, and access control", "Only the URL length", "Only the server's operating system", "Only the color of the frontend"],
            "correct_answer": "Status codes, response data, validation, and access control",
            "explanation": "API tests should cover both successful behavior and important failure cases."
        },
        {
            "id": "rest_035",
            "skill": "REST APIs",
            "topic": "Resource Design",
            "question": "Which URL is generally clearer for a collection of users?",
            "options": ["/users", "/getAllUsersNow", "/runUserDatabase", "/users-delete-everything"],
            "correct_answer": "/users",
            "explanation": "Resource-oriented URLs commonly use nouns, with HTTP methods describing the action."
        },
        {
            "id": "rest_036",
            "skill": "REST APIs",
            "topic": "CORS",
            "question": "What does CORS control in browser-based API access?",
            "options": ["Whether browser scripts may access responses from another origin", "Whether a user knows the API URL", "How SQL tables are joined", "How passwords are hashed"],
            "correct_answer": "Whether browser scripts may access responses from another origin",
            "explanation": "CORS is a browser-enforced cross-origin access mechanism, not an authentication system."
        },
        {
            "id": "rest_037",
            "skill": "REST APIs",
            "topic": "Webhooks",
            "question": "What is a webhook?",
            "options": ["An HTTP request sent to a configured endpoint when an event occurs", "A database table that stores CSS", "A method for compiling JavaScript", "A browser-only storage format"],
            "correct_answer": "An HTTP request sent to a configured endpoint when an event occurs",
            "explanation": "Webhooks let one system notify another about events, often through HTTP POST requests."
        },
        {
            "id": "rest_038",
            "skill": "REST APIs",
            "topic": "Reliability",
            "question": "Why should clients use timeouts when calling APIs?",
            "options": ["To avoid waiting indefinitely for a response", "To guarantee every request succeeds", "To bypass authentication", "To force the server to return JSON"],
            "correct_answer": "To avoid waiting indefinitely for a response",
            "explanation": "Timeouts help clients recover from slow or unresponsive services."
        },
        {
            "id": "rest_039",
            "skill": "REST APIs",
            "topic": "Reliability",
            "question": "Why should clients be careful when retrying a failed POST request?",
            "options": ["The original request may have succeeded even if its response was lost", "POST requests never create data", "Retries automatically roll back server changes", "HTTP does not support POST"],
            "correct_answer": "The original request may have succeeded even if its response was lost",
            "explanation": "Retries can create duplicate effects unless the API supports a suitable idempotency mechanism."
        },
        {
            "id": "rest_040",
            "skill": "REST APIs",
            "topic": "Best Practices",
            "question": "Which practice supports a reliable REST API?",
            "options": ["Use clear resource URLs, validation, suitable status codes, and access controls", "Return status 200 for every error", "Expose private credentials in responses", "Accept all input without checking it"],
            "correct_answer": "Use clear resource URLs, validation, suitable status codes, and access controls",
            "explanation": "Consistent API design and security checks improve reliability and client integration."
        }
    ],
    "sql": [
        {
            "id": "sql_001",
            "skill": "SQL",
            "topic": "SELECT",
            "question": "Which SQL statement retrieves data from a table?",
            "options": ["SELECT", "INSERT", "UPDATE", "DROP"],
            "correct_answer": "SELECT",
            "explanation": "SELECT retrieves rows and columns from database tables or other query sources."
        },
        {
            "id": "sql_002",
            "skill": "SQL",
            "topic": "Filtering",
            "question": "Which clause filters rows before grouping?",
            "options": ["WHERE", "ORDER BY", "SELECT", "LIMIT"],
            "correct_answer": "WHERE",
            "explanation": "WHERE filters rows that satisfy a condition."
        },
        {
            "id": "sql_003",
            "skill": "SQL",
            "topic": "Sorting",
            "question": "Which clause sorts query results?",
            "options": ["ORDER BY", "GROUP BY", "WHERE", "VALUES"],
            "correct_answer": "ORDER BY",
            "explanation": "ORDER BY sorts rows by one or more expressions."
        },
        {
            "id": "sql_004",
            "skill": "SQL",
            "topic": "Sorting",
            "question": "What does ORDER BY salary DESC do?",
            "options": ["Sorts salaries from highest to lowest", "Sorts salaries from lowest to highest", "Deletes rows with low salaries", "Groups all salaries together"],
            "correct_answer": "Sorts salaries from highest to lowest",
            "explanation": "DESC specifies descending order."
        },
        {
            "id": "sql_005",
            "skill": "SQL",
            "topic": "Filtering",
            "question": "Which operator checks whether a value matches any value in a specified list?",
            "options": ["IN", "BETWEEN", "LIKE", "IS NULL"],
            "correct_answer": "IN",
            "explanation": "IN tests whether an expression matches one of the values in a list or subquery."
        },
        {
            "id": "sql_006",
            "skill": "SQL",
            "topic": "Filtering",
            "question": "What does BETWEEN commonly test?",
            "options": ["Whether a value falls within an inclusive range", "Whether two tables have the same name", "Whether a column is a primary key", "Whether a query contains a join"],
            "correct_answer": "Whether a value falls within an inclusive range",
            "explanation": "BETWEEN commonly includes both the lower and upper bounds."
        },
        {
            "id": "sql_007",
            "skill": "SQL",
            "topic": "Pattern Matching",
            "question": "In a SQL LIKE pattern, what does % commonly represent?",
            "options": ["Zero or more characters", "Exactly one character", "Only a numeric digit", "A database table"],
            "correct_answer": "Zero or more characters",
            "explanation": "The percent wildcard matches any sequence of zero or more characters."
        },
        {
            "id": "sql_008",
            "skill": "SQL",
            "topic": "NULL",
            "question": "Which condition correctly checks whether a column has no value represented by NULL?",
            "options": ["column_name IS NULL", "column_name = NULL", "column_name == NULL", "column_name EQUALS NULL"],
            "correct_answer": "column_name IS NULL",
            "explanation": "SQL uses IS NULL because comparisons with NULL using ordinary equality do not evaluate to true."
        },
        {
            "id": "sql_009",
            "skill": "SQL",
            "topic": "Aggregation",
            "question": "Which function counts rows?",
            "options": ["COUNT()", "SUM()", "AVG()", "ROUND()"],
            "correct_answer": "COUNT()",
            "explanation": "COUNT(*) counts rows, while COUNT(column) counts non-NULL values in that column."
        },
        {
            "id": "sql_010",
            "skill": "SQL",
            "topic": "Aggregation",
            "question": "What does AVG(salary) calculate?",
            "options": ["The average of non-NULL salary values", "The total salary", "The number of employees", "The largest salary only"],
            "correct_answer": "The average of non-NULL salary values",
            "explanation": "AVG calculates the arithmetic mean of non-NULL input values."
        },
        {
            "id": "sql_011",
            "skill": "SQL",
            "topic": "Aggregation",
            "question": "What does GROUP BY department commonly do?",
            "options": ["Groups rows by department for aggregate calculations", "Sorts departments alphabetically in every case", "Deletes duplicate departments", "Creates a new department table"],
            "correct_answer": "Groups rows by department for aggregate calculations",
            "explanation": "GROUP BY forms groups that can be summarized with aggregate functions."
        },
        {
            "id": "sql_012",
            "skill": "SQL",
            "topic": "Aggregation",
            "question": "Which clause filters groups after aggregation?",
            "options": ["HAVING", "WHERE", "FROM", "VALUES"],
            "correct_answer": "HAVING",
            "explanation": "HAVING filters groups, often using aggregate expressions."
        },
        {
            "id": "sql_013",
            "skill": "SQL",
            "topic": "Joins",
            "question": "What does an INNER JOIN return?",
            "options": ["Rows with matching join conditions in both inputs", "Every row from the left table regardless of matches", "Only rows without matches", "All rows from every database table"],
            "correct_answer": "Rows with matching join conditions in both inputs",
            "explanation": "An INNER JOIN includes rows whose join condition matches."
        },
        {
            "id": "sql_014",
            "skill": "SQL",
            "topic": "Joins",
            "question": "What does a LEFT JOIN preserve?",
            "options": ["All rows from the left input and matching rows from the right", "Only matching rows from the right input", "Only rows with no NULL values", "Only duplicate rows"],
            "correct_answer": "All rows from the left input and matching rows from the right",
            "explanation": "Unmatched left-side rows remain, with NULLs for missing right-side columns."
        },
        {
            "id": "sql_015",
            "skill": "SQL",
            "topic": "Joins",
            "question": "What is a self join?",
            "options": ["Joining a table to itself", "Joining a table to a CSS file", "Joining only two databases with different engines", "Deleting a table and recreating it"],
            "correct_answer": "Joining a table to itself",
            "explanation": "A self join uses aliases to compare or relate rows within the same table."
        },
        {
            "id": "sql_016",
            "skill": "SQL",
            "topic": "Subqueries",
            "question": "What is a subquery?",
            "options": ["A query nested inside another SQL statement", "A database backup", "A column constraint", "A type of index only"],
            "correct_answer": "A query nested inside another SQL statement",
            "explanation": "Subqueries can appear in clauses such as WHERE, FROM, or SELECT."
        },
        {
            "id": "sql_017",
            "skill": "SQL",
            "topic": "Subqueries",
            "question": "What does EXISTS test?",
            "options": ["Whether a subquery returns at least one row", "Whether a table is empty of columns", "Whether a number is positive", "Whether a database server is installed"],
            "correct_answer": "Whether a subquery returns at least one row",
            "explanation": "EXISTS evaluates to true when its subquery returns one or more rows."
        },
        {
            "id": "sql_018",
            "skill": "SQL",
            "topic": "Data Modification",
            "question": "Which statement adds new rows to a table?",
            "options": ["INSERT", "SELECT", "ALTER", "GRANT"],
            "correct_answer": "INSERT",
            "explanation": "INSERT adds rows to a table."
        },
        {
            "id": "sql_019",
            "skill": "SQL",
            "topic": "Data Modification",
            "question": "Which statement changes existing rows?",
            "options": ["UPDATE", "CREATE", "SELECT", "COMMIT"],
            "correct_answer": "UPDATE",
            "explanation": "UPDATE modifies values in rows that match its conditions."
        },
        {
            "id": "sql_020",
            "skill": "SQL",
            "topic": "Data Modification",
            "question": "What is the risk of running DELETE without a WHERE clause?",
            "options": ["It can delete every row in the target table", "It deletes only duplicate rows", "It changes only the table name", "It creates a backup automatically"],
            "correct_answer": "It can delete every row in the target table",
            "explanation": "Without a filter, DELETE targets all rows in the table."
        },
        {
            "id": "sql_021",
            "skill": "SQL",
            "topic": "DDL",
            "question": "Which statement creates a new table?",
            "options": ["CREATE TABLE", "INSERT TABLE", "SELECT TABLE", "UPDATE TABLE"],
            "correct_answer": "CREATE TABLE",
            "explanation": "CREATE TABLE defines a new table and its columns."
        },
        {
            "id": "sql_022",
            "skill": "SQL",
            "topic": "DDL",
            "question": "What does ALTER TABLE commonly do?",
            "options": ["Changes a table definition", "Retrieves query results only", "Creates a user session", "Sorts rows by a column"],
            "correct_answer": "Changes a table definition",
            "explanation": "ALTER TABLE can modify columns or constraints, depending on the database."
        },
        {
            "id": "sql_023",
            "skill": "SQL",
            "topic": "DDL",
            "question": "What does DROP TABLE do?",
            "options": ["Removes the table definition and its data", "Deletes only one matching row", "Sorts the table", "Renames every column automatically"],
            "correct_answer": "Removes the table definition and its data",
            "explanation": "DROP TABLE removes the table object; exact recovery options depend on the database and backups."
        },
        {
            "id": "sql_024",
            "skill": "SQL",
            "topic": "Constraints",
            "question": "What does a PRIMARY KEY constraint ensure?",
            "options": ["Rows have a unique, non-NULL identifier", "Every column contains text", "Rows are automatically sorted", "The table contains no foreign keys"],
            "correct_answer": "Rows have a unique, non-NULL identifier",
            "explanation": "A primary key uniquely identifies each row and does not allow NULL key values."
        },
        {
            "id": "sql_025",
            "skill": "SQL",
            "topic": "Constraints",
            "question": "What does a FOREIGN KEY constraint help enforce?",
            "options": ["Referential integrity between related tables", "Alphabetical sorting", "Automatic encryption of all columns", "Unique values in every column"],
            "correct_answer": "Referential integrity between related tables",
            "explanation": "Foreign keys constrain references to matching keys in a related table or key set."
        },
        {
            "id": "sql_026",
            "skill": "SQL",
            "topic": "Constraints",
            "question": "What does a UNIQUE constraint generally enforce?",
            "options": ["No duplicate non-NULL key values under the database's rules", "No rows can contain NULL", "All rows have the same value", "Every value is numeric"],
            "correct_answer": "No duplicate non-NULL key values under the database's rules",
            "explanation": "UNIQUE prevents duplicate key combinations; treatment of NULL values varies by database."
        },
        {
            "id": "sql_027",
            "skill": "SQL",
            "topic": "Constraints",
            "question": "What does NOT NULL require?",
            "options": ["The column must have a non-NULL value", "The column must contain unique values", "The column must contain only integers", "The column must be a primary key"],
            "correct_answer": "The column must have a non-NULL value",
            "explanation": "NOT NULL prevents a column value from being NULL."
        },
        {
            "id": "sql_028",
            "skill": "SQL",
            "topic": "Constraints",
            "question": "What is a CHECK constraint used for?",
            "options": ["Enforcing a specified condition on inserted or updated values", "Sorting query results", "Joining tables", "Backing up a database"],
            "correct_answer": "Enforcing a specified condition on inserted or updated values",
            "explanation": "A CHECK constraint enforces a Boolean condition supported by the database."
        },
        {
            "id": "sql_029",
            "skill": "SQL",
            "topic": "Transactions",
            "question": "What does COMMIT do?",
            "options": ["Makes the current transaction's changes permanent", "Reverses all committed changes", "Deletes the database schema", "Starts a SELECT query"],
            "correct_answer": "Makes the current transaction's changes permanent",
            "explanation": "COMMIT completes a transaction and saves its changes according to the database's transaction rules."
        },
        {
            "id": "sql_030",
            "skill": "SQL",
            "topic": "Transactions",
            "question": "What does ROLLBACK do?",
            "options": ["Undoes uncommitted changes in the current transaction", "Sorts all tables", "Creates a new index", "Exports every record to CSV"],
            "correct_answer": "Undoes uncommitted changes in the current transaction",
            "explanation": "ROLLBACK reverses changes made in the current transaction that have not been committed."
        },
        {
            "id": "sql_031",
            "skill": "SQL",
            "topic": "Transactions",
            "question": "What does ACID's atomicity property mean?",
            "options": ["A transaction's operations succeed as a unit or are rolled back as a unit", "Every query runs at the same speed", "All database columns must be numeric", "Transactions never use locks"],
            "correct_answer": "A transaction's operations succeed as a unit or are rolled back as a unit",
            "explanation": "Atomicity treats a transaction as an indivisible unit of work."
        },
        {
            "id": "sql_032",
            "skill": "SQL",
            "topic": "Indexes",
            "question": "Why create an index on a database column?",
            "options": ["To speed up suitable lookups and queries", "To guarantee every query is faster", "To eliminate the need for primary keys", "To automatically remove duplicate rows"],
            "correct_answer": "To speed up suitable lookups and queries",
            "explanation": "Indexes can improve reads but consume storage and add maintenance cost to writes."
        },
        {
            "id": "sql_033",
            "skill": "SQL",
            "topic": "Indexes",
            "question": "What is a possible disadvantage of adding too many indexes?",
            "options": ["Writes may become slower and storage use may increase", "Queries can no longer use WHERE", "Tables stop supporting primary keys", "SQL becomes a programming language"],
            "correct_answer": "Writes may become slower and storage use may increase",
            "explanation": "Indexes must be maintained when indexed data changes."
        },
        {
            "id": "sql_034",
            "skill": "SQL",
            "topic": "Normalization",
            "question": "What is a common goal of database normalization?",
            "options": ["Reducing redundant data and update anomalies", "Making every query use a full table scan", "Removing all relationships", "Storing every value in one column"],
            "correct_answer": "Reducing redundant data and update anomalies",
            "explanation": "Normalization organizes data to reduce duplication and inconsistencies."
        },
        {
            "id": "sql_035",
            "skill": "SQL",
            "topic": "Normalization",
            "question": "What is a common requirement of First Normal Form (1NF)?",
            "options": ["Each field contains a single value rather than repeating groups", "Every table must have exactly two columns", "All tables must be joined", "Every column must be a foreign key"],
            "correct_answer": "Each field contains a single value rather than repeating groups",
            "explanation": "1NF commonly requires atomic values and no repeating groups."
        },
        {
            "id": "sql_036",
            "skill": "SQL",
            "topic": "Set Operations",
            "question": "What does UNION do by default?",
            "options": ["Combines result sets and removes duplicate rows", "Combines tables only when they have identical names", "Deletes rows present in both results", "Sorts every source table permanently"],
            "correct_answer": "Combines result sets and removes duplicate rows",
            "explanation": "UNION combines compatible query results and removes duplicates unless UNION ALL is used."
        },
        {
            "id": "sql_037",
            "skill": "SQL",
            "topic": "Window Functions",
            "question": "What is a window function useful for?",
            "options": ["Calculating values across related rows without collapsing them into one row per group", "Deleting duplicate tables", "Creating a new database", "Replacing all joins"],
            "correct_answer": "Calculating values across related rows without collapsing them into one row per group",
            "explanation": "Window functions calculate values such as rankings or running totals while preserving individual result rows."
        },
        {
            "id": "sql_038",
            "skill": "SQL",
            "topic": "Window Functions",
            "question": "What does ROW_NUMBER() commonly return?",
            "options": ["A sequential number for each row within a window ordering", "The total number of database tables", "The number of NULL columns only", "A unique database identifier guaranteed across all queries"],
            "correct_answer": "A sequential number for each row within a window ordering",
            "explanation": "ROW_NUMBER assigns sequential numbers according to the window's ordering and partition."
        },
        {
            "id": "sql_039",
            "skill": "SQL",
            "topic": "Query Performance",
            "question": "What is EXPLAIN commonly used for?",
            "options": ["Inspecting a query's execution plan", "Changing every table's schema", "Creating a new user account", "Automatically repairing all data"],
            "correct_answer": "Inspecting a query's execution plan",
            "explanation": "EXPLAIN helps developers understand how a database plans to execute a query."
        },
        {
            "id": "sql_040",
            "skill": "SQL",
            "topic": "Security",
            "question": "What is the safest general approach when inserting user input into SQL queries?",
            "options": ["Use parameterized queries", "Concatenate raw input into SQL text", "Disable all constraints", "Return the database password to the user"],
            "correct_answer": "Use parameterized queries",
            "explanation": "Parameterized queries separate data from SQL syntax and help prevent SQL injection."
        }
    ],
    
    "mysql": [
        {"id": "mysql_001", "skill": "MySQL", "topic": "Basics", "question": "Which statement retrieves all columns from a table named employees?", "options": ["GET ALL employees;", "SELECT * FROM employees;", "FETCH employees;", "SHOW COLUMNS employees;"], "correct_answer": "SELECT * FROM employees;", "explanation": "SELECT * retrieves every column from the specified table."},
        {"id": "mysql_002", "skill": "MySQL", "topic": "Basics", "question": "Which command creates a new database?", "options": ["MAKE DATABASE company;", "NEW DATABASE company;", "CREATE DATABASE company;", "ADD DATABASE company;"], "correct_answer": "CREATE DATABASE company;", "explanation": "CREATE DATABASE creates a database."},
        {"id": "mysql_003", "skill": "MySQL", "topic": "Filtering", "question": "Which clause filters rows based on a condition?", "options": ["WHERE", "ORDER BY", "GROUP BY", "LIMIT"], "correct_answer": "WHERE", "explanation": "WHERE selects rows that satisfy a condition."},
        {"id": "mysql_004", "skill": "MySQL", "topic": "Sorting", "question": "How do you sort salaries from highest to lowest?", "options": ["ORDER BY salary ASC", "SORT salary DESC", "ORDER salary DOWN", "ORDER BY salary DESC"], "correct_answer": "ORDER BY salary DESC", "explanation": "DESC sorts values in descending order."},
        {"id": "mysql_005", "skill": "MySQL", "topic": "Filtering", "question": "Which operator checks whether a value falls within a range?", "options": ["LIKE", "BETWEEN", "INTO", "MATCH"], "correct_answer": "BETWEEN", "explanation": "BETWEEN checks whether a value is within an inclusive range."},
        {"id": "mysql_006", "skill": "MySQL", "topic": "Filtering", "question": "Which operator checks whether a value matches any value in a list?", "options": ["BETWEEN", "RANGE", "IN", "ANYOF"], "correct_answer": "IN", "explanation": "IN tests a value against a list of possible values."},
        {"id": "mysql_007", "skill": "MySQL", "topic": "Filtering", "question": "Which pattern matches names beginning with 'A'?", "options": ["LIKE '%A'", "LIKE '_A%'", "LIKE '%A%'", "LIKE 'A%'"], "correct_answer": "LIKE 'A%'", "explanation": "A followed by % matches strings beginning with A."},
        {"id": "mysql_008", "skill": "MySQL", "topic": "NULL Values", "question": "How should you test whether a column contains NULL?", "options": ["column = NULL", "column IS NULL", "column == NULL", "column EQUALS NULL"], "correct_answer": "column IS NULL", "explanation": "IS NULL is the correct SQL test for NULL values."},
        {"id": "mysql_009", "skill": "MySQL", "topic": "Aggregation", "question": "Which function counts all rows, including rows with NULL columns?", "options": ["COUNT(*)", "COUNT(column)", "SUM(*)", "TOTAL(column)"], "correct_answer": "COUNT(*)", "explanation": "COUNT(*) counts rows regardless of NULL values in individual columns."},
        {"id": "mysql_010", "skill": "MySQL", "topic": "Aggregation", "question": "Which function returns the average of numeric values?", "options": ["MEAN()", "MID()", "AVG()", "AVERAGE()"], "correct_answer": "AVG()", "explanation": "AVG() calculates the arithmetic average."},
        {"id": "mysql_011", "skill": "MySQL", "topic": "Aggregation", "question": "Which clause filters grouped results after aggregation?", "options": ["WHERE", "ORDER BY", "LIMIT", "HAVING"], "correct_answer": "HAVING", "explanation": "HAVING filters groups, often using aggregate functions."},
        {"id": "mysql_012", "skill": "MySQL", "topic": "Grouping", "question": "Which clause groups rows that share the same department?", "options": ["ORDER BY department", "GROUP BY department", "PARTITION department", "MERGE BY department"], "correct_answer": "GROUP BY department", "explanation": "GROUP BY forms groups based on equal department values."},
        {"id": "mysql_013", "skill": "MySQL", "topic": "Joins", "question": "Which join returns matching rows from both tables only?", "options": ["LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "CROSS JOIN"], "correct_answer": "INNER JOIN", "explanation": "INNER JOIN returns rows satisfying the join condition."},
        {"id": "mysql_014", "skill": "MySQL", "topic": "Joins", "question": "Which join keeps every row from the left table even without a match?", "options": ["LEFT JOIN", "INNER JOIN", "CROSS JOIN", "SELF JOIN"], "correct_answer": "LEFT JOIN", "explanation": "LEFT JOIN preserves all left-table rows and fills unmatched right-side columns with NULL."},
        {"id": "mysql_015", "skill": "MySQL", "topic": "Joins", "question": "What is a self join?", "options": ["Joining two databases", "Joining a table to itself", "Joining only primary keys", "Joining without a condition"], "correct_answer": "Joining a table to itself", "explanation": "A self join compares rows within the same table using aliases."},
        {"id": "mysql_016", "skill": "MySQL", "topic": "Subqueries", "question": "What is a subquery?", "options": ["A query inside another SQL statement", "A database backup", "A table constraint", "A user account"], "correct_answer": "A query inside another SQL statement", "explanation": "A subquery is nested within a larger SQL statement."},
        {"id": "mysql_017", "skill": "MySQL", "topic": "Keys", "question": "What is the main purpose of a primary key?", "options": ["Allow duplicate row identifiers", "Store only text", "Uniquely identify each row", "Sort every query automatically"], "correct_answer": "Uniquely identify each row", "explanation": "A primary key uniquely identifies records and cannot contain NULL."},
        {"id": "mysql_018", "skill": "MySQL", "topic": "Keys", "question": "What does a foreign key help enforce?", "options": ["Faster text formatting", "Referential integrity", "Automatic backups", "Password encryption"], "correct_answer": "Referential integrity", "explanation": "A foreign key helps ensure references point to valid related records."},
        {"id": "mysql_019", "skill": "MySQL", "topic": "Constraints", "question": "Which constraint prevents duplicate values in a column or column combination?", "options": ["DEFAULT", "CHECK", "NOT NULL", "UNIQUE"], "correct_answer": "UNIQUE", "explanation": "UNIQUE prevents duplicate key values; NULL handling depends on the column definition and MySQL behavior."},
        {"id": "mysql_020", "skill": "MySQL", "topic": "Constraints", "question": "Which constraint prevents a column from storing NULL?", "options": ["NOT NULL", "UNIQUE", "DEFAULT", "INDEX"], "correct_answer": "NOT NULL", "explanation": "NOT NULL requires each row to provide a non-NULL value for that column."},
        {"id": "mysql_021", "skill": "MySQL", "topic": "Data Types", "question": "Which type is generally suitable for variable-length text?", "options": ["INT", "DATE", "VARCHAR", "BOOLEAN"], "correct_answer": "VARCHAR", "explanation": "VARCHAR stores variable-length character strings up to a defined limit."},
        {"id": "mysql_022", "skill": "MySQL", "topic": "Data Types", "question": "Which type is suitable for storing a calendar date?", "options": ["FLOAT", "DATE", "BLOB", "CHAR"], "correct_answer": "DATE", "explanation": "DATE stores a date value without a time component."},
        {"id": "mysql_023", "skill": "MySQL", "topic": "Data Types", "question": "Which type is commonly used for exact monetary decimal values?", "options": ["FLOAT", "DOUBLE", "TEXT", "DECIMAL"], "correct_answer": "DECIMAL", "explanation": "DECIMAL stores exact fixed-point numeric values, useful for money."},
        {"id": "mysql_024", "skill": "MySQL", "topic": "Data Modification", "question": "Which statement changes existing rows?", "options": ["CHANGE TABLE", "UPDATE", "MODIFY ROWS", "ALTER VALUE"], "correct_answer": "UPDATE", "explanation": "UPDATE changes column values in rows matching its condition."},
        {"id": "mysql_025", "skill": "MySQL", "topic": "Data Modification", "question": "Which statement removes selected rows from a table?", "options": ["DROP DATABASE", "REMOVE TABLE", "DELETE FROM", "CLEAR SCHEMA"], "correct_answer": "DELETE FROM", "explanation": "DELETE FROM removes rows that match its WHERE condition."},
        {"id": "mysql_026", "skill": "MySQL", "topic": "Data Definition", "question": "Which statement changes a table's structure?", "options": ["ALTER TABLE", "UPDATE TABLE", "CHANGE ROW", "REPLACE DATABASE"], "correct_answer": "ALTER TABLE", "explanation": "ALTER TABLE adds, changes, or removes columns and constraints."},
        {"id": "mysql_027", "skill": "MySQL", "topic": "Data Definition", "question": "What does DROP TABLE do?", "options": ["Deletes only duplicate rows", "Removes the table definition and its data", "Clears one column", "Renames a table"], "correct_answer": "Removes the table definition and its data", "explanation": "DROP TABLE removes the table itself, including its stored rows."},
        {"id": "mysql_028", "skill": "MySQL", "topic": "Indexes", "question": "What is a common purpose of an index?", "options": ["Guarantee every query is faster", "Replace all constraints", "Speed up data retrieval for suitable queries", "Automatically encrypt data"], "correct_answer": "Speed up data retrieval for suitable queries", "explanation": "Indexes can improve lookups but require storage and can slow writes."},
        {"id": "mysql_029", "skill": "MySQL", "topic": "Indexes", "question": "What is a possible disadvantage of creating many indexes?", "options": ["Writes may become slower", "Tables cannot be queried", "Primary keys stop working", "Rows become permanently sorted"], "correct_answer": "Writes may become slower", "explanation": "Insert, update, and delete operations may need to maintain multiple indexes."},
        {"id": "mysql_030", "skill": "MySQL", "topic": "Transactions", "question": "Which command saves a transaction's changes permanently?", "options": ["SAVEPOINT", "ROLLBACK", "COMMIT", "CLOSE"], "correct_answer": "COMMIT", "explanation": "COMMIT confirms the current transaction."},
        {"id": "mysql_031", "skill": "MySQL", "topic": "Transactions", "question": "Which command undoes uncommitted changes in a transaction?", "options": ["COMMIT", "ROLLBACK", "PUBLISH", "MERGE"], "correct_answer": "ROLLBACK", "explanation": "ROLLBACK reverses changes in the current transaction that have not been committed."},
        {"id": "mysql_032", "skill": "MySQL", "topic": "Transactions", "question": "Which ACID property means a transaction happens completely or not at all?", "options": ["Consistency", "Isolation", "Durability", "Atomicity"], "correct_answer": "Atomicity", "explanation": "Atomicity prevents a transaction from being only partially applied."},
        {"id": "mysql_033", "skill": "MySQL", "topic": "Views", "question": "What is a database view?", "options": ["A saved query presented like a table", "A physical backup by default", "A database user", "A type of index only"], "correct_answer": "A saved query presented like a table", "explanation": "A view is a named query that can be used like a table in many queries."},
        {"id": "mysql_034", "skill": "MySQL", "topic": "Functions", "question": "What does COALESCE(a, b) return when a is NULL and b is 5?", "options": ["NULL", "0", "5", "An error always"], "correct_answer": "5", "explanation": "COALESCE returns the first non-NULL argument."},
        {"id": "mysql_035", "skill": "MySQL", "topic": "Functions", "question": "Which function combines strings in MySQL?", "options": ["JOIN_TEXT()", "CONCAT()", "MERGE_STRING()", "APPEND()"], "correct_answer": "CONCAT()", "explanation": "CONCAT() joins its string arguments into one string."},
        {"id": "mysql_036", "skill": "MySQL", "topic": "Date Functions", "question": "Which function returns the current date and time?", "options": ["TODAY()", "CURRENT_CLOCK()", "NOW()", "DATE_TIME_NOW()"], "correct_answer": "NOW()", "explanation": "NOW() returns the current date and time in the session time zone."},
        {"id": "mysql_037", "skill": "MySQL", "topic": "Performance", "question": "What is EXPLAIN commonly used for?", "options": ["Creating a user", "Inspecting a query execution plan", "Encrypting a table", "Exporting all databases"], "correct_answer": "Inspecting a query execution plan", "explanation": "EXPLAIN shows how MySQL plans to execute a query."},
        {"id": "mysql_038", "skill": "MySQL", "topic": "Security", "question": "What is the safest common approach for passing user input into application SQL queries?", "options": ["Concatenate raw input", "Remove all spaces only", "Use prepared statements with parameters", "Trust input from forms"], "correct_answer": "Use prepared statements with parameters", "explanation": "Parameterized queries separate SQL code from user-provided values and help prevent SQL injection."},
        {"id": "mysql_039", "skill": "MySQL", "topic": "Auto Increment", "question": "What does AUTO_INCREMENT typically do for an integer column?", "options": ["Generates a new value automatically for inserted rows", "Makes every value negative", "Encrypts each value", "Prevents SELECT queries"], "correct_answer": "Generates a new value automatically for inserted rows", "explanation": "AUTO_INCREMENT generates successive values when a value is not explicitly supplied."},
        {"id": "mysql_040", "skill": "MySQL", "topic": "Pagination", "question": "What does LIMIT 10 OFFSET 20 do in a SELECT query?", "options": ["Returns 20 rows only", "Skips 10 rows and returns 20", "Returns at most 10 rows after skipping 20", "Deletes the first 20 rows"], "correct_answer": "Returns at most 10 rows after skipping 20", "explanation": "OFFSET skips the first 20 qualifying rows and LIMIT returns up to the next 10."}
    ],
    
    "postgresql": [
        {"id": "postgresql_001", "skill": "PostgreSQL", "topic": "Basics", "question": "Which command creates a database in PostgreSQL?", "options": ["MAKE DATABASE shop;", "CREATE DATABASE shop;", "NEW DATABASE shop;", "ADD DATABASE shop;"], "correct_answer": "CREATE DATABASE shop;", "explanation": "CREATE DATABASE creates a new PostgreSQL database."},
        {"id": "postgresql_002", "skill": "PostgreSQL", "topic": "Basics", "question": "Which command lists databases in the psql terminal?", "options": ["\\dt", "\\du", "\\l", "\\dn"], "correct_answer": "\\l", "explanation": "The psql meta-command \\l lists databases."},
        {"id": "postgresql_003", "skill": "PostgreSQL", "topic": "Basics", "question": "Which psql command lists tables in the current schema search path?", "options": ["\\dt", "\\l", "\\conn", "\\help"], "correct_answer": "\\dt", "explanation": "\\dt lists tables visible through the current search path."},
        {"id": "postgresql_004", "skill": "PostgreSQL", "topic": "Data Types", "question": "Which PostgreSQL type stores variable-length character strings without a fixed declared maximum?", "options": ["CHAR(5)", "VARCHAR(5)", "TEXT", "SMALLINT"], "correct_answer": "TEXT", "explanation": "TEXT stores strings of variable length, subject to PostgreSQL's overall field limits."},
        {"id": "postgresql_005", "skill": "PostgreSQL", "topic": "Data Types", "question": "Which type is suited to exact decimal values such as prices?", "options": ["REAL", "NUMERIC", "BOOLEAN", "BYTEA"], "correct_answer": "NUMERIC", "explanation": "NUMERIC supports exact decimal arithmetic."},
        {"id": "postgresql_006", "skill": "PostgreSQL", "topic": "Data Types", "question": "Which type stores a date and time with time-zone awareness?", "options": ["DATE", "TIME", "TIMESTAMP WITH TIME ZONE", "INTERVAL"], "correct_answer": "TIMESTAMP WITH TIME ZONE", "explanation": "This timestamp type represents an instant and handles time-zone conversions."},
        {"id": "postgresql_007", "skill": "PostgreSQL", "topic": "Data Types", "question": "Which PostgreSQL type stores JSON data in a decomposed binary format that supports indexing?", "options": ["JSONB", "XMLTEXT", "CHARJSON", "JSONFILE"], "correct_answer": "JSONB", "explanation": "JSONB stores JSON in a binary representation and supports useful index types."},
        {"id": "postgresql_008", "skill": "PostgreSQL", "topic": "Data Types", "question": "Which type is used for true or false values?", "options": ["BITTEXT", "BOOLEAN", "LOGICAL", "TINYINT"], "correct_answer": "BOOLEAN", "explanation": "PostgreSQL BOOLEAN stores true, false, or NULL."},
        {"id": "postgresql_009", "skill": "PostgreSQL", "topic": "Queries", "question": "Which clause filters rows before grouping?", "options": ["HAVING", "WHERE", "ORDER BY", "RETURNING"], "correct_answer": "WHERE", "explanation": "WHERE filters individual rows before grouping and aggregation."},
        {"id": "postgresql_010", "skill": "PostgreSQL", "topic": "Queries", "question": "Which clause filters results after GROUP BY aggregation?", "options": ["LIMIT", "WHERE", "HAVING", "OFFSET"], "correct_answer": "HAVING", "explanation": "HAVING applies conditions to groups created by GROUP BY."},
        {"id": "postgresql_011", "skill": "PostgreSQL", "topic": "Queries", "question": "Which keyword removes duplicate rows from a SELECT result?", "options": ["UNIQUE ROWS", "DISTINCT", "DEDUP", "ONLY"], "correct_answer": "DISTINCT", "explanation": "DISTINCT removes duplicate result rows."},
        {"id": "postgresql_012", "skill": "PostgreSQL", "topic": "Queries", "question": "Which clause limits the number of rows returned?", "options": ["LIMIT", "CAP", "STOP", "TOPROWS"], "correct_answer": "LIMIT", "explanation": "LIMIT specifies the maximum number of rows returned."},
        {"id": "postgresql_013", "skill": "PostgreSQL", "topic": "Joins", "question": "Which join returns only rows that match the join condition in both tables?", "options": ["FULL JOIN", "LEFT JOIN", "INNER JOIN", "CROSS JOIN"], "correct_answer": "INNER JOIN", "explanation": "INNER JOIN returns rows for which the join condition matches."},
        {"id": "postgresql_014", "skill": "PostgreSQL", "topic": "Joins", "question": "Which join retains unmatched rows from both tables?", "options": ["INNER JOIN", "FULL OUTER JOIN", "CROSS JOIN", "NATURAL INNER JOIN"], "correct_answer": "FULL OUTER JOIN", "explanation": "FULL OUTER JOIN includes matched rows and unmatched rows from either side."},
        {"id": "postgresql_015", "skill": "PostgreSQL", "topic": "Joins", "question": "What does CROSS JOIN produce?", "options": ["Only identical records", "A Cartesian product of the input rows", "Only unmatched records", "A database backup"], "correct_answer": "A Cartesian product of the input rows", "explanation": "Every row from one input is paired with every row from the other."},
        {"id": "postgresql_016", "skill": "PostgreSQL", "topic": "Returning", "question": "What does RETURNING do in a PostgreSQL INSERT statement?", "options": ["Returns specified values from inserted rows", "Rolls back the insert", "Renames the table", "Lists all database users"], "correct_answer": "Returns specified values from inserted rows", "explanation": "RETURNING can return generated IDs or other values from affected rows."},
        {"id": "postgresql_017", "skill": "PostgreSQL", "topic": "Returning", "question": "Can PostgreSQL UPDATE use RETURNING to show changed values?", "options": ["No, never", "Only with JSON tables", "Yes", "Only after dropping the table"], "correct_answer": "Yes", "explanation": "UPDATE ... RETURNING can return values from rows modified by the statement."},
        {"id": "postgresql_018", "skill": "PostgreSQL", "topic": "Keys", "question": "Which constraint uniquely identifies each row and disallows NULL values?", "options": ["CHECK", "PRIMARY KEY", "DEFAULT", "FOREIGN KEY"], "correct_answer": "PRIMARY KEY", "explanation": "A primary key enforces uniqueness and non-NULL values."},
        {"id": "postgresql_019", "skill": "PostgreSQL", "topic": "Keys", "question": "What is the purpose of a foreign key?", "options": ["To store binary files", "To enforce relationships between tables", "To sort query output", "To automatically compress rows"], "correct_answer": "To enforce relationships between tables", "explanation": "A foreign key enforces referential integrity between related tables."},
        {"id": "postgresql_020", "skill": "PostgreSQL", "topic": "Constraints", "question": "Which constraint restricts values according to a Boolean condition?", "options": ["CHECK", "ORDER", "INDEX", "VIEW"], "correct_answer": "CHECK", "explanation": "CHECK rejects inserted or updated rows when its condition evaluates to false."},
        {"id": "postgresql_021", "skill": "PostgreSQL", "topic": "Sequences", "question": "Which feature generates sequential numeric values commonly used for IDs?", "options": ["Sequence", "Schema", "Trigger only", "View"], "correct_answer": "Sequence", "explanation": "A sequence generates successive numeric values and can supply ID values."},
        {"id": "postgresql_022", "skill": "PostgreSQL", "topic": "Sequences", "question": "Which PostgreSQL data type is commonly used for an automatically generated identity column?", "options": ["IDENTITY TEXT", "GENERATED ALWAYS AS IDENTITY", "AUTO NUMBER", "SEQUENCE VARCHAR"], "correct_answer": "GENERATED ALWAYS AS IDENTITY", "explanation": "Identity columns generate values from an implicit sequence."},
        {"id": "postgresql_023", "skill": "PostgreSQL", "topic": "Indexes", "question": "Which index type is the default and commonly used for equality and range comparisons?", "options": ["B-tree", "Hash only", "Bitmap", "Heap"], "correct_answer": "B-tree", "explanation": "B-tree is the default index type and supports many common comparisons."},
        {"id": "postgresql_024", "skill": "PostgreSQL", "topic": "Indexes", "question": "Which index type is often useful for indexing JSONB containment operations?", "options": ["BRIN only", "GIN", "Sequence", "Heap"], "correct_answer": "GIN", "explanation": "GIN indexes can efficiently support JSONB containment and key searches."},
        {"id": "postgresql_025", "skill": "PostgreSQL", "topic": "Indexes", "question": "What is a partial index?", "options": ["An index covering only rows that satisfy a condition", "An index with half its data corrupted", "An index that stores only column names", "An index that cannot be queried"], "correct_answer": "An index covering only rows that satisfy a condition", "explanation": "A partial index indexes rows matching its WHERE predicate."},
        {"id": "postgresql_026", "skill": "PostgreSQL", "topic": "Transactions", "question": "Which command makes the current transaction's changes permanent?", "options": ["ROLLBACK", "COMMIT", "SAVEPOINT", "EXPLAIN"], "correct_answer": "COMMIT", "explanation": "COMMIT ends the transaction and makes its changes permanent."},
        {"id": "postgresql_027", "skill": "PostgreSQL", "topic": "Transactions", "question": "Which command cancels the current transaction's uncommitted changes?", "options": ["COMMIT", "GRANT", "ROLLBACK", "VACUUM"], "correct_answer": "ROLLBACK", "explanation": "ROLLBACK aborts the current transaction."},
        {"id": "postgresql_028", "skill": "PostgreSQL", "topic": "Transactions", "question": "What is a SAVEPOINT used for?", "options": ["Creating a database login", "Marking a point for partial rollback", "Creating a permanent backup", "Generating an index"], "correct_answer": "Marking a point for partial rollback", "explanation": "ROLLBACK TO SAVEPOINT reverses work performed after that savepoint."},
        {"id": "postgresql_029", "skill": "PostgreSQL", "topic": "Transactions", "question": "What does ACID durability mean?", "options": ["Committed changes survive failures as guaranteed by the system", "Every query is instant", "Every table has an index", "All users share one transaction"], "correct_answer": "Committed changes survive failures as guaranteed by the system", "explanation": "Durability means committed transaction results persist through failures within the system's guarantees."},
        {"id": "postgresql_030", "skill": "PostgreSQL", "topic": "Views", "question": "What is a materialized view?", "options": ["A query result stored on disk and refreshed when needed", "A temporary user password", "A normal index alias", "A database connection"], "correct_answer": "A query result stored on disk and refreshed when needed", "explanation": "A materialized view stores query results instead of recomputing them for every read."},
        {"id": "postgresql_031", "skill": "PostgreSQL", "topic": "Common Table Expressions", "question": "Which keyword introduces a common table expression?", "options": ["WITH", "DEFINE", "TEMPQUERY", "START"], "correct_answer": "WITH", "explanation": "WITH defines named query expressions that can be referenced by the main statement."},
        {"id": "postgresql_032", "skill": "PostgreSQL", "topic": "Common Table Expressions", "question": "What does WITH RECURSIVE support?", "options": ["Recursive queries such as walking a hierarchy", "Only database creation", "Password resets", "Index deletion only"], "correct_answer": "Recursive queries such as walking a hierarchy", "explanation": "Recursive CTEs repeatedly evaluate a query to process hierarchical or sequential data."},
        {"id": "postgresql_033", "skill": "PostgreSQL", "topic": "Window Functions", "question": "What does ROW_NUMBER() do when used as a window function?", "options": ["Counts only NULL values", "Assigns a sequential number within a window", "Deletes duplicate records", "Creates a table"], "correct_answer": "Assigns a sequential number within a window", "explanation": "ROW_NUMBER assigns a distinct sequence number based on the window ordering."},
        {"id": "postgresql_034", "skill": "PostgreSQL", "topic": "Window Functions", "question": "What is the purpose of the OVER clause?", "options": ["Defines the window for a window function", "Ends a database session", "Creates a new schema", "Encrypts query results"], "correct_answer": "Defines the window for a window function", "explanation": "OVER defines partitioning, ordering, and optionally a frame for a window function."},
        {"id": "postgresql_035", "skill": "PostgreSQL", "topic": "Functions", "question": "Which function returns the first non-NULL value from its arguments?", "options": ["NULLIF", "COALESCE", "GREATESTNULL", "ISNULLONLY"], "correct_answer": "COALESCE", "explanation": "COALESCE returns the first argument that is not NULL."},
        {"id": "postgresql_036", "skill": "PostgreSQL", "topic": "Functions", "question": "Which operator concatenates two strings in PostgreSQL?", "options": ["+", "||", "&", "->>"], "correct_answer": "||", "explanation": "The || operator concatenates string expressions."},
        {"id": "postgresql_037", "skill": "PostgreSQL", "topic": "JSON", "question": "Which operator extracts a JSON object field as text?", "options": ["->", "->>", "::", "@@"], "correct_answer": "->>", "explanation": "The ->> operator extracts a JSON field as text; -> returns JSON or JSONB."},
        {"id": "postgresql_038", "skill": "PostgreSQL", "topic": "Performance", "question": "What does EXPLAIN ANALYZE do?", "options": ["Only lists table columns", "Executes the query and reports actual execution statistics", "Creates a new database", "Restores a backup"], "correct_answer": "Executes the query and reports actual execution statistics", "explanation": "EXPLAIN ANALYZE runs the statement and reports measured execution details."},
        {"id": "postgresql_039", "skill": "PostgreSQL", "topic": "Maintenance", "question": "What is the purpose of VACUUM?", "options": ["Reclaim or make reusable space from dead tuples and support maintenance", "Create new users", "Rename every table", "Convert SQL to JSON"], "correct_answer": "Reclaim or make reusable space from dead tuples and support maintenance", "explanation": "VACUUM cleans up dead tuples and helps prevent transaction ID wraparound; it does not normally shrink the file size."},
        {"id": "postgresql_040", "skill": "PostgreSQL", "topic": "Security", "question": "Which SQL command gives a role permission to read a table?", "options": ["ALLOW SELECT", "GRANT SELECT", "ENABLE READ", "PERMIT TABLE"], "correct_answer": "GRANT SELECT", "explanation": "GRANT SELECT ON table_name TO role_name gives a role permission to query a table."}
    ],
    
    "mongodb": [
        {"id": "mongodb_001", "skill": "MongoDB", "topic": "Basics", "question": "What type of database is MongoDB?", "options": ["Relational database only", "Document-oriented NoSQL database", "Graph database only", "Spreadsheet database"], "correct_answer": "Document-oriented NoSQL database", "explanation": "MongoDB stores records as BSON documents in collections."},
        {"id": "mongodb_002", "skill": "MongoDB", "topic": "Basics", "question": "What is the MongoDB equivalent of a relational database table?", "options": ["Collection", "Document", "Field", "Index"], "correct_answer": "Collection", "explanation": "A collection groups documents, similar to how a table groups rows."},
        {"id": "mongodb_003", "skill": "MongoDB", "topic": "Basics", "question": "What is a document in MongoDB?", "options": ["A database password", "A group of databases", "A record containing field-value pairs", "A query execution plan"], "correct_answer": "A record containing field-value pairs", "explanation": "A document stores related data as fields and values."},
        {"id": "mongodb_004", "skill": "MongoDB", "topic": "BSON", "question": "What does BSON stand for?", "options": ["Basic Stored Object Names", "Binary JSON", "Business Standard Object Notation", "Binary SQL Object Network"], "correct_answer": "Binary JSON", "explanation": "BSON is a binary-encoded serialization format used by MongoDB."},
        {"id": "mongodb_005", "skill": "MongoDB", "topic": "CRUD", "question": "Which method retrieves documents from a collection?", "options": ["find()", "selectAll()", "fetchRows()", "readTable()"], "correct_answer": "find()", "explanation": "find() returns documents matching a query filter."},
        {"id": "mongodb_006", "skill": "MongoDB", "topic": "CRUD", "question": "Which method retrieves only the first matching document?", "options": ["findAll()", "findOne()", "firstRow()", "getEvery()"], "correct_answer": "findOne()", "explanation": "findOne() returns one matching document or null if none matches."},
        {"id": "mongodb_007", "skill": "MongoDB", "topic": "CRUD", "question": "Which method inserts one document?", "options": ["addRow()", "createRecord()", "insertOne()", "pushTable()"], "correct_answer": "insertOne()", "explanation": "insertOne() adds a single document to a collection."},
        {"id": "mongodb_008", "skill": "MongoDB", "topic": "CRUD", "question": "Which method inserts multiple documents in one operation?", "options": ["insertMany()", "insertBatchOnly()", "addManyRows()", "createCollection()"], "correct_answer": "insertMany()", "explanation": "insertMany() inserts an array of documents."},
        {"id": "mongodb_009", "skill": "MongoDB", "topic": "CRUD", "question": "Which method updates one matching document?", "options": ["changeOne()", "editDocument()", "updateOne()", "replaceAll()"], "correct_answer": "updateOne()", "explanation": "updateOne() modifies the first document matching the filter."},
        {"id": "mongodb_010", "skill": "MongoDB", "topic": "CRUD", "question": "Which method deletes multiple documents matching a filter?", "options": ["removeDatabase()", "deleteMany()", "dropFields()", "eraseAllTables()"], "correct_answer": "deleteMany()", "explanation": "deleteMany() removes all documents matching the supplied filter."},
        {"id": "mongodb_011", "skill": "MongoDB", "topic": "Query Operators", "question": "Which operator selects documents where a field is greater than a value?", "options": ["$lt", "$eq", "$gt", "$ne"], "correct_answer": "$gt", "explanation": "$gt means greater than."},
        {"id": "mongodb_012", "skill": "MongoDB", "topic": "Query Operators", "question": "Which operator checks whether a field's value is in a specified list?", "options": ["$inside", "$in", "$matchlist", "$contains"], "correct_answer": "$in", "explanation": "$in matches a field against any value in the supplied array."},
        {"id": "mongodb_013", "skill": "MongoDB", "topic": "Query Operators", "question": "Which operator matches documents where a field exists?", "options": ["$present", "$available", "$exists", "$field"], "correct_answer": "$exists", "explanation": "$exists tests whether a document contains the specified field."},
        {"id": "mongodb_014", "skill": "MongoDB", "topic": "Query Operators", "question": "Which operator matches values that are not equal to a specified value?", "options": ["$same", "$neqonly", "$ne", "$different"], "correct_answer": "$ne", "explanation": "$ne matches values not equal to the specified value, including documents where the field is missing."},
        {"id": "mongodb_015", "skill": "MongoDB", "topic": "Query Operators", "question": "Which operator can match documents containing an array element that satisfies a condition?", "options": ["$elemMatch", "$arrayOnly", "$eachRow", "$elementFind"], "correct_answer": "$elemMatch", "explanation": "$elemMatch matches an array when at least one element satisfies the specified criteria."},
        {"id": "mongodb_016", "skill": "MongoDB", "topic": "Updates", "question": "Which update operator changes the value of a field?", "options": ["$renameAll", "$set", "$change", "$modify"], "correct_answer": "$set", "explanation": "$set assigns a value to a field, creating it if necessary."},
        {"id": "mongodb_017", "skill": "MongoDB", "topic": "Updates", "question": "Which operator increases a numeric field by a specified amount?", "options": ["$push", "$multiplyOnly", "$inc", "$append"], "correct_answer": "$inc", "explanation": "$inc increments a numeric field by the specified amount."},
        {"id": "mongodb_018", "skill": "MongoDB", "topic": "Updates", "question": "Which operator adds an item to an array field?", "options": ["$push", "$set", "$rename", "$unset"], "correct_answer": "$push", "explanation": "$push adds an item to an array, creating the array if needed."},
        {"id": "mongodb_019", "skill": "MongoDB", "topic": "Updates", "question": "Which operator removes a field from a document?", "options": ["$deleteField", "$unset", "$drop", "$removeKey"], "correct_answer": "$unset", "explanation": "$unset removes the specified field from a document."},
        {"id": "mongodb_020", "skill": "MongoDB", "topic": "Updates", "question": "What does the upsert option do in an update operation?", "options": ["Always deletes a document", "Creates a document if no match is found", "Prevents every update", "Converts a collection into a database"], "correct_answer": "Creates a document if no match is found", "explanation": "With upsert enabled, MongoDB inserts a document if no document matches the filter."},
        {"id": "mongodb_021", "skill": "MongoDB", "topic": "Projection", "question": "What is projection used for in a find query?", "options": ["Selecting which fields to return", "Deleting a collection", "Creating a user", "Backing up the server"], "correct_answer": "Selecting which fields to return", "explanation": "Projection includes or excludes fields in returned documents."},
        {"id": "mongodb_022", "skill": "MongoDB", "topic": "Sorting", "question": "In a MongoDB sort specification, what does a value of -1 mean?", "options": ["Random order", "Ascending order", "Descending order", "Skip the field"], "correct_answer": "Descending order", "explanation": "A sort value of -1 specifies descending order; 1 specifies ascending order."},
        {"id": "mongodb_023", "skill": "MongoDB", "topic": "Pagination", "question": "What does skip(20) do in a cursor query?", "options": ["Deletes 20 documents", "Skips the first 20 matching results", "Returns exactly 20 results", "Skips all documents with NULL values"], "correct_answer": "Skips the first 20 matching results", "explanation": "skip() omits the specified number of results before returning the remaining cursor results."},
        {"id": "mongodb_024", "skill": "MongoDB", "topic": "Pagination", "question": "What does limit(5) do?", "options": ["Returns at most five results", "Deletes five results", "Creates five collections", "Skips five results"], "correct_answer": "Returns at most five results", "explanation": "limit() caps the number of documents returned by a query."},
        {"id": "mongodb_025", "skill": "MongoDB", "topic": "Aggregation", "question": "Which method runs an aggregation pipeline?", "options": ["aggregate()", "groupRows()", "pipelineRunOnly()", "calculateTable()"], "correct_answer": "aggregate()", "explanation": "aggregate() processes documents through a sequence of pipeline stages."},
        {"id": "mongodb_026", "skill": "MongoDB", "topic": "Aggregation", "question": "Which pipeline stage filters documents?", "options": ["$sort", "$project", "$match", "$limitOnly"], "correct_answer": "$match", "explanation": "$match selects documents that satisfy its query condition."},
        {"id": "mongodb_027", "skill": "MongoDB", "topic": "Aggregation", "question": "Which aggregation stage sorts documents?", "options": ["$order", "$sort", "$arrange", "$sequence"], "correct_answer": "$sort", "explanation": "$sort orders pipeline documents by specified fields."},
        {"id": "mongodb_028", "skill": "MongoDB", "topic": "Aggregation", "question": "Which stage groups documents by a specified expression?", "options": ["$bucketOnly", "$collect", "$group", "$combineRows"], "correct_answer": "$group", "explanation": "$group groups documents and can calculate values using accumulators."},
        {"id": "mongodb_029", "skill": "MongoDB", "topic": "Aggregation", "question": "Which stage reshapes documents by selecting or computing fields?", "options": ["$project", "$match", "$delete", "$connect"], "correct_answer": "$project", "explanation": "$project controls included, excluded, and computed output fields."},
        {"id": "mongodb_030", "skill": "MongoDB", "topic": "Aggregation", "question": "Which accumulator calculates the sum of values in a group?", "options": ["$total", "$sum", "$addAllRows", "$countSum"], "correct_answer": "$sum", "explanation": "$sum adds numeric values in an aggregation expression."},
        {"id": "mongodb_031", "skill": "MongoDB", "topic": "Indexes", "question": "What is a common benefit of an index?", "options": ["It can speed up suitable queries", "It guarantees every query is faster", "It removes the need for backups", "It automatically validates every business rule"], "correct_answer": "It can speed up suitable queries", "explanation": "Indexes can improve query performance but consume storage and add write overhead."},
        {"id": "mongodb_032", "skill": "MongoDB", "topic": "Indexes", "question": "Which method creates an index on a collection?", "options": ["makeIndex()", "createIndex()", "addSearchKey()", "indexCollectionOnly()"], "correct_answer": "createIndex()", "explanation": "createIndex() creates an index using the specified field specification."},
        {"id": "mongodb_033", "skill": "MongoDB", "topic": "Indexes", "question": "What does a unique index enforce?", "options": ["Documents must have identical values", "Indexed key values cannot be duplicated under the index rules", "Every query returns one document", "The collection becomes read-only"], "correct_answer": "Indexed key values cannot be duplicated under the index rules", "explanation": "A unique index rejects duplicate indexed key values, subject to index options and missing or null value behavior."},
        {"id": "mongodb_034", "skill": "MongoDB", "topic": "Relationships", "question": "What is embedding in MongoDB data modeling?", "options": ["Placing related data inside the same document", "Encrypting a collection", "Splitting one database across servers", "Creating an index for every field"], "correct_answer": "Placing related data inside the same document", "explanation": "Embedding stores related information in nested fields or arrays within a document."},
        {"id": "mongodb_035", "skill": "MongoDB", "topic": "Relationships", "question": "When may referencing be preferable to embedding?", "options": ["When related data is large or independently shared", "When the entire application has one field", "When indexes are forbidden", "When documents cannot contain fields"], "correct_answer": "When related data is large or independently shared", "explanation": "References can reduce duplication and suit independently managed or large related records."},
        {"id": "mongodb_036", "skill": "MongoDB", "topic": "Replication", "question": "What is the main purpose of a replica set?", "options": ["Provide redundancy and high availability", "Convert documents into SQL tables", "Replace all indexes", "Prevent all network failures"], "correct_answer": "Provide redundancy and high availability", "explanation": "A replica set maintains multiple copies of data and can elect a primary if needed."},
        {"id": "mongodb_037", "skill": "MongoDB", "topic": "Sharding", "question": "What is sharding used for?", "options": ["Distributing data across multiple machines", "Combining every document into one file", "Removing the primary key", "Running only local queries"], "correct_answer": "Distributing data across multiple machines", "explanation": "Sharding distributes data to support horizontal scaling."},
        {"id": "mongodb_038", "skill": "MongoDB", "topic": "Transactions", "question": "Can MongoDB support multi-document transactions?", "options": ["No, never", "Yes, on supported deployments and storage configurations", "Only for text fields", "Only in read-only collections"], "correct_answer": "Yes, on supported deployments and storage configurations", "explanation": "MongoDB supports transactions across multiple documents on supported replica set and sharded cluster deployments."},
        {"id": "mongodb_039", "skill": "MongoDB", "topic": "Security", "question": "Which practice helps protect a MongoDB deployment?", "options": ["Expose the server publicly without authentication", "Use authentication and least-privilege access", "Store passwords in plain text", "Disable all access controls"], "correct_answer": "Use authentication and least-privilege access", "explanation": "Authentication, appropriate authorization, and restricted network access reduce security risks."},
        {"id": "mongodb_040", "skill": "MongoDB", "topic": "Application Development", "question": "What is the role of a MongoDB driver in an application?", "options": ["Connects application code to MongoDB and performs database operations", "Designs the user interface automatically", "Replaces the operating system", "Compiles all database documents into HTML"], "correct_answer": "Connects application code to MongoDB and performs database operations", "explanation": "MongoDB drivers let application code connect to the database and run supported operations."}
    ],
    
    "data structures and algorithms": [
        {"id": "dsa_001", "skill": "Data Structures and Algorithms", "topic": "Arrays", "question": "What is the typical time complexity of accessing an array element by index?", "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"], "correct_answer": "O(1)", "explanation": "An array element can be accessed directly using its index."},
        {"id": "dsa_002", "skill": "Data Structures and Algorithms", "topic": "Arrays", "question": "What is the time complexity of searching for a value in an unsorted array?", "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "correct_answer": "O(n)", "explanation": "In the worst case, every element must be checked."},
        {"id": "dsa_003", "skill": "Data Structures and Algorithms", "topic": "Arrays", "question": "Which operation usually requires shifting elements in a contiguous array?", "options": ["Reading an element", "Inserting into the middle", "Accessing the first element", "Checking the array length"], "correct_answer": "Inserting into the middle", "explanation": "Elements after the insertion point may need to move."},
        {"id": "dsa_004", "skill": "Data Structures and Algorithms", "topic": "Linked Lists", "question": "What does a node in a singly linked list typically contain?", "options": ["Only an index", "Data and a link to the next node", "Only two child nodes", "A fixed array of all nodes"], "correct_answer": "Data and a link to the next node", "explanation": "A singly linked-list node stores its value and a reference to the next node."},
        {"id": "dsa_005", "skill": "Data Structures and Algorithms", "topic": "Linked Lists", "question": "What is the time complexity of accessing the nth element of a singly linked list by position?", "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "correct_answer": "O(n)", "explanation": "The list generally must be traversed from its beginning."},
        {"id": "dsa_006", "skill": "Data Structures and Algorithms", "topic": "Linked Lists", "question": "What is a key advantage of inserting a node after a known node in a singly linked list?", "options": ["It always sorts the list", "It can take O(1) time", "It requires binary search", "It always takes O(n²) time"], "correct_answer": "It can take O(1) time", "explanation": "Only a few links need updating when the insertion position is already known."},
        {"id": "dsa_007", "skill": "Data Structures and Algorithms", "topic": "Stacks", "question": "Which principle does a stack follow?", "options": ["FIFO", "LIFO", "Random access only", "Priority first"], "correct_answer": "LIFO", "explanation": "Last In, First Out means the most recently added item is removed first."},
        {"id": "dsa_008", "skill": "Data Structures and Algorithms", "topic": "Stacks", "question": "Which stack operation removes the top element?", "options": ["Push", "Peek", "Pop", "Search"], "correct_answer": "Pop", "explanation": "Pop removes and returns the top item of a stack."},
        {"id": "dsa_009", "skill": "Data Structures and Algorithms", "topic": "Stacks", "question": "Which data structure is commonly used to check balanced parentheses?", "options": ["Stack", "Graph", "Heap only", "Hash function"], "correct_answer": "Stack", "explanation": "A stack tracks opening brackets so matching closing brackets can be checked."},
        {"id": "dsa_010", "skill": "Data Structures and Algorithms", "topic": "Queues", "question": "Which principle does a standard queue follow?", "options": ["LIFO", "FIFO", "Highest value first", "Random removal"], "correct_answer": "FIFO", "explanation": "First In, First Out means the earliest inserted item leaves first."},
        {"id": "dsa_011", "skill": "Data Structures and Algorithms", "topic": "Queues", "question": "Where is an element normally inserted in a queue?", "options": ["At the front", "At the rear", "At every position", "At the middle only"], "correct_answer": "At the rear", "explanation": "Enqueue adds an item at the rear of a standard queue."},
        {"id": "dsa_012", "skill": "Data Structures and Algorithms", "topic": "Queues", "question": "What is the main purpose of a circular queue?", "options": ["To sort items automatically", "To reuse available positions in a fixed-size array", "To eliminate FIFO ordering", "To store only graph edges"], "correct_answer": "To reuse available positions in a fixed-size array", "explanation": "Circular indexing allows freed positions to be reused."},
        {"id": "dsa_013", "skill": "Data Structures and Algorithms", "topic": "Hashing", "question": "What is the purpose of a hash function in a hash table?", "options": ["To map a key to a table index or hash value", "To sort every key alphabetically", "To create a linked list automatically", "To encrypt all stored values"], "correct_answer": "To map a key to a table index or hash value", "explanation": "Hashing helps locate where a key's entry should be stored."},
        {"id": "dsa_014", "skill": "Data Structures and Algorithms", "topic": "Hashing", "question": "What is a hash collision?", "options": ["Deleting a hash table", "Two different keys mapping to the same hash location", "Finding a key in one step", "Sorting keys by value"], "correct_answer": "Two different keys mapping to the same hash location", "explanation": "Different keys can produce the same table index."},
        {"id": "dsa_015", "skill": "Data Structures and Algorithms", "topic": "Hashing", "question": "Which technique handles collisions by storing multiple entries in a bucket, often using a linked list?", "options": ["Binary search", "Separate chaining", "Merge sort", "Tree rotation"], "correct_answer": "Separate chaining", "explanation": "Separate chaining stores colliding entries together in a bucket."},
        {"id": "dsa_016", "skill": "Data Structures and Algorithms", "topic": "Searching", "question": "What is required for ordinary binary search to work correctly on an array?", "options": ["The array must be sorted", "The array must contain duplicates", "The array must have an even length", "The array must contain only negative values"], "correct_answer": "The array must be sorted", "explanation": "Binary search uses the sorted order to discard half of the remaining search range."},
        {"id": "dsa_017", "skill": "Data Structures and Algorithms", "topic": "Searching", "question": "What is the worst-case time complexity of binary search on a sorted array?", "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"], "correct_answer": "O(log n)", "explanation": "Each comparison approximately halves the remaining search interval."},
        {"id": "dsa_018", "skill": "Data Structures and Algorithms", "topic": "Searching", "question": "Which search method is suitable for a small unsorted collection?", "options": ["Linear search", "Binary search without sorting", "Binary tree rotation", "Heap construction only"], "correct_answer": "Linear search", "explanation": "Linear search checks elements one by one without requiring sorted data."},
        {"id": "dsa_019", "skill": "Data Structures and Algorithms", "topic": "Sorting", "question": "Which sorting algorithm repeatedly compares adjacent elements and swaps them when needed?", "options": ["Merge sort", "Bubble sort", "Counting sort", "Radix sort"], "correct_answer": "Bubble sort", "explanation": "Bubble sort compares adjacent items and swaps out-of-order pairs."},
        {"id": "dsa_020", "skill": "Data Structures and Algorithms", "topic": "Sorting", "question": "What is merge sort's typical time complexity in the worst case?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(n²)"], "correct_answer": "O(n log n)", "explanation": "Merge sort divides the input and merges sorted parts in O(n log n) time."},
        {"id": "dsa_021", "skill": "Data Structures and Algorithms", "topic": "Sorting", "question": "Which sorting algorithm often performs well on small or nearly sorted arrays?", "options": ["Insertion sort", "Bogosort", "Selection sort in every case", "Linear search"], "correct_answer": "Insertion sort", "explanation": "Insertion sort has low overhead and performs well on nearly sorted data."},
        {"id": "dsa_022", "skill": "Data Structures and Algorithms", "topic": "Sorting", "question": "What is the worst-case time complexity of standard quicksort?", "options": ["O(log n)", "O(n)", "O(n log n)", "O(n²)"], "correct_answer": "O(n²)", "explanation": "Repeatedly choosing very poor pivots can produce highly unbalanced partitions."},
        {"id": "dsa_023", "skill": "Data Structures and Algorithms", "topic": "Recursion", "question": "What prevents a recursive function from calling itself forever?", "options": ["A base case", "A larger input", "A global variable only", "An extra loop"], "correct_answer": "A base case", "explanation": "The base case stops further recursive calls when the stopping condition is reached."},
        {"id": "dsa_024", "skill": "Data Structures and Algorithms", "topic": "Recursion", "question": "What is a common risk of excessively deep recursion?", "options": ["Stack overflow", "Automatic sorting", "Guaranteed constant memory use", "Database deadlock"], "correct_answer": "Stack overflow", "explanation": "Too many active function calls can exceed the available call stack."},
        {"id": "dsa_025", "skill": "Data Structures and Algorithms", "topic": "Trees", "question": "In a binary tree, what is the maximum number of children a node can have?", "options": ["One", "Two", "Three", "Unlimited"], "correct_answer": "Two", "explanation": "A binary tree node has at most a left child and a right child."},
        {"id": "dsa_026", "skill": "Data Structures and Algorithms", "topic": "Trees", "question": "In a binary search tree, where are smaller keys conventionally placed?", "options": ["In the left subtree", "Only in the root", "In the right subtree", "Outside the tree"], "correct_answer": "In the left subtree", "explanation": "The standard BST ordering places smaller keys to the left and larger keys to the right, subject to its duplicate-key policy."},
        {"id": "dsa_027", "skill": "Data Structures and Algorithms", "topic": "Trees", "question": "Which traversal visits the root before its left and right subtrees?", "options": ["Inorder", "Postorder", "Preorder", "Level order only"], "correct_answer": "Preorder", "explanation": "Preorder traversal follows root, left subtree, then right subtree."},
        {"id": "dsa_028", "skill": "Data Structures and Algorithms", "topic": "Trees", "question": "Which traversal of a binary search tree returns keys in sorted order when the BST ordering is valid?", "options": ["Preorder", "Inorder", "Postorder", "Reverse level order only"], "correct_answer": "Inorder", "explanation": "Inorder visits the left subtree, root, and right subtree."},
        {"id": "dsa_029", "skill": "Data Structures and Algorithms", "topic": "Heaps", "question": "In a max-heap, which value is stored at the root?", "options": ["The smallest value", "The largest value", "Always zero", "The most recently inserted value"], "correct_answer": "The largest value", "explanation": "A max-heap maintains each parent value greater than or equal to its children."},
        {"id": "dsa_030", "skill": "Data Structures and Algorithms", "topic": "Heaps", "question": "Which data structure is commonly used to implement a priority queue?", "options": ["Heap", "Unsorted text file", "Stack only", "Hash function alone"], "correct_answer": "Heap", "explanation": "A heap efficiently supports accessing and removing a highest- or lowest-priority item."},
        {"id": "dsa_031", "skill": "Data Structures and Algorithms", "topic": "Graphs", "question": "What does a vertex represent in a graph?", "options": ["A node", "A sorting operation", "A recursion limit", "A hash collision"], "correct_answer": "A node", "explanation": "Vertices are the nodes of a graph; edges represent connections between them."},
        {"id": "dsa_032", "skill": "Data Structures and Algorithms", "topic": "Graphs", "question": "Which algorithm explores a graph level by level using a queue?", "options": ["Depth-first search", "Breadth-first search", "Quicksort", "Binary search"], "correct_answer": "Breadth-first search", "explanation": "BFS uses a queue to explore neighboring vertices before moving farther away."},
        {"id": "dsa_033", "skill": "Data Structures and Algorithms", "topic": "Graphs", "question": "Which data structure is commonly used to implement iterative depth-first search?", "options": ["Stack", "Queue only", "Priority table only", "Circular array only"], "correct_answer": "Stack", "explanation": "A stack supports the last-in-first-out exploration used by iterative DFS."},
        {"id": "dsa_034", "skill": "Data Structures and Algorithms", "topic": "Graphs", "question": "Which algorithm finds shortest paths from a source in a graph with non-negative edge weights?", "options": ["Dijkstra's algorithm", "Bubble sort", "Binary search", "Kruskal's algorithm in all cases"], "correct_answer": "Dijkstra's algorithm", "explanation": "Dijkstra's algorithm computes shortest paths when edge weights are non-negative."},
        {"id": "dsa_035", "skill": "Data Structures and Algorithms", "topic": "Dynamic Programming", "question": "What is the main idea of dynamic programming?", "options": ["Solve overlapping subproblems and reuse their results", "Repeat every calculation without storing results", "Always use recursion without a base case", "Sort every input first"], "correct_answer": "Solve overlapping subproblems and reuse their results", "explanation": "Dynamic programming stores subproblem results to avoid repeated computation."},
        {"id": "dsa_036", "skill": "Data Structures and Algorithms", "topic": "Greedy Algorithms", "question": "How does a greedy algorithm typically make decisions?", "options": ["It chooses a locally best available option at each step", "It checks every possible complete solution in all cases", "It always reverses its previous choice", "It randomly selects every result"], "correct_answer": "It chooses a locally best available option at each step", "explanation": "Greedy algorithms make locally optimal choices and work correctly for problems with suitable properties."},
        {"id": "dsa_037", "skill": "Data Structures and Algorithms", "topic": "Complexity", "question": "What does O(1) time complexity mean?", "options": ["Execution time grows linearly with input", "Execution time is bounded independently of input size", "Execution time doubles with every item", "The algorithm never terminates"], "correct_answer": "Execution time is bounded independently of input size", "explanation": "Constant time does not grow with the size of the input under the stated operation model."},
        {"id": "dsa_038", "skill": "Data Structures and Algorithms", "topic": "Complexity", "question": "Which complexity grows fastest for sufficiently large n among these choices?", "options": ["O(log n)", "O(n)", "O(n log n)", "O(n²)"], "correct_answer": "O(n²)", "explanation": "Quadratic growth eventually exceeds logarithmic, linear, and linearithmic growth."},
        {"id": "dsa_039", "skill": "Data Structures and Algorithms", "topic": "Algorithm Design", "question": "What is the divide-and-conquer approach?", "options": ["Break a problem into smaller subproblems, solve them, and combine results", "Store all data in one variable", "Use only loops and never functions", "Remove the input before processing"], "correct_answer": "Break a problem into smaller subproblems, solve them, and combine results", "explanation": "Divide and conquer divides the problem, solves smaller instances, and combines their solutions."},
        {"id": "dsa_040", "skill": "Data Structures and Algorithms", "topic": "Algorithm Design", "question": "What is a stable sorting algorithm?", "options": ["One that never uses memory", "One that preserves the relative order of equal-key elements", "One that only sorts integers", "One that always runs in O(1)"], "correct_answer": "One that preserves the relative order of equal-key elements", "explanation": "Stability keeps equal-key elements in their original relative order."}
    ],

    "object-oriented programming": [
        {"id": "oop_001", "skill": "Object-Oriented Programming", "topic": "Classes and Objects", "question": "What is a class in object-oriented programming?", "options": ["A blueprint for creating objects", "A running database server", "A loop condition", "A network protocol"], "correct_answer": "A blueprint for creating objects", "explanation": "A class defines the attributes and behavior that its objects can have."},
        {"id": "oop_002", "skill": "Object-Oriented Programming", "topic": "Classes and Objects", "question": "What is an object?", "options": ["An instance of a class", "A function parameter only", "A compiler error", "A source-code comment"], "correct_answer": "An instance of a class", "explanation": "An object is a concrete instance created from a class."},
        {"id": "oop_003", "skill": "Object-Oriented Programming", "topic": "Encapsulation", "question": "What is encapsulation?", "options": ["Combining data and related methods while controlling access", "Copying every class into one file", "Running two programs simultaneously", "Sorting object names"], "correct_answer": "Combining data and related methods while controlling access", "explanation": "Encapsulation groups state and behavior and controls how internal state is accessed."},
        {"id": "oop_004", "skill": "Object-Oriented Programming", "topic": "Abstraction", "question": "What does abstraction primarily do?", "options": ["Expose essential behavior while hiding unnecessary implementation details", "Make every field public", "Prevent all methods from running", "Duplicate every object"], "correct_answer": "Expose essential behavior while hiding unnecessary implementation details", "explanation": "Abstraction focuses on what an object does rather than all the details of how it works."},
        {"id": "oop_005", "skill": "Object-Oriented Programming", "topic": "Inheritance", "question": "What is inheritance used for?", "options": ["Creating a class based on another class", "Removing every method from a class", "Converting source code to SQL", "Creating a network connection"], "correct_answer": "Creating a class based on another class", "explanation": "Inheritance allows a derived class to reuse or specialize behavior from a base class."},
        {"id": "oop_006", "skill": "Object-Oriented Programming", "topic": "Polymorphism", "question": "What does polymorphism allow?", "options": ["Different object types to provide behavior through a common interface", "Only one object to exist in a program", "All variables to have the same value", "Methods to contain no code"], "correct_answer": "Different object types to provide behavior through a common interface", "explanation": "Polymorphism lets code work with different implementations through a shared type or interface."},
        {"id": "oop_007", "skill": "Object-Oriented Programming", "topic": "Constructors", "question": "What is a constructor commonly used for?", "options": ["Initializing a new object's state", "Deleting the source file", "Sorting all class names", "Stopping the operating system"], "correct_answer": "Initializing a new object's state", "explanation": "A constructor establishes an object's initial state when it is created."},
        {"id": "oop_008", "skill": "Object-Oriented Programming", "topic": "Methods", "question": "What is a method?", "options": ["A function associated with a class or object", "A database table only", "A network cable", "A programming language keyword for comments"], "correct_answer": "A function associated with a class or object", "explanation": "Methods define behavior associated with a class or its instances."},
        {"id": "oop_009", "skill": "Object-Oriented Programming", "topic": "Access Modifiers", "question": "What is the purpose of access modifiers?", "options": ["Control visibility or accessibility of class members", "Increase screen brightness", "Sort methods alphabetically at runtime", "Create database backups"], "correct_answer": "Control visibility or accessibility of class members", "explanation": "Access modifiers restrict which code can access fields, methods, or types."},
        {"id": "oop_010", "skill": "Object-Oriented Programming", "topic": "Access Modifiers", "question": "In Java, which access level allows access from anywhere?", "options": ["private", "protected only", "public", "package-private only"], "correct_answer": "public", "explanation": "Public members are accessible wherever their containing type is accessible."},
        {"id": "oop_011", "skill": "Object-Oriented Programming", "topic": "Method Overloading", "question": "What is method overloading?", "options": ["Defining methods with the same name but different parameter lists", "Deleting a method during execution", "Giving every method the same parameters and return type", "Creating objects without classes"], "correct_answer": "Defining methods with the same name but different parameter lists", "explanation": "Overloaded methods share a name but differ in their parameter signatures."},
        {"id": "oop_012", "skill": "Object-Oriented Programming", "topic": "Method Overriding", "question": "What is method overriding?", "options": ["A subclass providing its own implementation of an inherited method", "Creating a variable with no value", "Changing a comment into code", "Calling a constructor twice by definition"], "correct_answer": "A subclass providing its own implementation of an inherited method", "explanation": "Overriding specializes an inherited method's behavior in a subclass."},
        {"id": "oop_013", "skill": "Object-Oriented Programming", "topic": "Polymorphism", "question": "Which concept allows an overridden method to be selected according to an object's runtime type?", "options": ["Dynamic dispatch", "Static variable allocation only", "Lexical sorting", "Database normalization"], "correct_answer": "Dynamic dispatch", "explanation": "Dynamic dispatch selects the appropriate overridden implementation at runtime."},
        {"id": "oop_014", "skill": "Object-Oriented Programming", "topic": "Interfaces", "question": "What is a common purpose of an interface?", "options": ["Define a contract that implementing types must follow", "Store only image files", "Replace every object with a string", "Disable polymorphism"], "correct_answer": "Define a contract that implementing types must follow", "explanation": "An interface specifies operations that implementing types agree to provide."},
        {"id": "oop_015", "skill": "Object-Oriented Programming", "topic": "Abstract Classes", "question": "Which statement about an abstract class is generally correct?", "options": ["It can provide shared implementation and abstract methods", "It can never contain methods", "It must always be instantiated directly", "It cannot be extended"], "correct_answer": "It can provide shared implementation and abstract methods", "explanation": "Abstract classes can combine implemented behavior with methods that subclasses must implement."},
        {"id": "oop_016", "skill": "Object-Oriented Programming", "topic": "Relationships", "question": "What does composition represent?", "options": ["A strong whole-part relationship between objects", "A sorting algorithm", "A type of network address", "A variable without a type"], "correct_answer": "A strong whole-part relationship between objects", "explanation": "Composition models a whole object containing parts whose lifecycles are commonly tied to the whole."},
        {"id": "oop_017", "skill": "Object-Oriented Programming", "topic": "Relationships", "question": "What does aggregation represent in object modeling?", "options": ["A whole-part relationship where parts can exist independently", "A requirement that all objects be deleted together", "A method with two return values", "A type of loop"], "correct_answer": "A whole-part relationship where parts can exist independently", "explanation": "Aggregation models a weaker ownership relationship than composition."},
        {"id": "oop_018", "skill": "Object-Oriented Programming", "topic": "Relationships", "question": "What does association describe?", "options": ["A relationship between objects or classes", "A compilation error", "An array's index", "A class with no fields by definition"], "correct_answer": "A relationship between objects or classes", "explanation": "Association represents a connection between objects or types."},
        {"id": "oop_019", "skill": "Object-Oriented Programming", "topic": "Constructors", "question": "What is constructor overloading?", "options": ["Providing multiple constructors with different parameter lists", "Calling a method from a database", "Removing all constructors", "Overriding a private variable"], "correct_answer": "Providing multiple constructors with different parameter lists", "explanation": "Constructor overloading offers different ways to initialize objects."},
        {"id": "oop_020", "skill": "Object-Oriented Programming", "topic": "Static Members", "question": "What does a static field commonly represent?", "options": ["State shared at the class level", "A separate copy required for every instance", "A temporary network packet", "A field that can never be read"], "correct_answer": "State shared at the class level", "explanation": "A static field belongs to the class rather than to each individual instance."},
        {"id": "oop_021", "skill": "Object-Oriented Programming", "topic": "Static Members", "question": "Which statement about a static method in Java is correct?", "options": ["It can directly use instance fields without an object", "It belongs to the class and cannot directly access instance members without an instance", "It must be a constructor", "It cannot accept parameters"], "correct_answer": "It belongs to the class and cannot directly access instance members without an instance", "explanation": "A static method has no implicit current object, so instance members require an object reference."},
        {"id": "oop_022", "skill": "Object-Oriented Programming", "topic": "Immutability", "question": "What is an immutable object?", "options": ["An object whose state cannot be changed after construction", "An object that must be deleted immediately", "An object with no methods of any kind", "An object that is always stored in a database"], "correct_answer": "An object whose state cannot be changed after construction", "explanation": "An immutable object does not allow its observable state to change after creation."},
        {"id": "oop_023", "skill": "Object-Oriented Programming", "topic": "Equality", "question": "Why can object identity differ from object equality?", "options": ["Two separate objects may represent equal values", "Objects never have values", "Identity always compares strings only", "Equality is only possible for numbers"], "correct_answer": "Two separate objects may represent equal values", "explanation": "Identity concerns whether references point to the same object; equality concerns whether values are considered equivalent."},
        {"id": "oop_024", "skill": "Object-Oriented Programming", "topic": "Composition", "question": "Which design generally reduces tight coupling?", "options": ["Depend on a clear interface rather than a concrete implementation", "Let every class modify every other class's private fields", "Put all logic in one global method", "Duplicate every class in every module"], "correct_answer": "Depend on a clear interface rather than a concrete implementation", "explanation": "Programming to abstractions makes components easier to replace and test."},
        {"id": "oop_025", "skill": "Object-Oriented Programming", "topic": "SOLID Principles", "question": "What does the Single Responsibility Principle recommend?", "options": ["A class should have one main reason to change", "A class must have exactly one method", "Every class must inherit from two classes", "All code must be in one file"], "correct_answer": "A class should have one main reason to change", "explanation": "The principle encourages each class to have one cohesive responsibility."},
        {"id": "oop_026", "skill": "Object-Oriented Programming", "topic": "SOLID Principles", "question": "What does the Open/Closed Principle state?", "options": ["Software entities should be open for extension but closed for modification", "Every class must be closed to all use", "Programs should never be extended", "Every method must be public"], "correct_answer": "Software entities should be open for extension but closed for modification", "explanation": "Well-designed components allow new behavior without repeatedly changing stable existing code."},
        {"id": "oop_027", "skill": "Object-Oriented Programming", "topic": "SOLID Principles", "question": "What does the Liskov Substitution Principle require?", "options": ["Subtypes should be usable wherever their base types are expected without breaking correctness", "Every subclass must have more fields", "Base classes cannot have methods", "All objects must be immutable"], "correct_answer": "Subtypes should be usable wherever their base types are expected without breaking correctness", "explanation": "Subtypes should preserve the behavioral expectations of their base types."},
        {"id": "oop_028", "skill": "Object-Oriented Programming", "topic": "SOLID Principles", "question": "What does the Interface Segregation Principle recommend?", "options": ["Clients should not be forced to depend on methods they do not use", "All methods should be placed in one huge interface", "Interfaces should never contain operations", "Every class should have a private interface"], "correct_answer": "Clients should not be forced to depend on methods they do not use", "explanation": "Smaller, focused interfaces avoid unnecessary dependencies."},
        {"id": "oop_029", "skill": "Object-Oriented Programming", "topic": "SOLID Principles", "question": "What does the Dependency Inversion Principle encourage?", "options": ["High-level modules and low-level modules depending on abstractions", "All modules depending directly on one concrete class", "Removing all interfaces", "Replacing every method with a global variable"], "correct_answer": "High-level modules and low-level modules depending on abstractions", "explanation": "Abstractions help separate policy from implementation details."},
        {"id": "oop_030", "skill": "Object-Oriented Programming", "topic": "Design Patterns", "question": "What is the main purpose of the Factory design pattern?", "options": ["Encapsulate object creation", "Sort arrays in place", "Encrypt network traffic", "Normalize database tables"], "correct_answer": "Encapsulate object creation", "explanation": "Factory patterns centralize or abstract the process of creating objects."},
        {"id": "oop_031", "skill": "Object-Oriented Programming", "topic": "Design Patterns", "question": "What is the Singleton pattern intended to ensure?", "options": ["A class has one managed instance and a shared access point", "Every class has unlimited instances", "All methods are recursive", "Every object belongs to a different database"], "correct_answer": "A class has one managed instance and a shared access point", "explanation": "Singleton controls instance creation, although it should be used carefully because it can introduce global state."},
        {"id": "oop_032", "skill": "Object-Oriented Programming", "topic": "Design Patterns", "question": "Which pattern allows behavior to be selected or changed by composing interchangeable algorithms?", "options": ["Strategy", "Singleton", "Builder only", "Prototype only"], "correct_answer": "Strategy", "explanation": "The Strategy pattern encapsulates interchangeable algorithms behind a common interface."},
        {"id": "oop_033", "skill": "Object-Oriented Programming", "topic": "Exception Handling", "question": "Why is exception handling used in object-oriented applications?", "options": ["To manage exceptional conditions and failures", "To make every method return zero", "To eliminate all testing", "To prevent objects from being created"], "correct_answer": "To manage exceptional conditions and failures", "explanation": "Exception handling provides structured ways to handle or propagate runtime failures."},
        {"id": "oop_034", "skill": "Object-Oriented Programming", "topic": "Coupling and Cohesion", "question": "What does high cohesion generally indicate?", "options": ["A class's responsibilities are closely related", "A class depends on every other class", "A class contains unrelated features", "A program has no methods"], "correct_answer": "A class's responsibilities are closely related", "explanation": "High cohesion means a module's elements work together toward a focused purpose."},
        {"id": "oop_035", "skill": "Object-Oriented Programming", "topic": "Coupling and Cohesion", "question": "What is a common benefit of low coupling?", "options": ["Components can change with fewer effects on other components", "Every component must share all internal data", "Testing becomes impossible", "Inheritance is always required"], "correct_answer": "Components can change with fewer effects on other components", "explanation": "Low coupling limits dependencies between components and makes maintenance easier."},
        {"id": "oop_036", "skill": "Object-Oriented Programming", "topic": "Composition vs Inheritance", "question": "When is composition often preferred over inheritance?", "options": ["When behavior can be assembled from collaborating objects", "Whenever a class must be a subtype", "When no objects can be created", "Only when methods are private"], "correct_answer": "When behavior can be assembled from collaborating objects", "explanation": "Composition can provide flexible reuse without imposing a rigid inheritance hierarchy."},
        {"id": "oop_037", "skill": "Object-Oriented Programming", "topic": "UML", "question": "In a UML class diagram, what does a class box commonly show?", "options": ["Class name, attributes, and operations", "Only runtime CPU usage", "Only database passwords", "Only network packet contents"], "correct_answer": "Class name, attributes, and operations", "explanation": "A common UML class box has compartments for the name, attributes, and operations."},
        {"id": "oop_038", "skill": "Object-Oriented Programming", "topic": "UML", "question": "In UML, what does a generalization relationship represent?", "options": ["Inheritance between a specialized type and a general type", "A database transaction", "A method call count", "A loop dependency"], "correct_answer": "Inheritance between a specialized type and a general type", "explanation": "Generalization models an inheritance relationship between types."},
        {"id": "oop_039", "skill": "Object-Oriented Programming", "topic": "Testing", "question": "Why are interfaces useful in unit testing?", "options": ["They make it easier to substitute test doubles for dependencies", "They remove the need for assertions", "They guarantee all tests pass", "They prevent methods from being called"], "correct_answer": "They make it easier to substitute test doubles for dependencies", "explanation": "Interfaces help tests replace real services with mocks, stubs, or other test doubles."},
        {"id": "oop_040", "skill": "Object-Oriented Programming", "topic": "Design Principles", "question": "What is the main benefit of keeping object state private and exposing controlled methods?", "options": ["It protects invariants and controls valid state changes", "It guarantees zero memory use", "It removes the need for constructors", "It makes every field globally accessible"], "correct_answer": "It protects invariants and controls valid state changes", "explanation": "Controlled access helps prevent objects from entering invalid states."}
    ],

    "dbms": [
        {"id": "dbms_001", "skill": "DBMS", "topic": "Fundamentals", "question": "What is the main purpose of a Database Management System?", "options": ["Manage data storage, retrieval, and updates", "Only design web pages", "Only compile programming languages", "Replace all operating systems"], "correct_answer": "Manage data storage, retrieval, and updates", "explanation": "A DBMS provides tools to store, organize, retrieve, and manage data."},
        {"id": "dbms_002", "skill": "DBMS", "topic": "Fundamentals", "question": "What is metadata in a database?", "options": ["Data describing the structure or properties of other data", "Only deleted records", "A database password", "A query result containing no rows"], "correct_answer": "Data describing the structure or properties of other data", "explanation": "Metadata includes information such as column types, table definitions, and constraints."},
        {"id": "dbms_003", "skill": "DBMS", "topic": "Database Architecture", "question": "What does data independence mean?", "options": ["Changes at one schema level can be made without requiring certain changes at another level", "Data never changes", "Every user sees every record", "A database needs no storage"], "correct_answer": "Changes at one schema level can be made without requiring certain changes at another level", "explanation": "Data independence reduces the impact of changes to storage or logical structure on other levels."},
        {"id": "dbms_004", "skill": "DBMS", "topic": "Database Architecture", "question": "Which database architecture level describes the overall logical structure of the database?", "options": ["External level", "Conceptual level", "Physical level", "Network transport level"], "correct_answer": "Conceptual level", "explanation": "The conceptual level describes the database's overall logical organization."},
        {"id": "dbms_005", "skill": "DBMS", "topic": "Database Architecture", "question": "What does the physical or internal schema describe?", "options": ["How data is stored and organized internally", "Only what each user sees", "The business logo", "The application's color theme"], "correct_answer": "How data is stored and organized internally", "explanation": "The internal schema describes physical storage structures and access paths."},
        {"id": "dbms_006", "skill": "DBMS", "topic": "ER Modeling", "question": "In an ER diagram, what does an entity represent?", "options": ["A distinguishable real-world object or concept", "A query sorting rule", "A database connection error", "A file compression method"], "correct_answer": "A distinguishable real-world object or concept", "explanation": "Entities represent things about which the database stores information."},
        {"id": "dbms_007", "skill": "DBMS", "topic": "ER Modeling", "question": "What does a relationship represent in an ER model?", "options": ["An association between entities", "A numeric column type", "A backup schedule", "A storage device"], "correct_answer": "An association between entities", "explanation": "Relationships describe how entities are connected."},
        {"id": "dbms_008", "skill": "DBMS", "topic": "ER Modeling", "question": "What does a multivalued attribute represent?", "options": ["An attribute that can have multiple values for one entity", "An attribute that must always be NULL", "A table without rows", "A primary key that is always numeric"], "correct_answer": "An attribute that can have multiple values for one entity", "explanation": "For example, one person may have multiple phone numbers."},
        {"id": "dbms_009", "skill": "DBMS", "topic": "Keys", "question": "What is a candidate key?", "options": ["A minimal set of attributes that uniquely identifies a row", "Any column containing duplicates", "A column used only for sorting", "A key that must reference another table"], "correct_answer": "A minimal set of attributes that uniquely identifies a row", "explanation": "A candidate key uniquely identifies each row and has no unnecessary attributes."},
        {"id": "dbms_010", "skill": "DBMS", "topic": "Keys", "question": "What is a composite key?", "options": ["A key formed from two or more attributes", "A key with no columns", "A password for a database server", "A key that always contains duplicate values"], "correct_answer": "A key formed from two or more attributes", "explanation": "A composite key uses multiple attributes together to identify a row."},
        {"id": "dbms_011", "skill": "DBMS", "topic": "Keys", "question": "What is a superkey?", "options": ["Any set of attributes that uniquely identifies a row", "A key that always contains exactly one attribute", "A key that cannot uniquely identify a row", "An encrypted backup"], "correct_answer": "Any set of attributes that uniquely identifies a row", "explanation": "A superkey uniquely identifies rows and may contain extra attributes."},
        {"id": "dbms_012", "skill": "DBMS", "topic": "Relational Model", "question": "In the relational model, what is a tuple?", "options": ["A row in a relation", "A database server", "A collection of indexes only", "A query optimizer"], "correct_answer": "A row in a relation", "explanation": "A tuple represents one row or record in a relation."},
        {"id": "dbms_013", "skill": "DBMS", "topic": "Relational Model", "question": "In the relational model, what is an attribute?", "options": ["A column of a relation", "A backup file", "A network cable", "A database transaction"], "correct_answer": "A column of a relation", "explanation": "An attribute describes a property represented by a column."},
        {"id": "dbms_014", "skill": "DBMS", "topic": "Relational Algebra", "question": "Which relational algebra operation selects rows that satisfy a condition?", "options": ["Projection", "Selection", "Rename only", "Cartesian product"], "correct_answer": "Selection", "explanation": "Selection filters tuples based on a predicate."},
        {"id": "dbms_015", "skill": "DBMS", "topic": "Relational Algebra", "question": "Which relational algebra operation selects particular columns?", "options": ["Selection", "Projection", "Union only", "Difference only"], "correct_answer": "Projection", "explanation": "Projection returns chosen attributes from a relation."},
        {"id": "dbms_016", "skill": "DBMS", "topic": "Relational Algebra", "question": "What does the Cartesian product of two relations produce?", "options": ["All possible pairs of their tuples", "Only matching rows", "Only duplicate-free columns", "A transaction rollback"], "correct_answer": "All possible pairs of their tuples", "explanation": "Each tuple from the first relation is paired with every tuple from the second."},
        {"id": "dbms_017", "skill": "DBMS", "topic": "Normalization", "question": "What is the main goal of database normalization?", "options": ["Reduce undesirable redundancy and update anomalies", "Duplicate all information", "Remove all keys", "Make every table contain one row"], "correct_answer": "Reduce undesirable redundancy and update anomalies", "explanation": "Normalization organizes relations to reduce redundancy and insertion, update, and deletion anomalies."},
        {"id": "dbms_018", "skill": "DBMS", "topic": "Normalization", "question": "What is a basic requirement of First Normal Form (1NF)?", "options": ["Each attribute contains a single value from its domain in each row", "Every table must contain exactly one column", "All non-key attributes depend on the whole key", "Every table must have a timestamp"], "correct_answer": "Each attribute contains a single value from its domain in each row", "explanation": "1NF requires atomic attribute values rather than repeating groups or nested lists within a cell."},
        {"id": "dbms_019", "skill": "DBMS", "topic": "Normalization", "question": "What additional dependency condition does Second Normal Form address?", "options": ["Partial dependency of a non-prime attribute on part of a candidate key", "Every column must be unique", "Every table must contain a foreign key", "Every attribute must be a date"], "correct_answer": "Partial dependency of a non-prime attribute on part of a candidate key", "explanation": "2NF requires 1NF and removes partial dependencies of non-prime attributes on candidate-key subsets."},
        {"id": "dbms_020", "skill": "DBMS", "topic": "Normalization", "question": "What type of dependency does Third Normal Form primarily address?", "options": ["Transitive dependencies of non-prime attributes on candidate keys", "Network dependencies", "File permissions", "Index fragmentation"], "correct_answer": "Transitive dependencies of non-prime attributes on candidate keys", "explanation": "3NF builds on 2NF and restricts problematic dependencies on candidate keys."},
        {"id": "dbms_021", "skill": "DBMS", "topic": "Normalization", "question": "What is a key requirement of Boyce-Codd Normal Form (BCNF)?", "options": ["Every determinant of a non-trivial functional dependency is a superkey", "Every table must have exactly two columns", "Every attribute must be numeric", "Every relation must have a composite primary key"], "correct_answer": "Every determinant of a non-trivial functional dependency is a superkey", "explanation": "BCNF requires every determinant in a non-trivial functional dependency to be a superkey."},
        {"id": "dbms_022", "skill": "DBMS", "topic": "Functional Dependencies", "question": "What does a functional dependency X → Y mean?", "options": ["X uniquely determines Y values", "Y must always be greater than X", "X and Y must be identical columns", "X is always a foreign key"], "correct_answer": "X uniquely determines Y values", "explanation": "Equal X values must imply equal Y values in every valid relation instance."},
        {"id": "dbms_023", "skill": "DBMS", "topic": "Transactions", "question": "What does transaction atomicity guarantee?", "options": ["A transaction is completed entirely or not applied", "Every transaction executes instantly", "Every transaction uses one table only", "Data is never read during updates"], "correct_answer": "A transaction is completed entirely or not applied", "explanation": "Atomicity prevents partial transaction results."},
        {"id": "dbms_024", "skill": "DBMS", "topic": "Transactions", "question": "What does transaction consistency mean?", "options": ["A transaction preserves defined database rules and constraints", "Every query has the same runtime", "All users see identical screens", "Every table has the same number of rows"], "correct_answer": "A transaction preserves defined database rules and constraints", "explanation": "Consistency requires valid transactions to move the database between valid states."},
        {"id": "dbms_025", "skill": "DBMS", "topic": "Transactions", "question": "What does transaction isolation aim to control?", "options": ["Interference between concurrent transactions", "The number of database tables", "The font used in query results", "The size of column names"], "correct_answer": "Interference between concurrent transactions", "explanation": "Isolation controls how concurrent transactions can observe one another's work."},
        {"id": "dbms_026", "skill": "DBMS", "topic": "Concurrency Control", "question": "What is a dirty read?", "options": ["Reading data written by another transaction that has not committed", "Reading a row in sorted order", "Reading a database backup", "Reading a value from an index"], "correct_answer": "Reading data written by another transaction that has not committed", "explanation": "A dirty read can expose changes that may later be rolled back."},
        {"id": "dbms_027", "skill": "DBMS", "topic": "Concurrency Control", "question": "What is a non-repeatable read?", "options": ["Reading the same row twice and finding its committed value changed", "Reading a table with no index", "Reading two different tables", "Running the same query text twice without execution"], "correct_answer": "Reading the same row twice and finding its committed value changed", "explanation": "Another transaction can update and commit the row between the two reads."},
        {"id": "dbms_028", "skill": "DBMS", "topic": "Concurrency Control", "question": "What is a deadlock in a database?", "options": ["Transactions wait indefinitely for resources held by one another", "A table contains no records", "A query returns too many columns", "A database has no primary keys"], "correct_answer": "Transactions wait indefinitely for resources held by one another", "explanation": "A circular wait among transactions can prevent them from proceeding."},
        {"id": "dbms_029", "skill": "DBMS", "topic": "Concurrency Control", "question": "What is the purpose of two-phase locking (2PL)?", "options": ["Coordinate lock acquisition and release to support serializability", "Compress every row into two bytes", "Make all queries read-only", "Create two database servers automatically"], "correct_answer": "Coordinate lock acquisition and release to support serializability", "explanation": "In 2PL, a growing phase acquires locks and a shrinking phase releases locks; strict variants hold write locks until completion."},
        {"id": "dbms_030", "skill": "DBMS", "topic": "Recovery", "question": "What is the purpose of a transaction log?", "options": ["Record database changes to support recovery", "Store only user interface settings", "Replace the database schema", "Automatically remove all constraints"], "correct_answer": "Record database changes to support recovery", "explanation": "Logs help the DBMS recover from failures and restore transactional consistency."},
        {"id": "dbms_031", "skill": "DBMS", "topic": "Recovery", "question": "What is a checkpoint used for in database recovery?", "options": ["Reduce the work needed to recover after a failure", "Delete every committed transaction", "Create a new user role", "Sort all tables alphabetically"], "correct_answer": "Reduce the work needed to recover after a failure", "explanation": "A checkpoint records recovery-related progress so the DBMS need not process the entire log from the beginning."},
        {"id": "dbms_032", "skill": "DBMS", "topic": "Indexing", "question": "What is the main purpose of a database index?", "options": ["Speed up suitable data retrieval operations", "Guarantee every write is faster", "Replace transaction logs", "Prevent every duplicate value automatically"], "correct_answer": "Speed up suitable data retrieval operations", "explanation": "Indexes provide access paths that can reduce the amount of data examined."},
        {"id": "dbms_033", "skill": "DBMS", "topic": "Indexing", "question": "Which tree structure is commonly used for database indexes that support ordered range searches?", "options": ["B+ tree", "Expression tree only", "Syntax tree only", "Decision tree only"], "correct_answer": "B+ tree", "explanation": "B+ trees support balanced lookups and ordered range scans."},
        {"id": "dbms_034", "skill": "DBMS", "topic": "Query Processing", "question": "What does a query optimizer do?", "options": ["Chooses an efficient execution plan for a query", "Writes application passwords", "Designs database tables without input", "Guarantees every query has zero latency"], "correct_answer": "Chooses an efficient execution plan for a query", "explanation": "The optimizer compares possible plans using estimates and database statistics."},
        {"id": "dbms_035", "skill": "DBMS", "topic": "Distributed Databases", "question": "What is database replication?", "options": ["Maintaining copies of data on multiple database nodes", "Splitting a string into characters", "Removing all indexes", "Converting each row into a method"], "correct_answer": "Maintaining copies of data on multiple database nodes", "explanation": "Replication keeps data copies on different nodes for availability or read scaling."},
        {"id": "dbms_036", "skill": "DBMS", "topic": "Distributed Databases", "question": "What is database sharding?", "options": ["Partitioning data across multiple machines or shards", "Creating duplicate columns in one row", "Sorting data in descending order", "Encrypting every SQL keyword"], "correct_answer": "Partitioning data across multiple machines or shards", "explanation": "Sharding distributes portions of a dataset across machines for horizontal scaling."},
        {"id": "dbms_037", "skill": "DBMS", "topic": "Distributed Databases", "question": "In distributed systems, what does eventual consistency mean?", "options": ["Replicas may temporarily differ but converge if updates stop and propagation succeeds", "Every replica always returns identical data immediately", "No replica can accept updates", "Transactions never fail"], "correct_answer": "Replicas may temporarily differ but converge if updates stop and propagation succeeds", "explanation": "Eventual consistency allows temporary differences while updates propagate between replicas."},
        {"id": "dbms_038", "skill": "DBMS", "topic": "Security", "question": "What does the principle of least privilege mean for database users?", "options": ["Give each user only the permissions needed for their work", "Give every user administrator access", "Disable all authentication", "Share one account with every employee"], "correct_answer": "Give each user only the permissions needed for their work", "explanation": "Least privilege limits the damage caused by mistakes or compromised accounts."},
        {"id": "dbms_039", "skill": "DBMS", "topic": "Backup and Recovery", "question": "Why should database backups be tested through restoration?", "options": ["To verify that data can actually be recovered", "To guarantee every query is faster", "To remove the need for access control", "To change all primary keys"], "correct_answer": "To verify that data can actually be recovered", "explanation": "A backup is useful only if it can be restored successfully when needed."},
        {"id": "dbms_040", "skill": "DBMS", "topic": "Database Design", "question": "What is a database anomaly?", "options": ["An unintended problem with inserting, updating, or deleting data", "A required step in every SELECT query", "A type of primary key", "A database server's hostname"], "correct_answer": "An unintended problem with inserting, updating, or deleting data", "explanation": "Data anomalies often arise from poor table design and redundant information."}
    ],
    
    "operating systems": [
        {"id": "os_001", "skill": "Operating Systems", "topic": "Basics", "question": "What is the main role of an operating system?", "options": ["Manage hardware and software resources", "Design web pages", "Write database queries", "Create programming languages"], "correct_answer": "Manage hardware and software resources", "explanation": "An operating system manages hardware, processes, memory, files, and devices."},
        {"id": "os_002", "skill": "Operating Systems", "topic": "Processes", "question": "What is a process?", "options": ["A program in execution", "A file stored only on a hard disk", "A type of keyboard", "A network address"], "correct_answer": "A program in execution", "explanation": "A process is an executing instance of a program."},
        {"id": "os_003", "skill": "Operating Systems", "topic": "Processes", "question": "What information is typically stored in a Process Control Block (PCB)?", "options": ["Process state and CPU register information", "Only website URLs", "Only source-code comments", "Monitor resolution only"], "correct_answer": "Process state and CPU register information", "explanation": "A PCB stores information the operating system needs to manage a process."},
        {"id": "os_004", "skill": "Operating Systems", "topic": "Processes", "question": "Which state describes a process waiting to be assigned a CPU?", "options": ["Running", "Ready", "Terminated", "New only"], "correct_answer": "Ready", "explanation": "A ready process can execute but is waiting for CPU scheduling."},
        {"id": "os_005", "skill": "Operating Systems", "topic": "Threads", "question": "What is a thread?", "options": ["A unit of execution within a process", "A separate physical CPU", "A file system", "A network cable"], "correct_answer": "A unit of execution within a process", "explanation": "Threads share many process resources while maintaining their own execution state."},
        {"id": "os_006", "skill": "Operating Systems", "topic": "Threads", "question": "What is one common advantage of multithreading?", "options": ["Improved responsiveness for suitable workloads", "Guaranteed zero synchronization issues", "Elimination of all memory use", "Removal of the operating system"], "correct_answer": "Improved responsiveness for suitable workloads", "explanation": "Multiple threads can keep an application responsive while work proceeds."},
        {"id": "os_007", "skill": "Operating Systems", "topic": "CPU Scheduling", "question": "Which scheduling algorithm serves processes in arrival order?", "options": ["Round Robin", "FCFS", "Shortest Remaining Time First", "Priority scheduling only"], "correct_answer": "FCFS", "explanation": "First-Come, First-Served executes processes in their order of arrival."},
        {"id": "os_008", "skill": "Operating Systems", "topic": "CPU Scheduling", "question": "Which scheduling algorithm assigns each process a fixed time slice?", "options": ["FCFS", "Non-preemptive SJF", "Round Robin", "FIFO page replacement"], "correct_answer": "Round Robin", "explanation": "Round Robin gives each ready process a time quantum in turn."},
        {"id": "os_009", "skill": "Operating Systems", "topic": "CPU Scheduling", "question": "What is a common disadvantage of FCFS scheduling?", "options": ["The convoy effect", "It always requires a priority queue", "It cannot execute any process", "It always causes a deadlock"], "correct_answer": "The convoy effect", "explanation": "Short processes may wait behind a long process, reducing overall responsiveness."},
        {"id": "os_010", "skill": "Operating Systems", "topic": "CPU Scheduling", "question": "What is a possible problem with priority scheduling?", "options": ["Starvation of low-priority processes", "All processes execute simultaneously on one CPU", "Memory is never allocated", "Files cannot be created"], "correct_answer": "Starvation of low-priority processes", "explanation": "Low-priority processes may wait indefinitely if higher-priority work keeps arriving."},
        {"id": "os_011", "skill": "Operating Systems", "topic": "Synchronization", "question": "What is a race condition?", "options": ["An outcome that depends on the timing of concurrent operations", "A process that never starts", "A disk formatting method", "A fixed CPU frequency"], "correct_answer": "An outcome that depends on the timing of concurrent operations", "explanation": "Unsynchronized access to shared state can produce timing-dependent results."},
        {"id": "os_012", "skill": "Operating Systems", "topic": "Synchronization", "question": "What is the main purpose of a mutex?", "options": ["Provide mutual exclusion for a shared resource", "Increase file size", "Replace virtual memory", "Sort running processes"], "correct_answer": "Provide mutual exclusion for a shared resource", "explanation": "A mutex helps ensure that only one thread at a time enters a protected critical section."},
        {"id": "os_013", "skill": "Operating Systems", "topic": "Synchronization", "question": "What does a semaphore commonly control?", "options": ["Access to shared resources through a counter and synchronization operations", "Only file names", "CPU temperature directly", "Network domain names"], "correct_answer": "Access to shared resources through a counter and synchronization operations", "explanation": "Semaphores coordinate access and can manage a limited number of available resources."},
        {"id": "os_014", "skill": "Operating Systems", "topic": "Synchronization", "question": "What is a critical section?", "options": ["Code that accesses shared data or resources", "A section containing only comments", "The operating system startup screen", "A disk partition"], "correct_answer": "Code that accesses shared data or resources", "explanation": "Critical sections require suitable synchronization when concurrent access could cause errors."},
        {"id": "os_015", "skill": "Operating Systems", "topic": "Deadlocks", "question": "Which is one of the four necessary conditions for deadlock?", "options": ["Circular wait", "Automatic garbage collection", "File compression", "Dynamic web rendering"], "correct_answer": "Circular wait", "explanation": "The four necessary conditions are mutual exclusion, hold and wait, no preemption, and circular wait."},
        {"id": "os_016", "skill": "Operating Systems", "topic": "Deadlocks", "question": "What is deadlock prevention?", "options": ["Designing the system so at least one necessary deadlock condition cannot hold", "Increasing the number of files", "Allowing every process to hold every resource forever", "Disabling CPU scheduling"], "correct_answer": "Designing the system so at least one necessary deadlock condition cannot hold", "explanation": "Prevention eliminates a necessary condition for deadlock."},
        {"id": "os_017", "skill": "Operating Systems", "topic": "Deadlocks", "question": "What does the Banker's algorithm help with?", "options": ["Deadlock avoidance", "File compression", "Network routing only", "CPU manufacturing"], "correct_answer": "Deadlock avoidance", "explanation": "The Banker's algorithm checks whether resource allocation can leave the system in a safe state."},
        {"id": "os_018", "skill": "Operating Systems", "topic": "Memory Management", "question": "What is virtual memory?", "options": ["A memory-management technique that gives processes a virtual address space", "A physical keyboard", "A type of CPU register only", "A file extension"], "correct_answer": "A memory-management technique that gives processes a virtual address space", "explanation": "Virtual memory provides address-space abstraction and can use disk-backed storage for pages."},
        {"id": "os_019", "skill": "Operating Systems", "topic": "Memory Management", "question": "What is paging?", "options": ["Dividing virtual memory into fixed-size pages and physical memory into frames", "Dividing a CPU into threads", "Sorting files by name", "Compressing every instruction"], "correct_answer": "Dividing virtual memory into fixed-size pages and physical memory into frames", "explanation": "Paging maps fixed-size virtual pages to physical memory frames."},
        {"id": "os_020", "skill": "Operating Systems", "topic": "Memory Management", "question": "What is a page fault?", "options": ["An access requiring a page that is not currently mapped as available in physical memory", "A printer error", "A failed DNS lookup", "A missing source-code comment"], "correct_answer": "An access requiring a page that is not currently mapped as available in physical memory", "explanation": "The operating system handles a page fault by validating the access and arranging the required page if necessary."},
        {"id": "os_021", "skill": "Operating Systems", "topic": "Memory Management", "question": "What is internal fragmentation?", "options": ["Wasted space inside an allocated memory block", "Wasted space only between disk partitions", "A network packet loss", "A deadlock condition"], "correct_answer": "Wasted space inside an allocated memory block", "explanation": "Internal fragmentation occurs when allocated space exceeds the amount actually needed."},
        {"id": "os_022", "skill": "Operating Systems", "topic": "Memory Management", "question": "What is external fragmentation?", "options": ["Free memory divided into separate gaps that may not satisfy a large allocation", "Unused space inside a fixed-size allocated block only", "An error in a web page", "A CPU scheduling policy"], "correct_answer": "Free memory divided into separate gaps that may not satisfy a large allocation", "explanation": "Total free memory may be sufficient, but the available gaps may be too small or scattered."},
        {"id": "os_023", "skill": "Operating Systems", "topic": "Page Replacement", "question": "Which page replacement policy removes the page that has not been used for the longest time in the past?", "options": ["FIFO", "LRU", "Round Robin", "FCFS"], "correct_answer": "LRU", "explanation": "Least Recently Used uses past access recency as its replacement rule."},
        {"id": "os_024", "skill": "Operating Systems", "topic": "Page Replacement", "question": "Which page replacement policy removes the page that entered memory earliest?", "options": ["LRU", "Optimal", "FIFO", "Priority scheduling"], "correct_answer": "FIFO", "explanation": "First-In, First-Out replaces the page that has been resident the longest."},
        {"id": "os_025", "skill": "Operating Systems", "topic": "Page Replacement", "question": "What is thrashing?", "options": ["Excessive paging that leaves little time for useful execution", "Fast execution with no memory access", "A method for sorting files", "A type of network cable"], "correct_answer": "Excessive paging that leaves little time for useful execution", "explanation": "Thrashing occurs when page faults and page transfers dominate system activity."},
        {"id": "os_026", "skill": "Operating Systems", "topic": "File Systems", "question": "What is a file system responsible for?", "options": ["Organizing and managing files and directories", "Scheduling only CPU instructions", "Creating network protocols", "Designing user interfaces"], "correct_answer": "Organizing and managing files and directories", "explanation": "A file system defines how data and file metadata are stored and accessed."},
        {"id": "os_027", "skill": "Operating Systems", "topic": "File Systems", "question": "What is an inode in Unix-like file systems?", "options": ["A structure containing file metadata and references to file data", "A CPU scheduling queue", "A network gateway", "A programming language"], "correct_answer": "A structure containing file metadata and references to file data", "explanation": "An inode stores metadata such as ownership, permissions, and data-block references, not the filename itself."},
        {"id": "os_028", "skill": "Operating Systems", "topic": "File Systems", "question": "What does a file permission setting control?", "options": ["Which users can perform specified actions on a file", "The CPU clock speed", "The size of the monitor", "The number of network routers"], "correct_answer": "Which users can perform specified actions on a file", "explanation": "Permissions control actions such as reading, writing, and executing."},
        {"id": "os_029", "skill": "Operating Systems", "topic": "System Calls", "question": "What is a system call?", "options": ["A controlled interface for a program to request an operating-system service", "A call between two database tables", "A hardware power cable", "A type of sorting algorithm"], "correct_answer": "A controlled interface for a program to request an operating-system service", "explanation": "System calls let applications request services such as file access and process creation."},
        {"id": "os_030", "skill": "Operating Systems", "topic": "System Calls", "question": "What is a context switch?", "options": ["Saving one execution context and restoring another", "Changing a file extension", "Restarting a database query", "Changing a network domain name"], "correct_answer": "Saving one execution context and restoring another", "explanation": "A context switch allows the CPU to stop one process or thread and resume another."},
        {"id": "os_031", "skill": "Operating Systems", "topic": "Interrupts", "question": "What is the purpose of an interrupt?", "options": ["Notify the CPU that an event needs attention", "Delete every running process", "Format the system disk", "Compile all programs automatically"], "correct_answer": "Notify the CPU that an event needs attention", "explanation": "Interrupts allow the processor to respond to events without continuously polling every device."},
        {"id": "os_032", "skill": "Operating Systems", "topic": "Kernel", "question": "What is the kernel?", "options": ["The core part of the operating system", "A user document", "A database query", "A web browser extension"], "correct_answer": "The core part of the operating system", "explanation": "The kernel manages fundamental operations such as processes, memory, and hardware access."},
        {"id": "os_033", "skill": "Operating Systems", "topic": "Kernel", "question": "What is a key characteristic of a microkernel design?", "options": ["It keeps the kernel's core functions relatively small", "It places every application inside the kernel", "It cannot support processes", "It removes inter-process communication"], "correct_answer": "It keeps the kernel's core functions relatively small", "explanation": "Microkernels move many services outside the kernel, communicating through defined mechanisms."},
        {"id": "os_034", "skill": "Operating Systems", "topic": "Inter-Process Communication", "question": "What is inter-process communication (IPC) used for?", "options": ["Allowing processes to exchange data or coordinate", "Increasing screen resolution", "Formatting source code", "Changing file extensions"], "correct_answer": "Allowing processes to exchange data or coordinate", "explanation": "IPC mechanisms include pipes, message queues, shared memory, and sockets."},
        {"id": "os_035", "skill": "Operating Systems", "topic": "Inter-Process Communication", "question": "What is a pipe commonly used for in Unix-like systems?", "options": ["Passing data between processes", "Changing CPU architecture", "Creating a primary key", "Sorting physical memory addresses"], "correct_answer": "Passing data between processes", "explanation": "A pipe provides a communication channel, commonly carrying a byte stream."},
        {"id": "os_036", "skill": "Operating Systems", "topic": "Booting", "question": "What is the bootloader's main role?", "options": ["Help load the operating system kernel", "Execute every user application", "Manage all database records", "Replace the computer's RAM"], "correct_answer": "Help load the operating system kernel", "explanation": "A bootloader initializes the boot process and loads or transfers control to the kernel."},
        {"id": "os_037", "skill": "Operating Systems", "topic": "Virtualization", "question": "What does a hypervisor do?", "options": ["Creates and manages virtual machines", "Only edits text files", "Runs SQL queries exclusively", "Replaces network protocols"], "correct_answer": "Creates and manages virtual machines", "explanation": "A hypervisor allocates hardware resources to virtual machines."},
        {"id": "os_038", "skill": "Operating Systems", "topic": "Virtualization", "question": "What is a common difference between containers and virtual machines?", "options": ["Containers generally share the host kernel, while VMs run guest operating systems", "Containers always require separate physical computers", "VMs never use memory", "Containers cannot run applications"], "correct_answer": "Containers generally share the host kernel, while VMs run guest operating systems", "explanation": "Containers isolate applications while sharing the host kernel; VMs virtualize hardware to run guest operating systems."},
        {"id": "os_039", "skill": "Operating Systems", "topic": "Scheduling", "question": "What is starvation in process scheduling?", "options": ["A process waits indefinitely because resources keep going to others", "A process uses no memory", "A program completes instantly", "A disk has no files"], "correct_answer": "A process waits indefinitely because resources keep going to others", "explanation": "Starvation occurs when a process is repeatedly denied needed CPU time or another resource."},
        {"id": "os_040", "skill": "Operating Systems", "topic": "Real-Time Systems", "question": "What is a key requirement of a hard real-time system?", "options": ["Critical deadlines must be met", "Every task must use a graphical interface", "All tasks must run only once a day", "The system must never use interrupts"], "correct_answer": "Critical deadlines must be met", "explanation": "Missing a hard real-time deadline is considered a system failure."}
    ],

    "computer networks": [
        {"id": "networks_001", "skill": "Computer Networks", "topic": "Fundamentals", "question": "What is a computer network?", "options": ["Connected devices that exchange data and share resources", "A single offline text file", "A programming loop", "A database column"], "correct_answer": "Connected devices that exchange data and share resources", "explanation": "Networks allow connected devices to communicate and share information or services."},
        {"id": "networks_002", "skill": "Computer Networks", "topic": "Network Types", "question": "Which network type commonly covers a home, office, or campus building?", "options": ["LAN", "WAN only", "GAN only", "Satellite orbit"], "correct_answer": "LAN", "explanation": "A Local Area Network covers a relatively limited geographic area."},
        {"id": "networks_003", "skill": "Computer Networks", "topic": "Network Types", "question": "What does WAN stand for?", "options": ["Wireless Access Node", "Wide Area Network", "Web Application Network", "Wired Address Number"], "correct_answer": "Wide Area Network", "explanation": "A WAN connects networks across large geographic areas."},
        {"id": "networks_004", "skill": "Computer Networks", "topic": "OSI Model", "question": "How many layers are in the OSI reference model?", "options": ["Four", "Five", "Seven", "Eight"], "correct_answer": "Seven", "explanation": "The OSI model has seven layers, from Physical to Application."},
        {"id": "networks_005", "skill": "Computer Networks", "topic": "OSI Model", "question": "Which OSI layer is responsible for routing packets between networks?", "options": ["Physical", "Data Link", "Network", "Presentation"], "correct_answer": "Network", "explanation": "The Network layer handles logical addressing and routing."},
        {"id": "networks_006", "skill": "Computer Networks", "topic": "OSI Model", "question": "Which OSI layer is primarily responsible for end-to-end transport services?", "options": ["Transport", "Physical", "Presentation", "Data Link"], "correct_answer": "Transport", "explanation": "The Transport layer supports end-to-end delivery, including reliability for protocols such as TCP."},
        {"id": "networks_007", "skill": "Computer Networks", "topic": "OSI Model", "question": "At which OSI layer do Ethernet switches commonly forward frames using MAC addresses?", "options": ["Application", "Data Link", "Session", "Transport"], "correct_answer": "Data Link", "explanation": "Layer 2 switches commonly use MAC addresses to forward Ethernet frames."},
        {"id": "networks_008", "skill": "Computer Networks", "topic": "TCP/IP", "question": "Which protocol provides reliable, ordered byte-stream delivery?", "options": ["UDP", "TCP", "ARP", "ICMP only"], "correct_answer": "TCP", "explanation": "TCP provides connection-oriented, reliable, ordered byte-stream delivery."},
        {"id": "networks_009", "skill": "Computer Networks", "topic": "TCP/IP", "question": "Which transport protocol is connectionless and does not guarantee delivery?", "options": ["TCP", "UDP", "HTTPS", "SSH"], "correct_answer": "UDP", "explanation": "UDP sends datagrams without TCP-style delivery and ordering guarantees."},
        {"id": "networks_010", "skill": "Computer Networks", "topic": "IP Addressing", "question": "How many bits are in an IPv4 address?", "options": ["16", "32", "64", "128"], "correct_answer": "32", "explanation": "IPv4 addresses are 32 bits long."},
        {"id": "networks_011", "skill": "Computer Networks", "topic": "IP Addressing", "question": "How many bits are in an IPv6 address?", "options": ["32", "48", "64", "128"], "correct_answer": "128", "explanation": "IPv6 uses 128-bit addresses."},
        {"id": "networks_012", "skill": "Computer Networks", "topic": "IP Addressing", "question": "What does a subnet mask help identify?", "options": ["The network and host portions of an IPv4 address", "The website's HTML structure", "The CPU type", "The password length"], "correct_answer": "The network and host portions of an IPv4 address", "explanation": "A subnet mask identifies which IPv4 address bits represent the network prefix."},
        {"id": "networks_013", "skill": "Computer Networks", "topic": "IP Addressing", "question": "What is the main purpose of a default gateway?", "options": ["Forward traffic to destinations outside the local network", "Store browser bookmarks", "Assign every MAC address manually", "Encrypt every file on a computer"], "correct_answer": "Forward traffic to destinations outside the local network", "explanation": "A default gateway is used when traffic must leave the local subnet."},
        {"id": "networks_014", "skill": "Computer Networks", "topic": "Address Resolution", "question": "What does ARP commonly resolve in IPv4 local networks?", "options": ["An IPv4 address to a link-layer MAC address", "A domain name to an email address", "A port number to a process name", "An IPv6 address to a web page"], "correct_answer": "An IPv4 address to a link-layer MAC address", "explanation": "ARP discovers the link-layer address associated with a local IPv4 address."},
        {"id": "networks_015", "skill": "Computer Networks", "topic": "DNS", "question": "What is the main purpose of DNS?", "options": ["Resolve domain names to records such as IP addresses", "Encrypt all hard drives", "Assign CPU time", "Replace TCP connections"], "correct_answer": "Resolve domain names to records such as IP addresses", "explanation": "DNS translates names such as example.com into records used by network clients."},
        {"id": "networks_016", "skill": "Computer Networks", "topic": "DHCP", "question": "What does DHCP commonly provide to a network client?", "options": ["IP configuration such as an address, gateway, and DNS servers", "Source code for the operating system", "A permanent MAC address replacement", "A database schema"], "correct_answer": "IP configuration such as an address, gateway, and DNS servers", "explanation": "DHCP automatically supplies network configuration to clients."},
        {"id": "networks_017", "skill": "Computer Networks", "topic": "Ports", "question": "Which port is the default for HTTP?", "options": ["21", "25", "80", "443"], "correct_answer": "80", "explanation": "HTTP commonly uses TCP port 80 by default."},
        {"id": "networks_018", "skill": "Computer Networks", "topic": "Ports", "question": "Which port is the default for HTTPS?", "options": ["22", "53", "110", "443"], "correct_answer": "443", "explanation": "HTTPS commonly uses TCP port 443 by default."},
        {"id": "networks_019", "skill": "Computer Networks", "topic": "Ports", "question": "Which port is commonly used by SSH?", "options": ["22", "23", "80", "3306"], "correct_answer": "22", "explanation": "SSH commonly uses TCP port 22 for secure remote access."},
        {"id": "networks_020", "skill": "Computer Networks", "topic": "Ports", "question": "Which port is commonly associated with DNS queries?", "options": ["25", "53", "143", "8080"], "correct_answer": "53", "explanation": "DNS commonly uses port 53 over UDP or TCP, depending on the operation."},
        {"id": "networks_021", "skill": "Computer Networks", "topic": "Network Devices", "question": "What is a router primarily used for?", "options": ["Forward packets between networks", "Connect only USB devices", "Compile source code", "Store database tables"], "correct_answer": "Forward packets between networks", "explanation": "Routers use routing information to forward packets toward destination networks."},
        {"id": "networks_022", "skill": "Computer Networks", "topic": "Network Devices", "question": "What does a network switch commonly do?", "options": ["Forward frames within a LAN using MAC address information", "Translate every domain name", "Assign every process a thread", "Replace the transport layer"], "correct_answer": "Forward frames within a LAN using MAC address information", "explanation": "A Layer 2 switch learns MAC addresses and forwards frames to appropriate ports."},
        {"id": "networks_023", "skill": "Computer Networks", "topic": "Network Devices", "question": "What is a modem commonly used for?", "options": ["Modulate and demodulate signals for a communication link", "Store web application source code", "Manage database indexes", "Schedule operating system threads"], "correct_answer": "Modulate and demodulate signals for a communication link", "explanation": "A modem adapts signals for transmission over a particular communications medium."},
        {"id": "networks_024", "skill": "Computer Networks", "topic": "Network Security", "question": "What is the primary purpose of a firewall?", "options": ["Filter network traffic according to security rules", "Increase the number of CPU cores", "Automatically repair every application bug", "Replace IP addressing"], "correct_answer": "Filter network traffic according to security rules", "explanation": "Firewalls allow or block traffic based on configured rules and connection state."},
        {"id": "networks_025", "skill": "Computer Networks", "topic": "Network Security", "question": "What does TLS help provide for network communication?", "options": ["Encryption, integrity, and authenticated peers when properly configured", "Guaranteed zero network delay", "Unlimited bandwidth", "Automatic removal of malware from every device"], "correct_answer": "Encryption, integrity, and authenticated peers when properly configured", "explanation": "TLS protects data in transit and can authenticate servers using certificates."},
        {"id": "networks_026", "skill": "Computer Networks", "topic": "Network Security", "question": "What is a VPN commonly used for?", "options": ["Creating a protected tunnel across an untrusted network", "Increasing screen resolution", "Replacing all application protocols", "Deleting router configurations"], "correct_answer": "Creating a protected tunnel across an untrusted network", "explanation": "A VPN can encrypt traffic between endpoints over a network such as the internet."},
        {"id": "networks_027", "skill": "Computer Networks", "topic": "Network Performance", "question": "What does bandwidth describe in networking?", "options": ["The capacity of a link to carry data per unit time", "The physical weight of a router", "The number of files in a folder", "The length of an IP address only"], "correct_answer": "The capacity of a link to carry data per unit time", "explanation": "Bandwidth describes a link's data-carrying capacity, commonly measured in bits per second."},
        {"id": "networks_028", "skill": "Computer Networks", "topic": "Network Performance", "question": "What is latency?", "options": ["The time taken for data to travel between points", "The total disk capacity", "The number of users in a database", "The size of an HTML document only"], "correct_answer": "The time taken for data to travel between points", "explanation": "Latency measures delay, often expressed in milliseconds."},
        {"id": "networks_029", "skill": "Computer Networks", "topic": "Network Performance", "question": "What is packet loss?", "options": ["Packets that fail to reach their intended destination", "A packet with a long filename", "A successful DNS lookup", "A type of database index"], "correct_answer": "Packets that fail to reach their intended destination", "explanation": "Packet loss can result from congestion, transmission errors, or network faults."},
        {"id": "networks_030", "skill": "Computer Networks", "topic": "Routing", "question": "What is the purpose of a routing table?", "options": ["Help determine where packets should be forwarded", "Store passwords for every website", "Keep a list of CPU instructions", "Sort documents by file size"], "correct_answer": "Help determine where packets should be forwarded", "explanation": "Routing tables contain destination prefixes and next-hop or interface information."},
        {"id": "networks_031", "skill": "Computer Networks", "topic": "Routing", "question": "What is the purpose of a routing metric?", "options": ["Help compare possible routes", "Encrypt a user password", "Set the browser font", "Determine database column types"], "correct_answer": "Help compare possible routes", "explanation": "Routing protocols use metrics such as cost, hop count, or delay to evaluate routes."},
        {"id": "networks_032", "skill": "Computer Networks", "topic": "Wireless Networks", "question": "What does an SSID identify?", "options": ["A wireless network name", "A unique CPU instruction", "A database primary key", "An Ethernet frame checksum"], "correct_answer": "A wireless network name", "explanation": "The SSID is the name used to identify a Wi-Fi network."},
        {"id": "networks_033", "skill": "Computer Networks", "topic": "Wireless Networks", "question": "Which security protocol is generally preferable for modern Wi-Fi when supported?", "options": ["WEP", "WPA3", "Open access without authentication", "Telnet"], "correct_answer": "WPA3", "explanation": "WPA3 offers stronger protections than legacy WEP and older security configurations."},
        {"id": "networks_034", "skill": "Computer Networks", "topic": "Protocols", "question": "What is the primary purpose of ICMP?", "options": ["Carry network control and diagnostic messages", "Transfer database tables only", "Render HTML pages", "Assign JavaScript variables"], "correct_answer": "Carry network control and diagnostic messages", "explanation": "ICMP supports error reporting and diagnostics; ping commonly uses ICMP echo messages."},
        {"id": "networks_035", "skill": "Computer Networks", "topic": "Protocols", "question": "What is the main purpose of SMTP?", "options": ["Send email between clients and mail servers or between mail servers", "Resolve domain names", "Assign IP addresses automatically", "Transfer files using a block device"], "correct_answer": "Send email between clients and mail servers or between mail servers", "explanation": "SMTP is used for sending and relaying email."},
        {"id": "networks_036", "skill": "Computer Networks", "topic": "Protocols", "question": "Which protocol is commonly used to securely transfer files over an SSH connection?", "options": ["SFTP", "HTTP without TLS", "ARP", "ICMP"], "correct_answer": "SFTP", "explanation": "SFTP provides file-transfer operations over SSH."},
        {"id": "networks_037", "skill": "Computer Networks", "topic": "NAT", "question": "What is Network Address Translation (NAT) commonly used for?", "options": ["Translate address information between network address spaces", "Increase the number of OSI layers", "Compress all files on a server", "Convert SQL into JavaScript"], "correct_answer": "Translate address information between network address spaces", "explanation": "NAT commonly allows private-addressed devices to communicate through a public address."},
        {"id": "networks_038", "skill": "Computer Networks", "topic": "Network Topologies", "question": "In a star topology, how are devices commonly connected?", "options": ["Through a central device", "Only in a single closed loop", "Only in a straight line with no central point", "Without any links"], "correct_answer": "Through a central device", "explanation": "Star networks connect devices to a central switch or access point."},
        {"id": "networks_039", "skill": "Computer Networks", "topic": "Network Troubleshooting", "question": "Which command-line tool is commonly used to test reachability with echo requests?", "options": ["ping", "mkdir", "grep", "chmod"], "correct_answer": "ping", "explanation": "Ping commonly tests IP reachability using ICMP echo messages where permitted."},
        {"id": "networks_040", "skill": "Computer Networks", "topic": "Network Troubleshooting", "question": "What can traceroute or tracert help reveal?", "options": ["The network hops toward a destination", "The contents of every encrypted packet", "All passwords stored on a computer", "The source code of a remote application"], "correct_answer": "The network hops toward a destination", "explanation": "Traceroute-style tools use probe packets and responses to identify intermediate routing hops."}
    ],

    "numpy": [
        {"id": "numpy_001", "skill": "NumPy", "topic": "Basics", "question": "What is NumPy primarily used for in Python?", "options": ["Numerical computing with arrays", "Building HTML layouts", "Managing network routers", "Creating relational database tables only"], "correct_answer": "Numerical computing with arrays", "explanation": "NumPy provides efficient multidimensional arrays and numerical operations."},
        {"id": "numpy_002", "skill": "NumPy", "topic": "Array Creation", "question": "Which function creates a NumPy array from a Python list?", "options": ["np.array()", "np.table()", "np.list_to_db()", "np.makeclass()"], "correct_answer": "np.array()", "explanation": "np.array() converts compatible input data into a NumPy ndarray."},
        {"id": "numpy_003", "skill": "NumPy", "topic": "Array Creation", "question": "What does np.zeros((2, 3)) create?", "options": ["A 2-by-3 array filled with zeros", "A 3-by-2 array filled with ones", "A one-dimensional array of length 2", "An array containing six random integers"], "correct_answer": "A 2-by-3 array filled with zeros", "explanation": "The shape argument specifies two rows and three columns."},
        {"id": "numpy_004", "skill": "NumPy", "topic": "Array Creation", "question": "What does np.ones(4) return?", "options": ["Four zeros", "Four ones in a one-dimensional array", "A 4-by-4 identity matrix", "Four random numbers"], "correct_answer": "Four ones in a one-dimensional array", "explanation": "np.ones creates an array of the requested shape filled with ones."},
        {"id": "numpy_005", "skill": "NumPy", "topic": "Array Creation", "question": "What does np.arange(1, 6) produce?", "options": ["[1, 2, 3, 4, 5]", "[1, 2, 3, 4, 5, 6]", "[0, 1, 2, 3, 4, 5]", "[6, 5, 4, 3, 2, 1]"], "correct_answer": "[1, 2, 3, 4, 5]", "explanation": "arange includes the start value and excludes the stop value."},
        {"id": "numpy_006", "skill": "NumPy", "topic": "Array Creation", "question": "What does np.linspace(0, 1, 5) create?", "options": ["Five evenly spaced values from 0 to 1, including endpoints", "Five random integers", "Only the values 0 and 1", "A 5-by-5 matrix"], "correct_answer": "Five evenly spaced values from 0 to 1, including endpoints", "explanation": "linspace returns the requested number of evenly spaced samples across the interval by default."},
        {"id": "numpy_007", "skill": "NumPy", "topic": "Array Attributes", "question": "Which attribute returns the dimensions or shape of a NumPy array?", "options": [".shape", ".length", ".columns_only", ".format"], "correct_answer": ".shape", "explanation": "The shape attribute returns the size along each dimension."},
        {"id": "numpy_008", "skill": "NumPy", "topic": "Array Attributes", "question": "What does the ndim attribute report?", "options": ["Number of dimensions", "Number of nonzero elements only", "Total memory of the computer", "Largest array value"], "correct_answer": "Number of dimensions", "explanation": "ndim gives the number of axes in an array."},
        {"id": "numpy_009", "skill": "NumPy", "topic": "Array Attributes", "question": "What does arr.size return?", "options": ["The total number of elements", "The number of dimensions only", "The array's largest value", "The number of rows only"], "correct_answer": "The total number of elements", "explanation": "size is the product of all dimensions in the array's shape."},
        {"id": "numpy_010", "skill": "NumPy", "topic": "Data Types", "question": "Which attribute shows the element data type of a NumPy array?", "options": [".dtype", ".shape", ".axes", ".columns"], "correct_answer": ".dtype", "explanation": "dtype identifies the data type used to represent array elements."},
        {"id": "numpy_011", "skill": "NumPy", "topic": "Indexing", "question": "For arr = np.array([10, 20, 30]), what is arr[1]?", "options": ["10", "20", "30", "1"], "correct_answer": "20", "explanation": "NumPy uses zero-based indexing, so index 1 refers to the second element."},
        {"id": "numpy_012", "skill": "NumPy", "topic": "Slicing", "question": "For arr = np.array([2, 4, 6, 8]), what does arr[1:3] return?", "options": ["[2, 4]", "[4, 6]", "[4, 6, 8]", "[6, 8]"], "correct_answer": "[4, 6]", "explanation": "Slicing includes the start index and excludes the stop index."},
        {"id": "numpy_013", "skill": "NumPy", "topic": "Multidimensional Arrays", "question": "For a 2D array arr, what does arr[0, 1] access?", "options": ["The first row, second column", "The second row, first column", "The first element of the last row", "The entire first column"], "correct_answer": "The first row, second column", "explanation": "The first index selects the row and the second selects the column."},
        {"id": "numpy_014", "skill": "NumPy", "topic": "Reshaping", "question": "What must be true to reshape an array into a new shape?", "options": ["The total number of elements must remain the same", "The new shape must always be square", "The array must contain only zeros", "The array must have one dimension originally"], "correct_answer": "The total number of elements must remain the same", "explanation": "Reshaping rearranges the dimensions without changing the total element count."},
        {"id": "numpy_015", "skill": "NumPy", "topic": "Reshaping", "question": "What does arr.flatten() return?", "options": ["A flattened one-dimensional copy of the array", "A sorted two-dimensional array", "Only the diagonal elements", "An array with twice as many elements"], "correct_answer": "A flattened one-dimensional copy of the array", "explanation": "flatten() returns a one-dimensional copy of the array's elements."},
        {"id": "numpy_016", "skill": "NumPy", "topic": "Reshaping", "question": "What does np.transpose(arr) generally do to a 2D array?", "options": ["Swaps rows and columns", "Deletes every other row", "Sorts all values", "Changes every value to a string"], "correct_answer": "Swaps rows and columns", "explanation": "Transposition exchanges the axes of a two-dimensional array."},
        {"id": "numpy_017", "skill": "NumPy", "topic": "Vectorization", "question": "What happens when you calculate arr + 5 for a numeric NumPy array?", "options": ["Five is added to each element", "Only the first element changes", "The array is converted to a list", "The array is sorted automatically"], "correct_answer": "Five is added to each element", "explanation": "NumPy applies scalar arithmetic element-wise through broadcasting."},
        {"id": "numpy_018", "skill": "NumPy", "topic": "Vectorization", "question": "What is vectorization in NumPy?", "options": ["Applying operations to arrays without writing explicit Python loops for each element", "Converting every number into a vector graphic", "Sorting an array by its memory address", "Using only nested Python loops"], "correct_answer": "Applying operations to arrays without writing explicit Python loops for each element", "explanation": "Vectorized operations use optimized array operations and often reduce Python-level loop overhead."},
        {"id": "numpy_019", "skill": "NumPy", "topic": "Broadcasting", "question": "What does broadcasting allow NumPy to do?", "options": ["Perform compatible operations on arrays with different shapes", "Send arrays across a network automatically", "Convert all arrays to strings", "Guarantee every shape combination works"], "correct_answer": "Perform compatible operations on arrays with different shapes", "explanation": "Broadcasting aligns dimensions according to compatibility rules, but not every shape combination is valid."},
        {"id": "numpy_020", "skill": "NumPy", "topic": "Aggregation", "question": "What does np.sum(arr) calculate?", "options": ["The sum of array elements", "The largest array dimension", "The median only", "The number of unique values only"], "correct_answer": "The sum of array elements", "explanation": "np.sum adds array values, optionally along a specified axis."},
        {"id": "numpy_021", "skill": "NumPy", "topic": "Aggregation", "question": "What does np.mean(arr) calculate for numeric values?", "options": ["Arithmetic average", "Largest element", "Smallest element", "Number of dimensions"], "correct_answer": "Arithmetic average", "explanation": "np.mean computes the arithmetic mean of the selected values."},
        {"id": "numpy_022", "skill": "NumPy", "topic": "Aggregation", "question": "Which function returns the median of numeric array values?", "options": ["np.midpoint()", "np.median()", "np.middle_value()", "np.average_only()"], "correct_answer": "np.median()", "explanation": "np.median computes the middle value after considering the data order."},
        {"id": "numpy_023", "skill": "NumPy", "topic": "Aggregation", "question": "What does np.argmax(arr) return?", "options": ["The index of a maximum value", "The minimum value itself", "The sum of all indices", "The number of array dimensions"], "correct_answer": "The index of a maximum value", "explanation": "argmax returns the index of the first maximum along the selected axis by default."},
        {"id": "numpy_024", "skill": "NumPy", "topic": "Aggregation", "question": "What does np.std(arr) measure?", "options": ["Standard deviation", "The number of rows", "The median", "The data type"], "correct_answer": "Standard deviation", "explanation": "Standard deviation measures the spread of values around their mean."},
        {"id": "numpy_025", "skill": "NumPy", "topic": "Boolean Indexing", "question": "What does arr[arr > 5] return?", "options": ["Elements whose values are greater than 5", "Only elements equal to 5", "The indices of every element", "A sorted copy of the whole array"], "correct_answer": "Elements whose values are greater than 5", "explanation": "Boolean indexing selects elements where the condition evaluates to true."},
        {"id": "numpy_026", "skill": "NumPy", "topic": "Boolean Indexing", "question": "Which function returns the indices of elements satisfying a condition?", "options": ["np.where()", "np.reshape()", "np.transpose()", "np.linspace()"], "correct_answer": "np.where()", "explanation": "With a condition as its argument, np.where returns indices where the condition is true."},
        {"id": "numpy_027", "skill": "NumPy", "topic": "Array Combination", "question": "Which function commonly joins arrays along an existing axis?", "options": ["np.concatenate()", "np.average()", "np.argmax()", "np.std()"], "correct_answer": "np.concatenate()", "explanation": "concatenate joins arrays along an existing axis when the other dimensions are compatible."},
        {"id": "numpy_028", "skill": "NumPy", "topic": "Array Combination", "question": "What does np.vstack() do?", "options": ["Stacks arrays vertically", "Sorts all values in descending order", "Converts numbers into strings", "Finds the largest element"], "correct_answer": "Stacks arrays vertically", "explanation": "vstack combines arrays along the vertical direction, subject to compatible shapes."},
        {"id": "numpy_029", "skill": "NumPy", "topic": "Array Combination", "question": "What does np.hstack() do for compatible arrays?", "options": ["Stacks arrays horizontally", "Removes all columns", "Calculates a histogram only", "Reverses the array's data type"], "correct_answer": "Stacks arrays horizontally", "explanation": "hstack combines arrays along their horizontal direction."},
        {"id": "numpy_030", "skill": "NumPy", "topic": "Linear Algebra", "question": "Which operator performs matrix multiplication for compatible NumPy arrays?", "options": ["@", "%", "//", "**"], "correct_answer": "@", "explanation": "The @ operator performs matrix multiplication for supported array shapes."},
        {"id": "numpy_031", "skill": "NumPy", "topic": "Linear Algebra", "question": "Which NumPy function computes the dot product for suitable inputs?", "options": ["np.dot()", "np.merge()", "np.flatten()", "np.unique()"], "correct_answer": "np.dot()", "explanation": "np.dot computes dot products and, for two-dimensional arrays, matrix multiplication."},
        {"id": "numpy_032", "skill": "NumPy", "topic": "Linear Algebra", "question": "What does np.linalg.inv(A) attempt to calculate?", "options": ["The inverse of a square matrix A", "The average of A", "The unique elements of A", "The transpose of a string"], "correct_answer": "The inverse of a square matrix A", "explanation": "The function calculates a matrix inverse when the square matrix is nonsingular."},
        {"id": "numpy_033", "skill": "NumPy", "topic": "Random Numbers", "question": "What is a common use of np.random.default_rng()?", "options": ["Create a random number generator", "Sort an array in place", "Open a CSV file", "Calculate matrix rank only"], "correct_answer": "Create a random number generator", "explanation": "default_rng creates a Generator for random sampling."},
        {"id": "numpy_034", "skill": "NumPy", "topic": "Random Numbers", "question": "Why set a random generator seed when testing code?", "options": ["To make generated sequences reproducible", "To guarantee all numbers are unique", "To make arrays contain only zeros", "To increase array dimensions"], "correct_answer": "To make generated sequences reproducible", "explanation": "A fixed seed allows the same pseudorandom sequence to be reproduced with the same generator and calls."},
        {"id": "numpy_035", "skill": "NumPy", "topic": "Missing Values", "question": "Which function checks for NaN values in a NumPy array?", "options": ["np.isnan()", "np.isempty()", "np.ismissingonly()", "np.nancheckall()"], "correct_answer": "np.isnan()", "explanation": "np.isnan returns a Boolean result indicating which values are NaN."},
        {"id": "numpy_036", "skill": "NumPy", "topic": "Unique Values", "question": "What does np.unique(arr) return?", "options": ["The sorted unique values by default", "Only the largest value", "The original array with duplicates unchanged", "The array's shape only"], "correct_answer": "The sorted unique values by default", "explanation": "np.unique returns unique elements and can optionally return counts or indices."},
        {"id": "numpy_037", "skill": "NumPy", "topic": "Sorting", "question": "What does np.sort(arr) generally return?", "options": ["A sorted copy of the array", "The number of dimensions", "A Boolean mask only", "A random permutation every time"], "correct_answer": "A sorted copy of the array", "explanation": "np.sort returns a sorted copy by default, leaving the original array unchanged."},
        {"id": "numpy_038", "skill": "NumPy", "topic": "Copying and Views", "question": "What is an important difference between a NumPy view and a copy?", "options": ["A view may share underlying data with the original array, while a copy has separate data", "A copy always uses no memory", "A view always sorts its data", "There is never any difference"], "correct_answer": "A view may share underlying data with the original array, while a copy has separate data", "explanation": "Changes through a view can affect the original array when they share memory."},
        {"id": "numpy_039", "skill": "NumPy", "topic": "File Input and Output", "question": "Which function can save an array in NumPy's .npy format?", "options": ["np.save()", "np.export_html()", "np.write_sql()", "np.store_image()"], "correct_answer": "np.save()", "explanation": "np.save writes a single array to a binary .npy file."},
        {"id": "numpy_040", "skill": "NumPy", "topic": "Performance", "question": "Why are NumPy arrays often more efficient than Python lists for large numerical computations?", "options": ["They use typed storage and optimized array operations", "They never allocate memory", "They automatically distribute all work across the internet", "They guarantee every algorithm is O(1)"], "correct_answer": "They use typed storage and optimized array operations", "explanation": "Typed contiguous storage and optimized operations often reduce memory overhead and Python-level looping."}
    ],
    
    "pandas": [
        {"id": "pandas_001", "skill": "Pandas", "topic": "Basics", "question": "What is Pandas primarily used for?", "options": ["Data manipulation and analysis", "Building network routers", "Creating operating systems", "Designing HTML pages"], "correct_answer": "Data manipulation and analysis", "explanation": "Pandas provides data structures and tools for working with structured data."},
        {"id": "pandas_002", "skill": "Pandas", "topic": "Data Structures", "question": "Which Pandas structure is one-dimensional?", "options": ["DataFrame", "Series", "Index pair", "Panel table"], "correct_answer": "Series", "explanation": "A Series is a one-dimensional labeled array."},
        {"id": "pandas_003", "skill": "Pandas", "topic": "Data Structures", "question": "Which Pandas structure represents two-dimensional tabular data?", "options": ["Series", "Tuple", "DataFrame", "Scalar"], "correct_answer": "DataFrame", "explanation": "A DataFrame organizes data into labeled rows and columns."},
        {"id": "pandas_004", "skill": "Pandas", "topic": "Data Import", "question": "Which function reads a CSV file into a DataFrame?", "options": ["pd.open_csv()", "pd.read_csv()", "pd.load_table()", "pd.import_file()"], "correct_answer": "pd.read_csv()", "explanation": "read_csv loads comma-separated data into a DataFrame."},
        {"id": "pandas_005", "skill": "Pandas", "topic": "Data Export", "question": "Which method exports a DataFrame to a CSV file?", "options": ["to_csv()", "save_dataframe()", "write_table()", "export_series()"], "correct_answer": "to_csv()", "explanation": "DataFrame.to_csv() writes data to a CSV file."},
        {"id": "pandas_006", "skill": "Pandas", "topic": "Inspection", "question": "What does df.head() return by default?", "options": ["The last five rows", "The first five rows", "Only column names", "Only missing rows"], "correct_answer": "The first five rows", "explanation": "head() returns the first five rows by default."},
        {"id": "pandas_007", "skill": "Pandas", "topic": "Inspection", "question": "What does df.tail(3) return?", "options": ["The first three rows", "Three random rows", "The last three rows", "Three columns"], "correct_answer": "The last three rows", "explanation": "tail(3) returns the final three rows."},
        {"id": "pandas_008", "skill": "Pandas", "topic": "Inspection", "question": "Which attribute returns the number of rows and columns?", "options": ["df.size", "df.shape", "df.dtype", "df.index_only"], "correct_answer": "df.shape", "explanation": "shape returns a tuple containing the row and column counts."},
        {"id": "pandas_009", "skill": "Pandas", "topic": "Inspection", "question": "Which method shows column types and non-null counts?", "options": ["df.info()", "df.describe()", "df.sort()", "df.preview()"], "correct_answer": "df.info()", "explanation": "info() summarizes columns, data types, and non-null counts."},
        {"id": "pandas_010", "skill": "Pandas", "topic": "Statistics", "question": "What does df.describe() commonly provide for numeric columns?", "options": ["Only column names", "Summary statistics", "Only missing values", "A database connection"], "correct_answer": "Summary statistics", "explanation": "describe() provides statistics such as count, mean, standard deviation, and quartiles."},
        {"id": "pandas_011", "skill": "Pandas", "topic": "Selection", "question": "What is df['salary'] commonly used for?", "options": ["Selecting the salary column", "Deleting the DataFrame", "Sorting every column", "Reading a JSON file"], "correct_answer": "Selecting the salary column", "explanation": "Bracket selection by column name returns that column as a Series."},
        {"id": "pandas_012", "skill": "Pandas", "topic": "Selection", "question": "What does df.loc[] primarily use for selection?", "options": ["Label-based indexing", "Only physical memory addresses", "Random indexing", "File paths"], "correct_answer": "Label-based indexing", "explanation": "loc selects rows and columns using labels and Boolean conditions."},
        {"id": "pandas_013", "skill": "Pandas", "topic": "Selection", "question": "What does df.iloc[] use for selection?", "options": ["Column names only", "Integer-position indexing", "Database passwords", "File extensions"], "correct_answer": "Integer-position indexing", "explanation": "iloc selects rows and columns by their integer positions."},
        {"id": "pandas_014", "skill": "Pandas", "topic": "Filtering", "question": "How can you select rows where age is greater than 25?", "options": ["df['age' > 25]", "df[df['age'] > 25]", "df.select(age, 25)", "df.filter_rows(25)"], "correct_answer": "df[df['age'] > 25]", "explanation": "The Boolean condition creates a mask used to filter the rows."},
        {"id": "pandas_015", "skill": "Pandas", "topic": "Filtering", "question": "How do you combine two Boolean conditions element-wise in Pandas?", "options": ["Use and with Series conditions", "Use & with each condition in parentheses", "Use commas between conditions", "Use == between conditions"], "correct_answer": "Use & with each condition in parentheses", "explanation": "Pandas Series conditions are combined element-wise with operators such as & and |."},
        {"id": "pandas_016", "skill": "Pandas", "topic": "Missing Data", "question": "Which method identifies missing values?", "options": ["isnull()", "sort_values()", "reset_index()", "astype()"], "correct_answer": "isnull()", "explanation": "isnull() returns a Boolean result indicating missing values."},
        {"id": "pandas_017", "skill": "Pandas", "topic": "Missing Data", "question": "Which method removes rows containing missing values by default?", "options": ["fillna()", "dropna()", "replace()", "rename()"], "correct_answer": "dropna()", "explanation": "dropna() removes rows containing missing values by default."},
        {"id": "pandas_018", "skill": "Pandas", "topic": "Missing Data", "question": "Which method can replace missing values with a chosen value?", "options": ["fillna()", "drop_duplicates()", "head()", "memory_usage()"], "correct_answer": "fillna()", "explanation": "fillna() replaces missing values with a specified value or filling strategy."},
        {"id": "pandas_019", "skill": "Pandas", "topic": "Data Cleaning", "question": "Which method removes duplicate rows?", "options": ["drop_duplicates()", "remove_index()", "unique_rows_only()", "clear_columns()"], "correct_answer": "drop_duplicates()", "explanation": "drop_duplicates() removes duplicate rows according to the selected columns and options."},
        {"id": "pandas_020", "skill": "Pandas", "topic": "Data Cleaning", "question": "Which method changes a column's data type?", "options": ["astype()", "describe()", "head()", "groupby()"], "correct_answer": "astype()", "explanation": "astype() converts data to a specified type when conversion is supported."},
        {"id": "pandas_021", "skill": "Pandas", "topic": "Sorting", "question": "Which method sorts a DataFrame by a column's values?", "options": ["sort_values()", "sort_index_only()", "order_rows()", "arrange_file()"], "correct_answer": "sort_values()", "explanation": "sort_values() sorts rows using the values in specified columns."},
        {"id": "pandas_022", "skill": "Pandas", "topic": "Sorting", "question": "Which method sorts a DataFrame by its index labels?", "options": ["sort_values()", "sort_index()", "sort_columns()", "index_order()"], "correct_answer": "sort_index()", "explanation": "sort_index() orders rows or columns according to index labels."},
        {"id": "pandas_023", "skill": "Pandas", "topic": "Grouping", "question": "What is the main purpose of groupby()?", "options": ["Group data to calculate summaries for each group", "Delete all duplicate columns", "Read an Excel file", "Convert every value to text"], "correct_answer": "Group data to calculate summaries for each group", "explanation": "groupby() supports split-apply-combine operations."},
        {"id": "pandas_024", "skill": "Pandas", "topic": "Grouping", "question": "What does df.groupby('department')['salary'].mean() calculate?", "options": ["Overall maximum salary only", "Mean salary for each department", "Number of columns in each department", "All salaries sorted alphabetically"], "correct_answer": "Mean salary for each department", "explanation": "The operation groups by department and calculates the mean salary per group."},
        {"id": "pandas_025", "skill": "Pandas", "topic": "Aggregation", "question": "Which method counts non-missing values in each column by default?", "options": ["count()", "sum()", "nunique()", "dropna()"], "correct_answer": "count()", "explanation": "count() counts non-missing values along the chosen axis."},
        {"id": "pandas_026", "skill": "Pandas", "topic": "Aggregation", "question": "Which method counts the number of distinct values in a Series?", "options": ["nunique()", "unique_count_only()", "shape()", "columns()"], "correct_answer": "nunique()", "explanation": "nunique() returns the number of distinct values, excluding missing values by default."},
        {"id": "pandas_027", "skill": "Pandas", "topic": "Combining Data", "question": "Which function combines DataFrames using database-style join logic?", "options": ["pd.merge()", "pd.reshape()", "pd.describe()", "pd.fill()"], "correct_answer": "pd.merge()", "explanation": "merge() combines DataFrames using matching key columns or indexes."},
        {"id": "pandas_028", "skill": "Pandas", "topic": "Combining Data", "question": "Which function stacks DataFrames along an axis?", "options": ["pd.concat()", "pd.describe()", "pd.cut()", "pd.isna()"], "correct_answer": "pd.concat()", "explanation": "concat() combines objects along rows or columns."},
        {"id": "pandas_029", "skill": "Pandas", "topic": "Combining Data", "question": "What is the default join type for pd.merge(left, right, on='id')?", "options": ["Outer join", "Inner join", "Left join", "Cross join"], "correct_answer": "Inner join", "explanation": "merge() uses an inner join by default, retaining matching keys."},
        {"id": "pandas_030", "skill": "Pandas", "topic": "Indexing", "question": "What does reset_index() commonly do?", "options": ["Moves the existing index into columns and creates a default index", "Deletes every row", "Sorts all numeric columns", "Converts the DataFrame to JSON"], "correct_answer": "Moves the existing index into columns and creates a default index", "explanation": "By default, reset_index() replaces the index with a default integer index and preserves the old index as a column."},
        {"id": "pandas_031", "skill": "Pandas", "topic": "Indexing", "question": "What does set_index('id') do by default?", "options": ["Uses the id column as the index", "Deletes the id column and every row", "Sorts all columns by id", "Creates a new database"], "correct_answer": "Uses the id column as the index", "explanation": "set_index() uses the selected column as the DataFrame index; drop=True by default removes it from the ordinary columns."},
        {"id": "pandas_032", "skill": "Pandas", "topic": "Text Processing", "question": "Which accessor provides vectorized string operations for a Series?", "options": [".str", ".text", ".string_methods_only", ".chars"], "correct_answer": ".str", "explanation": "The .str accessor provides string operations for Series values."},
        {"id": "pandas_033", "skill": "Pandas", "topic": "Text Processing", "question": "Which operation can convert strings to lowercase in a text column?", "options": ["series.str.lower()", "series.to_numeric()", "series.sort_index()", "series.groupby()"], "correct_answer": "series.str.lower()", "explanation": "str.lower() converts string values to lowercase."},
        {"id": "pandas_034", "skill": "Pandas", "topic": "Date and Time", "question": "Which function converts supported values to Pandas datetime values?", "options": ["pd.to_datetime()", "pd.to_timestamp_text()", "pd.date_column()", "pd.time_parse_only()"], "correct_answer": "pd.to_datetime()", "explanation": "to_datetime() converts supported input into datetime-like values."},
        {"id": "pandas_035", "skill": "Pandas", "topic": "Date and Time", "question": "After converting a Series to datetime, which accessor can extract its year?", "options": [".dt.year", ".str.year", ".index.year_only", ".date.year_text"], "correct_answer": ".dt.year", "explanation": "The .dt accessor exposes datetime components such as year and month."},
        {"id": "pandas_036", "skill": "Pandas", "topic": "Reshaping", "question": "What does pivot_table() commonly do?", "options": ["Summarizes data across row and column categories", "Deletes all missing values", "Converts every value to a string", "Loads a database driver"], "correct_answer": "Summarizes data across row and column categories", "explanation": "pivot_table() creates a spreadsheet-like summary using grouping and aggregation."},
        {"id": "pandas_037", "skill": "Pandas", "topic": "Reshaping", "question": "What does melt() generally do?", "options": ["Transforms wide data into a longer format", "Sorts all columns alphabetically", "Removes every row with a number", "Creates a database index"], "correct_answer": "Transforms wide data into a longer format", "explanation": "melt() unpivots selected columns into variable and value columns."},
        {"id": "pandas_038", "skill": "Pandas", "topic": "Categorical Data", "question": "What is a common benefit of using categorical dtype for repeated labels?", "options": ["It may reduce memory usage and support category-aware operations", "It guarantees all missing values disappear", "It converts categories into database tables", "It makes every operation constant time"], "correct_answer": "It may reduce memory usage and support category-aware operations", "explanation": "Categorical data stores category codes and a set of categories, which can save memory for repeated values."},
        {"id": "pandas_039", "skill": "Pandas", "topic": "Performance", "question": "Which approach is usually preferable for a simple element-wise numeric calculation in Pandas?", "options": ["Use vectorized operations when suitable", "Always loop through every cell in Python", "Convert the entire DataFrame to HTML first", "Create a separate database for each row"], "correct_answer": "Use vectorized operations when suitable", "explanation": "Vectorized operations often reduce Python-loop overhead and use optimized underlying routines."},
        {"id": "pandas_040", "skill": "Pandas", "topic": "Export", "question": "Which method exports a DataFrame to an Excel workbook?", "options": ["to_excel()", "write_xlsx_only()", "excel_export_table()", "save_sheet_data()"], "correct_answer": "to_excel()", "explanation": "DataFrame.to_excel() writes tabular data to an Excel file when a compatible engine is available."}
    ],

    "scikit-learn": [
        {"id": "sklearn_001", "skill": "scikit-learn", "topic": "Basics", "question": "What is scikit-learn primarily used for?", "options": ["Machine learning in Python", "Building operating systems", "Editing videos", "Managing network switches"], "correct_answer": "Machine learning in Python", "explanation": "scikit-learn provides tools for supervised and unsupervised learning, preprocessing, and evaluation."},
        {"id": "sklearn_002", "skill": "scikit-learn", "topic": "Estimator API", "question": "Which method typically learns model parameters from training data?", "options": ["fit()", "predict_only()", "render()", "compile_html()"], "correct_answer": "fit()", "explanation": "fit() trains an estimator using the supplied data."},
        {"id": "sklearn_003", "skill": "scikit-learn", "topic": "Estimator API", "question": "Which method commonly produces predictions from a trained estimator?", "options": ["fit()", "predict()", "describe()", "groupby()"], "correct_answer": "predict()", "explanation": "predict() produces outputs using a fitted estimator."},
        {"id": "sklearn_004", "skill": "scikit-learn", "topic": "Estimator API", "question": "What is the purpose of fit_transform() in a transformer?", "options": ["Fit the transformation and apply it to the supplied data", "Only evaluate model accuracy", "Delete training labels", "Save a web page"], "correct_answer": "Fit the transformation and apply it to the supplied data", "explanation": "fit_transform() learns transformation parameters and returns transformed data."},
        {"id": "sklearn_005", "skill": "scikit-learn", "topic": "Data Preparation", "question": "What does train_test_split() help do?", "options": ["Split data into subsets such as training and testing", "Sort all features alphabetically", "Create a database connection", "Remove every categorical feature"], "correct_answer": "Split data into subsets such as training and testing", "explanation": "It divides input arrays or datasets into separate subsets."},
        {"id": "sklearn_006", "skill": "scikit-learn", "topic": "Data Preparation", "question": "Why use random_state in a train-test split?", "options": ["To make the random split reproducible", "To guarantee a perfect model", "To eliminate all missing data", "To force every class to be equally sized"], "correct_answer": "To make the random split reproducible", "explanation": "A fixed random state makes repeated splits reproducible for the same data and settings."},
        {"id": "sklearn_007", "skill": "scikit-learn", "topic": "Preprocessing", "question": "What does StandardScaler generally do?", "options": ["Centers features and scales them to unit variance", "Converts all values to strings", "Removes the target column", "Creates additional training labels"], "correct_answer": "Centers features and scales them to unit variance", "explanation": "StandardScaler subtracts the training mean and scales by the training standard deviation."},
        {"id": "sklearn_008", "skill": "scikit-learn", "topic": "Preprocessing", "question": "What is the main purpose of MinMaxScaler?", "options": ["Scale features to a specified range, commonly 0 to 1", "Always convert features to integers", "Remove all outliers", "Create a decision tree"], "correct_answer": "Scale features to a specified range, commonly 0 to 1", "explanation": "MinMaxScaler maps feature values to a selected range based on training data extrema."},
        {"id": "sklearn_009", "skill": "scikit-learn", "topic": "Preprocessing", "question": "Which transformer can replace missing numeric values with the median?", "options": ["SimpleImputer(strategy='median')", "StandardScaler(strategy='median')", "PCA(strategy='median')", "KFold(strategy='median')"], "correct_answer": "SimpleImputer(strategy='median')", "explanation": "SimpleImputer supports median imputation for numeric features."},
        {"id": "sklearn_010", "skill": "scikit-learn", "topic": "Preprocessing", "question": "Which transformer converts categorical values into indicator columns?", "options": ["OneHotEncoder", "LinearRegression", "KMeans", "PCA"], "correct_answer": "OneHotEncoder", "explanation": "OneHotEncoder represents categories using separate binary columns."},
        {"id": "sklearn_011", "skill": "scikit-learn", "topic": "Classification", "question": "Which estimator is commonly used for binary classification?", "options": ["LogisticRegression", "LinearRegression only", "PCA", "StandardScaler"], "correct_answer": "LogisticRegression", "explanation": "Despite its name, LogisticRegression is a classification estimator."},
        {"id": "sklearn_012", "skill": "scikit-learn", "topic": "Classification", "question": "Which estimator can classify data using a tree of feature-based decisions?", "options": ["DecisionTreeClassifier", "StandardScaler", "SimpleImputer", "PCA"], "correct_answer": "DecisionTreeClassifier", "explanation": "A decision tree learns feature-based splits to predict class labels."},
        {"id": "sklearn_013", "skill": "scikit-learn", "topic": "Classification", "question": "What is a common advantage of RandomForestClassifier?", "options": ["It combines predictions from multiple decision trees", "It requires no training data", "It only supports text generation", "It always has zero prediction error"], "correct_answer": "It combines predictions from multiple decision trees", "explanation": "A random forest aggregates many randomized trees to improve generalization."},
        {"id": "sklearn_014", "skill": "scikit-learn", "topic": "Classification", "question": "Which classifier is based on the idea of finding a separating boundary with a large margin?", "options": ["SVC", "KMeans", "PCA", "LinearRegression"], "correct_answer": "SVC", "explanation": "Support Vector Classification seeks a decision boundary with a large margin, using kernels when configured."},
        {"id": "sklearn_015", "skill": "scikit-learn", "topic": "Classification", "question": "What does KNeighborsClassifier use to make a prediction?", "options": ["Labels of nearby training samples", "Only the largest feature name", "A fixed database query", "Random labels regardless of input"], "correct_answer": "Labels of nearby training samples", "explanation": "K-nearest neighbors predicts from the labels of the selected nearest samples."},
        {"id": "sklearn_016", "skill": "scikit-learn", "topic": "Regression", "question": "Which estimator is designed to predict continuous numeric values using a linear relationship?", "options": ["LinearRegression", "KMeans", "OneHotEncoder", "LabelEncoder"], "correct_answer": "LinearRegression", "explanation": "LinearRegression fits coefficients for a linear prediction function."},
        {"id": "sklearn_017", "skill": "scikit-learn", "topic": "Regression", "question": "Which metric calculates the average squared prediction error?", "options": ["mean_squared_error", "accuracy_score", "precision_score", "roc_auc_score"], "correct_answer": "mean_squared_error", "explanation": "Mean squared error averages the squared differences between true and predicted values."},
        {"id": "sklearn_018", "skill": "scikit-learn", "topic": "Regression", "question": "What does an R² score generally measure in regression?", "options": ["How well predictions explain variation relative to a baseline", "The number of input columns", "The training time in seconds", "The count of missing values"], "correct_answer": "How well predictions explain variation relative to a baseline", "explanation": "R² compares model fit with a constant-mean baseline; it can be negative for poor predictions."},
        {"id": "sklearn_019", "skill": "scikit-learn", "topic": "Clustering", "question": "Which estimator groups samples into a specified number of clusters?", "options": ["KMeans", "LogisticRegression", "StandardScaler", "GridSearchCV"], "correct_answer": "KMeans", "explanation": "KMeans partitions samples into k clusters based on distances to cluster centers."},
        {"id": "sklearn_020", "skill": "scikit-learn", "topic": "Dimensionality Reduction", "question": "What is PCA commonly used for?", "options": ["Reducing dimensionality by projecting data onto principal components", "Creating target labels automatically in all cases", "Replacing train-test splits", "Converting Python into SQL"], "correct_answer": "Reducing dimensionality by projecting data onto principal components", "explanation": "PCA identifies directions of high variance and projects data into a lower-dimensional space."},
        {"id": "sklearn_021", "skill": "scikit-learn", "topic": "Evaluation", "question": "What does accuracy_score calculate for classification?", "options": ["The fraction of predictions that are correct", "The average feature magnitude", "The number of clusters", "The training dataset size only"], "correct_answer": "The fraction of predictions that are correct", "explanation": "Accuracy is the number of correct predictions divided by the total predictions."},
        {"id": "sklearn_022", "skill": "scikit-learn", "topic": "Evaluation", "question": "What does precision measure for a particular positive class?", "options": ["The fraction of predicted positives that are truly positive", "The fraction of all negatives correctly identified", "The total number of training features", "The percentage of missing data"], "correct_answer": "The fraction of predicted positives that are truly positive", "explanation": "Precision equals true positives divided by true positives plus false positives."},
        {"id": "sklearn_023", "skill": "scikit-learn", "topic": "Evaluation", "question": "What does recall measure for a positive class?", "options": ["The fraction of actual positives that are identified", "The fraction of predicted positives that are correct", "The total number of model parameters", "The average training time"], "correct_answer": "The fraction of actual positives that are identified", "explanation": "Recall equals true positives divided by true positives plus false negatives."},
        {"id": "sklearn_024", "skill": "scikit-learn", "topic": "Evaluation", "question": "What does a confusion matrix summarize?", "options": ["Counts of actual versus predicted classes", "Feature scaling ranges only", "The time needed to import a library", "Database table relationships"], "correct_answer": "Counts of actual versus predicted classes", "explanation": "A confusion matrix shows correct and incorrect predictions by class."},
        {"id": "sklearn_025", "skill": "scikit-learn", "topic": "Evaluation", "question": "What is cross-validation commonly used for?", "options": ["Assessing model performance across multiple data splits", "Removing all model parameters", "Replacing all features with zeros", "Creating an HTML interface"], "correct_answer": "Assessing model performance across multiple data splits", "explanation": "Cross-validation evaluates a model across several train-validation splits."},
        {"id": "sklearn_026", "skill": "scikit-learn", "topic": "Hyperparameter Tuning", "question": "What does GridSearchCV do?", "options": ["Searches specified parameter combinations using cross-validation", "Automatically repairs missing source files", "Only computes a confusion matrix", "Converts a classifier to a database"], "correct_answer": "Searches specified parameter combinations using cross-validation", "explanation": "GridSearchCV evaluates a defined parameter grid using cross-validation."},
        {"id": "sklearn_027", "skill": "scikit-learn", "topic": "Hyperparameter Tuning", "question": "What is a hyperparameter?", "options": ["A setting chosen before or during model selection rather than learned as an ordinary model parameter", "A label that must be predicted", "A missing row in a DataFrame", "A feature that is always removed"], "correct_answer": "A setting chosen before or during model selection rather than learned as an ordinary model parameter", "explanation": "Hyperparameters include choices such as tree depth or the number of neighbors."},
        {"id": "sklearn_028", "skill": "scikit-learn", "topic": "Pipelines", "question": "What is the purpose of sklearn.pipeline.Pipeline?", "options": ["Chain transformers and an optional final estimator into one workflow", "Only store images", "Create network routes", "Replace all evaluation metrics"], "correct_answer": "Chain transformers and an optional final estimator into one workflow", "explanation": "A pipeline applies transformations in sequence and then fits or uses the final estimator."},
        {"id": "sklearn_029", "skill": "scikit-learn", "topic": "Data Leakage", "question": "How can a pipeline help prevent preprocessing leakage during cross-validation?", "options": ["It fits preprocessing steps separately within each training fold", "It trains every step on the test labels", "It removes the need for validation", "It guarantees the data has no missing values"], "correct_answer": "It fits preprocessing steps separately within each training fold", "explanation": "Pipeline fitting within each fold prevents preprocessing parameters from being learned from validation data."},
        {"id": "sklearn_030", "skill": "scikit-learn", "topic": "Data Leakage", "question": "Which practice helps avoid leakage when scaling train and test data?", "options": ["Fit the scaler on training data and transform both sets", "Fit a separate scaler on the full dataset before splitting", "Scale using the test labels", "Skip all data splitting"], "correct_answer": "Fit the scaler on training data and transform both sets", "explanation": "The test set must not influence preprocessing parameters learned during training."},
        {"id": "sklearn_031", "skill": "scikit-learn", "topic": "Feature Selection", "question": "What is the purpose of feature selection?", "options": ["Choose a subset of useful input features", "Increase the number of labels without evidence", "Convert all features into database tables", "Remove the target from every evaluation"], "correct_answer": "Choose a subset of useful input features", "explanation": "Feature selection can reduce complexity and remove irrelevant or redundant inputs."},
        {"id": "sklearn_032", "skill": "scikit-learn", "topic": "Ensemble Learning", "question": "What is the basic idea of bagging?", "options": ["Train models on sampled datasets and combine their predictions", "Train only one model without data", "Remove all model predictions", "Use the test set as training data repeatedly"], "correct_answer": "Train models on sampled datasets and combine their predictions", "explanation": "Bagging trains estimators on bootstrap samples and aggregates their predictions."},
        {"id": "sklearn_033", "skill": "scikit-learn", "topic": "Class Imbalance", "question": "Why can accuracy be misleading on a highly imbalanced classification dataset?", "options": ["A model may predict the majority class and still score high accuracy", "Accuracy always becomes negative", "Imbalanced data cannot be used for classification", "Accuracy measures only training time"], "correct_answer": "A model may predict the majority class and still score high accuracy", "explanation": "Precision, recall, F1, and suitable class-specific metrics may reveal errors hidden by accuracy."},
        {"id": "sklearn_034", "skill": "scikit-learn", "topic": "Class Imbalance", "question": "Which option is commonly available in some scikit-learn classifiers to address unequal class importance?", "options": ["class_weight", "table_color", "html_mode", "network_port"], "correct_answer": "class_weight", "explanation": "Supported estimators can use class_weight to assign different penalties to class errors."},
        {"id": "sklearn_035", "skill": "scikit-learn", "topic": "Model Persistence", "question": "What is a common way to persist a fitted scikit-learn model?", "options": ["joblib.dump()", "df.head()", "np.linspace()", "pd.groupby()"], "correct_answer": "joblib.dump()", "explanation": "joblib can serialize fitted Python objects, including many scikit-learn models."},
        {"id": "sklearn_036", "skill": "scikit-learn", "topic": "Model Persistence", "question": "Why should a serialized model file from an untrusted source be handled carefully?", "options": ["Some Python serialization formats can execute code during loading", "It always contains only plain text", "It cannot contain model parameters", "It automatically deletes the training data"], "correct_answer": "Some Python serialization formats can execute code during loading", "explanation": "Pickle-based formats can execute arbitrary code, so only load trusted artifacts."},
        {"id": "sklearn_037", "skill": "scikit-learn", "topic": "Probability", "question": "Which method commonly returns class probability estimates when supported by a classifier?", "options": ["predict_proba()", "fit_transform()", "inverse_scale()", "split_labels()"], "correct_answer": "predict_proba()", "explanation": "predict_proba() returns estimated class probabilities for estimators that support it."},
        {"id": "sklearn_038", "skill": "scikit-learn", "topic": "Unsupervised Learning", "question": "Which statement describes unsupervised learning?", "options": ["Learning patterns from data without supplied target labels", "Learning only from manually labeled outputs", "Using no input data", "Always predicting a continuous target"], "correct_answer": "Learning patterns from data without supplied target labels", "explanation": "Unsupervised methods discover structure such as clusters or lower-dimensional representations."},
        {"id": "sklearn_039", "skill": "scikit-learn", "topic": "Reproducibility", "question": "Why set random_state for a randomized estimator when supported?", "options": ["To make randomized behavior reproducible", "To guarantee perfect generalization", "To increase the number of classes", "To prevent every model update"], "correct_answer": "To make randomized behavior reproducible", "explanation": "A fixed random state helps reproduce randomized training or sampling behavior."},
        {"id": "sklearn_040", "skill": "scikit-learn", "topic": "Model Selection", "question": "Why should a final test set be kept separate from repeated model tuning?", "options": ["To obtain a less biased estimate of performance on unseen data", "To make training accuracy equal to test accuracy", "To eliminate the need for features", "To ensure every model gets a perfect score"], "correct_answer": "To obtain a less biased estimate of performance on unseen data", "explanation": "Repeated tuning against the test set leaks information from it into model selection."}
    ],

    "machine learning": [
        {"id": "ml_001", "skill": "Machine Learning", "topic": "Fundamentals", "question": "What is machine learning?", "options": ["A field where systems learn patterns from data", "A method for designing only web pages", "A database backup technique", "A hardware cable standard"], "correct_answer": "A field where systems learn patterns from data", "explanation": "Machine learning uses data and algorithms to learn patterns for prediction or decision-making."},
        {"id": "ml_002", "skill": "Machine Learning", "topic": "Learning Types", "question": "What characterizes supervised learning?", "options": ["Training data includes target labels or outcomes", "Training data never contains inputs", "The algorithm cannot make predictions", "Every result is chosen randomly"], "correct_answer": "Training data includes target labels or outcomes", "explanation": "Supervised algorithms learn relationships between input features and known targets."},
        {"id": "ml_003", "skill": "Machine Learning", "topic": "Learning Types", "question": "Which task is an example of classification?", "options": ["Predicting whether an email is spam", "Predicting the exact house price", "Calculating a column sum", "Sorting filenames alphabetically"], "correct_answer": "Predicting whether an email is spam", "explanation": "Classification predicts discrete categories such as spam or not spam."},
        {"id": "ml_004", "skill": "Machine Learning", "topic": "Learning Types", "question": "Which task is an example of regression?", "options": ["Predicting a house's sale price", "Classifying an image as cat or dog", "Grouping customers without labels", "Detecting whether a password contains a symbol"], "correct_answer": "Predicting a house's sale price", "explanation": "Regression predicts numeric values, such as a price."},
        {"id": "ml_005", "skill": "Machine Learning", "topic": "Learning Types", "question": "What is unsupervised learning?", "options": ["Learning structure from data without supplied target labels", "Learning only from labeled outcomes", "Using no data at all", "Always predicting a known class"], "correct_answer": "Learning structure from data without supplied target labels", "explanation": "Unsupervised methods can discover groups or compact representations without target labels."},
        {"id": "ml_006", "skill": "Machine Learning", "topic": "Learning Types", "question": "What is reinforcement learning based on?", "options": ["An agent learning through actions and rewards", "Only sorting labeled rows", "A fixed list of database queries", "Manual assignment of every future action"], "correct_answer": "An agent learning through actions and rewards", "explanation": "An agent interacts with an environment and learns a policy to maximize cumulative reward."},
        {"id": "ml_007", "skill": "Machine Learning", "topic": "Dataset Splitting", "question": "Why split data into training and test sets?", "options": ["To evaluate how well a model generalizes to unseen data", "To guarantee zero prediction errors", "To increase the number of original observations", "To remove the need for evaluation"], "correct_answer": "To evaluate how well a model generalizes to unseen data", "explanation": "A separate test set estimates performance on data not used for fitting."},
        {"id": "ml_008", "skill": "Machine Learning", "topic": "Dataset Splitting", "question": "What is the purpose of a validation set?", "options": ["Help select models or tune hyperparameters", "Replace all training data permanently", "Guarantee the test score is 100%", "Store only the target column"], "correct_answer": "Help select models or tune hyperparameters", "explanation": "Validation data helps compare model choices without repeatedly using the final test set."},
        {"id": "ml_009", "skill": "Machine Learning", "topic": "Overfitting", "question": "What is overfitting?", "options": ["A model learns training details that do not generalize well", "A model is never trained", "A dataset contains no features", "A model always predicts the average"], "correct_answer": "A model learns training details that do not generalize well", "explanation": "Overfit models perform well on training data but poorly on unseen examples."},
        {"id": "ml_010", "skill": "Machine Learning", "topic": "Underfitting", "question": "What is underfitting?", "options": ["A model is too simple or insufficiently trained to capture important patterns", "A model memorizes every training example", "A test dataset is always too large", "A model has no input features by definition"], "correct_answer": "A model is too simple or insufficiently trained to capture important patterns", "explanation": "Underfitting commonly produces poor performance on both training and unseen data."},
        {"id": "ml_011", "skill": "Machine Learning", "topic": "Bias and Variance", "question": "What does high variance commonly indicate?", "options": ["The model is sensitive to changes in its training data", "The model always predicts a constant", "The model has no parameters", "The dataset contains no noise"], "correct_answer": "The model is sensitive to changes in its training data", "explanation": "High-variance models can fit training data closely and generalize poorly."},
        {"id": "ml_012", "skill": "Machine Learning", "topic": "Bias and Variance", "question": "What does high bias commonly indicate?", "options": ["The model makes overly simple assumptions and misses patterns", "The model has memorized all noise", "The model has unlimited flexibility", "The dataset is perfectly balanced"], "correct_answer": "The model makes overly simple assumptions and misses patterns", "explanation": "High bias is associated with overly restrictive models and underfitting."},
        {"id": "ml_013", "skill": "Machine Learning", "topic": "Feature Engineering", "question": "What is feature engineering?", "options": ["Creating or transforming useful input variables from available data", "Replacing all targets with random values", "Deleting the model after training", "Changing the operating system"], "correct_answer": "Creating or transforming useful input variables from available data", "explanation": "Feature engineering prepares informative representations for learning algorithms."},
        {"id": "ml_014", "skill": "Machine Learning", "topic": "Feature Scaling", "question": "Why can feature scaling matter for algorithms such as K-nearest neighbors?", "options": ["Features with larger numeric scales can dominate distance calculations", "It guarantees no missing values", "It turns classification into regression", "It removes the need for training"], "correct_answer": "Features with larger numeric scales can dominate distance calculations", "explanation": "Distance-based algorithms can be strongly affected by differences in feature scales."},
        {"id": "ml_015", "skill": "Machine Learning", "topic": "Feature Scaling", "question": "Which algorithm is often less sensitive to feature scaling than distance-based methods?", "options": ["Decision tree", "K-nearest neighbors", "K-means", "RBF-kernel SVM"], "correct_answer": "Decision tree", "explanation": "Tree splits depend on feature ordering and thresholds, so monotonic scaling generally has less effect than for distance-based methods."},
        {"id": "ml_016", "skill": "Machine Learning", "topic": "Data Leakage", "question": "What is data leakage?", "options": ["Using information during training that would not legitimately be available at prediction time", "A model using a training set", "Splitting data before training", "Measuring a model's accuracy"], "correct_answer": "Using information during training that would not legitimately be available at prediction time", "explanation": "Leakage creates misleading evaluation results by exposing inappropriate information to model development."},
        {"id": "ml_017", "skill": "Machine Learning", "topic": "Data Leakage", "question": "What is a good way to avoid leakage when imputing missing values?", "options": ["Fit the imputer on training data only, then transform validation and test data", "Calculate imputation values using the entire dataset before splitting", "Use the test labels to fill missing features", "Remove the test set after every prediction"], "correct_answer": "Fit the imputer on training data only, then transform validation and test data", "explanation": "Learning preprocessing values only from training data prevents information from evaluation data leaking into training."},
        {"id": "ml_018", "skill": "Machine Learning", "topic": "Evaluation Metrics", "question": "When can accuracy be a misleading classification metric?", "options": ["When classes are highly imbalanced", "When all examples have labels", "When a model makes predictions", "When a dataset contains two columns"], "correct_answer": "When classes are highly imbalanced", "explanation": "A model can achieve high accuracy by predicting the majority class while missing minority cases."},
        {"id": "ml_019", "skill": "Machine Learning", "topic": "Evaluation Metrics", "question": "What is the F1 score?", "options": ["The harmonic mean of precision and recall", "The arithmetic mean of every feature", "The number of false positives only", "The square of accuracy in all cases"], "correct_answer": "The harmonic mean of precision and recall", "explanation": "F1 balances precision and recall using their harmonic mean."},
        {"id": "ml_020", "skill": "Machine Learning", "topic": "Evaluation Metrics", "question": "What does mean absolute error measure?", "options": ["The average absolute difference between predictions and true values", "The fraction of correct classification labels", "The number of model parameters", "The variance of the target labels only"], "correct_answer": "The average absolute difference between predictions and true values", "explanation": "MAE averages the absolute prediction errors."},
        {"id": "ml_021", "skill": "Machine Learning", "topic": "Evaluation Metrics", "question": "What is a false positive in binary classification?", "options": ["A negative example incorrectly predicted as positive", "A positive example correctly predicted as positive", "A negative example correctly predicted as negative", "A positive example incorrectly predicted as negative"], "correct_answer": "A negative example incorrectly predicted as positive", "explanation": "A false positive is a negative case incorrectly classified as positive."},
        {"id": "ml_022", "skill": "Machine Learning", "topic": "Evaluation Metrics", "question": "What is a false negative?", "options": ["A positive example incorrectly predicted as negative", "A negative example incorrectly predicted as positive", "A positive example correctly predicted as positive", "A negative example correctly predicted as negative"], "correct_answer": "A positive example incorrectly predicted as negative", "explanation": "A false negative occurs when a real positive case is missed."},
        {"id": "ml_023", "skill": "Machine Learning", "topic": "Linear Models", "question": "What is the main assumption of ordinary linear regression about the modeled relationship?", "options": ["The target is represented as a linear function of the features and coefficients", "The target must always be a category", "All features must be text", "The training data must have no rows"], "correct_answer": "The target is represented as a linear function of the features and coefficients", "explanation": "Linear regression models the expected target as a linear combination of features and coefficients."},
        {"id": "ml_024", "skill": "Machine Learning", "topic": "Linear Models", "question": "What is logistic regression commonly used for?", "options": ["Classification", "Image file compression only", "Database indexing", "Operating system scheduling"], "correct_answer": "Classification", "explanation": "Logistic regression models class probabilities and is commonly used for classification."},
        {"id": "ml_025", "skill": "Machine Learning", "topic": "Regularization", "question": "What is the purpose of regularization?", "options": ["Penalize model complexity to help reduce overfitting", "Increase every coefficient without limit", "Remove the need for training data", "Guarantee a perfect training score"], "correct_answer": "Penalize model complexity to help reduce overfitting", "explanation": "Regularization discourages overly complex models and may improve generalization."},
        {"id": "ml_026", "skill": "Machine Learning", "topic": "Regularization", "question": "Which regularization method commonly encourages some coefficients to become exactly zero?", "options": ["L1 regularization", "L2 regularization only", "Min-max scaling", "One-hot encoding"], "correct_answer": "L1 regularization", "explanation": "The L1 penalty can produce sparse coefficient vectors."},
        {"id": "ml_027", "skill": "Machine Learning", "topic": "Regularization", "question": "What is a common effect of L2 regularization?", "options": ["Penalizing large squared coefficient values", "Forcing every coefficient to be exactly one", "Removing the target column", "Turning continuous values into categories"], "correct_answer": "Penalizing large squared coefficient values", "explanation": "L2 regularization discourages large coefficients and is commonly associated with weight shrinkage."},
        {"id": "ml_028", "skill": "Machine Learning", "topic": "Decision Trees", "question": "How does a decision tree make predictions?", "options": ["Follow feature-based splits from the root to a leaf", "Average every row without using features", "Choose a random target for each input", "Use only the dataset filename"], "correct_answer": "Follow feature-based splits from the root to a leaf", "explanation": "A tree applies learned decision rules until it reaches a prediction leaf."},
        {"id": "ml_029", "skill": "Machine Learning", "topic": "Ensemble Learning", "question": "What is the basic idea behind a random forest?", "options": ["Combine predictions from many randomized decision trees", "Use one fixed linear equation only", "Remove all training examples", "Predict solely from column names"], "correct_answer": "Combine predictions from many randomized decision trees", "explanation": "Random forests aggregate predictions from trees trained with data and feature randomness."},
        {"id": "ml_030", "skill": "Machine Learning", "topic": "Ensemble Learning", "question": "What is boosting?", "options": ["Build models sequentially so later models focus on previous errors or residuals", "Train only one model without feedback", "Remove the need for labels in every task", "Randomly delete all difficult examples"], "correct_answer": "Build models sequentially so later models focus on previous errors or residuals", "explanation": "Boosting combines sequentially trained weak learners to improve predictive performance."},
        {"id": "ml_031", "skill": "Machine Learning", "topic": "Clustering", "question": "What is the objective of K-means clustering?", "options": ["Partition samples into k groups using distances to cluster centroids", "Predict a known target label only", "Find the largest database table", "Create a linear regression equation"], "correct_answer": "Partition samples into k groups using distances to cluster centroids", "explanation": "K-means seeks clusters that minimize within-cluster squared distances to centroids."},
        {"id": "ml_032", "skill": "Machine Learning", "topic": "Clustering", "question": "What is a limitation of K-means?", "options": ["The number of clusters k must be specified", "It cannot process numeric data", "It always requires class labels", "It only works with text documents"], "correct_answer": "The number of clusters k must be specified", "explanation": "Standard K-means requires a chosen number of clusters before fitting."},
        {"id": "ml_033", "skill": "Machine Learning", "topic": "Dimensionality Reduction", "question": "Why might dimensionality reduction be useful?", "options": ["Reduce feature count while retaining useful structure", "Guarantee every prediction is correct", "Increase missing data deliberately", "Remove all relationships from data"], "correct_answer": "Reduce feature count while retaining useful structure", "explanation": "Dimensionality reduction can simplify models, reduce noise, and help visualization."},
        {"id": "ml_034", "skill": "Machine Learning", "topic": "Hyperparameters", "question": "What is hyperparameter tuning?", "options": ["Choosing settings that improve validation performance", "Changing test labels to match predictions", "Removing all input features", "Changing the database password"], "correct_answer": "Choosing settings that improve validation performance", "explanation": "Tuning compares candidate settings using validation data or cross-validation."},
        {"id": "ml_035", "skill": "Machine Learning", "topic": "Cross-Validation", "question": "In k-fold cross-validation, what happens to the data?", "options": ["It is divided into k folds that take turns serving as validation data", "All data is used only for testing", "Each row is permanently removed after one pass", "The labels are randomly rewritten"], "correct_answer": "It is divided into k folds that take turns serving as validation data", "explanation": "Each fold is used for validation once while the remaining folds are used for training."},
        {"id": "ml_036", "skill": "Machine Learning", "topic": "Class Imbalance", "question": "Which approach may help a classifier learn from an underrepresented class?", "options": ["Use suitable class weights or resampling within training data", "Delete every minority-class example", "Evaluate only on training accuracy", "Always predict the majority class"], "correct_answer": "Use suitable class weights or resampling within training data", "explanation": "Class weighting and carefully applied resampling can reduce the effect of imbalance."},
        {"id": "ml_037", "skill": "Machine Learning", "topic": "Interpretability", "question": "Why is model interpretability important in some applications?", "options": ["It helps people understand and scrutinize model decisions", "It guarantees that the model has no bias", "It always increases model accuracy", "It removes the need to validate data"], "correct_answer": "It helps people understand and scrutinize model decisions", "explanation": "Interpretability can support debugging, accountability, and informed decisions."},
        {"id": "ml_038", "skill": "Machine Learning", "topic": "Model Deployment", "question": "What is model inference?", "options": ["Using a trained model to produce outputs for new inputs", "Training the model from scratch every time", "Deleting the training dataset", "Choosing a programming language"], "correct_answer": "Using a trained model to produce outputs for new inputs", "explanation": "Inference applies the fitted model to new data to generate predictions or scores."},
        {"id": "ml_039", "skill": "Machine Learning", "topic": "Model Monitoring", "question": "What is data drift?", "options": ["A change in the distribution of input data over time", "A model's file extension changing", "A fixed train-test split", "A guaranteed improvement in accuracy"], "correct_answer": "A change in the distribution of input data over time", "explanation": "Data drift occurs when incoming data characteristics change compared with the training or reference data."},
        {"id": "ml_040", "skill": "Machine Learning", "topic": "Responsible ML", "question": "Why should a machine learning model be evaluated across relevant groups when appropriate?", "options": ["To identify differences in performance and possible unfair outcomes", "To guarantee every group has identical features", "To eliminate the need for privacy controls", "To ensure the training data is never reviewed"], "correct_answer": "To identify differences in performance and possible unfair outcomes", "explanation": "Group-based evaluation can reveal performance disparities that aggregate metrics may hide."}
    ],
    
    "statistics": [
        {"id": "statistics_001", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What is the mean of 2, 4, and 6?", "options": ["3", "4", "5", "6"], "correct_answer": "4", "explanation": "Mean = (2 + 4 + 6) / 3 = 4."},
        {"id": "statistics_002", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What is the median of 3, 7, and 9?", "options": ["3", "7", "9", "19"], "correct_answer": "7", "explanation": "The median is the middle value in sorted data."},
        {"id": "statistics_003", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What is the mode of 2, 3, 3, 5?", "options": ["2", "3", "4", "5"], "correct_answer": "3", "explanation": "The mode is the most frequently occurring value."},
        {"id": "statistics_004", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What does the range measure?", "options": ["Average value", "Highest minus lowest value", "Middle value", "Most common value"], "correct_answer": "Highest minus lowest value", "explanation": "Range is the maximum value minus the minimum value."},
        {"id": "statistics_005", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "Which measure is most affected by extreme values?", "options": ["Median", "Mode", "Mean", "Quartile"], "correct_answer": "Mean", "explanation": "Extreme values can pull the mean upward or downward."},
        {"id": "statistics_006", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What does standard deviation measure?", "options": ["Data spread around the mean", "Number of observations", "Most frequent value", "Sample name"], "correct_answer": "Data spread around the mean", "explanation": "Standard deviation describes how far values typically vary from the mean."},
        {"id": "statistics_007", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What is the variance of a dataset based on?", "options": ["Squared deviations from the mean", "Only the largest value", "The median alone", "The number of categories"], "correct_answer": "Squared deviations from the mean", "explanation": "Variance averages squared deviations from the mean, with the denominator depending on whether it is a population or sample."},
        {"id": "statistics_008", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What is the median of 2, 4, 6, and 8?", "options": ["4", "5", "6", "8"], "correct_answer": "5", "explanation": "For an even number of values, average the two middle values: (4 + 6) / 2 = 5."},
        {"id": "statistics_009", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What is the first quartile commonly called?", "options": ["Q1", "Q2", "Q3", "Q4"], "correct_answer": "Q1", "explanation": "Q1 is the first quartile, commonly representing the 25th percentile."},
        {"id": "statistics_010", "skill": "Statistics", "topic": "Descriptive Statistics", "question": "What does the interquartile range measure?", "options": ["Maximum plus minimum", "Q3 minus Q1", "Mean minus median", "Total number of values"], "correct_answer": "Q3 minus Q1", "explanation": "The IQR measures the spread of the middle 50% of the data."},
        {"id": "statistics_011", "skill": "Statistics", "topic": "Probability", "question": "What is the probability of getting heads on a fair coin toss?", "options": ["0", "0.25", "0.5", "1"], "correct_answer": "0.5", "explanation": "A fair coin has two equally likely outcomes, so the probability is 1/2."},
        {"id": "statistics_012", "skill": "Statistics", "topic": "Probability", "question": "What is the probability of an impossible event?", "options": ["0", "0.5", "1", "-1"], "correct_answer": "0", "explanation": "An impossible event has probability zero."},
        {"id": "statistics_013", "skill": "Statistics", "topic": "Probability", "question": "What is the probability of a certain event?", "options": ["0", "0.25", "0.75", "1"], "correct_answer": "1", "explanation": "A certain event always occurs, so its probability is one."},
        {"id": "statistics_014", "skill": "Statistics", "topic": "Probability", "question": "If two fair dice are rolled, how many equally likely ordered outcomes are there?", "options": ["6", "12", "36", "42"], "correct_answer": "36", "explanation": "Each die has six outcomes, giving 6 × 6 = 36 ordered outcomes."},
        {"id": "statistics_015", "skill": "Statistics", "topic": "Probability", "question": "What is the complement of an event?", "options": ["The event always occurs", "The event does not occur", "The event occurs twice", "The event has probability above one"], "correct_answer": "The event does not occur", "explanation": "The complement contains outcomes where the original event does not happen."},
        {"id": "statistics_016", "skill": "Statistics", "topic": "Probability", "question": "For independent events A and B, what is P(A and B)?", "options": ["P(A) + P(B)", "P(A) × P(B)", "P(A) - P(B)", "P(A) / P(B)"], "correct_answer": "P(A) × P(B)", "explanation": "Independent events satisfy P(A and B) = P(A)P(B)."},
        {"id": "statistics_017", "skill": "Statistics", "topic": "Probability", "question": "What is conditional probability?", "options": ["Probability given another event", "Probability of an impossible event", "The mean of probabilities", "The largest probability"], "correct_answer": "Probability given another event", "explanation": "Conditional probability measures an event's probability when some information is known."},
        {"id": "statistics_018", "skill": "Statistics", "topic": "Probability", "question": "What is the probability of rolling a 6 on a fair six-sided die?", "options": ["1/2", "1/3", "1/6", "5/6"], "correct_answer": "1/6", "explanation": "Only one of the six equally likely faces shows a 6."},
        {"id": "statistics_019", "skill": "Statistics", "topic": "Probability", "question": "Which rule is used to calculate P(A or B) for mutually exclusive events?", "options": ["P(A) × P(B)", "P(A) + P(B)", "P(A) / P(B)", "P(A) - P(B)"], "correct_answer": "P(A) + P(B)", "explanation": "Mutually exclusive events cannot occur together, so their probabilities add."},
        {"id": "statistics_020", "skill": "Statistics", "topic": "Probability", "question": "What is a sample space?", "options": ["The set of all possible outcomes", "The average of a dataset", "A single observation", "A graph of the mean"], "correct_answer": "The set of all possible outcomes", "explanation": "The sample space lists every possible outcome of an experiment."},
        {"id": "statistics_021", "skill": "Statistics", "topic": "Distributions", "question": "What is a normal distribution commonly shaped like?", "options": ["Bell curve", "Straight line", "Rectangle only", "U-shaped curve"], "correct_answer": "Bell curve", "explanation": "A normal distribution is symmetric and bell-shaped."},
        {"id": "statistics_022", "skill": "Statistics", "topic": "Distributions", "question": "In a perfectly symmetric normal distribution, which values coincide?", "options": ["Mean, median, and mode", "Mean and range only", "Median and variance only", "Mode and standard deviation"], "correct_answer": "Mean, median, and mode", "explanation": "For an ideal normal distribution, all three measures of central tendency are equal."},
        {"id": "statistics_023", "skill": "Statistics", "topic": "Distributions", "question": "Approximately what percentage of normal-distribution values lie within one standard deviation of the mean?", "options": ["34%", "68%", "95%", "99.7%"], "correct_answer": "68%", "explanation": "The empirical rule gives approximately 68% within one standard deviation."},
        {"id": "statistics_024", "skill": "Statistics", "topic": "Distributions", "question": "What does a positively skewed distribution generally have?", "options": ["A longer right tail", "A longer left tail", "No variation", "Only negative values"], "correct_answer": "A longer right tail", "explanation": "Positive skew means the distribution has a longer tail toward larger values."},
        {"id": "statistics_025", "skill": "Statistics", "topic": "Distributions", "question": "Which distribution models the number of successes in a fixed number of independent trials with the same success probability?", "options": ["Binomial", "Normal only", "Uniform only", "Exponential only"], "correct_answer": "Binomial", "explanation": "The binomial distribution models successes across a fixed number of Bernoulli trials."},
        {"id": "statistics_026", "skill": "Statistics", "topic": "Distributions", "question": "Which distribution is commonly used to model counts of events in a fixed interval under suitable assumptions?", "options": ["Poisson", "Normal", "Uniform", "Student's t only"], "correct_answer": "Poisson", "explanation": "The Poisson distribution models event counts when events occur at a stable average rate under appropriate assumptions."},
        {"id": "statistics_027", "skill": "Statistics", "topic": "Distributions", "question": "What does a z-score represent?", "options": ["Distance from the mean in standard deviations", "The sample size", "The range of values", "The number of categories"], "correct_answer": "Distance from the mean in standard deviations", "explanation": "A z-score expresses how many standard deviations a value is above or below the mean."},
        {"id": "statistics_028", "skill": "Statistics", "topic": "Distributions", "question": "What is the z-score of a value equal to the mean?", "options": ["-1", "0", "1", "10"], "correct_answer": "0", "explanation": "A value equal to the mean has zero deviation from the mean."},
        {"id": "statistics_029", "skill": "Statistics", "topic": "Sampling", "question": "What is a population in statistics?", "options": ["The entire group being studied", "Only the selected observations", "A single variable", "A type of chart"], "correct_answer": "The entire group being studied", "explanation": "A population includes all individuals or observations relevant to the study."},
        {"id": "statistics_030", "skill": "Statistics", "topic": "Sampling", "question": "What is a sample?", "options": ["A subset of a population", "Always the whole population", "A probability of one", "A measurement unit"], "correct_answer": "A subset of a population", "explanation": "A sample is selected from the population to learn about it."},
        {"id": "statistics_031", "skill": "Statistics", "topic": "Sampling", "question": "What is simple random sampling?", "options": ["Every population member has an equal chance of selection", "Only nearby members are selected", "The largest values are selected", "Selection is based only on convenience"], "correct_answer": "Every population member has an equal chance of selection", "explanation": "Simple random sampling gives each member an equal selection chance."},
        {"id": "statistics_032", "skill": "Statistics", "topic": "Sampling", "question": "What is sampling bias?", "options": ["A sample systematically misrepresents the population", "A perfectly representative sample", "A larger sample size", "A correct calculation"], "correct_answer": "A sample systematically misrepresents the population", "explanation": "Sampling bias occurs when the selection process favors certain members or outcomes."},
        {"id": "statistics_033", "skill": "Statistics", "topic": "Sampling", "question": "What generally happens to the standard error of the sample mean as sample size increases?", "options": ["It decreases", "It always becomes zero", "It always increases", "It becomes the sample mean"], "correct_answer": "It decreases", "explanation": "For independent observations with finite variance, standard error is proportional to 1 divided by the square root of sample size."},
        {"id": "statistics_034", "skill": "Statistics", "topic": "Sampling", "question": "What is the central limit theorem about?", "options": ["The approximate distribution of sample means under suitable conditions", "The largest value in every dataset", "The absence of sampling error", "The exact distribution of every raw dataset"], "correct_answer": "The approximate distribution of sample means under suitable conditions", "explanation": "For sufficiently large samples under common conditions, sample means tend toward a normal distribution."},
        {"id": "statistics_035", "skill": "Statistics", "topic": "Hypothesis Testing", "question": "What is the null hypothesis?", "options": ["A default claim tested using sample evidence", "A claim that must always be true", "The sample average", "The observed maximum"], "correct_answer": "A default claim tested using sample evidence", "explanation": "The null hypothesis is the starting claim assessed by a statistical test."},
        {"id": "statistics_036", "skill": "Statistics", "topic": "Hypothesis Testing", "question": "What does a p-value measure?", "options": ["How surprising the observed result or a more extreme result is under the null hypothesis", "The probability that the null hypothesis is true", "The sample size", "The effect size in every case"], "correct_answer": "How surprising the observed result or a more extreme result is under the null hypothesis", "explanation": "The p-value is calculated assuming the null hypothesis and the test assumptions hold."},
        {"id": "statistics_037", "skill": "Statistics", "topic": "Hypothesis Testing", "question": "What is a Type I error?", "options": ["Rejecting a true null hypothesis", "Failing to reject a false null hypothesis", "Correctly accepting every alternative", "Using a large sample"], "correct_answer": "Rejecting a true null hypothesis", "explanation": "A Type I error is a false positive in hypothesis testing."},
        {"id": "statistics_038", "skill": "Statistics", "topic": "Hypothesis Testing", "question": "What is a Type II error?", "options": ["Rejecting a true null hypothesis", "Failing to reject a false null hypothesis", "Calculating the mean correctly", "Choosing a random sample"], "correct_answer": "Failing to reject a false null hypothesis", "explanation": "A Type II error is a false negative in hypothesis testing."},
        {"id": "statistics_039", "skill": "Statistics", "topic": "Correlation", "question": "What values can Pearson's correlation coefficient take?", "options": ["0 to 100", "-1 to 1", "0 to infinity", "-100 to 100"], "correct_answer": "-1 to 1", "explanation": "Pearson's correlation coefficient ranges from -1 to 1."},
        {"id": "statistics_040", "skill": "Statistics", "topic": "Correlation", "question": "Does correlation by itself prove causation?", "options": ["Yes, always", "No", "Only for positive correlation", "Only for large datasets"], "correct_answer": "No", "explanation": "An association may arise from confounding variables, coincidence, or other factors."}
    ],
    "git": [
        {"id": "git_001", "skill": "Git", "topic": "Basics", "question": "What is Git?", "options": ["A version control system", "A database server", "A web browser", "A programming language"], "correct_answer": "A version control system", "explanation": "Git records changes to files and supports collaborative development."},
        {"id": "git_002", "skill": "Git", "topic": "Basics", "question": "Which command checks the current working tree and staging area?", "options": ["git status", "git start", "git inspect-all", "git check"], "correct_answer": "git status", "explanation": "git status reports changed, staged, and untracked files."},
        {"id": "git_003", "skill": "Git", "topic": "Basics", "question": "Which command creates a new Git repository in the current directory?", "options": ["git init", "git begin", "git newrepo", "git start"], "correct_answer": "git init", "explanation": "git init initializes a repository in the current directory."},
        {"id": "git_004", "skill": "Git", "topic": "Basics", "question": "Which command copies a remote repository to your computer?", "options": ["git clone", "git copy-remote", "git download", "git fork-local"], "correct_answer": "git clone", "explanation": "git clone creates a local copy of a remote repository."},
        {"id": "git_005", "skill": "Git", "topic": "Staging", "question": "Which command stages a specific file?", "options": ["git add file.txt", "git stage-now file.txt", "git commit file.txt", "git push file.txt"], "correct_answer": "git add file.txt", "explanation": "git add places the file's current changes in the staging area."},
        {"id": "git_006", "skill": "Git", "topic": "Commits", "question": "Which command records staged changes in the repository history?", "options": ["git commit", "git stage", "git upload", "git fetch"], "correct_answer": "git commit", "explanation": "git commit creates a snapshot from staged changes."},
        {"id": "git_007", "skill": "Git", "topic": "Commits", "question": "What does a commit message describe?", "options": ["The purpose of the changes", "The computer password", "The repository URL only", "The Git installation path"], "correct_answer": "The purpose of the changes", "explanation": "A useful commit message briefly explains what the change does."},
        {"id": "git_008", "skill": "Git", "topic": "History", "question": "Which command displays commit history?", "options": ["git log", "git history-clear", "git status", "git list-files"], "correct_answer": "git log", "explanation": "git log displays commits and their metadata."},
        {"id": "git_009", "skill": "Git", "topic": "History", "question": "What is a commit hash?", "options": ["An identifier for a commit", "A branch name requirement", "A file extension", "A password for GitHub"], "correct_answer": "An identifier for a commit", "explanation": "A commit hash identifies a specific commit object."},
        {"id": "git_010", "skill": "Git", "topic": "Branches", "question": "Why are branches useful?", "options": ["They allow separate lines of development", "They delete the repository", "They replace commits", "They automatically fix all bugs"], "correct_answer": "They allow separate lines of development", "explanation": "Branches let developers work on features or fixes independently."},
        {"id": "git_011", "skill": "Git", "topic": "Branches", "question": "Which command lists local branches?", "options": ["git branch", "git list-commits", "git status -all", "git remote"], "correct_answer": "git branch", "explanation": "git branch without additional arguments lists local branches."},
        {"id": "git_012", "skill": "Git", "topic": "Branches", "question": "Which command creates a branch named feature?", "options": ["git branch feature", "git commit feature", "git init feature", "git clone feature"], "correct_answer": "git branch feature", "explanation": "git branch feature creates the branch without switching to it."},
        {"id": "git_013", "skill": "Git", "topic": "Branches", "question": "Which command switches to an existing branch using modern Git syntax?", "options": ["git switch feature", "git branch --delete feature", "git log feature", "git add feature"], "correct_answer": "git switch feature", "explanation": "git switch changes the current branch to feature."},
        {"id": "git_014", "skill": "Git", "topic": "Branches", "question": "What does merging a branch usually do?", "options": ["Combines changes from another line of development", "Deletes all commits", "Changes the repository name", "Removes Git tracking"], "correct_answer": "Combines changes from another line of development", "explanation": "A merge integrates changes from one branch into the current branch."},
        {"id": "git_015", "skill": "Git", "topic": "Branches", "question": "What is a merge conflict?", "options": ["Git cannot automatically reconcile overlapping changes", "A successful commit", "A missing Git installation", "An empty repository"], "correct_answer": "Git cannot automatically reconcile overlapping changes", "explanation": "Conflicts require the developer to choose or combine the intended changes."},
        {"id": "git_016", "skill": "Git", "topic": "Remote Repositories", "question": "What is a remote in Git?", "options": ["A reference to another repository", "A local text editor", "A commit message", "A programming variable"], "correct_answer": "A reference to another repository", "explanation": "A remote records a name and URL for another repository."},
        {"id": "git_017", "skill": "Git", "topic": "Remote Repositories", "question": "Which command uploads local commits to a remote branch?", "options": ["git push", "git pull", "git init", "git status"], "correct_answer": "git push", "explanation": "git push sends local commits to the configured remote."},
        {"id": "git_018", "skill": "Git", "topic": "Remote Repositories", "question": "Which command fetches remote changes and integrates them into the current branch by default?", "options": ["git pull", "git add", "git reset", "git clean"], "correct_answer": "git pull", "explanation": "git pull fetches remote updates and then integrates them, commonly by merge or configured rebase."},
        {"id": "git_019", "skill": "Git", "topic": "Remote Repositories", "question": "What does git fetch do?", "options": ["Downloads remote updates without automatically integrating them into the current branch", "Deletes remote commits", "Creates a new local file", "Stages every changed file"], "correct_answer": "Downloads remote updates without automatically integrating them into the current branch", "explanation": "git fetch updates remote-tracking references without merging into the current branch."},
        {"id": "git_020", "skill": "Git", "topic": "Remote Repositories", "question": "Which command shows configured remotes and their URLs?", "options": ["git remote -v", "git status -v", "git branch -v", "git log -v"], "correct_answer": "git remote -v", "explanation": "The -v option displays remote names and fetch/push URLs."},
        {"id": "git_021", "skill": "Git", "topic": "Undoing Changes", "question": "Which command discards unstaged changes in a tracked file using modern Git syntax?", "options": ["git restore file.txt", "git push file.txt", "git clone file.txt", "git log file.txt"], "correct_answer": "git restore file.txt", "explanation": "git restore can replace working-tree content with the indexed version; discarded changes may be lost."},
        {"id": "git_022", "skill": "Git", "topic": "Undoing Changes", "question": "What does git revert do?", "options": ["Creates a new commit that reverses an earlier commit", "Deletes the entire repository", "Always rewrites all history", "Only lists changed files"], "correct_answer": "Creates a new commit that reverses an earlier commit", "explanation": "git revert records an inverse change and is useful for shared history."},
        {"id": "git_023", "skill": "Git", "topic": "Undoing Changes", "question": "What can git reset do?", "options": ["Move the current branch reference and optionally change the index or working tree", "Only upload commits", "Create a GitHub account", "Install Git"], "correct_answer": "Move the current branch reference and optionally change the index or working tree", "explanation": "Different reset modes affect the branch reference, staging area, and working tree differently."},
        {"id": "git_024", "skill": "Git", "topic": "Undoing Changes", "question": "Which command unstages a file while keeping its working-tree changes in modern Git?", "options": ["git restore --staged file.txt", "git clean -fd", "git push file.txt", "git clone file.txt"], "correct_answer": "git restore --staged file.txt", "explanation": "This restores the staged version from HEAD while leaving the working file unchanged."},
        {"id": "git_025", "skill": "Git", "topic": "Ignore Files", "question": "What is the purpose of a .gitignore file?", "options": ["Specify intentionally untracked files Git should ignore", "Store all commit messages", "Rename every branch", "Automatically publish code"], "correct_answer": "Specify intentionally untracked files Git should ignore", "explanation": ".gitignore patterns help prevent selected untracked files from being added."},
        {"id": "git_026", "skill": "Git", "topic": "Ignore Files", "question": "Will adding a tracked file to .gitignore automatically untrack it?", "options": ["Yes, always", "No", "Only after git push", "Only on Windows"], "correct_answer": "No", "explanation": "Already tracked files remain tracked until removed from the index, for example with git rm --cached."},
        {"id": "git_027", "skill": "Git", "topic": "Staging", "question": "What does git add . commonly do?", "options": ["Stages eligible changes under the current directory", "Commits changes automatically", "Pushes to GitHub", "Deletes every ignored file"], "correct_answer": "Stages eligible changes under the current directory", "explanation": "It stages changes under the current directory subject to Git's path and ignore rules."},
        {"id": "git_028", "skill": "Git", "topic": "Repository Concepts", "question": "What is the Git working tree?", "options": ["The checked-out files you work on", "Only remote commits", "A list of GitHub users", "The Git installation program"], "correct_answer": "The checked-out files you work on", "explanation": "The working tree contains the files currently checked out for editing."},
        {"id": "git_029", "skill": "Git", "topic": "Repository Concepts", "question": "What is the staging area used for?", "options": ["Preparing changes for the next commit", "Hosting a website", "Running database queries", "Creating user passwords"], "correct_answer": "Preparing changes for the next commit", "explanation": "The index lets you select which changes will be included in the next commit."},
        {"id": "git_030", "skill": "Git", "topic": "Repository Concepts", "question": "What is HEAD in Git usually pointing to?", "options": ["The current checkout, usually the current branch or commit", "The largest file", "The remote URL only", "The newest untracked file"], "correct_answer": "The current checkout, usually the current branch or commit", "explanation": "HEAD identifies the current checkout and commonly refers to the current branch."},
        {"id": "git_031", "skill": "Git", "topic": "Tags", "question": "Why are Git tags often used?", "options": ["To mark important points such as releases", "To hide every commit", "To stage files", "To create database tables"], "correct_answer": "To mark important points such as releases", "explanation": "Tags name particular commits, often for version releases."},
        {"id": "git_032", "skill": "Git", "topic": "Inspection", "question": "Which command compares changes between revisions or files?", "options": ["git diff", "git init", "git clean", "git tag"], "correct_answer": "git diff", "explanation": "git diff shows line-level differences between specified states."},
        {"id": "git_033", "skill": "Git", "topic": "Inspection", "question": "Which command can show the files tracked by Git?", "options": ["git ls-files", "git remote", "git switch", "git fetch"], "correct_answer": "git ls-files", "explanation": "git ls-files lists files in Git's index, which normally contains tracked files."},
        {"id": "git_034", "skill": "Git", "topic": "Stashing", "question": "What is git stash commonly used for?", "options": ["Temporarily saving uncommitted changes", "Permanently deleting all branches", "Publishing a package", "Creating a remote account"], "correct_answer": "Temporarily saving uncommitted changes", "explanation": "Stashing lets you set aside work and return to a cleaner working tree."},
        {"id": "git_035", "skill": "Git", "topic": "Stashing", "question": "Which command reapplies stashed changes and removes that stash entry when successful?", "options": ["git stash pop", "git stash list", "git stash clear", "git stash show"], "correct_answer": "git stash pop", "explanation": "git stash pop applies a stash and removes it if the application succeeds."},
        {"id": "git_036", "skill": "Git", "topic": "Collaboration", "question": "What is a pull request commonly used for?", "options": ["Proposing changes for review and merging", "Automatically deleting the main branch", "Replacing the local repository", "Installing Git"], "correct_answer": "Proposing changes for review and merging", "explanation": "Pull requests support discussion, review, and integration of proposed changes on hosting platforms."},
        {"id": "git_037", "skill": "Git", "topic": "Collaboration", "question": "Why should you usually pull or fetch before pushing collaborative work?", "options": ["To learn about remote changes and reduce integration surprises", "To delete local commits", "To rename every file", "To disable version control"], "correct_answer": "To learn about remote changes and reduce integration surprises", "explanation": "Remote updates can affect whether your branch can be pushed cleanly."},
        {"id": "git_038", "skill": "Git", "topic": "Configuration", "question": "Which command sets the Git commit author name globally?", "options": ["git config --global user.name \"Your Name\"", "git user set \"Your Name\"", "git author --all \"Your Name\"", "git init --name \"Your Name\""], "correct_answer": "git config --global user.name \"Your Name\"", "explanation": "This sets the default author name in the user's global Git configuration."},
        {"id": "git_039", "skill": "Git", "topic": "Configuration", "question": "Which command sets the default branch name for newly initialized repositories?", "options": ["git config --global init.defaultBranch main", "git branch --global main", "git push --default main", "git set-head main"], "correct_answer": "git config --global init.defaultBranch main", "explanation": "This configuration sets the initial branch name for newly initialized repositories."},
        {"id": "git_040", "skill": "Git", "topic": "Best Practices", "question": "Which is a good Git commit practice?", "options": ["Make focused commits with clear messages", "Commit passwords and API keys", "Use one enormous commit for unrelated changes", "Never inspect changes before committing"], "correct_answer": "Make focused commits with clear messages", "explanation": "Small, focused commits with clear messages are easier to review and troubleshoot."}
    ],
    "github": [
        {"id": "github_001", "skill": "GitHub", "topic": "Basics", "question": "What is GitHub?", "options": ["A platform for hosting Git repositories and collaboration", "A programming language", "A relational database", "An operating system"], "correct_answer": "A platform for hosting Git repositories and collaboration", "explanation": "GitHub hosts repositories and provides tools for collaboration and project management."},
        {"id": "github_002", "skill": "GitHub", "topic": "Repositories", "question": "What is a GitHub repository?", "options": ["A project space containing files and version history", "Only a user password", "A web browser extension", "A computer processor"], "correct_answer": "A project space containing files and version history", "explanation": "A repository stores project files and their version history."},
        {"id": "github_003", "skill": "GitHub", "topic": "Repositories", "question": "What is the main difference between a public and private repository?", "options": ["Public repositories are visible to everyone; private repositories have restricted access", "Public repositories cannot contain code", "Private repositories cannot use Git", "There is no difference"], "correct_answer": "Public repositories are visible to everyone; private repositories have restricted access", "explanation": "Visibility controls who can view a repository, subject to platform rules and access settings."},
        {"id": "github_004", "skill": "GitHub", "topic": "Repositories", "question": "What is a README.md file commonly used for?", "options": ["Explaining the project and how to use it", "Storing secret passwords", "Replacing all source code", "Keeping Git commit hashes only"], "correct_answer": "Explaining the project and how to use it", "explanation": "A README introduces the project, setup instructions, features, and other useful details."},
        {"id": "github_005", "skill": "GitHub", "topic": "Repositories", "question": "What does forking a repository do?", "options": ["Creates your own copy of a repository under your account", "Deletes the original repository", "Automatically merges all branches", "Changes your account password"], "correct_answer": "Creates your own copy of a repository under your account", "explanation": "A fork is a separate repository copy commonly used to propose contributions."},
        {"id": "github_006", "skill": "GitHub", "topic": "Repositories", "question": "What does starring a GitHub repository usually indicate?", "options": ["You want to bookmark or show appreciation for it", "You have admin access", "You have merged its branches", "You own its copyright"], "correct_answer": "You want to bookmark or show appreciation for it", "explanation": "Stars help users save repositories and express interest."},
        {"id": "github_007", "skill": "GitHub", "topic": "Repositories", "question": "What is a GitHub repository description useful for?", "options": ["Briefly explaining the project's purpose", "Storing the entire codebase", "Replacing the README in every case", "Configuring the computer keyboard"], "correct_answer": "Briefly explaining the project's purpose", "explanation": "A short description helps visitors quickly understand what the project does."},
        {"id": "github_008", "skill": "GitHub", "topic": "Branches", "question": "Why do developers create branches on GitHub projects?", "options": ["To work on features or fixes separately", "To remove version history", "To disable pull requests", "To encrypt all source files automatically"], "correct_answer": "To work on features or fixes separately", "explanation": "Branches isolate development work until it is ready to integrate."},
        {"id": "github_009", "skill": "GitHub", "topic": "Pull Requests", "question": "What is a pull request?", "options": ["A proposal to review and merge changes", "A request to download a programming language", "A repository password", "A Git installation command"], "correct_answer": "A proposal to review and merge changes", "explanation": "A pull request provides a place to review and discuss proposed code changes."},
        {"id": "github_010", "skill": "GitHub", "topic": "Pull Requests", "question": "What is the purpose of reviewing a pull request?", "options": ["Check changes for correctness, quality, and problems", "Automatically rewrite the whole project", "Delete every branch", "Hide all code from collaborators"], "correct_answer": "Check changes for correctness, quality, and problems", "explanation": "Code review helps identify defects and improve maintainability before merging."},
        {"id": "github_011", "skill": "GitHub", "topic": "Pull Requests", "question": "What does merging a pull request do?", "options": ["Integrates the proposed changes into the target branch", "Deletes the entire account", "Creates a new programming language", "Automatically makes the repository private"], "correct_answer": "Integrates the proposed changes into the target branch", "explanation": "Merging incorporates the pull request's changes into its base branch."},
        {"id": "github_012", "skill": "GitHub", "topic": "Issues", "question": "What are GitHub Issues commonly used for?", "options": ["Tracking bugs, tasks, and feature requests", "Storing compiled operating systems", "Replacing Git commits", "Managing computer memory"], "correct_answer": "Tracking bugs, tasks, and feature requests", "explanation": "Issues organize work, questions, bugs, and enhancement requests."},
        {"id": "github_013", "skill": "GitHub", "topic": "Issues", "question": "What is a good bug report likely to include?", "options": ["Steps to reproduce and expected versus actual behavior", "Only the word 'bug'", "A personal password", "An unrelated project logo"], "correct_answer": "Steps to reproduce and expected versus actual behavior", "explanation": "Clear reproduction steps and observed results help others investigate the problem."},
        {"id": "github_014", "skill": "GitHub", "topic": "Collaboration", "question": "What is a collaborator on a repository?", "options": ["A person granted permissions to contribute", "An automatic backup file", "A type of commit hash", "A branch naming rule"], "correct_answer": "A person granted permissions to contribute", "explanation": "Collaborators receive repository access according to the permissions granted."},
        {"id": "github_015", "skill": "GitHub", "topic": "Collaboration", "question": "What is a CODEOWNERS file used for?", "options": ["Identifying people or teams responsible for reviewing parts of a codebase", "Storing all usernames and passwords", "Compiling the application", "Creating database indexes"], "correct_answer": "Identifying people or teams responsible for reviewing parts of a codebase", "explanation": "CODEOWNERS rules can request reviews from designated owners for changed files."},
        {"id": "github_016", "skill": "GitHub", "topic": "GitHub Actions", "question": "What is GitHub Actions used for?", "options": ["Automating workflows such as testing and deployment", "Replacing every programming language", "Managing physical computer parts", "Editing images only"], "correct_answer": "Automating workflows such as testing and deployment", "explanation": "GitHub Actions runs automated workflows in response to configured events or schedules."},
        {"id": "github_017", "skill": "GitHub", "topic": "GitHub Actions", "question": "Where are repository workflow files commonly stored?", "options": [".github/workflows/", "src/workflows-only/", "git/actions/", "public/github/"], "correct_answer": ".github/workflows/", "explanation": "Workflow YAML files are commonly placed in the .github/workflows directory."},
        {"id": "github_018", "skill": "GitHub", "topic": "GitHub Actions", "question": "What is continuous integration intended to help with?", "options": ["Frequently building and testing changes", "Manually deleting source code", "Preventing all commits", "Making every repository public"], "correct_answer": "Frequently building and testing changes", "explanation": "CI runs automated checks regularly so integration problems can be discovered early."},
        {"id": "github_019", "skill": "GitHub", "topic": "Security", "question": "Why should API keys not be committed to a public repository?", "options": ["Others could copy and misuse them", "They make Python slower", "Git cannot store strings", "They prevent README rendering"], "correct_answer": "Others could copy and misuse them", "explanation": "Exposed secrets may allow unauthorized access and should be kept out of version control."},
        {"id": "github_020", "skill": "GitHub", "topic": "Security", "question": "What should you do if an API key is accidentally published?", "options": ["Revoke or rotate it and investigate exposure", "Only delete the visible line and do nothing else", "Rename the repository", "Add the key to README"], "correct_answer": "Revoke or rotate it and investigate exposure", "explanation": "A published secret may remain in history or copies, so revocation or rotation is essential."},
        {"id": "github_021", "skill": "GitHub", "topic": "Security", "question": "What does two-factor authentication add to account security?", "options": ["A second verification step", "A second repository branch", "A second README", "A larger commit message"], "correct_answer": "A second verification step", "explanation": "Two-factor authentication requires an additional proof beyond the password."},
        {"id": "github_022", "skill": "GitHub", "topic": "Security", "question": "What is Dependabot commonly used for?", "options": ["Finding dependency issues and proposing updates", "Designing website layouts", "Creating user passwords", "Replacing the Git history"], "correct_answer": "Finding dependency issues and proposing updates", "explanation": "Dependabot can alert about vulnerable dependencies and open update pull requests."},
        {"id": "github_023", "skill": "GitHub", "topic": "Documentation", "question": "Which file is commonly used to explain licensing terms?", "options": ["LICENSE", "PASSWORD", "BRANCH", "EXECUTE"], "correct_answer": "LICENSE", "explanation": "A LICENSE file communicates the terms under which others may use the project."},
        {"id": "github_024", "skill": "GitHub", "topic": "Documentation", "question": "What is Markdown used for in README files?", "options": ["Formatting headings, lists, links, and code examples", "Executing server processes", "Encrypting repositories", "Managing network routers"], "correct_answer": "Formatting headings, lists, links, and code examples", "explanation": "Markdown provides readable plain-text syntax for formatted documentation."},
        {"id": "github_025", "skill": "GitHub", "topic": "GitHub Pages", "question": "What is GitHub Pages used for?", "options": ["Hosting supported static websites", "Running every backend service continuously", "Storing private passwords", "Replacing Git branches"], "correct_answer": "Hosting supported static websites", "explanation": "GitHub Pages can publish static sites from a repository."},
        {"id": "github_026", "skill": "GitHub", "topic": "GitHub Pages", "question": "Can GitHub Pages directly run a traditional server-side Flask application as its backend?", "options": ["Yes, always", "No, it is for static site hosting", "Only if the file is README.md", "Only with a public repository"], "correct_answer": "No, it is for static site hosting", "explanation": "A Flask backend needs a separate server or hosting service; Pages serves static content."},
        {"id": "github_027", "skill": "GitHub", "topic": "Repository Settings", "question": "What does changing repository visibility control?", "options": ["Who can view the repository", "The programming language used", "The number of lines of code", "The computer's screen size"], "correct_answer": "Who can view the repository", "explanation": "Visibility settings determine whether the repository is public or restricted."},
        {"id": "github_028", "skill": "GitHub", "topic": "Repository Settings", "question": "What is branch protection used for?", "options": ["Applying rules to important branches", "Encrypting every source file automatically", "Deleting all pull requests", "Disabling commit history"], "correct_answer": "Applying rules to important branches", "explanation": "Branch protection can require reviews, checks, or other safeguards before changes are merged."},
        {"id": "github_029", "skill": "GitHub", "topic": "Repository Settings", "question": "What is a release commonly used to publish?", "options": ["A version of a project with notes and possibly downloadable assets", "A user's private password", "A list of every open browser tab", "An operating system kernel automatically"], "correct_answer": "A version of a project with notes and possibly downloadable assets", "explanation": "GitHub Releases associate release notes and assets with a version, often a tag."},
        {"id": "github_030", "skill": "GitHub", "topic": "Project Management", "question": "What are GitHub Projects useful for?", "options": ["Organizing and tracking project work", "Replacing all programming code", "Running SQL queries only", "Changing computer hardware"], "correct_answer": "Organizing and tracking project work", "explanation": "Projects provide planning and tracking views for issues, pull requests, and tasks."},
        {"id": "github_031", "skill": "GitHub", "topic": "Project Management", "question": "What is a milestone commonly used to group?", "options": ["Issues and pull requests associated with a goal or deadline", "All user passwords", "Only image files", "Git installations"], "correct_answer": "Issues and pull requests associated with a goal or deadline", "explanation": "Milestones help organize work toward a target release or objective."},
        {"id": "github_032", "skill": "GitHub", "topic": "Collaboration", "question": "What is an organization on GitHub?", "options": ["An account that groups repositories and collaborators", "A programming language", "A single commit", "A local text file"], 'correct_answer': 'An account that groups repositories and collaborators', "explanation": "Organizations support team collaboration and centralized repository permissions."},
        {"id": "github_033", "skill": "GitHub", "topic": "Collaboration", "question": "What does @mentioning a user in an issue or pull request commonly do?", "options": ["References them and may notify them", "Automatically grants administrator access", "Deletes their account", "Changes the repository license"], "correct_answer": "References them and may notify them", "explanation": "Mentions can draw a user's attention, depending on notification settings and context."},
        {"id": "github_034", "skill": "GitHub", "topic": "GitHub CLI", "question": "What is the GitHub CLI used for?", "options": ["Working with GitHub features from a terminal", "Replacing the operating system", "Creating physical network cables", "Editing only spreadsheet cells"], "correct_answer": "Working with GitHub features from a terminal", "explanation": "The gh command-line tool can manage pull requests, issues, repositories, and more."},
        {"id": "github_035", "skill": "GitHub", "topic": "GitHub CLI", "question": "Which command commonly lists pull requests using GitHub CLI?", "options": ["gh pr list", "git pr show-all", "github pull every", "gh branch delete"], "correct_answer": "gh pr list", "explanation": "The gh pr list command displays pull requests for the relevant repository."},
        {"id": "github_036", "skill": "GitHub", "topic": "Contributions", "question": "What is an open-source contribution?", "options": ["A change or improvement shared with an open-source project", "A private password upload", "A computer restart", "A repository visibility setting"], "correct_answer": "A change or improvement shared with an open-source project", "explanation": "Contributions may include code, documentation, tests, bug reports, and other improvements."},
        {"id": "github_037", "skill": "GitHub", "topic": "Contributions", "question": "Why should you read a project's CONTRIBUTING guide before contributing?", "options": ["To understand its contribution process and standards", "To obtain its owner's password", "To disable code review", "To delete its license"], "correct_answer": "To understand its contribution process and standards", "explanation": "Contribution guides explain setup, testing, formatting, and submission expectations."},
        {"id": "github_038", "skill": "GitHub", "topic": "GitHub API", "question": "What is the GitHub REST API used for?", "options": ["Programmatically accessing supported GitHub resources and actions", "Replacing the Git version control system", "Running arbitrary desktop applications", "Automatically writing all project code"], "correct_answer": "Programmatically accessing supported GitHub resources and actions", "explanation": "The REST API lets applications interact with supported GitHub resources through HTTP requests."},
        {"id": "github_039", "skill": "GitHub", "topic": "Best Practices", "question": "What should a good project README include?", "options": ["Purpose, setup instructions, usage, and relevant examples", "Only secret keys", "Only the developer's password", "No information about the project"], "correct_answer": "Purpose, setup instructions, usage, and relevant examples", "explanation": "Clear documentation helps users understand, install, and use the project."},
        {"id": "github_040", "skill": "GitHub", "topic": "Best Practices", "question": "Before publishing a project publicly, what is a good practice?", "options": ["Check for secrets, sensitive files, and appropriate documentation", "Upload all passwords for convenience", "Delete the README", "Disable all access controls without review"], "correct_answer": "Check for secrets, sensitive files, and appropriate documentation", "explanation": "Reviewing files before publication reduces accidental exposure and improves project usability."}
    ],
    
    "linux": [
        {"id": "linux_001", "skill": "Linux", "topic": "Commands", "question": "Which command displays the current working directory?", "options": ["pwd", "ls", "cd", "mkdir"], "correct_answer": "pwd", "explanation": "pwd prints the current working directory path."},
        {"id": "linux_002", "skill": "Linux", "topic": "Commands", "question": "Which command lists files and directories?", "options": ["ls", "pwd", "touch", "whoami"], "correct_answer": "ls", "explanation": "ls lists directory contents."},
        {"id": "linux_003", "skill": "Linux", "topic": "Commands", "question": "Which command changes the current directory?", "options": ["cd", "mv", "cat", "grep"], "correct_answer": "cd", "explanation": "cd changes the shell's current directory."},
        {"id": "linux_004", "skill": "Linux", "topic": "Files", "question": "Which command creates a directory?", "options": ["mkdir", "rmdir", "touch", "head"], "correct_answer": "mkdir", "explanation": "mkdir creates a new directory."},
        {"id": "linux_005", "skill": "Linux", "topic": "Files", "question": "Which command creates an empty file if it does not exist?", "options": ["touch", "pwd", "grep", "chmod"], "correct_answer": "touch", "explanation": "touch creates an empty file or updates timestamps on an existing file."},
        {"id": "linux_006", "skill": "Linux", "topic": "Files", "question": "Which command displays a text file's contents?", "options": ["cat", "mkdir", "cd", "kill"], "correct_answer": "cat", "explanation": "cat outputs file contents to the terminal."},
        {"id": "linux_007", "skill": "Linux", "topic": "Files", "question": "Which command copies a file?", "options": ["cp", "mv", "rm", "pwd"], "correct_answer": "cp", "explanation": "cp copies files or directories."},
        {"id": "linux_008", "skill": "Linux", "topic": "Files", "question": "Which command moves or renames a file?", "options": ["mv", "cp", "cat", "ls"], "correct_answer": "mv", "explanation": "mv moves a file or renames it by changing its path."},
        {"id": "linux_009", "skill": "Linux", "topic": "Files", "question": "Which command removes a file?", "options": ["rm", "touch", "pwd", "echo"], "correct_answer": "rm", "explanation": "rm removes directory entries for files; deletion can be difficult to reverse."},
        {"id": "linux_010", "skill": "Linux", "topic": "Files", "question": "Which command searches text for a matching pattern?", "options": ["grep", "mkdir", "cd", "date"], "correct_answer": "grep", "explanation": "grep searches input for lines matching a pattern."},
        {"id": "linux_011", "skill": "Linux", "topic": "Permissions", "question": "Which command changes file permissions?", "options": ["chmod", "chown", "grep", "find"], "correct_answer": "chmod", "explanation": "chmod modifies file permission bits."},
        {"id": "linux_012", "skill": "Linux", "topic": "Permissions", "question": "Which command changes file ownership?", "options": ["chown", "chmod", "touch", "ps"], "correct_answer": "chown", "explanation": "chown changes the owner or group associated with a file."},
        {"id": "linux_013", "skill": "Linux", "topic": "Permissions", "question": "In Linux permissions, what does r represent?", "options": ["Read", "Run only", "Rename", "Remove"], "correct_answer": "Read", "explanation": "The r permission allows reading a file or listing a directory's contents."},
        {"id": "linux_014", "skill": "Linux", "topic": "Permissions", "question": "What does the numeric permission 755 commonly mean?", "options": ["Owner rwx, group r-x, others r-x", "Everyone has read-only access", "Owner has no access", "Everyone has write access"], "correct_answer": "Owner rwx, group r-x, others r-x", "explanation": "7 means rwx, while 5 means r-x."},
        {"id": "linux_015", "skill": "Linux", "topic": "Permissions", "question": "What does sudo allow an authorized user to do?", "options": ["Run a command with elevated privileges", "Automatically delete Linux", "Change every file permanently", "Connect to every server"], "correct_answer": "Run a command with elevated privileges", "explanation": "sudo runs commands with privileges allowed by the system's configuration."},
        {"id": "linux_016", "skill": "Linux", "topic": "Processes", "question": "Which command displays running processes?", "options": ["ps", "pwd", "touch", "mkdir"], "correct_answer": "ps", "explanation": "ps reports information about processes."},
        {"id": "linux_017", "skill": "Linux", "topic": "Processes", "question": "Which command can interactively display processes and resource usage?", "options": ["top", "cat", "cp", "clear"], "correct_answer": "top", "explanation": "top provides a continuously updating process and resource overview."},
        {"id": "linux_018", "skill": "Linux", "topic": "Processes", "question": "Which command sends a signal to a process by PID?", "options": ["kill", "mkdir", "ls", "whoami"], "correct_answer": "kill", "explanation": "kill sends a signal to a process; the default signal is SIGTERM."},
        {"id": "linux_019", "skill": "Linux", "topic": "Processes", "question": "Which keyboard shortcut commonly interrupts a foreground terminal command?", "options": ["Ctrl+C", "Ctrl+Z only", "Ctrl+S", "Alt+F4 only"], "correct_answer": "Ctrl+C", "explanation": "Ctrl+C typically sends SIGINT to the foreground process group."},
        {"id": "linux_020", "skill": "Linux", "topic": "Processes", "question": "Which command runs a command with its standard output redirected to a file, replacing the file's contents?", "options": ["command > file.txt", "command < file.txt", "command | file.txt", "command && file.txt"], "correct_answer": "command > file.txt", "explanation": "The > operator redirects standard output and truncates an existing destination file."},
        {"id": "linux_021", "skill": "Linux", "topic": "Pipes", "question": "What does the pipe operator | do?", "options": ["Sends one command's standard output to another command's standard input", "Deletes a directory", "Changes file permissions", "Starts a new user account"], "correct_answer": "Sends one command's standard output to another command's standard input", "explanation": "Pipes connect the output stream of one command to the input stream of another."},
        {"id": "linux_022", "skill": "Linux", "topic": "Pipes", "question": "Which command displays the first lines of a file by default?", "options": ["head", "tail", "sort", "uniq"], "correct_answer": "head", "explanation": "head displays the first ten lines by default."},
        {"id": "linux_023", "skill": "Linux", "topic": "Pipes", "question": "Which command displays the last lines of a file by default?", "options": ["tail", "head", "cut", "pwd"], "correct_answer": "tail", "explanation": "tail displays the last ten lines by default."},
        {"id": "linux_024", "skill": "Linux", "topic": "Pipes", "question": "Which command sorts lines of text?", "options": ["sort", "chmod", "kill", "cd"], "correct_answer": "sort", "explanation": "sort arranges input lines according to the selected sorting rules."},
        {"id": "linux_025", "skill": "Linux", "topic": "Search", "question": "Which command searches for files and directories by specified criteria?", "options": ["find", "echo", "whoami", "uname"], "correct_answer": "find", "explanation": "find searches directory trees using conditions such as name and type."},
        {"id": "linux_026", "skill": "Linux", "topic": "System Information", "question": "Which command displays the current username?", "options": ["whoami", "hostname", "uname", "date"], "correct_answer": "whoami", "explanation": "whoami prints the effective user name."},
        {"id": "linux_027", "skill": "Linux", "topic": "System Information", "question": "Which command displays system information such as the kernel name?", "options": ["uname", "grep", "touch", "mv"], "correct_answer": "uname", "explanation": "uname reports system information; uname -a displays additional details."},
        {"id": "linux_028", "skill": "Linux", "topic": "System Information", "question": "Which command displays disk space usage for mounted filesystems?", "options": ["df", "du", "free", "ps"], "correct_answer": "df", "explanation": "df reports filesystem space usage."},
        {"id": "linux_029", "skill": "Linux", "topic": "System Information", "question": "Which command estimates the disk space used by files and directories?", "options": ["du", "df", "top", "date"], "correct_answer": "du", "explanation": "du summarizes disk usage for files and directories."},
        {"id": "linux_030", "skill": "Linux", "topic": "System Information", "question": "Which command displays memory usage information?", "options": ["free", "grep", "mkdir", "mv"], "correct_answer": "free", "explanation": "free reports used and available system memory."},
        {"id": "linux_031", "skill": "Linux", "topic": "Networking", "question": "Which command-line utility can test network reachability using ICMP echo requests?", "options": ["ping", "chmod", "touch", "sort"], "correct_answer": "ping", "explanation": "ping sends ICMP echo requests where permitted to test reachability and response time."},
        {"id": "linux_032", "skill": "Linux", "topic": "Networking", "question": "Which command-line tool can make HTTP requests to a web server?", "options": ["curl", "mkdir", "chown", "whoami"], "correct_answer": "curl", "explanation": "curl transfers data using protocols including HTTP and HTTPS."},
        {"id": "linux_033", "skill": "Linux", "topic": "Networking", "question": "Which file commonly contains local hostname-to-IP mappings?", "options": ["/etc/hosts", "/etc/passwd", "/etc/fstab", "/etc/shadow"], "correct_answer": "/etc/hosts", "explanation": "The hosts file stores static local hostname mappings."},
        {"id": "linux_034", "skill": "Linux", "topic": "Shell", "question": "What is a shell?", "options": ["A program that interprets commands", "A type of hard disk", "A database table", "A network cable"], "correct_answer": "A program that interprets commands", "explanation": "A shell provides an interface for running commands and scripts."},
        {"id": "linux_035", "skill": "Linux", "topic": "Shell", "question": "What does the environment variable PATH contain?", "options": ["Directories searched for executable commands", "All user passwords", "Only the current filename", "The system's screen resolution"], "correct_answer": "Directories searched for executable commands", "explanation": "The shell searches PATH directories when resolving commands without explicit paths."},
        {"id": "linux_036", "skill": "Linux", "topic": "Shell", "question": "What is a shell script?", "options": ["A file containing commands to be executed by a shell", "A physical computer component", "A database index", "A browser extension"], "correct_answer": "A file containing commands to be executed by a shell", "explanation": "Shell scripts automate command sequences."},
        {"id": "linux_037", "skill": "Linux", "topic": "Package Management", "question": "Which command is commonly used to update package lists on Debian-based systems?", "options": ["sudo apt update", "sudo apt erase-all", "git update", "python apt"], "correct_answer": "sudo apt update", "explanation": "apt update refreshes package metadata; it does not itself upgrade installed packages."},
        {"id": "linux_038", "skill": "Linux", "topic": "Package Management", "question": "Which command commonly installs a package on Debian-based systems?", "options": ["sudo apt install package-name", "sudo apt create-user", "git install package-name", "chmod install package-name"], "correct_answer": "sudo apt install package-name", "explanation": "apt install installs a package and its required dependencies."},
        {"id": "linux_039", "skill": "Linux", "topic": "Logs", "question": "Which directory commonly contains system log files?", "options": ["/var/log", "/bin/logs-only", "/home/logs", "/etc/bin"], "correct_answer": "/var/log", "explanation": "Many Linux services and system components store logs under /var/log."},
        {"id": "linux_040", "skill": "Linux", "topic": "Best Practices", "question": "Why should you avoid running unfamiliar commands with sudo?", "options": ["They may make privileged changes or damage the system", "sudo makes all commands read-only", "It disables the keyboard", "It automatically backs up every file"], "correct_answer": "They may make privileged changes or damage the system", "explanation": "Elevated privileges can allow commands to change or delete important system files."}
    ],
    "docker": [
        {"id": "docker_001", "skill": "Docker", "topic": "Basics", "question": "What is Docker primarily used for?", "options": ["Building and running containerized applications", "Creating spreadsheet formulas", "Replacing every operating system", "Designing database tables only"], "correct_answer": "Building and running containerized applications", "explanation": "Docker packages applications and dependencies into portable containers."},
        {"id": "docker_002", "skill": "Docker", "topic": "Basics", "question": "What is a Docker image?", "options": ["A template used to create containers", "A running container only", "A physical server", "A network cable"], "correct_answer": "A template used to create containers", "explanation": "An image contains the filesystem and configuration used to create containers."},
        {"id": "docker_003", "skill": "Docker", "topic": "Basics", "question": "What is a Docker container?", "options": ["An isolated running instance created from an image", "A programming language", "A Git branch", "A database query"], "correct_answer": "An isolated running instance created from an image", "explanation": "A container runs an application using an image and container configuration."},
        {"id": "docker_004", "skill": "Docker", "topic": "Commands", "question": "Which command displays installed Docker images?", "options": ["docker images", "docker ps", "docker ports", "docker folders"], "correct_answer": "docker images", "explanation": "docker images lists images stored locally."},
        {"id": "docker_005", "skill": "Docker", "topic": "Commands", "question": "Which command lists running containers?", "options": ["docker ps", "docker images", "docker build", "docker login"], "correct_answer": "docker ps", "explanation": "docker ps lists running containers; docker ps -a also includes stopped containers."},
        {"id": "docker_006", "skill": "Docker", "topic": "Commands", "question": "Which command starts a new container from an image?", "options": ["docker run", "docker image-list", "docker commit-only", "docker stop"], "correct_answer": "docker run", "explanation": "docker run creates and starts a container from an image."},
        {"id": "docker_007", "skill": "Docker", "topic": "Commands", "question": "Which command builds an image from a Dockerfile?", "options": ["docker build", "docker ps", "docker kill", "docker pull-only"], "correct_answer": "docker build", "explanation": "docker build processes a build context and Dockerfile to create an image."},
        {"id": "docker_008", "skill": "Docker", "topic": "Commands", "question": "Which command downloads an image from a registry?", "options": ["docker pull", "docker push", "docker run-only", "docker exec"], "correct_answer": "docker pull", "explanation": "docker pull downloads an image from a container registry."},
        {"id": "docker_009", "skill": "Docker", "topic": "Commands", "question": "Which command uploads an image to a registry?", "options": ["docker push", "docker pull", "docker logs", "docker inspect"], "correct_answer": "docker push", "explanation": "docker push uploads an image to a registry the user can access."},
        {"id": "docker_010", "skill": "Docker", "topic": "Commands", "question": "Which command stops a running container gracefully?", "options": ["docker stop", "docker build", "docker tag", "docker search"], "correct_answer": "docker stop", "explanation": "docker stop sends a termination signal and waits before forcing termination if necessary."},
        {"id": "docker_011", "skill": "Docker", "topic": "Dockerfile", "question": "What is a Dockerfile?", "options": ["A text file containing image build instructions", "A running container", "A Docker account password", "A database backup format"], "correct_answer": "A text file containing image build instructions", "explanation": "Docker reads Dockerfile instructions to build an image."},
        {"id": "docker_012", "skill": "Docker", "topic": "Dockerfile", "question": "What does the FROM instruction specify?", "options": ["The base image", "The host computer password", "The Git branch", "The container's final exit code"], "correct_answer": "The base image", "explanation": "FROM identifies the base image for a build stage."},
        {"id": "docker_013", "skill": "Docker", "topic": "Dockerfile", "question": "What is the purpose of WORKDIR?", "options": ["Set the working directory for subsequent instructions", "Publish a container image", "Stop all containers", "Create a Docker registry account"], "correct_answer": "Set the working directory for subsequent instructions", "explanation": "WORKDIR sets the working directory for later build instructions such as RUN, COPY, and CMD."},
        {"id": "docker_014", "skill": "Docker", "topic": "Dockerfile", "question": "What does COPY do in a Dockerfile?", "options": ["Copies files from the build context into the image", "Copies an image to GitHub automatically", "Stops a container", "Creates a network port"], "correct_answer": "Copies files from the build context into the image", "explanation": "COPY transfers selected files and directories from the build context into the image filesystem."},
        {"id": "docker_015", "skill": "Docker", "topic": "Dockerfile", "question": "What is CMD commonly used for?", "options": ["Providing the default command or arguments for a container", "Choosing the base image", "Uploading an image to a registry", "Creating a volume"], "correct_answer": "Providing the default command or arguments for a container", "explanation": "CMD specifies the default command or default arguments when a container starts."},
        {"id": "docker_016", "skill": "Docker", "topic": "Dockerfile", "question": "What does EXPOSE document in a Dockerfile?", "options": ["A port the application is expected to listen on", "A password for the container", "The image's file size", "The container's source code license"], "correct_answer": "A port the application is expected to listen on", "explanation": "EXPOSE documents a port; publishing it to the host generally requires runtime port configuration."},
        {"id": "docker_017", "skill": "Docker", "topic": "Networking", "question": "What does the -p option in docker run commonly do?", "options": ["Publishes a container port to a host port", "Pulls an image silently", "Creates a password", "Pauses the container"], "correct_answer": "Publishes a container port to a host port", "explanation": "For example, -p 5000:5000 maps host port 5000 to container port 5000."},
        {"id": "docker_018", "skill": "Docker", "topic": "Networking", "question": "What is a Docker network used for?", "options": ["Connecting containers and controlling their network communication", "Storing source code versions", "Compiling Python code", "Creating image layers manually"], "correct_answer": "Connecting containers and controlling their network communication", "explanation": "Docker networks allow containers to communicate according to network configuration."},
        {"id": "docker_019", "skill": "Docker", "topic": "Storage", "question": "Why are Docker volumes useful?", "options": ["They persist data beyond a container's writable layer", "They automatically fix source code", "They replace container images", "They publish ports"], "correct_answer": "They persist data beyond a container's writable layer", "explanation": "Volumes store data separately from a container's writable layer and can be reused."},
        {"id": "docker_020", "skill": "Docker", "topic": "Storage", "question": "What is a bind mount?", "options": ["Mounting a specified host path into a container", "A type of image tag", "A container stop command", "A Docker registry login"], "correct_answer": "Mounting a specified host path into a container", "explanation": "Bind mounts expose a selected host file or directory inside the container."},
        {"id": "docker_021", "skill": "Docker", "topic": "Docker Compose", "question": "What is Docker Compose used for?", "options": ["Defining and managing multi-container applications", "Writing only HTML pages", "Replacing the Linux kernel", "Creating Git commits"], "correct_answer": "Defining and managing multi-container applications", "explanation": "Compose describes services, networks, volumes, and related settings in a configuration file."},
        {"id": "docker_022", "skill": "Docker", "topic": "Docker Compose", "question": "Which file format is commonly used for Docker Compose configuration?", "options": ["YAML", "MP3", "JPEG", "EXE"], "correct_answer": "YAML", "explanation": "Compose configuration is commonly written in compose.yaml or compose.yml using YAML."},
        {"id": "docker_023", "skill": "Docker", "topic": "Docker Compose", "question": "Which command starts services defined in a Compose file?", "options": ["docker compose up", "docker compose erase", "docker compose compile-only", "docker compose branch"], "correct_answer": "docker compose up", "explanation": "docker compose up creates and starts the configured services."},
        {"id": "docker_024", "skill": "Docker", "topic": "Docker Compose", "question": "Which command stops and removes Compose-managed containers and networks by default?", "options": ["docker compose down", "docker compose ps", "docker compose logs", "docker compose config"], "correct_answer": "docker compose down", "explanation": "docker compose down stops and removes the project's containers and networks; volumes are retained unless removal is requested."},
        {"id": "docker_025", "skill": "Docker", "topic": "Registries", "question": "What is Docker Hub?", "options": ["A container image registry and distribution service", "A programming language", "A container's memory allocation", "A Dockerfile instruction"], "correct_answer": "A container image registry and distribution service", "explanation": "Docker Hub hosts and distributes container images."},
        {"id": "docker_026", "skill": "Docker", "topic": "Images", "question": "What is an image tag commonly used for?", "options": ["Identifying a named image version or variant", "Setting a host password", "Stopping a container", "Changing a file's permissions"], "correct_answer": "Identifying a named image version or variant", "explanation": "Tags provide readable references such as app:1.0; mutable tags should not always be treated as immutable versions."},
        {"id": "docker_027", "skill": "Docker", "topic": "Images", "question": "What is a benefit of using smaller container images?", "options": ["Reduced transfer and storage costs and often faster deployment", "Guaranteed absence of bugs", "Automatic encryption of all data", "Unlimited container memory"], "correct_answer": "Reduced transfer and storage costs and often faster deployment", "explanation": "Smaller images usually require less storage and take less time to transfer."},
        {"id": "docker_028", "skill": "Docker", "topic": "Containers", "question": "What does docker exec commonly do?", "options": ["Runs a command inside an existing running container", "Builds an image from scratch", "Deletes all images", "Creates a Docker Hub account"], "correct_answer": "Runs a command inside an existing running container", "explanation": "docker exec starts an additional process inside a running container."},
        {"id": "docker_029", "skill": "Docker", "topic": "Containers", "question": "Which command displays a container's standard output and error logs?", "options": ["docker logs", "docker images", "docker build", "docker tag"], "correct_answer": "docker logs", "explanation": "docker logs retrieves logs collected from a container's configured output streams."},
        {"id": "docker_030", "skill": "Docker", "topic": "Containers", "question": "What does docker inspect provide?", "options": ["Detailed metadata and configuration for Docker objects", "Only source-code syntax errors", "A list of Git commits", "A Python package installation"], "correct_answer": "Detailed metadata and configuration for Docker objects", "explanation": "docker inspect returns detailed information about containers, images, networks, and other objects."},
        {"id": "docker_031", "skill": "Docker", "topic": "Architecture", "question": "What is the Docker daemon responsible for?", "options": ["Managing Docker objects and responding to Docker API requests", "Writing application business logic", "Serving only HTML files", "Replacing the host operating system"], "correct_answer": "Managing Docker objects and responding to Docker API requests", "explanation": "The Docker daemon manages objects such as images, containers, networks, and volumes."},
        {"id": "docker_032", "skill": "Docker", "topic": "Architecture", "question": "How do containers generally differ from virtual machines?", "options": ["Containers share the host kernel, while VMs run separate guest operating systems", "Containers always require more memory than VMs", "VMs cannot run applications", "Containers are database tables"], "correct_answer": "Containers share the host kernel, while VMs run separate guest operating systems", "explanation": "Containers isolate processes while sharing a kernel; virtual machines virtualize hardware and run guest operating systems."},
        {"id": "docker_033", "skill": "Docker", "topic": "Build Optimization", "question": "What is a Docker build cache used for?", "options": ["Reusing eligible previous build steps", "Storing all container passwords", "Replacing image registries", "Running containers without images"], "correct_answer": "Reusing eligible previous build steps", "explanation": "Cached layers can reduce the work needed for subsequent image builds."},
        {"id": "docker_034", "skill": "Docker", "topic": "Build Optimization", "question": "Why use a .dockerignore file?", "options": ["Exclude selected files from the build context", "Stop every running container", "Publish ports automatically", "Create new image tags"], "correct_answer": "Exclude selected files from the build context", "explanation": "It reduces unnecessary context files and helps avoid including unwanted data in builds."},
        {"id": "docker_035", "skill": "Docker", "topic": "Security", "question": "Why should containers run as a non-root user when practical?", "options": ["To reduce the impact of a compromised application", "To guarantee no bugs exist", "To increase image size", "To disable networking permanently"], "correct_answer": "To reduce the impact of a compromised application", "explanation": "Running with fewer privileges limits what an exploited process may be able to do."},
        {"id": "docker_036", "skill": "Docker", "topic": "Security", "question": "Where should production secrets generally be supplied instead of hardcoding them into an image?", "options": ["A suitable secrets-management mechanism", "A public Dockerfile", "A public README", "A container image tag"], "correct_answer": "A suitable secrets-management mechanism", "explanation": "Secrets should be provided securely at runtime or through an appropriate secret-management system."},
        {"id": "docker_037", "skill": "Docker", "topic": "Troubleshooting", "question": "A container exits immediately after starting. What is a useful first step?", "options": ["Inspect its logs and exit status", "Delete every project file", "Reinstall the operating system immediately", "Change the Git username"], "correct_answer": "Inspect its logs and exit status", "explanation": "Logs and exit information often reveal command failures or application startup errors."},
        {"id": "docker_038", "skill": "Docker", "topic": "Troubleshooting", "question": "Why might a host be unable to reach an application inside a container?", "options": ["The port may not be published or the application may listen on the wrong interface", "Docker images cannot contain applications", "Containers cannot run servers", "The container must always use port 80"], "correct_answer": "The port may not be published or the application may listen on the wrong interface", "explanation": "Check port mapping, application binding, firewall rules, and container health."},
        {"id": "docker_039", "skill": "Docker", "topic": "Deployment", "question": "Why is a container image useful for deployment?", "options": ["It packages application files and dependencies in a repeatable format", "It guarantees identical hardware everywhere", "It removes the need for configuration", "It automatically fixes every vulnerability"], "correct_answer": "It packages application files and dependencies in a repeatable format", "explanation": "Images help standardize the application environment across supported systems."},
        {"id": "docker_040", "skill": "Docker", "topic": "Best Practices", "question": "Which is a good Dockerfile practice?", "options": ["Use trusted base images and keep images updated", "Store credentials directly in image layers", "Run every process as root without reason", "Copy every host file into every image"], "correct_answer": "Use trusted base images and keep images updated", "explanation": "Trusted, maintained base images and minimal build contexts help reduce risk and unnecessary image content."}
    ],
    "software testing": [
        {"id": "software_testing_001", "skill": "Software Testing", "topic": "Fundamentals", "question": "What is software testing?", "options": ["Evaluating software to find defects and check requirements", "Writing code without checking it", "Only designing user interfaces", "Only installing an operating system"], "correct_answer": "Evaluating software to find defects and check requirements", "explanation": "Testing provides information about software quality and whether it meets specified expectations."},
        {"id": "software_testing_002", "skill": "Software Testing", "topic": "Fundamentals", "question": "What is a software defect?", "options": ["A flaw that can cause incorrect behavior", "A successful test result", "A project deadline", "A type of database"], "correct_answer": "A flaw that can cause incorrect behavior", "explanation": "A defect is a problem in a software artifact that may lead to a failure."},
        {"id": "software_testing_003", "skill": "Software Testing", "topic": "Fundamentals", "question": "What is verification concerned with?", "options": ["Checking whether work products meet specified requirements", "Only asking end users about colors", "Deploying without review", "Measuring only server speed"], "correct_answer": "Checking whether work products meet specified requirements", "explanation": "Verification checks whether the product is being built according to specified requirements and design."},
        {"id": "software_testing_004", "skill": "Software Testing", "topic": "Fundamentals", "question": "What is validation concerned with?", "options": ["Checking whether the product meets user needs and intended use", "Checking only indentation", "Counting source files", "Renaming variables only"], "correct_answer": "Checking whether the product meets user needs and intended use", "explanation": "Validation assesses whether the right product has been built for its intended users and context."},
        {"id": "software_testing_005", "skill": "Software Testing", "topic": "Test Levels", "question": "What does unit testing usually test?", "options": ["A small individual component or function", "The entire company network", "Only the final deployment server", "A complete organization"], "correct_answer": "A small individual component or function", "explanation": "Unit tests check individual units of code in isolation where practical."},
        {"id": "software_testing_006", "skill": "Software Testing", "topic": "Test Levels", "question": "What is integration testing designed to check?", "options": ["Interactions between combined components", "Only a single line's indentation", "Only user satisfaction surveys", "Only hardware temperature"], "correct_answer": "Interactions between combined components", "explanation": "Integration tests identify issues in interfaces and interactions between components."},
        {"id": "software_testing_007", "skill": "Software Testing", "topic": "Test Levels", "question": "What does system testing evaluate?", "options": ["The complete integrated system against its requirements", "Only one isolated function", "Only source-code formatting", "Only a database column"], "correct_answer": "The complete integrated system against its requirements", "explanation": "System testing evaluates the complete system as a whole."},
        {"id": "software_testing_008", "skill": "Software Testing", "topic": "Test Levels", "question": "What is acceptance testing intended to establish?", "options": ["Whether the solution is acceptable for its intended use", "Whether every variable is named perfectly", "Whether code has no comments", "Whether the developer's computer is new"], "correct_answer": "Whether the solution is acceptable for its intended use", "explanation": "Acceptance testing evaluates whether acceptance criteria and user or business needs are met."},
        {"id": "software_testing_009", "skill": "Software Testing", "topic": "Test Types", "question": "What is regression testing?", "options": ["Checking that changes have not broken existing behavior", "Testing only brand-new hardware", "Deleting old test cases", "Testing without expected results"], "correct_answer": "Checking that changes have not broken existing behavior", "explanation": "Regression tests detect unintended side effects after code or configuration changes."},
        {"id": "software_testing_010", "skill": "Software Testing", "topic": "Test Types", "question": "What is smoke testing?", "options": ["A basic check that major functions work after a build", "A test of physical smoke detectors only", "A complete security audit in every case", "Testing only database backups"], "correct_answer": "A basic check that major functions work after a build", "explanation": "Smoke tests quickly check whether a build is stable enough for further testing."},
        {"id": "software_testing_011", "skill": "Software Testing", "topic": "Test Types", "question": "What is sanity testing commonly used for?", "options": ["A focused check of a specific change or functionality", "Testing every feature in full detail", "Replacing all regression testing", "Measuring only CPU temperature"], "correct_answer": "A focused check of a specific change or functionality", "explanation": "Sanity testing is a narrow check that a particular change or area behaves reasonably."},
        {"id": "software_testing_012", "skill": "Software Testing", "topic": "Test Types", "question": "What is exploratory testing?", "options": ["Learning, designing tests, and testing while investigating the software", "Executing only fixed scripts without investigation", "Testing without interacting with software", "Checking only spelling in a report"], "correct_answer": "Learning, designing tests, and testing while investigating the software", "explanation": "Exploratory testing combines investigation and test design as the tester learns about the product."},
        {"id": "software_testing_013", "skill": "Software Testing", "topic": "Test Design", "question": "What is black-box testing?", "options": ["Testing behavior without relying on internal code structure", "Testing only private source-code branches", "Testing only hardware components", "Testing without inputs"], "correct_answer": "Testing behavior without relying on internal code structure", "explanation": "Black-box tests use inputs and expected outputs based on requirements or behavior."},
        {"id": "software_testing_014", "skill": "Software Testing", "topic": "Test Design", "question": "What is white-box testing?", "options": ["Testing informed by internal code structure", "Testing without knowing anything about the program's behavior", "Testing only product pricing", "Testing only network cables"], "correct_answer": "Testing informed by internal code structure", "explanation": "White-box testing uses knowledge of internal logic, paths, or code structure."},
        {"id": "software_testing_015", "skill": "Software Testing", "topic": "Test Design", "question": "What is boundary value analysis?", "options": ["Testing values at and near input limits", "Testing only average values", "Testing without input data", "Testing only visual colors"], "correct_answer": "Testing values at and near input limits", "explanation": "Defects frequently occur at boundaries, so boundary values receive focused tests."},
        {"id": "software_testing_016", "skill": "Software Testing", "topic": "Test Design", "question": "What is equivalence partitioning?", "options": ["Dividing inputs into groups expected to behave similarly", "Testing every possible input in every case", "Grouping developers by age", "Removing all invalid inputs"], "correct_answer": "Dividing inputs into groups expected to behave similarly", "explanation": "Representative values from equivalence classes can reduce redundant test cases."},
        {"id": "software_testing_017", "skill": "Software Testing", "topic": "Test Design", "question": "What is a positive test?", "options": ["Testing with valid inputs and expected usage", "Testing only invalid passwords", "Testing without requirements", "Testing only server shutdown"], "correct_answer": "Testing with valid inputs and expected usage", "explanation": "Positive testing checks that valid inputs and normal actions produce expected results."},
        {"id": "software_testing_018", "skill": "Software Testing", "topic": "Test Design", "question": "What is a negative test?", "options": ["Checking how the system handles invalid inputs or unexpected actions", "Checking only successful inputs", "Testing only the user interface color", "Testing only the application's title"], "correct_answer": "Checking how the system handles invalid inputs or unexpected actions", "explanation": "Negative tests check error handling and protection against invalid conditions."},
        {"id": "software_testing_019", "skill": "Software Testing", "topic": "Test Cases", "question": "What should a test case normally include?", "options": ["Inputs, steps, and expected results", "Only the tester's name", "Only a screenshot without context", "Only the application logo"], "correct_answer": "Inputs, steps, and expected results", "explanation": "A test case describes how to perform a check and determine whether it passes."},
        {"id": "software_testing_020", "skill": "Software Testing", "topic": "Test Cases", "question": "What is a test plan?", "options": ["A document describing the testing approach, scope, resources, and activities", "A list of programming keywords only", "A user password file", "A completed application binary"], "correct_answer": "A document describing the testing approach, scope, resources, and activities", "explanation": "A test plan organizes the intended testing work and its responsibilities."},
        {"id": "software_testing_021", "skill": "Software Testing", "topic": "Defect Management", "question": "What is a bug report?", "options": ["A record describing a defect and how to reproduce it", "A software license", "A deployment server", "A programming language"], "correct_answer": "A record describing a defect and how to reproduce it", "explanation": "A good bug report documents observed behavior, expected behavior, and reproduction steps."},
        {"id": "software_testing_022", "skill": "Software Testing", "topic": "Defect Management", "question": "What does defect severity describe?", "options": ["The impact of a defect on the system", "The order in which a tester prefers tasks", "The developer's job title", "The number of source files"], "correct_answer": "The impact of a defect on the system", "explanation": "Severity describes how seriously the defect affects functionality or users."},
        {"id": "software_testing_023", "skill": "Software Testing", "topic": "Defect Management", "question": "What does defect priority usually describe?", "options": ["How urgently the defect should be addressed", "The size of the application", "The programming language used", "The number of test environments"], "correct_answer": "How urgently the defect should be addressed", "explanation": "Priority helps determine the order in which defects should be fixed."},
        {"id": "software_testing_024", "skill": "Software Testing", "topic": "Defect Management", "question": "What is defect retesting?", "options": ["Checking whether a reported defect has been fixed", "Repeating every test without purpose", "Deleting a defect report", "Checking only application colors"], "correct_answer": "Checking whether a reported defect has been fixed", "explanation": "Retesting verifies the specific defect fix under relevant conditions."},
        {"id": "software_testing_025", "skill": "Software Testing", "topic": "Automation", "question": "What is automated testing?", "options": ["Using tools or scripts to execute checks and compare results", "Testing without defining expected behavior", "Only manually reading documentation", "Writing code without running it"], "correct_answer": "Using tools or scripts to execute checks and compare results", "explanation": "Automation helps repeat tests efficiently and consistently."},
        {"id": "software_testing_026", "skill": "Software Testing", "topic": "Automation", "question": "Which Python framework is commonly used for writing unit tests?", "options": ["unittest", "Flask only", "NumPy only", "Matplotlib only"], "correct_answer": "unittest", "explanation": "Python's standard library includes unittest for organizing and running tests."},
        {"id": "software_testing_027", "skill": "Software Testing", "topic": "Automation", "question": "What is pytest commonly used for?", "options": ["Writing and running Python tests", "Creating container images only", "Managing Git branches only", "Designing CSS layouts"], "correct_answer": "Writing and running Python tests", "explanation": "pytest provides test discovery, assertions, fixtures, and a broad plugin ecosystem."},
        {"id": "software_testing_028", "skill": "Software Testing", "topic": "Automation", "question": "What is a test fixture commonly used for?", "options": ["Setting up and cleaning up test resources", "Storing production passwords in source code", "Replacing all assertions", "Creating user interface icons"], "correct_answer": "Setting up and cleaning up test resources", "explanation": "Fixtures provide reusable setup and teardown for tests."},
        {"id": "software_testing_029", "skill": "Software Testing", "topic": "Automation", "question": "What is a mock object used for?", "options": ["Simulating a dependency during a test", "Replacing the entire application permanently", "Measuring screen brightness", "Publishing source code"], "correct_answer": "Simulating a dependency during a test", "explanation": "Mocks can isolate a unit from external services or control dependency behavior."},
        {"id": "software_testing_030", "skill": "Software Testing", "topic": "Coverage", "question": "What does code coverage measure?", "options": ["How much code is exercised by tests under a chosen coverage metric", "Whether the application has no defects", "How popular a repository is", "The total number of developers"], "correct_answer": "How much code is exercised by tests under a chosen coverage metric", "explanation": "Coverage measures execution of code elements, but high coverage does not guarantee correct tests."},
        {"id": "software_testing_031", "skill": "Software Testing", "topic": "Coverage", "question": "What is statement coverage?", "options": ["The proportion of executable statements run by tests", "The number of written requirements", "The number of bugs fixed", "The percentage of users logged in"], "correct_answer": "The proportion of executable statements run by tests", "explanation": "Statement coverage checks whether executable statements were exercised."},
        {"id": "software_testing_032", "skill": "Software Testing", "topic": "Performance Testing", "question": "What is load testing?", "options": ["Evaluating behavior under expected or specified workload", "Checking only invalid login forms", "Testing the installation of an editor", "Reviewing code comments only"], "correct_answer": "Evaluating behavior under expected or specified workload", "explanation": "Load testing assesses performance under a defined level and pattern of demand."},
        {"id": "software_testing_033", "skill": "Software Testing", "topic": "Performance Testing", "question": "What is stress testing?", "options": ["Evaluating behavior beyond normal operating conditions", "Checking only a normal single request", "Reviewing only documentation", "Testing only file names"], "correct_answer": "Evaluating behavior beyond normal operating conditions", "explanation": "Stress testing examines system limits and how it behaves under excessive demand."},
        {"id": "software_testing_034", "skill": "Software Testing", "topic": "Performance Testing", "question": "What does response time measure?", "options": ["Time taken for a system to respond to a request", "Number of developers in a team", "Size of the source code", "Number of files in a repository"], "correct_answer": "Time taken for a system to respond to a request", "explanation": "Response time measures the elapsed time between a request and its response."},
        {"id": "software_testing_035", "skill": "Software Testing", "topic": "Security Testing", "question": "What is security testing intended to identify?", "options": ["Security weaknesses and vulnerabilities", "Only spelling mistakes", "Only user interface colors", "Only slow typing"], "correct_answer": "Security weaknesses and vulnerabilities", "explanation": "Security testing checks whether software protects data and resists relevant threats."},
        {"id": "software_testing_036", "skill": "Software Testing", "topic": "API Testing", "question": "When testing a REST API, what should be checked for a successful request?", "options": ["Status code, response body, and relevant headers", "Only the browser's wallpaper", "Only the developer's username", "Only the number of folders"], "correct_answer": "Status code, response body, and relevant headers", "explanation": "API tests verify response status and content against the endpoint's contract."},
        {"id": "software_testing_037", "skill": "Software Testing", "topic": "API Testing", "question": "What does HTTP status code 404 usually mean?", "options": ["The requested resource was not found", "The request succeeded", "The server returned a successful creation response", "The server always crashed"], "correct_answer": "The requested resource was not found", "explanation": "HTTP 404 indicates that the requested resource was not found."},
        {"id": "software_testing_038", "skill": "Software Testing", "topic": "CI/CD", "question": "Why run automated tests in a CI pipeline?", "options": ["To detect problems automatically when changes are integrated", "To prevent all developers from committing", "To delete the repository after every build", "To replace requirements gathering"], "correct_answer": "To detect problems automatically when changes are integrated", "explanation": "CI pipelines can run tests on changes and report failures early."},
        {"id": "software_testing_039", "skill": "Software Testing", "topic": "Test Strategy", "question": "Why should tests include both valid and invalid inputs?", "options": ["To check normal behavior and error handling", "To guarantee the software has no bugs", "To avoid defining expected results", "To test only the homepage"], "correct_answer": "To check normal behavior and error handling", "explanation": "Valid and invalid cases help assess functionality, validation, and robustness."},
        {"id": "software_testing_040", "skill": "Software Testing", "topic": "Best Practices", "question": "What is a good testing practice?", "options": ["Write clear, repeatable tests with meaningful assertions", "Make tests depend on execution order without reason", "Ignore failing tests permanently", "Use production secrets in test code"], "correct_answer": "Write clear, repeatable tests with meaningful assertions", "explanation": "Reliable, understandable tests provide useful feedback and are easier to maintain."}
    ],
    
    "cybersecurity": [
        {"id": "cybersecurity_001", "skill": "Cybersecurity", "topic": "Security Basics", "question": "What is the main goal of cybersecurity?", "options": ["Protect systems and data from digital threats", "Increase screen brightness", "Improve typing speed", "Design website layouts"], "correct_answer": "Protect systems and data from digital threats", "explanation": "Cybersecurity protects systems, networks, applications, and data from attacks."},
        {"id": "cybersecurity_002", "skill": "Cybersecurity", "topic": "Security Basics", "question": "What does the CIA triad stand for?", "options": ["Confidentiality, Integrity, Availability", "Control, Internet, Access", "Cybersecurity, Intelligence, Authentication", "Communication, Inspection, Authorization"], "correct_answer": "Confidentiality, Integrity, Availability", "explanation": "The CIA triad describes three fundamental information security objectives."},
        {"id": "cybersecurity_003", "skill": "Cybersecurity", "topic": "Security Basics", "question": "What does confidentiality ensure?", "options": ["Only authorized people can access information", "All files are publicly available", "Data is always deleted", "Systems never require updates"], "correct_answer": "Only authorized people can access information", "explanation": "Confidentiality prevents unauthorized disclosure of information."},
        {"id": "cybersecurity_004", "skill": "Cybersecurity", "topic": "Security Basics", "question": "What does data integrity mean?", "options": ["Data remains accurate and is not improperly altered", "Data is always public", "Data is always compressed", "Data is stored without permissions"], "correct_answer": "Data remains accurate and is not improperly altered", "explanation": "Integrity protects information from unauthorized or unintended changes."},
        {"id": "cybersecurity_005", "skill": "Cybersecurity", "topic": "Security Basics", "question": "What does availability mean in information security?", "options": ["Authorized users can access systems when needed", "Every user has administrator access", "All information is encrypted forever", "Passwords are publicly displayed"], "correct_answer": "Authorized users can access systems when needed", "explanation": "Availability ensures systems and information remain accessible to authorized users."},
        {"id": "cybersecurity_006", "skill": "Cybersecurity", "topic": "Threats", "question": "What is malware?", "options": ["Software designed to cause harm or perform unauthorized actions", "A secure backup method", "A programming standard", "A network cable"], "correct_answer": "Software designed to cause harm or perform unauthorized actions", "explanation": "Malware includes malicious programs such as ransomware, spyware, and viruses."},
        {"id": "cybersecurity_007", "skill": "Cybersecurity", "topic": "Threats", "question": "What is a computer virus?", "options": ["Malicious code that attaches to a host and can spread when it runs", "A normal database table", "A security certificate", "A backup application"], "correct_answer": "Malicious code that attaches to a host and can spread when it runs", "explanation": "Traditional viruses attach to files or programs and spread when infected content is executed."},
        {"id": "cybersecurity_008", "skill": "Cybersecurity", "topic": "Threats", "question": "What is ransomware?", "options": ["Malware that can encrypt or lock data and demand payment", "Software used only for backups", "A method of compressing images", "A secure login protocol"], "correct_answer": "Malware that can encrypt or lock data and demand payment", "explanation": "Ransomware commonly denies access to data or systems and demands a ransom."},
        {"id": "cybersecurity_009", "skill": "Cybersecurity", "topic": "Threats", "question": "What is spyware?", "options": ["Software that secretly collects information about users or their activity", "A tool for creating backups", "A type of firewall rule", "A programming language"], "correct_answer": "Software that secretly collects information about users or their activity", "explanation": "Spyware gathers information without appropriate user knowledge or authorization."},
        {"id": "cybersecurity_010", "skill": "Cybersecurity", "topic": "Threats", "question": "What is a Trojan horse in cybersecurity?", "options": ["Malicious software disguised as legitimate software", "A secure password manager", "A network monitoring standard", "A backup file"], "correct_answer": "Malicious software disguised as legitimate software", "explanation": "A Trojan tricks users into running it by appearing legitimate."},
        {"id": "cybersecurity_011", "skill": "Cybersecurity", "topic": "Social Engineering", "question": "What is phishing?", "options": ["Tricking people into revealing information or taking unsafe actions", "Encrypting a hard drive for protection", "Updating an application", "Creating a secure backup"], "correct_answer": "Tricking people into revealing information or taking unsafe actions", "explanation": "Phishing commonly uses deceptive messages or websites to steal credentials or information."},
        {"id": "cybersecurity_012", "skill": "Cybersecurity", "topic": "Social Engineering", "question": "What should you do with a suspicious email asking for your password?", "options": ["Avoid the link and verify the request through an official channel", "Reply with your password", "Forward your credentials to the sender", "Disable account security"], "correct_answer": "Avoid the link and verify the request through an official channel", "explanation": "Independent verification helps prevent credential theft."},
        {"id": "cybersecurity_013", "skill": "Cybersecurity", "topic": "Passwords", "question": "Which password practice is safest?", "options": ["Use long, unique passwords for different accounts", "Reuse one short password everywhere", "Share passwords in public messages", "Use your name for every password"], "correct_answer": "Use long, unique passwords for different accounts", "explanation": "Unique passwords limit the damage if one account is compromised."},
        {"id": "cybersecurity_014", "skill": "Cybersecurity", "topic": "Authentication", "question": "What is multi-factor authentication?", "options": ["Using two or more different types of verification factors", "Using the same password twice", "Creating multiple usernames only", "Disabling login verification"], "correct_answer": "Using two or more different types of verification factors", "explanation": "MFA combines different factors, such as something you know and something you have."},
        {"id": "cybersecurity_015", "skill": "Cybersecurity", "topic": "Authentication", "question": "Which is an example of a biometric authentication factor?", "options": ["Fingerprint", "Username", "PIN written on paper", "Website address"], "correct_answer": "Fingerprint", "explanation": "Biometrics use physical or behavioral characteristics to help verify identity."},
        {"id": "cybersecurity_016", "skill": "Cybersecurity", "topic": "Access Control", "question": "What is the principle of least privilege?", "options": ["Give users only the permissions they need", "Give everyone administrator access", "Disable all user accounts", "Share one account among all employees"], "correct_answer": "Give users only the permissions they need", "explanation": "Least privilege limits unnecessary access and reduces potential damage."},
        {"id": "cybersecurity_017", "skill": "Cybersecurity", "topic": "Access Control", "question": "What is authentication?", "options": ["Verifying a user's identity", "Deciding which files to delete", "Compressing network traffic", "Creating a backup"], "correct_answer": "Verifying a user's identity", "explanation": "Authentication checks that a user or system is who or what it claims to be."},
        {"id": "cybersecurity_018", "skill": "Cybersecurity", "topic": "Access Control", "question": "What is authorization?", "options": ["Determining what an authenticated user is allowed to do", "Checking a computer's temperature", "Creating a username only", "Encrypting every file automatically"], "correct_answer": "Determining what an authenticated user is allowed to do", "explanation": "Authorization defines permitted actions and resources after identity verification."},
        {"id": "cybersecurity_019", "skill": "Cybersecurity", "topic": "Network Security", "question": "What is a firewall used for?", "options": ["Controlling network traffic according to security rules", "Writing application code", "Increasing monitor resolution", "Replacing all passwords"], "correct_answer": "Controlling network traffic according to security rules", "explanation": "Firewalls filter network traffic based on configured policies."},
        {"id": "cybersecurity_020", "skill": "Cybersecurity", "topic": "Network Security", "question": "What is a VPN commonly used for?", "options": ["Creating an encrypted connection over a network", "Guaranteeing complete anonymity online", "Removing all malware automatically", "Replacing multi-factor authentication"], "correct_answer": "Creating an encrypted connection over a network", "explanation": "A VPN can protect traffic between a device and a VPN endpoint, but does not guarantee complete anonymity."},
        {"id": "cybersecurity_021", "skill": "Cybersecurity", "topic": "Network Security", "question": "What is HTTPS designed to provide?", "options": ["Encrypted and authenticated communication with a website endpoint", "A guarantee that a website is honest", "Automatic removal of viruses", "A replacement for strong passwords"], "correct_answer": "Encrypted and authenticated communication with a website endpoint", "explanation": "HTTPS uses TLS to protect web traffic and authenticate the server's identity."},
        {"id": "cybersecurity_022", "skill": "Cybersecurity", "topic": "Encryption", "question": "What is encryption?", "options": ["Transforming readable data into a protected form using a key", "Deleting all data permanently", "Sorting files alphabetically", "Creating duplicate usernames"], "correct_answer": "Transforming readable data into a protected form using a key", "explanation": "Encryption protects information by converting plaintext into ciphertext."},
        {"id": "cybersecurity_023", "skill": "Cybersecurity", "topic": "Encryption", "question": "What is the main difference between hashing and encryption?", "options": ["Hashing is generally one-way, while encryption is designed to be reversible with the proper key", "Hashing always requires two keys", "Encryption cannot protect data", "They are exactly the same"], "correct_answer": "Hashing is generally one-way, while encryption is designed to be reversible with the proper key", "explanation": "Cryptographic hashes are designed to be computationally infeasible to reverse, while encryption supports decryption with the correct key."},
        {"id": "cybersecurity_024", "skill": "Cybersecurity", "topic": "Encryption", "question": "How should an application store user passwords?", "options": ["Using a salted password hash with a suitable password-hashing algorithm", "As plain text in a public file", "In a URL query parameter", "In an unencrypted log file"], "correct_answer": "Using a salted password hash with a suitable password-hashing algorithm", "explanation": "Algorithms such as Argon2id, scrypt, or bcrypt are designed for password storage."},
        {"id": "cybersecurity_025", "skill": "Cybersecurity", "topic": "Web Security", "question": "What is SQL injection?", "options": ["An attack that manipulates database queries through unsafe input handling", "A technique for improving query speed only", "A method for encrypting images", "A type of software backup"], "correct_answer": "An attack that manipulates database queries through unsafe input handling", "explanation": "Parameterized queries help prevent user input from being interpreted as SQL code."},
        {"id": "cybersecurity_026", "skill": "Cybersecurity", "topic": "Web Security", "question": "What is cross-site scripting (XSS)?", "options": ["Injecting malicious script into content viewed by other users", "Copying a database backup", "Encrypting network packets", "Changing a server's hostname"], "correct_answer": "Injecting malicious script into content viewed by other users", "explanation": "XSS can be reduced through contextual output encoding and safe handling of untrusted content."},
        {"id": "cybersecurity_027", "skill": "Cybersecurity", "topic": "Web Security", "question": "What is cross-site request forgery (CSRF)?", "options": ["Tricking a browser into sending an unwanted authenticated request", "Stealing a laptop physically", "Encrypting a database backup", "Creating a strong password"], "correct_answer": "Tricking a browser into sending an unwanted authenticated request", "explanation": "CSRF defenses may include anti-CSRF tokens, SameSite cookies, and origin checks."},
        {"id": "cybersecurity_028", "skill": "Cybersecurity", "topic": "Web Security", "question": "Why should web applications validate input on the server?", "options": ["Client-side checks can be bypassed", "Browsers always send safe data", "Server validation removes the need for authorization", "It automatically encrypts the database"], "correct_answer": "Client-side checks can be bypassed", "explanation": "Server-side validation is necessary because attackers can send requests without using the normal interface."},
        {"id": "cybersecurity_029", "skill": "Cybersecurity", "topic": "Vulnerability Management", "question": "What is a software vulnerability?", "options": ["A weakness that could be exploited to affect security", "A feature that improves usability", "A normal backup", "A type of password manager"], "correct_answer": "A weakness that could be exploited to affect security", "explanation": "Vulnerabilities may exist in software design, implementation, configuration, or dependencies."},
        {"id": "cybersecurity_030", "skill": "Cybersecurity", "topic": "Vulnerability Management", "question": "Why are security updates important?", "options": ["They can fix known vulnerabilities and other defects", "They guarantee no future attacks", "They remove the need for backups", "They make every account public"], "correct_answer": "They can fix known vulnerabilities and other defects", "explanation": "Applying trusted updates reduces exposure to vulnerabilities addressed by those updates."},
        {"id": "cybersecurity_031", "skill": "Cybersecurity", "topic": "Incident Response", "question": "What should an organization do when it detects a security incident?", "options": ["Follow its incident response process to contain, investigate, and recover", "Delete all evidence immediately", "Ignore the alert", "Publish all credentials online"], "correct_answer": "Follow its incident response process to contain, investigate, and recover", "explanation": "A planned response helps limit harm and preserve evidence for investigation."},
        {"id": "cybersecurity_032", "skill": "Cybersecurity", "topic": "Incident Response", "question": "Why are backups important for cybersecurity?", "options": ["They can help restore data after loss or ransomware", "They prevent every attack from occurring", "They replace access control", "They guarantee the server never fails"], "correct_answer": "They can help restore data after loss or ransomware", "explanation": "Tested, protected backups support recovery when data is damaged or unavailable."},
        {"id": "cybersecurity_033", "skill": "Cybersecurity", "topic": "Monitoring", "question": "Why are security logs useful?", "options": ["They help investigate activity and detect suspicious events", "They automatically prevent every intrusion", "They replace all software updates", "They should always contain plaintext passwords"], "correct_answer": "They help investigate activity and detect suspicious events", "explanation": "Logs support monitoring and incident investigation, but must be protected and managed appropriately."},
        {"id": "cybersecurity_034", "skill": "Cybersecurity", "topic": "Monitoring", "question": "What is an intrusion detection system (IDS) designed to do?", "options": ["Identify and alert on suspicious activity", "Automatically guarantee every attack is blocked", "Create user interfaces", "Replace encryption keys"], "correct_answer": "Identify and alert on suspicious activity", "explanation": "An IDS monitors activity and generates alerts; blocking is more characteristic of an IPS."},
        {"id": "cybersecurity_035", "skill": "Cybersecurity", "topic": "Risk Management", "question": "What is a security risk?", "options": ["The possibility that a threat will exploit a weakness and cause harm", "A guaranteed software feature", "A harmless user interface element", "A type of source-code comment"], "correct_answer": "The possibility that a threat will exploit a weakness and cause harm", "explanation": "Risk considers threats, vulnerabilities, likelihood, and potential impact."},
        {"id": "cybersecurity_036", "skill": "Cybersecurity", "topic": "Risk Management", "question": "What is a security policy?", "options": ["A set of rules and expectations for protecting information and systems", "A database query", "A programming language", "A list of website colors"], "correct_answer": "A set of rules and expectations for protecting information and systems", "explanation": "Security policies define required practices, responsibilities, and controls."},
        {"id": "cybersecurity_037", "skill": "Cybersecurity", "topic": "Secure Development", "question": "What is secure coding?", "options": ["Writing software to reduce common security weaknesses", "Writing code without testing", "Storing passwords in source files", "Disabling all error handling"], "correct_answer": "Writing software to reduce common security weaknesses", "explanation": "Secure coding uses practices such as input validation, safe APIs, and appropriate access controls."},
        {"id": "cybersecurity_038", "skill": "Cybersecurity", "topic": "Secure Development", "question": "Why should applications avoid exposing detailed internal error messages to users?", "options": ["They may reveal sensitive implementation details", "They always slow down the internet", "They prevent all debugging", "They automatically create vulnerabilities in every case"], "correct_answer": "They may reveal sensitive implementation details", "explanation": "User-facing errors should be safe while detailed diagnostic information is kept in protected logs."},
        {"id": "cybersecurity_039", "skill": "Cybersecurity", "topic": "Security Testing", "question": "What is penetration testing?", "options": ["Authorized testing that attempts to identify exploitable security weaknesses", "Testing without permission on any system", "Checking only spelling mistakes", "Installing routine application updates"], "correct_answer": "Authorized testing that attempts to identify exploitable security weaknesses", "explanation": "Penetration testing must have clear authorization and a defined scope."},
        {"id": "cybersecurity_040", "skill": "Cybersecurity", "topic": "Best Practices", "question": "Which practice best supports everyday security?", "options": ["Keep software updated, use unique passwords, and enable MFA", "Reuse one password everywhere", "Ignore suspicious messages", "Disable backups and logging"], "correct_answer": "Keep software updated, use unique passwords, and enable MFA", "explanation": "Layered security practices reduce common account and system risks."}
    ],
    "tailwind css": [
        {"id": "tailwind_001", "skill": "Tailwind CSS", "topic": "Basics", "question": "What is Tailwind CSS?", "options": ["A utility-first CSS framework", "A JavaScript database", "A backend programming language", "A web browser"], "correct_answer": "A utility-first CSS framework", "explanation": "Tailwind provides utility classes for styling elements directly in markup."},
        {"id": "tailwind_002", "skill": "Tailwind CSS", "topic": "Basics", "question": "Which class commonly adds a blue background in Tailwind?", "options": ["bg-blue-500", "blue-background", "background-blue", "color-bg-blue"], "correct_answer": "bg-blue-500", "explanation": "The bg- utility controls background color, and blue-500 selects a shade."},
        {"id": "tailwind_003", "skill": "Tailwind CSS", "topic": "Typography", "question": "Which class makes text bold?", "options": ["font-bold", "text-bold", "bold-font", "weight-bold-text"], "correct_answer": "font-bold", "explanation": "font-bold applies a bold font weight."},
        {"id": "tailwind_004", "skill": "Tailwind CSS", "topic": "Typography", "question": "Which class increases text size to a large preset?", "options": ["text-lg", "font-lg", "size-text-large", "large-font"], "correct_answer": "text-lg", "explanation": "text-lg applies Tailwind's large text-size utility."},
        {"id": "tailwind_005", "skill": "Tailwind CSS", "topic": "Spacing", "question": "Which utility adds padding on all sides?", "options": ["p-4", "m-4", "gap-4", "w-4"], "correct_answer": "p-4", "explanation": "The p- prefix controls padding on all sides."},
        {"id": "tailwind_006", "skill": "Tailwind CSS", "topic": "Spacing", "question": "Which utility adds margin on all sides?", "options": ["m-4", "p-4", "px-4", "rounded-4"], "correct_answer": "m-4", "explanation": "The m- prefix controls margin."},
        {"id": "tailwind_007", "skill": "Tailwind CSS", "topic": "Spacing", "question": "What does px-4 control?", "options": ["Horizontal padding", "Vertical margin", "Text color", "Element opacity"], "correct_answer": "Horizontal padding", "explanation": "px- applies padding on the left and right sides."},
        {"id": "tailwind_008", "skill": "Tailwind CSS", "topic": "Spacing", "question": "What does py-4 control?", "options": ["Vertical padding", "Horizontal margin", "Border width", "Font weight"], "correct_answer": "Vertical padding", "explanation": "py- applies padding on the top and bottom sides."},
        {"id": "tailwind_009", "skill": "Tailwind CSS", "topic": "Layout", "question": "Which class makes an element use Flexbox?", "options": ["flex", "display-flexbox", "flexbox-on", "d-flexbox"], "correct_answer": "flex", "explanation": "The flex utility sets display to flex."},
        {"id": "tailwind_010", "skill": "Tailwind CSS", "topic": "Layout", "question": "Which class creates a CSS Grid container?", "options": ["grid", "grid-on", "display-grid-layout", "columns-grid"], "correct_answer": "grid", "explanation": "The grid utility sets display to grid."},
        {"id": "tailwind_011", "skill": "Tailwind CSS", "topic": "Layout", "question": "Which utility centers flex items along the main axis?", "options": ["justify-center", "items-center", "text-center", "content-bold"], "correct_answer": "justify-center", "explanation": "justify-center sets main-axis alignment to center in a flex container."},
        {"id": "tailwind_012", "skill": "Tailwind CSS", "topic": "Layout", "question": "Which utility aligns flex items along the cross axis?", "options": ["items-center", "justify-center", "text-center", "align-text-center"], "correct_answer": "items-center", "explanation": "items-center applies align-items: center."},
        {"id": "tailwind_013", "skill": "Tailwind CSS", "topic": "Layout", "question": "Which utility adds spacing between children in a flex or grid layout?", "options": ["gap-4", "space-color-4", "margin-text-4", "border-gap-4"], "correct_answer": "gap-4", "explanation": "The gap utility sets the gap between layout items."},
        {"id": "tailwind_014", "skill": "Tailwind CSS", "topic": "Sizing", "question": "Which utility sets an element's width to 100%?", "options": ["w-full", "h-full", "width-max", "full-width-only"], "correct_answer": "w-full", "explanation": "w-full sets width to 100% of the containing block."},
        {"id": "tailwind_015", "skill": "Tailwind CSS", "topic": "Sizing", "question": "Which utility sets an element's height to 100%?", "options": ["h-full", "w-full", "height-max", "full-height-only"], "correct_answer": "h-full", "explanation": "h-full sets height to 100%, subject to the containing block's sizing."},
        {"id": "tailwind_016", "skill": "Tailwind CSS", "topic": "Borders", "question": "Which utility commonly rounds an element's corners?", "options": ["rounded", "corner-round", "border-circle-only", "curve"], "correct_answer": "rounded", "explanation": "rounded applies a border-radius utility."},
        {"id": "tailwind_017", "skill": "Tailwind CSS", "topic": "Borders", "question": "Which utility adds a border?", "options": ["border", "outline-only", "line-add", "edge-on"], "correct_answer": "border", "explanation": "The border utility adds a border using the configured default width and color."},
        {"id": "tailwind_018", "skill": "Tailwind CSS", "topic": "Responsive Design", "question": "What does the md: prefix commonly represent?", "options": ["Apply a utility at the medium breakpoint and above", "Apply a utility only to mobile phones", "Disable the utility everywhere", "Create a database model"], "correct_answer": "Apply a utility at the medium breakpoint and above", "explanation": "Tailwind responsive prefixes generally apply at their breakpoint and larger widths."},
        {"id": "tailwind_019", "skill": "Tailwind CSS", "topic": "Responsive Design", "question": "Which is an example of responsive width styling?", "options": ["w-full md:w-1/2", "width-full-medium-half", "responsive-width-50", "w-md-only-mobile"], "correct_answer": "w-full md:w-1/2", "explanation": "This makes the element full width by default and half width at the medium breakpoint and above."},
        {"id": "tailwind_020", "skill": "Tailwind CSS", "topic": "States", "question": "What does hover:bg-blue-700 do?", "options": ["Changes the background on hover", "Changes the background only while printing", "Sets the text to bold", "Hides the element permanently"], "correct_answer": "Changes the background on hover", "explanation": "The hover variant applies the background utility while the element is hovered."},
        {"id": "tailwind_021", "skill": "Tailwind CSS", "topic": "States", "question": "Which prefix applies a utility when a button receives keyboard focus?", "options": ["focus:", "hover:", "group:", "dark:"], "correct_answer": "focus:", "explanation": "The focus variant applies styles when the element matches the focus state."},
        {"id": "tailwind_022", "skill": "Tailwind CSS", "topic": "States", "question": "What does disabled:opacity-50 do?", "options": ["Applies 50% opacity when the element is disabled", "Disables the entire website", "Sets width to 50%", "Changes the border to 50 pixels"], "correct_answer": "Applies 50% opacity when the element is disabled", "explanation": "The disabled variant styles an element when it is disabled."},
        {"id": "tailwind_023", "skill": "Tailwind CSS", "topic": "Dark Mode", "question": "What does dark:bg-gray-900 commonly do?", "options": ["Applies a dark background in the configured dark mode", "Always hides the background", "Makes the font size smaller", "Creates a dark database"], "correct_answer": "Applies a dark background in the configured dark mode", "explanation": "The dark variant applies its utility when Tailwind's configured dark-mode condition is active."},
        {"id": "tailwind_024", "skill": "Tailwind CSS", "topic": "Display", "question": "Which utility hides an element from layout?", "options": ["hidden", "invisible-text-only", "opacity-full", "display-show"], "correct_answer": "hidden", "explanation": "hidden sets display: none, removing the element from layout."},
        {"id": "tailwind_025", "skill": "Tailwind CSS", "topic": "Display", "question": "What is the difference between invisible and hidden?", "options": ["Invisible preserves layout space; hidden removes the element from layout", "They always have identical effects", "Invisible makes the element bold", "Hidden only changes text color"], "correct_answer": "Invisible preserves layout space; hidden removes the element from layout", "explanation": "invisible uses visibility: hidden, while hidden uses display: none."},
        {"id": "tailwind_026", "skill": "Tailwind CSS", "topic": "Positioning", "question": "Which utility establishes relative positioning?", "options": ["relative", "position-relative-on", "rel", "place-relative"], "correct_answer": "relative", "explanation": "relative applies position: relative."},
        {"id": "tailwind_027", "skill": "Tailwind CSS", "topic": "Positioning", "question": "Which utility positions an element absolutely?", "options": ["absolute", "relative", "fixed-layout-only", "position-free"], "correct_answer": "absolute", "explanation": "absolute applies position: absolute and positions the element relative to its containing block."},
        {"id": "tailwind_028", "skill": "Tailwind CSS", "topic": "Typography", "question": "Which utility centers text horizontally?", "options": ["text-center", "items-center", "justify-center", "font-center"], "correct_answer": "text-center", "explanation": "text-center applies centered text alignment."},
        {"id": "tailwind_029", "skill": "Tailwind CSS", "topic": "Typography", "question": "Which utility changes text color?", "options": ["text-red-500", "bg-red-500", "border-red-500", "fill-red-500-only"], "correct_answer": "text-red-500", "explanation": "The text- prefix controls text color when followed by a color utility."},
        {"id": "tailwind_030", "skill": "Tailwind CSS", "topic": "Effects", "question": "Which utility adds a box shadow?", "options": ["shadow", "box-glow-only", "border-shadow", "elevation-text"], "correct_answer": "shadow", "explanation": "shadow applies a predefined box-shadow utility."},
        {"id": "tailwind_031", "skill": "Tailwind CSS", "topic": "Effects", "question": "Which utility controls an element's opacity?", "options": ["opacity-50", "transparency-50", "alpha-text-50", "fade-width-50"], "correct_answer": "opacity-50", "explanation": "opacity-50 sets the element's opacity to 50%."},
        {"id": "tailwind_032", "skill": "Tailwind CSS", "topic": "Transitions", "question": "Which utility enables a transition for supported CSS properties?", "options": ["transition", "animate-only-transition", "motion-on", "change-smooth"], "correct_answer": "transition", "explanation": "transition configures transition properties using Tailwind's predefined transition utility."},
        {"id": "tailwind_033", "skill": "Tailwind CSS", "topic": "Transitions", "question": "What does duration-300 control?", "options": ["Transition or animation duration in milliseconds", "Element width in pixels", "Font weight", "Border radius"], "correct_answer": "Transition or animation duration in milliseconds", "explanation": "duration-300 sets a 300-millisecond duration for supported transitions or animations."},
        {"id": "tailwind_034", "skill": "Tailwind CSS", "topic": "Configuration", "question": "What is the purpose of Tailwind's theme configuration?", "options": ["Customize design tokens such as colors, spacing, and fonts", "Store database passwords", "Run backend Python code", "Manage Git commits"], "correct_answer": "Customize design tokens such as colors, spacing, and fonts", "explanation": "Theme configuration defines or extends reusable design values."},
        {"id": "tailwind_035", "skill": "Tailwind CSS", "topic": "Configuration", "question": "Why must Tailwind detect class names used in source files?", "options": ["To generate the CSS utilities required by the project", "To run JavaScript functions", "To create a database", "To authenticate users"], "correct_answer": "To generate the CSS utilities required by the project", "explanation": "Tailwind scans configured sources to identify utilities that need to be included in the generated CSS."},
        {"id": "tailwind_036", "skill": "Tailwind CSS", "topic": "Customization", "question": "How can you style an element with a one-off custom value in Tailwind?", "options": ["Use an arbitrary value such as w-[250px]", "Write width=250 directly as a class", "Use python-width-250", "Use only the HTML id attribute"], "correct_answer": "Use an arbitrary value such as w-[250px]", "explanation": "Arbitrary values allow supported CSS values to be expressed in utility classes."},
        {"id": "tailwind_037", "skill": "Tailwind CSS", "topic": "Best Practices", "question": "What is a benefit of utility classes?", "options": ["They let developers style elements directly using reusable CSS utilities", "They eliminate the need for HTML", "They guarantee every design is accessible", "They replace JavaScript in all projects"], "correct_answer": "They let developers style elements directly using reusable CSS utilities", "explanation": "Utility classes provide a consistent set of styling tools that can be composed in markup."},
        {"id": "tailwind_038", "skill": "Tailwind CSS", "topic": "Best Practices", "question": "Why should responsive layouts be tested at multiple viewport sizes?", "options": ["To identify layout issues across different screen widths", "To guarantee a database is secure", "To increase API request limits", "To install additional fonts automatically"], "correct_answer": "To identify layout issues across different screen widths", "explanation": "Testing multiple viewport sizes helps identify overflow and layout problems."},
        {"id": "tailwind_039", "skill": "Tailwind CSS", "topic": "Accessibility", "question": "What should you consider when styling keyboard focus?", "options": ["Keep a clearly visible focus indicator", "Remove all focus indicators without replacement", "Make all text transparent", "Disable keyboard navigation"], "correct_answer": "Keep a clearly visible focus indicator", "explanation": "Visible focus styles help keyboard users understand which element is active."},
        {"id": "tailwind_040", "skill": "Tailwind CSS", "topic": "Tailwind CSS Versions", "question": "In Tailwind CSS v4, which directive is commonly used to import the framework in a CSS entry file?", "options": ["@import \"tailwindcss\";", "@tailwind-v4 all;", "import tailwind from html;", "require(\"tailwind.css\") inside HTML"], "correct_answer": "@import \"tailwindcss\";", "explanation": "Tailwind CSS v4 commonly uses @import \"tailwindcss\"; as the CSS entry point."}
    ],
    "bootstrap": [
        {"id": "bootstrap_001", "skill": "Bootstrap", "topic": "Basics", "question": "What is Bootstrap?", "options": ["A frontend framework for responsive websites", "A database management system", "A backend-only language", "A version control system"], "correct_answer": "A frontend framework for responsive websites", "explanation": "Bootstrap provides CSS components, layout utilities, and optional JavaScript plugins."},
        {"id": "bootstrap_002", "skill": "Bootstrap", "topic": "Setup", "question": "What is a common way to add Bootstrap CSS to a webpage quickly?", "options": ["Include its stylesheet using a CDN link", "Install a database table", "Add a Python import to HTML", "Create a Git branch"], "correct_answer": "Include its stylesheet using a CDN link", "explanation": "A CDN stylesheet can make Bootstrap CSS available without downloading it into the project manually."},
        {"id": "bootstrap_003", "skill": "Bootstrap", "topic": "Grid System", "question": "How many columns are in Bootstrap's standard grid at each breakpoint?", "options": ["6", "8", "12", "16"], "correct_answer": "12", "explanation": "Bootstrap's standard grid is based on 12 columns."},
        {"id": "bootstrap_004", "skill": "Bootstrap", "topic": "Grid System", "question": "Which class commonly creates a responsive fixed-width container?", "options": ["container", "row", "col", "btn"], "correct_answer": "container", "explanation": "The container class provides responsive maximum-width behavior at defined breakpoints."},
        {"id": "bootstrap_005", "skill": "Bootstrap", "topic": "Grid System", "question": "What is the purpose of the row class?", "options": ["Group columns in the grid layout", "Create a password field", "Display an alert message only", "Load JavaScript automatically"], "correct_answer": "Group columns in the grid layout", "explanation": "Rows organize columns and manage the grid's horizontal layout and gutters."},
        {"id": "bootstrap_006", "skill": "Bootstrap", "topic": "Grid System", "question": "Which class commonly represents a grid column?", "options": ["col", "row", "container", "navbar"], "correct_answer": "col", "explanation": "The col class creates a flexible grid column."},
        {"id": "bootstrap_007", "skill": "Bootstrap", "topic": "Grid System", "question": "What does col-md-6 commonly mean?", "options": ["Half-width column at the medium breakpoint and above", "A six-pixel margin", "A column hidden at every size", "A six-row table"], "correct_answer": "Half-width column at the medium breakpoint and above", "explanation": "In the 12-column grid, 6 columns represent half the row width."},
        {"id": "bootstrap_008", "skill": "Bootstrap", "topic": "Grid System", "question": "What is the purpose of Bootstrap breakpoints?", "options": ["Apply responsive layout rules at different viewport widths", "Set database connection limits", "Manage user passwords", "Create server-side routes"], "correct_answer": "Apply responsive layout rules at different viewport widths", "explanation": "Breakpoints allow layouts and components to adapt to screen sizes."},
        {"id": "bootstrap_009", "skill": "Bootstrap", "topic": "Buttons", "question": "Which class creates a standard Bootstrap button style?", "options": ["btn", "button-bootstrap-only", "clickable", "form-button-style"], "correct_answer": "btn", "explanation": "The btn class provides the base styling for Bootstrap buttons."},
        {"id": "bootstrap_010", "skill": "Bootstrap", "topic": "Buttons", "question": "Which class gives a button the primary theme style?", "options": ["btn-primary", "btn-main-only", "primary-button", "button-blue-default"], "correct_answer": "btn-primary", "explanation": "btn-primary applies Bootstrap's primary button appearance."},
        {"id": "bootstrap_011", "skill": "Bootstrap", "topic": "Typography", "question": "Which class centers text?", "options": ["text-center", "align-middle-only", "center-font", "font-center"], "correct_answer": "text-center", "explanation": "text-center applies centered text alignment."},
        {"id": "bootstrap_012", "skill": "Bootstrap", "topic": "Spacing", "question": "What does the Bootstrap class mt-3 represent?", "options": ["Top margin using spacing level 3", "Top padding of three pixels", "Text size 3", "A three-column layout"], "correct_answer": "Top margin using spacing level 3", "explanation": "The m prefix means margin and t specifies the top side; 3 selects a spacing scale value."},
        {"id": "bootstrap_013", "skill": "Bootstrap", "topic": "Spacing", "question": "What does the class p-3 control?", "options": ["Padding on all sides", "Only bottom margin", "Text alignment", "Border color only"], "correct_answer": "Padding on all sides", "explanation": "The p prefix applies padding, and 3 selects a spacing scale value."},
        {"id": "bootstrap_014", "skill": "Bootstrap", "topic": "Colors", "question": "Which class commonly applies Bootstrap's success text color?", "options": ["text-success", "font-green-only", "success-font", "color-good"], "correct_answer": "text-success", "explanation": "text-success uses the theme's success text color."},
        {"id": "bootstrap_015", "skill": "Bootstrap", "topic": "Alerts", "question": "Which class provides the base Bootstrap alert styling?", "options": ["alert", "message-box", "notice-only", "warning-container"], "correct_answer": "alert", "explanation": "The alert class supplies the base styling for alert components."},
        {"id": "bootstrap_016", "skill": "Bootstrap", "topic": "Alerts", "question": "Which class combines the alert component with its success variant?", "options": ["alert alert-success", "success-message-only", "alert-green-text", "btn-success alert"], "correct_answer": "alert alert-success", "explanation": "The base alert class and alert-success variant create a success alert."},
        {"id": "bootstrap_017", "skill": "Bootstrap", "topic": "Navigation", "question": "Which class is commonly used for a Bootstrap navigation bar?", "options": ["navbar", "nav-container-only", "navigation-flex", "menu-bar-bootstrap"], "correct_answer": "navbar", "explanation": "navbar is the base class for Bootstrap navigation bars."},
        {"id": "bootstrap_018", "skill": "Bootstrap", "topic": "Navigation", "question": "What does navbar-expand-lg generally control?", "options": ["When the navbar expands into its larger-screen layout", "The navbar's font size only", "The number of navigation links allowed", "The height of every page"], "correct_answer": "When the navbar expands into its larger-screen layout", "explanation": "The lg breakpoint controls when the navbar switches to its expanded layout."},
        {"id": "bootstrap_019", "skill": "Bootstrap", "topic": "Forms", "question": "Which class commonly styles a text input in Bootstrap?", "options": ["form-control", "input-bootstrap-only", "text-input-style", "form-input-box"], "correct_answer": "form-control", "explanation": "form-control styles standard form inputs and textareas."},
        {"id": "bootstrap_020", "skill": "Bootstrap", "topic": "Forms", "question": "Which class commonly styles a form label?", "options": ["form-label", "label-control-only", "input-label-box", "form-text-title"], "correct_answer": "form-label", "explanation": "form-label provides standard spacing and styling for form labels."},
        {"id": "bootstrap_021", "skill": "Bootstrap", "topic": "Forms", "question": "Which HTML attribute makes a form field mandatory in browser validation?", "options": ["required", "mandatory-bootstrap", "validate-now", "must-fill-class"], "correct_answer": "required", "explanation": "The required HTML attribute enables native browser checks that the field has a value."},
        {"id": "bootstrap_022", "skill": "Bootstrap", "topic": "Tables", "question": "Which class provides Bootstrap's basic table styling?", "options": ["table", "table-style-only", "grid-table", "bootstrap-data"], "correct_answer": "table", "explanation": "The table class applies Bootstrap's base table styles."},
        {"id": "bootstrap_023", "skill": "Bootstrap", "topic": "Tables", "question": "Which class adds alternating background colors to table body rows?", "options": ["table-striped", "table-alternate-only", "row-colors", "striped-body"], "correct_answer": "table-striped", "explanation": "table-striped styles alternating rows to improve readability."},
        {"id": "bootstrap_024", "skill": "Bootstrap", "topic": "Cards", "question": "Which class is the base for a Bootstrap card component?", "options": ["card", "panel-bootstrap-only", "box-card", "content-tile"], "correct_answer": "card", "explanation": "The card class creates a flexible content container."},
        {"id": "bootstrap_025", "skill": "Bootstrap", "topic": "Cards", "question": "Which class is commonly used for the main content area inside a card?", "options": ["card-body", "card-content-only", "body-card-text", "card-main"], "correct_answer": "card-body", "explanation": "card-body adds padding for a card's main content."},
        {"id": "bootstrap_026", "skill": "Bootstrap", "topic": "Images", "question": "Which class makes an image scale responsively within its parent?", "options": ["img-fluid", "image-responsive-only", "img-scale", "fluid-picture"], "correct_answer": "img-fluid", "explanation": "img-fluid applies max-width: 100% and height: auto."},
        {"id": "bootstrap_027", "skill": "Bootstrap", "topic": "Display Utilities", "question": "Which class hides an element at the medium breakpoint and above while leaving it displayed below that breakpoint?", "options": ["d-md-none", "d-none d-md-block", "d-block", "visible-md"], "correct_answer": "d-md-none", "explanation": "d-md-none applies display: none at the medium breakpoint and larger sizes."},
        {"id": "bootstrap_028", "skill": "Bootstrap", "topic": "Flex Utilities", "question": "Which class applies Flexbox display?", "options": ["d-flex", "flex-on", "display-flexbox", "flex-container-bootstrap"], "correct_answer": "d-flex", "explanation": "d-flex sets display: flex."},
        {"id": "bootstrap_029", "skill": "Bootstrap", "topic": "Flex Utilities", "question": "Which class centers flex items along the main axis?", "options": ["justify-content-center", "align-items-center", "text-center", "center-flex-only"], "correct_answer": "justify-content-center", "explanation": "justify-content-center centers flex items along the main axis."},
        {"id": "bootstrap_030", "skill": "Bootstrap", "topic": "Flex Utilities", "question": "Which class aligns flex items along the cross axis at the center?", "options": ["align-items-center", "justify-content-center", "text-center", "align-text-center"], "correct_answer": "align-items-center", "explanation": "align-items-center applies center alignment on the cross axis."},
        {"id": "bootstrap_031", "skill": "Bootstrap", "topic": "JavaScript Components", "question": "What does Bootstrap's JavaScript bundle include?", "options": ["Bootstrap JavaScript plugins and Popper where required", "A complete Python interpreter", "A SQL database server", "A Git command-line tool"], "correct_answer": "Bootstrap JavaScript plugins and Popper where required", "explanation": "The Bootstrap bundle includes its JavaScript plugins and Popper for components that need it."},
        {"id": "bootstrap_032", "skill": "Bootstrap", "topic": "Modals", "question": "What is a modal used for?", "options": ["Displaying content in an overlay that requires user attention", "Creating a database index", "Styling only inline text", "Managing Git branches"], "correct_answer": "Displaying content in an overlay that requires user attention", "explanation": "Modals display focused content above the main page, commonly with a backdrop."},
        {"id": "bootstrap_033", "skill": "Bootstrap", "topic": "Dropdowns", "question": "What does a Bootstrap dropdown commonly provide?", "options": ["A toggleable menu of links or actions", "A permanent page footer", "A database query editor", "A replacement for the grid system"], "correct_answer": "A toggleable menu of links or actions", "explanation": "Dropdowns show a menu that users can open and close."},
        {"id": "bootstrap_034", "skill": "Bootstrap", "topic": "Responsive Design", "question": "What is mobile-first design?", "options": ["Designing for smaller screens first and enhancing for larger screens", "Designing only for desktop computers", "Removing all responsive behavior", "Using only fixed-width layouts"], "correct_answer": "Designing for smaller screens first and enhancing for larger screens", "explanation": "Mobile-first approaches start with small-screen layouts and progressively add larger-screen behavior."},
        {"id": "bootstrap_035", "skill": "Bootstrap", "topic": "Customization", "question": "How can developers customize Bootstrap theme variables during a Sass build?", "options": ["Override supported Sass variables before importing Bootstrap Sass", "Edit a database row", "Change only the HTML title", "Use Git push to change CSS variables"], "correct_answer": "Override supported Sass variables before importing Bootstrap Sass", "explanation": "Sass customization lets developers configure supported design variables during compilation."},
        {"id": "bootstrap_036", "skill": "Bootstrap", "topic": "Accessibility", "question": "Why should Bootstrap forms use associated labels?", "options": ["They help users and assistive technologies identify form fields", "They automatically encrypt form submissions", "They eliminate server-side validation", "They make every field optional"], "correct_answer": "They help users and assistive technologies identify form fields", "explanation": "Proper labels improve usability and accessibility, including for screen-reader users."},
        {"id": "bootstrap_037", "skill": "Bootstrap", "topic": "Accessibility", "question": "Why should color not be the only way to communicate an error?", "options": ["Some users may not distinguish the colors", "Color always slows down websites", "Bootstrap does not support text", "Errors cannot be displayed in forms"], "correct_answer": "Some users may not distinguish the colors", "explanation": "Text or icons with accessible labels provide additional information beyond color alone."},
        {"id": "bootstrap_038", "skill": "Bootstrap", "topic": "Utilities", "question": "Which utility commonly adds a shadow to an element?", "options": ["shadow", "box-shadow-bootstrap-only", "elevation-on", "border-glow"], "correct_answer": "shadow", "explanation": "Bootstrap provides shadow utilities such as shadow, shadow-sm, and shadow-lg."},
        {"id": "bootstrap_039", "skill": "Bootstrap", "topic": "Utilities", "question": "Which utility rounds an element's corners in Bootstrap?", "options": ["rounded", "corner-round", "radius-on", "border-curve-only"], "correct_answer": "rounded", "explanation": "The rounded utility applies a border radius."},
        {"id": "bootstrap_040", "skill": "Bootstrap", "topic": "Best Practices", "question": "What is a good practice when building with Bootstrap?", "options": ["Test responsive behavior and customize components to fit the project", "Assume every default component is automatically accessible", "Ignore mobile screen sizes", "Use every component on every page"], "correct_answer": "Test responsive behavior and customize components to fit the project", "explanation": "Responsive testing and thoughtful customization help produce usable, consistent interfaces."}
    ],
    
    "data analysis": [
        {"id": "data_analysis_001", "skill": "Data Analysis", "topic": "Fundamentals", "question": "What is data analysis?", "options": ["Examining data to find useful insights", "Deleting all stored data", "Writing code without data", "Designing computer hardware"], "correct_answer": "Examining data to find useful insights", "explanation": "Data analysis examines and interprets data to support decisions."},
        {"id": "data_analysis_002", "skill": "Data Analysis", "topic": "Data Types", "question": "Which is an example of numerical data?", "options": ["Age in years", "Favorite color", "City name", "Product category"], "correct_answer": "Age in years", "explanation": "Numerical data represents quantities that can be counted or measured."},
        {"id": "data_analysis_003", "skill": "Data Analysis", "topic": "Data Types", "question": "Which is an example of categorical data?", "options": ["Blood group", "Height in centimeters", "Monthly income", "Temperature"], "correct_answer": "Blood group", "explanation": "Categorical data represents groups or labels rather than measured quantities."},
        {"id": "data_analysis_004", "skill": "Data Analysis", "topic": "Data Collection", "question": "What is structured data?", "options": ["Data organized into a defined format such as rows and columns", "Data without any organization", "Only image files", "Only audio recordings"], "correct_answer": "Data organized into a defined format such as rows and columns", "explanation": "Structured data follows a predefined schema, often in tables."},
        {"id": "data_analysis_005", "skill": "Data Analysis", "topic": "Data Cleaning", "question": "What is data cleaning?", "options": ["Identifying and correcting data quality problems", "Changing every value randomly", "Deleting all valid records", "Creating charts without checking data"], "correct_answer": "Identifying and correcting data quality problems", "explanation": "Data cleaning handles missing, invalid, inconsistent, or duplicate data."},
        {"id": "data_analysis_006", "skill": "Data Analysis", "topic": "Data Cleaning", "question": "What is a missing value?", "options": ["A field with no recorded value", "A value that is always zero", "A duplicate row", "A column heading"], "correct_answer": "A field with no recorded value", "explanation": "Missing values indicate information that was not recorded or is unavailable."},
        {"id": "data_analysis_007", "skill": "Data Analysis", "topic": "Data Cleaning", "question": "How can duplicate records affect analysis?", "options": ["They may cause counts or summaries to be incorrect", "They always improve accuracy", "They automatically fill missing values", "They convert text into numbers"], "correct_answer": "They may cause counts or summaries to be incorrect", "explanation": "Unintended duplicates can overrepresent observations and distort results."},
        {"id": "data_analysis_008", "skill": "Data Analysis", "topic": "Data Cleaning", "question": "What is an outlier?", "options": ["An observation unusually far from most other observations", "The first column in every table", "A missing column name", "The average of a dataset"], "correct_answer": "An observation unusually far from most other observations", "explanation": "Outliers are unusual observations that may reflect real events or data errors."},
        {"id": "data_analysis_009", "skill": "Data Analysis", "topic": "Python Tools", "question": "Which Python library is widely used for tabular data analysis?", "options": ["Pandas", "Flask", "Pygame", "Tkinter"], "correct_answer": "Pandas", "explanation": "Pandas provides Series and DataFrame structures for data manipulation."},
        {"id": "data_analysis_010", "skill": "Data Analysis", "topic": "Python Tools", "question": "Which Pandas structure represents a two-dimensional table?", "options": ["DataFrame", "Series", "Tuple", "Set"], "correct_answer": "DataFrame", "explanation": "A DataFrame stores tabular data organized into rows and columns."},
        {"id": "data_analysis_011", "skill": "Data Analysis", "topic": "Python Tools", "question": "Which Pandas function reads a CSV file?", "options": ["pd.read_csv()", "pd.open_table()", "pd.load_html_only()", "pd.read_image()"], "correct_answer": "pd.read_csv()", "explanation": "pd.read_csv() loads comma-separated data into a DataFrame."},
        {"id": "data_analysis_012", "skill": "Data Analysis", "topic": "Python Tools", "question": "Which command displays the first five rows of a DataFrame by default?", "options": ["df.head()", "df.tail()", "df.describe()", "df.drop()"], "correct_answer": "df.head()", "explanation": "head() returns the first five rows unless another number is specified."},
        {"id": "data_analysis_013", "skill": "Data Analysis", "topic": "Python Tools", "question": "Which Pandas method provides common numerical summary statistics?", "options": ["describe()", "rename()", "dropna()", "sort_index()"], "correct_answer": "describe()", "explanation": "describe() summarizes statistics such as count, mean, standard deviation, and quartiles for numerical columns."},
        {"id": "data_analysis_014", "skill": "Data Analysis", "topic": "Filtering", "question": "What is data filtering?", "options": ["Selecting records that meet specified conditions", "Deleting every column", "Changing all numbers to text", "Sorting files by size only"], "correct_answer": "Selecting records that meet specified conditions", "explanation": "Filtering selects observations that satisfy one or more conditions."},
        {"id": "data_analysis_015", "skill": "Data Analysis", "topic": "Filtering", "question": "In Pandas, what does df[df['age'] > 18] return?", "options": ["Rows where age is greater than 18", "Only the age column for all rows", "Rows where age equals zero", "The number of columns"], "correct_answer": "Rows where age is greater than 18", "explanation": "Boolean indexing selects rows whose age condition evaluates to true."},
        {"id": "data_analysis_016", "skill": "Data Analysis", "topic": "Aggregation", "question": "What does aggregation do in data analysis?", "options": ["Combines data into summaries such as totals or averages", "Encrypts every row", "Creates random values", "Removes the dataset schema"], "correct_answer": "Combines data into summaries such as totals or averages", "explanation": "Aggregation summarizes groups of observations using calculations."},
        {"id": "data_analysis_017", "skill": "Data Analysis", "topic": "Aggregation", "question": "What is the purpose of groupby() in Pandas?", "options": ["Group records by values for analysis", "Rename the Python installation", "Delete the entire DataFrame", "Convert every column into an image"], "correct_answer": "Group records by values for analysis", "explanation": "groupby() supports operations such as calculating totals or averages for each group."},
        {"id": "data_analysis_018", "skill": "Data Analysis", "topic": "Statistics", "question": "How is the mean calculated?", "options": ["Sum of values divided by their count", "Largest value minus smallest value", "Most frequent value only", "Middle value only"], "correct_answer": "Sum of values divided by their count", "explanation": "The arithmetic mean is the sum of observations divided by the number of observations."},
        {"id": "data_analysis_019", "skill": "Data Analysis", "topic": "Statistics", "question": "What does the median represent?", "options": ["The middle value in sorted data", "The sum of all values", "The largest value", "The number of columns"], "correct_answer": "The middle value in sorted data", "explanation": "The median is the middle observation, or the average of the two middle observations for even-sized data."},
        {"id": "data_analysis_020", "skill": "Data Analysis", "topic": "Statistics", "question": "What does correlation measure?", "options": ["The strength and direction of an association between variables", "The number of missing rows only", "The file size", "The exact cause of every event"], "correct_answer": "The strength and direction of an association between variables", "explanation": "Correlation measures association but does not by itself establish causation."},
        {"id": "data_analysis_021", "skill": "Data Analysis", "topic": "Visualization", "question": "Which chart is commonly used to compare values across categories?", "options": ["Bar chart", "Scatter plot only", "Network diagram only", "Map only"], "correct_answer": "Bar chart", "explanation": "Bar charts make it easy to compare quantities across categories."},
        {"id": "data_analysis_022", "skill": "Data Analysis", "topic": "Visualization", "question": "Which chart is often useful for showing a trend over time?", "options": ["Line chart", "Pie chart only", "Word cloud", "Venn diagram"], "correct_answer": "Line chart", "explanation": "Line charts show how values change across an ordered sequence such as dates."},
        {"id": "data_analysis_023", "skill": "Data Analysis", "topic": "Visualization", "question": "Which chart helps examine the relationship between two numerical variables?", "options": ["Scatter plot", "Pie chart", "Organization chart", "Gantt chart"], "correct_answer": "Scatter plot", "explanation": "Each point in a scatter plot represents a pair of numerical values."},
        {"id": "data_analysis_024", "skill": "Data Analysis", "topic": "Visualization", "question": "Which chart is useful for viewing the distribution of a numerical variable?", "options": ["Histogram", "Flowchart", "Org chart", "Network topology"], "correct_answer": "Histogram", "explanation": "A histogram groups numerical values into bins to show their frequency distribution."},
        {"id": "data_analysis_025", "skill": "Data Analysis", "topic": "Exploratory Analysis", "question": "What is exploratory data analysis (EDA)?", "options": ["Examining data to understand patterns, relationships, and quality", "Deploying an application without inspecting data", "Writing a license file", "Creating passwords for a database"], "correct_answer": "Examining data to understand patterns, relationships, and quality", "explanation": "EDA uses summaries and visualizations to understand a dataset before deeper analysis."},
        {"id": "data_analysis_026", "skill": "Data Analysis", "topic": "Exploratory Analysis", "question": "Why should data types be checked before analysis?", "options": ["Incorrect types can cause calculations and comparisons to behave incorrectly", "Data types always determine chart colors", "Checking types deletes duplicate records", "Types replace the need for validation"], "correct_answer": "Incorrect types can cause calculations and comparisons to behave incorrectly", "explanation": "For example, numbers stored as strings may not behave as expected in numerical calculations."},
        {"id": "data_analysis_027", "skill": "Data Analysis", "topic": "Data Transformation", "question": "What is data normalization commonly used for in data preparation?", "options": ["Scaling numerical features to a defined range or scale", "Removing all rows", "Renaming every file", "Converting every value into a date"], "correct_answer": "Scaling numerical features to a defined range or scale", "explanation": "Feature normalization can put variables on comparable scales, depending on the method used."},
        {"id": "data_analysis_028", "skill": "Data Analysis", "topic": "Data Transformation", "question": "What is one-hot encoding used for?", "options": ["Representing categories as separate binary indicator columns", "Compressing every image into one pixel", "Deleting categorical information", "Sorting dates alphabetically"], "correct_answer": "Representing categories as separate binary indicator columns", "explanation": "One-hot encoding represents category membership using binary columns."},
        {"id": "data_analysis_029", "skill": "Data Analysis", "topic": "Data Integration", "question": "What does merging datasets usually mean?", "options": ["Combining records using shared keys or matching columns", "Deleting all common columns", "Changing all values to zero", "Creating a chart without data"], "correct_answer": "Combining records using shared keys or matching columns", "explanation": "Merging joins information from different datasets using specified keys."},
        {"id": "data_analysis_030", "skill": "Data Analysis", "topic": "Data Integration", "question": "What is a primary key useful for in a relational dataset?", "options": ["Uniquely identifying each record in a table", "Storing chart colors", "Sorting every row randomly", "Replacing all data types"], "correct_answer": "Uniquely identifying each record in a table", "explanation": "A primary key uniquely identifies a row and cannot contain duplicate key values."},
        {"id": "data_analysis_031", "skill": "Data Analysis", "topic": "Data Quality", "question": "What does data consistency mean?", "options": ["Values and formats follow compatible rules across records and sources", "Every value is identical", "The dataset contains no numerical values", "The file never changes"], "correct_answer": "Values and formats follow compatible rules across records and sources", "explanation": "Consistent data uses compatible formats and definitions across the dataset."},
        {"id": "data_analysis_032", "skill": "Data Analysis", "topic": "Data Quality", "question": "Why should missing data not always be replaced with zero?", "options": ["Zero may be a real value and could distort analysis", "Zero is never a number", "Missing data always means zero", "Replacing values automatically fixes bias"], "correct_answer": "Zero may be a real value and could distort analysis", "explanation": "Missingness should be handled according to its meaning and the analysis requirements."},
        {"id": "data_analysis_033", "skill": "Data Analysis", "topic": "Business Intelligence", "question": "What is a KPI?", "options": ["A key performance indicator used to measure progress toward an objective", "A Python data type", "A database connection string", "A file compression format"], "correct_answer": "A key performance indicator used to measure progress toward an objective", "explanation": "KPIs track important measures of performance against defined goals."},
        {"id": "data_analysis_034", "skill": "Data Analysis", "topic": "Business Intelligence", "question": "What is a dashboard?", "options": ["A visual display of important metrics and summaries", "A programming language", "A database password", "A method for deleting data"], "correct_answer": "A visual display of important metrics and summaries", "explanation": "Dashboards bring important metrics and visual summaries together for monitoring."},
        {"id": "data_analysis_035", "skill": "Data Analysis", "topic": "SQL Analysis", "question": "Which SQL clause filters rows before grouping?", "options": ["WHERE", "ORDER BY", "CREATE", "ALTER"], "correct_answer": "WHERE", "explanation": "WHERE filters individual rows before grouping and aggregation."},
        {"id": "data_analysis_036", "skill": "Data Analysis", "topic": "SQL Analysis", "question": "Which SQL clause filters groups after aggregation?", "options": ["HAVING", "FROM", "INSERT", "LIMIT only"], "correct_answer": "HAVING", "explanation": "HAVING applies conditions to groups, commonly using aggregate results."},
        {"id": "data_analysis_037", "skill": "Data Analysis", "topic": "Reporting", "question": "What should a good data analysis report include?", "options": ["Methods, key findings, limitations, and actionable conclusions", "Only colorful charts without labels", "Only the raw data file name", "Unverified claims presented as facts"], "correct_answer": "Methods, key findings, limitations, and actionable conclusions", "explanation": "A clear report explains how results were obtained and what they mean."},
        {"id": "data_analysis_038", "skill": "Data Analysis", "topic": "Ethics", "question": "Why should sensitive personal data be protected during analysis?", "options": ["To respect privacy and reduce unauthorized disclosure", "To make every dataset public", "To avoid documenting methods", "To guarantee every prediction is accurate"], "correct_answer": "To respect privacy and reduce unauthorized disclosure", "explanation": "Data analysts should minimize unnecessary personal data access and follow appropriate protections."},
        {"id": "data_analysis_039", "skill": "Data Analysis", "topic": "Interpretation", "question": "Why should conclusions be checked against the data and context?", "options": ["To avoid misleading interpretations and unsupported claims", "To ensure every chart has the same color", "To eliminate the need for cleaning", "To guarantee causation from correlation"], "correct_answer": "To avoid misleading interpretations and unsupported claims", "explanation": "Results need context, validation, and appropriate caveats before drawing conclusions."},
        {"id": "data_analysis_040", "skill": "Data Analysis", "topic": "Best Practices", "question": "What is a good data analysis practice?", "options": ["Keep work reproducible and document important cleaning decisions", "Change values without recording why", "Ignore unusual observations automatically", "Publish private records without permission"], "correct_answer": "Keep work reproducible and document important cleaning decisions", "explanation": "Documented, reproducible workflows make findings easier to verify and maintain."}
    ],
    "problem solving": [
        {"id": "problem_solving_001", "skill": "Problem Solving", "topic": "Fundamentals", "question": "What is the first useful step when solving a programming problem?", "options": ["Understand the problem and its requirements", "Immediately write random code", "Ignore the input format", "Choose the longest algorithm"], "correct_answer": "Understand the problem and its requirements", "explanation": "Clear understanding of inputs, outputs, and constraints guides the solution."},
        {"id": "problem_solving_002", "skill": "Problem Solving", "topic": "Fundamentals", "question": "What is an algorithm?", "options": ["A sequence of steps for solving a problem", "A physical computer part", "A database password", "A programming error"], "correct_answer": "A sequence of steps for solving a problem", "explanation": "An algorithm defines steps for transforming inputs into desired outputs."},
        {"id": "problem_solving_003", "skill": "Problem Solving", "topic": "Fundamentals", "question": "What is pseudocode?", "options": ["A language-independent description of an algorithm", "Executable machine code in every case", "A database schema", "A network protocol"], "correct_answer": "A language-independent description of an algorithm", "explanation": "Pseudocode describes logic in a readable form without strict programming-language syntax."},
        {"id": "problem_solving_004", "skill": "Problem Solving", "topic": "Fundamentals", "question": "What is a flowchart?", "options": ["A diagram showing steps and decisions in a process", "A compiled program", "A database table", "A password manager"], "correct_answer": "A diagram showing steps and decisions in a process", "explanation": "Flowcharts use symbols and arrows to represent process flow."},
        {"id": "problem_solving_005", "skill": "Problem Solving", "topic": "Decomposition", "question": "What is decomposition in problem solving?", "options": ["Breaking a complex problem into smaller parts", "Combining unrelated errors", "Deleting all requirements", "Increasing program size without reason"], "correct_answer": "Breaking a complex problem into smaller parts", "explanation": "Smaller subproblems are easier to understand, implement, and test."},
        {"id": "problem_solving_006", "skill": "Problem Solving", "topic": "Pattern Recognition", "question": "What is pattern recognition in problem solving?", "options": ["Identifying similarities or repeated structures in problems", "Randomly changing values", "Ignoring previous examples", "Writing code without testing"], "correct_answer": "Identifying similarities or repeated structures in problems", "explanation": "Recognizing patterns can help reuse known approaches to solve related problems."},
        {"id": "problem_solving_007", "skill": "Problem Solving", "topic": "Abstraction", "question": "What is abstraction?", "options": ["Focusing on relevant details while ignoring unnecessary complexity", "Including every possible detail in every step", "Removing all requirements", "Converting all variables to strings"], "correct_answer": "Focusing on relevant details while ignoring unnecessary complexity", "explanation": "Abstraction simplifies a problem by emphasizing information relevant to the solution."},
        {"id": "problem_solving_008", "skill": "Problem Solving", "topic": "Testing", "question": "Why test a solution with edge cases?", "options": ["To check behavior at unusual or boundary inputs", "To guarantee the code has no possible defects", "To avoid understanding the problem", "To increase the number of variables"], "correct_answer": "To check behavior at unusual or boundary inputs", "explanation": "Edge cases often reveal problems that ordinary examples do not expose."},
        {"id": "problem_solving_009", "skill": "Problem Solving", "topic": "Testing", "question": "What is a useful test for a function that sums a list of numbers?", "options": ["Test an empty list if the expected behavior is defined", "Test only a list of positive numbers", "Never test a single item", "Change the function after every run without checking results"], "correct_answer": "Test an empty list if the expected behavior is defined", "explanation": "Empty inputs are a common edge case and should have explicitly defined behavior."},
        {"id": "problem_solving_010", "skill": "Problem Solving", "topic": "Debugging", "question": "What is debugging?", "options": ["Finding and fixing causes of incorrect program behavior", "Adding random features", "Deleting all test cases", "Installing a new keyboard"], "correct_answer": "Finding and fixing causes of incorrect program behavior", "explanation": "Debugging investigates failures to identify and correct their underlying causes."},
        {"id": "problem_solving_011", "skill": "Problem Solving", "topic": "Debugging", "question": "What should you do when a test fails unexpectedly?", "options": ["Reproduce the failure and inspect inputs and execution", "Ignore the failure permanently", "Delete the test immediately", "Assume the test is always wrong"], "correct_answer": "Reproduce the failure and inspect inputs and execution", "explanation": "Reproduction and inspection help isolate the source of a failure."},
        {"id": "problem_solving_012", "skill": "Problem Solving", "topic": "Complexity", "question": "What does time complexity describe?", "options": ["How an algorithm's running work grows with input size", "The age of the computer", "The number of comments in code", "The physical length of a file"], "correct_answer": "How an algorithm's running work grows with input size", "explanation": "Time complexity describes growth in computational work as input size increases."},
        {"id": "problem_solving_013", "skill": "Problem Solving", "topic": "Complexity", "question": "What does space complexity describe?", "options": ["How memory requirements grow with input size", "The number of screens in an application", "The size of the monitor", "The time needed to type code"], "correct_answer": "How memory requirements grow with input size", "explanation": "Space complexity estimates memory required by an algorithm as input grows."},
        {"id": "problem_solving_014", "skill": "Problem Solving", "topic": "Complexity", "question": "What does O(1) time complexity mean?", "options": ["Constant time with respect to input size", "Time always increases linearly", "The algorithm never finishes", "The algorithm uses no memory"], "correct_answer": "Constant time with respect to input size", "explanation": "O(1) means the operation count is bounded independently of input size."},
        {"id": "problem_solving_015", "skill": "Problem Solving", "topic": "Complexity", "question": "Which complexity grows linearly with input size?", "options": ["O(n)", "O(1)", "O(log n)", "O(1) for every n"], "correct_answer": "O(n)", "explanation": "Linear complexity grows proportionally to the input size."},
        {"id": "problem_solving_016", "skill": "Problem Solving", "topic": "Complexity", "question": "What is the typical time complexity of binary search on a sorted array?", "options": ["O(log n)", "O(n squared)", "O(2^n)", "O(n!)"], "correct_answer": "O(log n)", "explanation": "Binary search repeatedly halves the remaining search interval."},
        {"id": "problem_solving_017", "skill": "Problem Solving", "topic": "Searching", "question": "Which search method checks elements one by one?", "options": ["Linear search", "Binary search", "Merge sort", "Hashing only"], "correct_answer": "Linear search", "explanation": "Linear search examines elements sequentially until a match is found or the list ends."},
        {"id": "problem_solving_018", "skill": "Problem Solving", "topic": "Searching", "question": "What is required for standard binary search on an array?", "options": ["The array must be sorted", "The array must contain only strings", "The array must have exactly ten elements", "The array must contain no numbers"], "correct_answer": "The array must be sorted", "explanation": "Binary search relies on sorted order to discard half of the remaining candidates."},
        {"id": "problem_solving_019", "skill": "Problem Solving", "topic": "Sorting", "question": "What is the main purpose of sorting?", "options": ["Arranging values in a defined order", "Removing all values", "Encrypting a dataset", "Increasing every number"], "correct_answer": "Arranging values in a defined order", "explanation": "Sorting orders data by a key, such as ascending numerical value."},
        {"id": "problem_solving_020", "skill": "Problem Solving", "topic": "Sorting", "question": "What is the average time complexity of merge sort?", "options": ["O(n log n)", "O(1)", "O(log n)", "O(n squared log n)"], "correct_answer": "O(n log n)", "explanation": "Merge sort divides the input and merges sorted parts, giving O(n log n) time."},
        {"id": "problem_solving_021", "skill": "Problem Solving", "topic": "Recursion", "question": "What is recursion?", "options": ["A function solving a problem by calling itself on smaller cases", "A loop that cannot stop", "A database connection", "A type of network cable"], "correct_answer": "A function solving a problem by calling itself on smaller cases", "explanation": "Recursive solutions reduce a problem to smaller instances of the same problem."},
        {"id": "problem_solving_022", "skill": "Problem Solving", "topic": "Recursion", "question": "Why is a base case important in recursion?", "options": ["It provides a stopping condition", "It increases recursion forever", "It sorts all arrays automatically", "It creates a new programming language"], "correct_answer": "It provides a stopping condition", "explanation": "Without a reachable base case, recursion may continue until resources are exhausted."},
        {"id": "problem_solving_023", "skill": "Problem Solving", "topic": "Data Structures", "question": "Which data structure follows last-in, first-out order?", "options": ["Stack", "Queue", "Graph", "Sorted array only"], "correct_answer": "Stack", "explanation": "A stack removes the most recently added item first."},
        {"id": "problem_solving_024", "skill": "Problem Solving", "topic": "Data Structures", "question": "Which data structure commonly follows first-in, first-out order?", "options": ["Queue", "Stack", "Heap only", "Recursive function"], "correct_answer": "Queue", "explanation": "A queue typically removes elements in the order they were added."},
        {"id": "problem_solving_025", "skill": "Problem Solving", "topic": "Hashing", "question": "Why is a hash table useful?", "options": ["It supports efficient average-case lookup by key", "It always sorts keys automatically", "It guarantees every operation is O(1) in all cases", "It replaces all algorithms"], "correct_answer": "It supports efficient average-case lookup by key", "explanation": "Hash tables often provide average-case constant-time lookup, insertion, and deletion."},
        {"id": "problem_solving_026", "skill": "Problem Solving", "topic": "Greedy Algorithms", "question": "What does a greedy algorithm do?", "options": ["Chooses a locally attractive option at each step", "Always examines every possible solution", "Randomly deletes input data", "Never makes decisions"], "correct_answer": "Chooses a locally attractive option at each step", "explanation": "Greedy algorithms make local choices and are correct only for problems with suitable properties."},
        {"id": "problem_solving_027", "skill": "Problem Solving", "topic": "Dynamic Programming", "question": "When is dynamic programming especially useful?", "options": ["When subproblems overlap and their results can be reused", "When there are no repeated subproblems ever", "Only when inputs are text", "Only for sorting one number"], "correct_answer": "When subproblems overlap and their results can be reused", "explanation": "Dynamic programming stores subproblem results to avoid repeated computation."},
        {"id": "problem_solving_028", "skill": "Problem Solving", "topic": "Dynamic Programming", "question": "What is memoization?", "options": ["Caching results of function calls to avoid repeated work", "Deleting previously computed results", "Sorting data without comparisons", "Creating a network connection"], "correct_answer": "Caching results of function calls to avoid repeated work", "explanation": "Memoization stores computed results and reuses them for the same inputs."},
        {"id": "problem_solving_029", "skill": "Problem Solving", "topic": "Graphs", "question": "Which algorithm is commonly used to find shortest paths in an unweighted graph?", "options": ["Breadth-first search", "Bubble sort", "Binary search on an unsorted array", "Insertion sort"], "correct_answer": "Breadth-first search", "explanation": "BFS explores vertices by distance in edges and finds shortest paths in unweighted graphs."},
        {"id": "problem_solving_030", "skill": "Problem Solving", "topic": "Graphs", "question": "What does depth-first search do?", "options": ["Explores along a path before backtracking", "Always selects the smallest numeric value", "Only sorts arrays", "Calculates an average automatically"], "correct_answer": "Explores along a path before backtracking", "explanation": "DFS explores deeply through neighbors before returning to earlier vertices."},
        {"id": "problem_solving_031", "skill": "Problem Solving", "topic": "Logic", "question": "What is a Boolean condition?", "options": ["An expression that evaluates to true or false", "An expression that always returns a string", "A list of files", "A sorting algorithm"], "correct_answer": "An expression that evaluates to true or false", "explanation": "Boolean expressions represent logical truth values used in decisions."},
        {"id": "problem_solving_032", "skill": "Problem Solving", "topic": "Logic", "question": "What is the purpose of a loop?", "options": ["Repeat a block of instructions", "Store only one constant", "Create a database automatically", "End a program before it starts"], "correct_answer": "Repeat a block of instructions", "explanation": "Loops repeat instructions while a condition holds or for each item in a sequence."},
        {"id": "problem_solving_033", "skill": "Problem Solving", "topic": "Optimization", "question": "What is a trade-off in algorithm design?", "options": ["Balancing competing factors such as time and memory", "Making every resource unlimited", "Ignoring all performance measurements", "Removing the problem statement"], "correct_answer": "Balancing competing factors such as time and memory", "explanation": "An algorithm may use more memory to run faster or less memory at the cost of time."},
        {"id": "problem_solving_034", "skill": "Problem Solving", "topic": "Optimization", "question": "Why should you measure performance before optimizing code?", "options": ["To identify actual bottlenecks instead of guessing", "To ensure the code becomes longer", "To avoid testing correctness", "To remove all comments"], "correct_answer": "To identify actual bottlenecks instead of guessing", "explanation": "Measurement helps focus optimization on the parts that matter most."},
        {"id": "problem_solving_035", "skill": "Problem Solving", "topic": "Correctness", "question": "What is an invariant in algorithm reasoning?", "options": ["A property that remains true at specified points during execution", "A value that must always be zero", "A random input", "A type of compiler error"], "correct_answer": "A property that remains true at specified points during execution", "explanation": "Loop and algorithm invariants help establish correctness."},
        {"id": "problem_solving_036", "skill": "Problem Solving", "topic": "Correctness", "question": "What is a precondition?", "options": ["A condition expected to hold before an operation begins", "A result produced after execution", "A random test output", "A variable that cannot exist"], "correct_answer": "A condition expected to hold before an operation begins", "explanation": "Preconditions specify assumptions that must be satisfied before executing an operation."},
        {"id": "problem_solving_037", "skill": "Problem Solving", "topic": "Input Constraints", "question": "Why are input constraints important when selecting an algorithm?", "options": ["They help determine whether an approach will be correct and efficient enough", "They determine the monitor size", "They remove the need to understand the problem", "They guarantee the fastest possible solution automatically"], "correct_answer": "They help determine whether an approach will be correct and efficient enough", "explanation": "Input sizes and restrictions influence feasible time and memory complexity."},
        {"id": "problem_solving_038", "skill": "Problem Solving", "topic": "Problem Solving Strategy", "question": "What is a useful way to approach an unfamiliar problem?", "options": ["Work through a small example by hand before implementing", "Immediately copy unrelated code", "Ignore expected output", "Avoid testing any assumptions"], "correct_answer": "Work through a small example by hand before implementing", "explanation": "A worked example helps reveal patterns, assumptions, and possible edge cases."},
        {"id": "problem_solving_039", "skill": "Problem Solving", "topic": "Problem Solving Strategy", "question": "What does divide and conquer involve?", "options": ["Dividing a problem into smaller subproblems, solving them, and combining results", "Choosing one random answer", "Repeating the same operation without a stopping condition", "Deleting half the requirements"], "correct_answer": "Dividing a problem into smaller subproblems, solving them, and combining results", "explanation": "Divide and conquer breaks a problem into subproblems and combines their solutions."},
        {"id": "problem_solving_040", "skill": "Problem Solving", "topic": "Best Practices", "question": "What is a good problem-solving practice?", "options": ["Explain the approach, analyze complexity, and test edge cases", "Optimize before confirming correctness", "Ignore constraints and expected outputs", "Assume one example proves all cases"], "correct_answer": "Explain the approach, analyze complexity, and test edge cases", "explanation": "A clear algorithm, complexity analysis, and systematic tests improve solution reliability."}
    ],
    "api integration": [
        {"id": "api_integration_001", "skill": "API Integration", "topic": "Fundamentals", "question": "What is an API?", "options": ["An interface that allows software systems to communicate", "A database table only", "A programming language", "A computer monitor"], "correct_answer": "An interface that allows software systems to communicate", "explanation": "An API defines how software components request and exchange functionality or data."},
        {"id": "api_integration_002", "skill": "API Integration", "topic": "HTTP", "question": "Which HTTP method is commonly used to retrieve a resource?", "options": ["GET", "POST", "DELETE", "PATCH"], "correct_answer": "GET", "explanation": "GET requests representation of a resource and is intended to be safe."},
        {"id": "api_integration_003", "skill": "API Integration", "topic": "HTTP", "question": "Which HTTP method is commonly used to submit data to create a resource?", "options": ["POST", "GET", "HEAD", "OPTIONS only"], "correct_answer": "POST", "explanation": "POST submits data for processing and is commonly used to create resources."},
        {"id": "api_integration_004", "skill": "API Integration", "topic": "HTTP", "question": "Which HTTP method is commonly used to replace a resource representation?", "options": ["PUT", "GET", "TRACE", "HEAD"], "correct_answer": "PUT", "explanation": "PUT commonly creates or replaces the target resource representation and is idempotent by definition."},
        {"id": "api_integration_005", "skill": "API Integration", "topic": "HTTP", "question": "Which HTTP method is commonly used for a partial resource update?", "options": ["PATCH", "GET", "CONNECT", "TRACE"], "correct_answer": "PATCH", "explanation": "PATCH applies partial modifications to a resource."},
        {"id": "api_integration_006", "skill": "API Integration", "topic": "HTTP", "question": "Which HTTP method is commonly used to delete a resource?", "options": ["DELETE", "GET", "OPTIONS", "HEAD"], "correct_answer": "DELETE", "explanation": "DELETE requests removal of the target resource."},
        {"id": "api_integration_007", "skill": "API Integration", "topic": "HTTP Status Codes", "question": "What does HTTP status code 200 usually indicate?", "options": ["The request succeeded", "The resource was not found", "The server is always offline", "Authentication is always required"], "correct_answer": "The request succeeded", "explanation": "200 OK indicates successful handling of the request."},
        {"id": "api_integration_008", "skill": "API Integration", "topic": "HTTP Status Codes", "question": "What does HTTP status code 201 usually indicate?", "options": ["A resource was created successfully", "The request was unauthorized", "The server encountered an error", "The resource was not found"], "correct_answer": "A resource was created successfully", "explanation": "201 Created indicates that the request resulted in creation of a resource."},
        {"id": "api_integration_009", "skill": "API Integration", "topic": "HTTP Status Codes", "question": "What does HTTP status code 400 usually mean?", "options": ["The request was invalid or could not be processed as sent", "The request succeeded", "A resource was created", "The server is redirecting permanently"], "correct_answer": "The request was invalid or could not be processed as sent", "explanation": "400 Bad Request indicates a client-side request problem."},
        {"id": "api_integration_010", "skill": "API Integration", "topic": "HTTP Status Codes", "question": "What does HTTP status code 401 generally indicate?", "options": ["Authentication is required or has failed", "The request succeeded", "The resource was created", "The server returned a redirect only"], "correct_answer": "Authentication is required or has failed", "explanation": "401 Unauthorized indicates missing or invalid authentication credentials."},
        {"id": "api_integration_011", "skill": "API Integration", "topic": "HTTP Status Codes", "question": "What does HTTP status code 403 generally mean?", "options": ["The server refuses to authorize the request", "The request always succeeded", "The resource was created", "The client must retry every millisecond"], "correct_answer": "The server refuses to authorize the request", "explanation": "403 Forbidden means the server understood the request but refuses to fulfill it."},
        {"id": "api_integration_012", "skill": "API Integration", "topic": "HTTP Status Codes", "question": "What does HTTP status code 404 indicate?", "options": ["The requested resource was not found", "The request succeeded", "The server created a resource", "The user is always authenticated"], "correct_answer": "The requested resource was not found", "explanation": "404 Not Found means the server cannot find the requested resource."},
        {"id": "api_integration_013", "skill": "API Integration", "topic": "HTTP Status Codes", "question": "What does HTTP status code 500 generally indicate?", "options": ["An internal server error", "A successful request", "A resource was created", "A valid redirect"], "correct_answer": "An internal server error", "explanation": "500 Internal Server Error indicates an unexpected server-side failure."},
        {"id": "api_integration_014", "skill": "API Integration", "topic": "Data Formats", "question": "What is JSON commonly used for in APIs?", "options": ["Representing structured data in text form", "Encrypting all network traffic automatically", "Replacing HTTP", "Compiling JavaScript"], "correct_answer": "Representing structured data in text form", "explanation": "JSON represents objects, arrays, strings, numbers, booleans, and null."},
        {"id": "api_integration_015", "skill": "API Integration", "topic": "Data Formats", "question": "Which HTTP header commonly indicates that a request body contains JSON?", "options": ["Content-Type: application/json", "Accept-Language: JSON", "Host: application/json", "Cache-Control: JSON-only"], "correct_answer": "Content-Type: application/json", "explanation": "Content-Type identifies the media type of the request body."},
        {"id": "api_integration_016", "skill": "API Integration", "topic": "Data Formats", "question": "What does the Accept header commonly specify?", "options": ["Response media types the client can accept", "The user's password", "The database name only", "The server's source code"], "correct_answer": "Response media types the client can accept", "explanation": "Accept communicates preferred response media types, such as application/json."},
        {"id": "api_integration_017", "skill": "API Integration", "topic": "Authentication", "question": "What is an API key commonly used for?", "options": ["Identifying or authenticating a client according to the API's security design", "Replacing every server-side permission check", "Encrypting all response data automatically", "Formatting JSON indentation"], "correct_answer": "Identifying or authenticating a client according to the API's security design", "explanation": "API keys can identify clients, but they should be protected and are not a complete authorization system by themselves."},
        {"id": "api_integration_018", "skill": "API Integration", "topic": "Authentication", "question": "What is a bearer token?", "options": ["A credential presented by a client to access a protected resource", "A type of database index", "A public image file", "A programming loop"], "correct_answer": "A credential presented by a client to access a protected resource", "explanation": "Bearer tokens are typically sent in the Authorization header and must be protected from disclosure."},
        {"id": "api_integration_019", "skill": "API Integration", "topic": "Authentication", "question": "Why should API credentials be kept out of frontend source code when they are secret?", "options": ["Users may inspect client-side code and extract them", "JavaScript cannot store strings", "APIs do not use credentials", "It prevents JSON parsing"], "correct_answer": "Users may inspect client-side code and extract them", "explanation": "Secrets should be stored securely on a trusted backend or secret-management service."},
        {"id": "api_integration_020", "skill": "API Integration", "topic": "Requests", "question": "What is a query parameter commonly used for?", "options": ["Filtering, searching, or modifying request options in the URL", "Replacing the HTTP method", "Storing a private key safely", "Changing the server operating system"], "correct_answer": "Filtering, searching, or modifying request options in the URL", "explanation": "Query parameters commonly carry search terms, filters, pagination, or other request options."},
        {"id": "api_integration_021", "skill": "API Integration", "topic": "Requests", "question": "What is a path parameter commonly used for in a REST API?", "options": ["Identifying a specific resource in the URL path", "Storing a full database backup", "Setting the browser's screen size", "Replacing response headers"], "correct_answer": "Identifying a specific resource in the URL path", "explanation": "A path such as /users/42 uses 42 to identify a particular user resource."},
        {"id": "api_integration_022", "skill": "API Integration", "topic": "Requests", "question": "Why should an API client set a timeout?", "options": ["To avoid waiting indefinitely for a response", "To guarantee every request succeeds", "To disable server validation", "To encrypt credentials automatically"], "correct_answer": "To avoid waiting indefinitely for a response", "explanation": "Timeouts help clients recover from slow or unresponsive services."},
        {"id": "api_integration_023", "skill": "API Integration", "topic": "Error Handling", "question": "What should a client do when an API returns a non-success status?", "options": ["Handle the error based on its status and response details", "Assume the request succeeded", "Ignore the response body in every case", "Delete its local configuration"], "correct_answer": "Handle the error based on its status and response details", "explanation": "Clients should interpret status codes and handle expected failures safely."},
        {"id": "api_integration_024", "skill": "API Integration", "topic": "Error Handling", "question": "Why should retry logic use care with non-idempotent requests?", "options": ["A repeated request may create duplicate side effects", "Retries always delete data", "POST requests cannot contain data", "HTTP has no status codes"], "correct_answer": "A repeated request may create duplicate side effects", "explanation": "Retrying a non-idempotent operation can repeat its effect unless the API supports safe deduplication."},
        {"id": "api_integration_025", "skill": "API Integration", "topic": "Rate Limits", "question": "What does HTTP status code 429 commonly indicate?", "options": ["Too many requests", "Resource created", "Request succeeded", "Resource permanently moved"], "correct_answer": "Too many requests", "explanation": "429 indicates rate limiting; the client may need to wait before sending more requests."},
        {"id": "api_integration_026", "skill": "API Integration", "topic": "Rate Limits", "question": "What is a useful response to an API rate limit?", "options": ["Respect retry guidance and use backoff where appropriate", "Send requests as fast as possible", "Create unlimited duplicate accounts", "Ignore all response headers"], "correct_answer": "Respect retry guidance and use backoff where appropriate", "explanation": "Backoff and rate-limit guidance reduce repeated failures and unnecessary load."},
        {"id": "api_integration_027", "skill": "API Integration", "topic": "Pagination", "question": "Why do APIs use pagination?", "options": ["To return large result sets in manageable portions", "To encrypt all returned values", "To remove authentication", "To guarantee every result is returned in one response"], "correct_answer": "To return large result sets in manageable portions", "explanation": "Pagination reduces response sizes and lets clients retrieve results incrementally."},
        {"id": "api_integration_028", "skill": "API Integration", "topic": "Pagination", "question": "What should a client do when an API response includes a next-page link?", "options": ["Follow it when more results are needed", "Treat it as a password", "Delete the current response", "Change every HTTP method to DELETE"], "correct_answer": "Follow it when more results are needed", "explanation": "A next-page link indicates how to request the next portion of results."},
        {"id": "api_integration_029", "skill": "API Integration", "topic": "Integration Design", "question": "What is API versioning used for?", "options": ["Managing changes to an API contract over time", "Making every endpoint identical", "Removing all documentation", "Increasing the computer's memory"], "correct_answer": "Managing changes to an API contract over time", "explanation": "Versioning helps manage compatibility when API behavior or schemas change."},
        {"id": "api_integration_030", "skill": "API Integration", "topic": "Integration Design", "question": "What is an API contract?", "options": ["A description of expected endpoints, inputs, outputs, and behavior", "A physical agreement between servers", "A list of user passwords", "A file compression algorithm"], "correct_answer": "A description of expected endpoints, inputs, outputs, and behavior", "explanation": "An API contract defines how clients and servers are expected to interact."},
        {"id": "api_integration_031", "skill": "API Integration", "topic": "Testing", "question": "What is API integration testing intended to verify?", "options": ["That connected components communicate and exchange expected data correctly", "Only the font style of a page", "Only the developer's computer name", "That every API request succeeds under all conditions"], "correct_answer": "That connected components communicate and exchange expected data correctly", "explanation": "Integration tests check interactions across API clients, services, and dependencies."},
        {"id": "api_integration_032", "skill": "API Integration", "topic": "Testing", "question": "What is a mock API response useful for?", "options": ["Testing client behavior without depending on a live service", "Publishing secret credentials", "Replacing all production monitoring", "Changing the API's real data automatically"], "correct_answer": "Testing client behavior without depending on a live service", "explanation": "Mock responses support repeatable tests for success, failure, and edge cases."},
        {"id": "api_integration_033", "skill": "API Integration", "topic": "CORS", "question": "What is CORS?", "options": ["A browser mechanism that controls cross-origin web requests", "A database query language", "An encryption algorithm", "A version control command"], "correct_answer": "A browser mechanism that controls cross-origin web requests", "explanation": "Cross-Origin Resource Sharing uses response headers to tell browsers which origins may access resources."},
        {"id": "api_integration_034", "skill": "API Integration", "topic": "CORS", "question": "Where should CORS permissions generally be configured for a browser-based API integration?", "options": ["On the server that returns the relevant CORS headers", "Only in the user's browser settings", "Inside a Git commit message", "In the JSON response body alone"], "correct_answer": "On the server that returns the relevant CORS headers", "explanation": "The server must return appropriate CORS headers for browser access to be permitted."},
        {"id": "api_integration_035", "skill": "API Integration", "topic": "Webhooks", "question": "What is a webhook?", "options": ["An HTTP callback sent when a configured event occurs", "A method for sorting a database", "A local CSS utility", "A replacement for all API authentication"], "correct_answer": "An HTTP callback sent when a configured event occurs", "explanation": "Webhooks notify a receiving service about events without requiring constant polling."},
        {"id": "api_integration_036", "skill": "API Integration", "topic": "Webhooks", "question": "Why should a webhook receiver verify the event's authenticity?", "options": ["To reduce the risk of processing forged requests", "To make the event arrive twice", "To remove the need for HTTPS", "To automatically trust every sender"], "correct_answer": "To reduce the risk of processing forged requests", "explanation": "Signature verification or another supported authentication mechanism helps establish that a webhook is genuine."},
        {"id": "api_integration_037", "skill": "API Integration", "topic": "Security", "question": "Why is HTTPS important when calling an API?", "options": ["It protects traffic in transit using TLS", "It guarantees the API returns correct data", "It removes the need for authentication", "It prevents all application bugs"], "correct_answer": "It protects traffic in transit using TLS", "explanation": "HTTPS protects confidentiality and integrity in transit and authenticates the server endpoint."},
        {"id": "api_integration_038", "skill": "API Integration", "topic": "Data Validation", "question": "Why validate API response data before using it?", "options": ["Responses may be incomplete, unexpected, or malformed", "Every server always returns perfect data", "Validation automatically repairs every network error", "It guarantees the API is available forever"], "correct_answer": "Responses may be incomplete, unexpected, or malformed", "explanation": "Validating response structure and types helps prevent incorrect assumptions and runtime errors."},
        {"id": "api_integration_039", "skill": "API Integration", "topic": "Monitoring", "question": "Which information is useful for monitoring API integration reliability?", "options": ["Success rates, response times, and error rates", "Only the website background color", "Only the developer's age", "Only the number of code comments"], "correct_answer": "Success rates, response times, and error rates", "explanation": "These metrics help identify outages, slow responses, and recurring integration problems."},
        {"id": "api_integration_040", "skill": "API Integration", "topic": "Best Practices", "question": "What is a good API integration practice?", "options": ["Handle errors, protect credentials, validate responses, and document dependencies", "Hardcode secrets into public code", "Retry every failure without limits", "Assume the remote service will never change"], "correct_answer": "Handle errors, protect credentials, validate responses, and document dependencies", "explanation": "Reliable integrations use defensive error handling, secure credentials, validation, and clear documentation."}
    ],
    
    "pytorch": [
        {"id": "pytorch_001", "skill": "PyTorch", "topic": "Basics", "question": "What is PyTorch mainly used for?", "options": ["Web styling", "Deep learning", "Database design", "File compression"], "correct_answer": "Deep learning", "explanation": "PyTorch is a framework for building and training machine learning models."},
        {"id": "pytorch_002", "skill": "PyTorch", "topic": "Tensors", "question": "What is a tensor in PyTorch?", "options": ["A database table", "A multi-dimensional data structure", "A web page", "A network protocol"], "correct_answer": "A multi-dimensional data structure", "explanation": "Tensors store numerical data in one or more dimensions."},
        {"id": "pytorch_003", "skill": "PyTorch", "topic": "Tensors", "question": "Which function creates a tensor from a Python list?", "options": ["torch.tensor()", "torch.list()", "torch.arraylist()", "torch.make()"], "correct_answer": "torch.tensor()", "explanation": "torch.tensor() converts data such as a list into a tensor."},
        {"id": "pytorch_004", "skill": "PyTorch", "topic": "Tensors", "question": "Which attribute gives a tensor's dimensions?", "options": ["length", "shape", "format", "columns"], "correct_answer": "shape", "explanation": "The shape attribute describes the size of each tensor dimension."},
        {"id": "pytorch_005", "skill": "PyTorch", "topic": "Tensors", "question": "Which function creates a tensor filled with zeros?", "options": ["torch.empty()", "torch.zeros()", "torch.none()", "torch.clear()"], "correct_answer": "torch.zeros()", "explanation": "torch.zeros() creates a tensor whose elements are all zero."},
        {"id": "pytorch_006", "skill": "PyTorch", "topic": "Tensors", "question": "Which function creates a tensor filled with ones?", "options": ["torch.ones()", "torch.fullzero()", "torch.one()", "torch.fillnone()"], "correct_answer": "torch.ones()", "explanation": "torch.ones() initializes every element to one."},
        {"id": "pytorch_007", "skill": "PyTorch", "topic": "Tensors", "question": "What does tensor.dtype indicate?", "options": ["Tensor shape", "Data type of elements", "GPU model", "Number of files"], "correct_answer": "Data type of elements", "explanation": "dtype identifies types such as float32 or int64."},
        {"id": "pytorch_008", "skill": "PyTorch", "topic": "Tensors", "question": "What does tensor.device tell you?", "options": ["Where the tensor is stored or computed", "Its mathematical rank only", "Its filename", "Its accuracy"], "correct_answer": "Where the tensor is stored or computed", "explanation": "The device indicates whether a tensor is on the CPU or an accelerator such as a GPU."},
        {"id": "pytorch_009", "skill": "PyTorch", "topic": "Autograd", "question": "What is PyTorch autograd used for?", "options": ["Drawing charts", "Automatic gradient calculation", "Creating databases", "Compressing models"], "correct_answer": "Automatic gradient calculation", "explanation": "Autograd tracks operations and computes gradients for differentiation."},
        {"id": "pytorch_010", "skill": "PyTorch", "topic": "Autograd", "question": "Which tensor setting requests gradient tracking?", "options": ["requires_grad=True", "track=False", "gradient=off", "autograd=None"], "correct_answer": "requires_grad=True", "explanation": "This setting asks autograd to track relevant operations on the tensor."},
        {"id": "pytorch_011", "skill": "PyTorch", "topic": "Autograd", "question": "Which method commonly computes gradients from a scalar loss?", "options": ["loss.backward()", "loss.forward()", "loss.gradient()", "loss.train()"], "correct_answer": "loss.backward()", "explanation": "backward() propagates gradients through the computation graph."},
        {"id": "pytorch_012", "skill": "PyTorch", "topic": "Training", "question": "Why call optimizer.zero_grad() during training?", "options": ["To delete model weights", "To clear accumulated gradients", "To reset the dataset", "To stop learning permanently"], "correct_answer": "To clear accumulated gradients", "explanation": "Gradients accumulate by default, so they are usually cleared before the next backward pass."},
        {"id": "pytorch_013", "skill": "PyTorch", "topic": "Training", "question": "What does optimizer.step() usually do?", "options": ["Updates model parameters", "Loads an image", "Splits the dataset", "Calculates accuracy automatically"], "correct_answer": "Updates model parameters", "explanation": "The optimizer uses gradients to adjust trainable parameters."},
        {"id": "pytorch_014", "skill": "PyTorch", "topic": "Neural Networks", "question": "What is torch.nn used for?", "options": ["Building neural network components", "Managing website routes", "Writing SQL queries", "Creating spreadsheets"], "correct_answer": "Building neural network components", "explanation": "torch.nn provides layers, loss functions, and other neural network building blocks."},
        {"id": "pytorch_015", "skill": "PyTorch", "topic": "Neural Networks", "question": "What is the purpose of nn.Linear?", "options": ["Perform a linear transformation", "Resize an image file", "Sort a dataset", "Connect to a database"], "correct_answer": "Perform a linear transformation", "explanation": "nn.Linear applies a learned transformation using weights and a bias."},
        {"id": "pytorch_016", "skill": "PyTorch", "topic": "Neural Networks", "question": "What does ReLU do?", "options": ["Returns the maximum of input and zero", "Always returns one", "Sorts values", "Converts text to tokens"], "correct_answer": "Returns the maximum of input and zero", "explanation": "ReLU replaces negative input values with zero and keeps positive values."},
        {"id": "pytorch_017", "skill": "PyTorch", "topic": "Loss Functions", "question": "What is a loss function used to measure?", "options": ["Model prediction error", "File size", "Training computer temperature", "Number of source files"], "correct_answer": "Model prediction error", "explanation": "A loss function quantifies the difference between predictions and target values."},
        {"id": "pytorch_018", "skill": "PyTorch", "topic": "Loss Functions", "question": "Which loss is commonly used for multi-class classification with class indices?", "options": ["CrossEntropyLoss", "L1 loss only", "Cosine distance only", "FileLoss"], "correct_answer": "CrossEntropyLoss", "explanation": "CrossEntropyLoss is commonly used for mutually exclusive class prediction."},
        {"id": "pytorch_019", "skill": "PyTorch", "topic": "Training", "question": "What is an epoch?", "options": ["One full pass through the training dataset", "One model parameter", "One prediction only", "A GPU memory address"], "correct_answer": "One full pass through the training dataset", "explanation": "An epoch means the model has processed the entire training dataset once."},
        {"id": "pytorch_020", "skill": "PyTorch", "topic": "Training", "question": "What is a batch in model training?", "options": ["A group of samples processed together", "A trained model file", "A loss function", "A programming language"], "correct_answer": "A group of samples processed together", "explanation": "Batch processing lets a model handle several samples before an optimizer update."},
        {"id": "pytorch_021", "skill": "PyTorch", "topic": "Data Loading", "question": "What is the role of Dataset in PyTorch?", "options": ["Represent and access samples", "Update model weights", "Render a web page", "Configure a GPU driver"], "correct_answer": "Represent and access samples", "explanation": "A Dataset defines how individual data samples and their labels are retrieved."},
        {"id": "pytorch_022", "skill": "PyTorch", "topic": "Data Loading", "question": "What does DataLoader commonly provide?", "options": ["Batching and data iteration", "Automatic website deployment", "SQL table creation", "Model explanations only"], "correct_answer": "Batching and data iteration", "explanation": "DataLoader iterates through datasets and can batch and shuffle samples."},
        {"id": "pytorch_023", "skill": "PyTorch", "topic": "Training", "question": "Why shuffle training data?", "options": ["To reduce dependence on sample order", "To increase image resolution", "To remove all labels", "To freeze the model"], "correct_answer": "To reduce dependence on sample order", "explanation": "Shuffling can improve training by changing the order in which examples are presented."},
        {"id": "pytorch_024", "skill": "PyTorch", "topic": "Evaluation", "question": "What does model.eval() do?", "options": ["Sets the model to evaluation mode", "Deletes the model", "Starts a new training epoch", "Exports every tensor"], "correct_answer": "Sets the model to evaluation mode", "explanation": "Evaluation mode changes the behavior of modules such as dropout and batch normalization."},
        {"id": "pytorch_025", "skill": "PyTorch", "topic": "Evaluation", "question": "What is the purpose of torch.no_grad()?", "options": ["Disable gradient tracking in its scope", "Set every weight to zero", "Enable training gradients", "Create a new optimizer"], "correct_answer": "Disable gradient tracking in its scope", "explanation": "It reduces unnecessary autograd work during operations that do not need gradients."},
        {"id": "pytorch_026", "skill": "PyTorch", "topic": "Evaluation", "question": "Does model.eval() alone disable gradient tracking?", "options": ["Yes, always", "No, it changes module behavior only", "Only on a GPU", "Only for linear layers"], "correct_answer": "No, it changes module behavior only", "explanation": "Use no_grad() or inference_mode() separately when gradient tracking is unnecessary."},
        {"id": "pytorch_027", "skill": "PyTorch", "topic": "GPU", "question": "Which device string commonly identifies an NVIDIA CUDA GPU?", "options": ["cuda", "html", "sql", "browser"], "correct_answer": "cuda", "explanation": "PyTorch uses CUDA devices to run supported operations on compatible NVIDIA GPUs."},
        {"id": "pytorch_028", "skill": "PyTorch", "topic": "GPU", "question": "What must generally be true to perform an operation between two tensors on the same device?", "options": ["Their devices must be compatible", "Their variable names must match", "They must contain only integers", "They must have identical filenames"], "correct_answer": "Their devices must be compatible", "explanation": "Device mismatches commonly cause runtime errors unless tensors are moved appropriately."},
        {"id": "pytorch_029", "skill": "PyTorch", "topic": "Model Saving", "question": "What does a model state_dict primarily contain?", "options": ["Learned parameters and registered buffers", "The entire training dataset", "Python documentation", "Only model accuracy"], "correct_answer": "Learned parameters and registered buffers", "explanation": "A state_dict stores a module's parameters and persistent buffers."},
        {"id": "pytorch_030", "skill": "PyTorch", "topic": "Model Saving", "question": "Which method loads saved weights into a compatible model?", "options": ["load_state_dict()", "load_weights_web()", "read_epoch()", "restore_dataset()"], "correct_answer": "load_state_dict()", "explanation": "load_state_dict() restores saved parameter and buffer values into a model."},
        {"id": "pytorch_031", "skill": "PyTorch", "topic": "Model Design", "question": "Why define a forward() method in a custom nn.Module?", "options": ["To describe the forward computation", "To install Python", "To create database tables", "To download every dataset"], "correct_answer": "To describe the forward computation", "explanation": "forward() defines how input data passes through the model."},
        {"id": "pytorch_032", "skill": "PyTorch", "topic": "Model Design", "question": "Why call super().__init__() in a custom nn.Module constructor?", "options": ["To initialize the base module", "To calculate final accuracy", "To delete child layers", "To convert Python to C"], "correct_answer": "To initialize the base module", "explanation": "The base initializer sets up module functionality and parameter registration."},
        {"id": "pytorch_033", "skill": "PyTorch", "topic": "Optimizers", "question": "What is the learning rate?", "options": ["A value controlling update size", "The number of dataset labels", "The size of the model file", "The number of GPUs"], "correct_answer": "A value controlling update size", "explanation": "The learning rate controls how strongly an optimizer adjusts parameters."},
        {"id": "pytorch_034", "skill": "PyTorch", "topic": "Optimizers", "question": "What can happen if the learning rate is too high?", "options": ["Training may become unstable", "The dataset becomes labeled automatically", "The model cannot use tensors", "All gradients become correct"], "correct_answer": "Training may become unstable", "explanation": "Large updates can overshoot useful parameter values and prevent convergence."},
        {"id": "pytorch_035", "skill": "PyTorch", "topic": "Overfitting", "question": "What is overfitting?", "options": ["Learning training data patterns that do not generalize well", "Using too few Python files", "Training without any input", "Saving a model twice"], "correct_answer": "Learning training data patterns that do not generalize well", "explanation": "An overfit model performs well on training data but poorly on unseen data."},
        {"id": "pytorch_036", "skill": "PyTorch", "topic": "Regularization", "question": "What is dropout used for in neural networks?", "options": ["Reducing overfitting during training", "Increasing dataset labels", "Saving files automatically", "Replacing every activation"], "correct_answer": "Reducing overfitting during training", "explanation": "Dropout randomly disables some activations during training to discourage reliance on particular units."},
        {"id": "pytorch_037", "skill": "PyTorch", "topic": "Transfer Learning", "question": "What is transfer learning?", "options": ["Reusing knowledge from a previously trained model", "Moving a file between folders", "Changing Python versions", "Deleting old training data"], "correct_answer": "Reusing knowledge from a previously trained model", "explanation": "Transfer learning adapts an existing model to a new but related task."},
        {"id": "pytorch_038", "skill": "PyTorch", "topic": "Transfer Learning", "question": "What does freezing a layer's parameters mean?", "options": ["Preventing those parameters from being updated", "Deleting the layer", "Converting the layer to text", "Increasing all its gradients"], "correct_answer": "Preventing those parameters from being updated", "explanation": "Frozen parameters are typically excluded from gradient-based updates."},
        {"id": "pytorch_039", "skill": "PyTorch", "topic": "Reproducibility", "question": "Why set random seeds during experiments?", "options": ["To improve repeatability of random operations", "To guarantee perfect accuracy", "To remove the need for testing", "To make every model identical"], "correct_answer": "To improve repeatability of random operations", "explanation": "Seeds help make randomized operations more reproducible, though complete determinism is not always guaranteed."},
        {"id": "pytorch_040", "skill": "PyTorch", "topic": "Debugging", "question": "What is a common cause of a tensor shape mismatch error?", "options": ["Incompatible dimensions for an operation", "Using comments in code", "Choosing a variable name", "Saving a Python file"], "correct_answer": "Incompatible dimensions for an operation", "explanation": "Tensor operations require dimensions that satisfy their shape rules."}
    ],
    "tensorflow": [
        {"id": "tensorflow_001", "skill": "TensorFlow", "topic": "Basics", "question": "What is TensorFlow mainly used for?", "options": ["Machine learning", "Web page styling", "Database administration only", "Audio file compression only"], "correct_answer": "Machine learning", "explanation": "TensorFlow is a framework for building and running machine learning models."},
        {"id": "tensorflow_002", "skill": "TensorFlow", "topic": "Tensors", "question": "What is a tensor?", "options": ["A multi-dimensional numerical structure", "A web server", "A database key", "A text editor"], "correct_answer": "A multi-dimensional numerical structure", "explanation": "Tensors represent data across zero or more dimensions."},
        {"id": "tensorflow_003", "skill": "TensorFlow", "topic": "Tensors", "question": "Which TensorFlow API is commonly used to create a constant tensor?", "options": ["tf.constant()", "tf.createpage()", "tf.database()", "tf.freezeall()"], "correct_answer": "tf.constant()", "explanation": "tf.constant() creates a tensor with a constant value."},
        {"id": "tensorflow_004", "skill": "TensorFlow", "topic": "Tensors", "question": "What does a tensor's shape describe?", "options": ["Its dimensions", "Its file location", "Its accuracy", "Its training history"], "correct_answer": "Its dimensions", "explanation": "Shape specifies the size along each dimension."},
        {"id": "tensorflow_005", "skill": "TensorFlow", "topic": "Keras", "question": "What is tf.keras commonly used for?", "options": ["Building and training neural networks", "Designing SQL tables", "Managing Git branches", "Writing CSS animations"], "correct_answer": "Building and training neural networks", "explanation": "Keras provides high-level APIs for defining and training neural network models."},
        {"id": "tensorflow_006", "skill": "TensorFlow", "topic": "Keras", "question": "Which Keras model type is convenient for a simple stack of layers?", "options": ["Sequential", "Database", "Router", "Compiler"], "correct_answer": "Sequential", "explanation": "Sequential is suitable when layers can be arranged in a straightforward sequence."},
        {"id": "tensorflow_007", "skill": "TensorFlow", "topic": "Keras", "question": "What does a Dense layer do?", "options": ["Connects each input unit to each output unit", "Stores files on disk", "Sorts labels alphabetically", "Creates a network connection"], "correct_answer": "Connects each input unit to each output unit", "explanation": "A Dense layer applies a learned fully connected transformation."},
        {"id": "tensorflow_008", "skill": "TensorFlow", "topic": "Activation Functions", "question": "What does the ReLU activation function do?", "options": ["Outputs zero for negative inputs and the input for positive values", "Always outputs one", "Sorts its input", "Converts images to files"], "correct_answer": "Outputs zero for negative inputs and the input for positive values", "explanation": "ReLU is defined as max(0, x)."},
        {"id": "tensorflow_009", "skill": "TensorFlow", "topic": "Model Training", "question": "What is the purpose of model.compile() in Keras?", "options": ["Configure training with an optimizer, loss, and optional metrics", "Delete all model layers", "Install TensorFlow", "Create a database"], "correct_answer": "Configure training with an optimizer, loss, and optional metrics", "explanation": "compile() configures how the model will be trained and evaluated."},
        {"id": "tensorflow_010", "skill": "TensorFlow", "topic": "Model Training", "question": "Which Keras method commonly trains a model?", "options": ["fit()", "compile_only()", "render()", "connect()"], "correct_answer": "fit()", "explanation": "fit() runs the training process on provided data."},
        {"id": "tensorflow_011", "skill": "TensorFlow", "topic": "Model Evaluation", "question": "Which Keras method evaluates a model on test data?", "options": ["evaluate()", "train_forever()", "build_html()", "sort_data()"], "correct_answer": "evaluate()", "explanation": "evaluate() computes the configured loss and metrics on supplied data."},
        {"id": "tensorflow_012", "skill": "TensorFlow", "topic": "Prediction", "question": "Which Keras method generates predictions?", "options": ["predict()", "compile()", "install()", "label()"], "correct_answer": "predict()", "explanation": "predict() runs inference on new input samples."},
        {"id": "tensorflow_013", "skill": "TensorFlow", "topic": "Training", "question": "What is an epoch?", "options": ["One full pass through the training data", "One individual model weight", "One class label", "One saved file"], "correct_answer": "One full pass through the training data", "explanation": "An epoch processes the full training dataset once."},
        {"id": "tensorflow_014", "skill": "TensorFlow", "topic": "Training", "question": "What does batch_size control?", "options": ["Samples processed in a batch", "Number of model names", "Number of source files", "GPU brand"], "correct_answer": "Samples processed in a batch", "explanation": "Batch size determines how many samples are handled together during training."},
        {"id": "tensorflow_015", "skill": "TensorFlow", "topic": "Loss Functions", "question": "What does a loss function measure?", "options": ["Prediction error according to a chosen objective", "Network speed only", "File count", "Number of model layers"], "correct_answer": "Prediction error according to a chosen objective", "explanation": "The loss quantifies how far predictions are from target values under the chosen objective."},
        {"id": "tensorflow_016", "skill": "TensorFlow", "topic": "Loss Functions", "question": "Which loss is often used for binary classification with probabilities?", "options": ["Binary cross-entropy", "Mean absolute percentage error only", "Image resize loss", "Sorting loss"], "correct_answer": "Binary cross-entropy", "explanation": "Binary cross-entropy measures prediction error for binary labels and probabilities."},
        {"id": "tensorflow_017", "skill": "TensorFlow", "topic": "Optimizers", "question": "What is the role of an optimizer?", "options": ["Update trainable parameters using gradients", "Create labels manually", "Display web pages", "Remove validation data"], "correct_answer": "Update trainable parameters using gradients", "explanation": "Optimizers adjust model parameters to reduce the training objective."},
        {"id": "tensorflow_018", "skill": "TensorFlow", "topic": "Optimizers", "question": "What does the learning rate control?", "options": ["Size of parameter updates", "Number of classes", "Input image width only", "Number of training files"], "correct_answer": "Size of parameter updates", "explanation": "The learning rate influences how large optimization steps are."},
        {"id": "tensorflow_019", "skill": "TensorFlow", "topic": "Callbacks", "question": "What is a Keras callback?", "options": ["An action performed at training events", "A dataset format only", "A type of tensor dimension", "A database query"], "correct_answer": "An action performed at training events", "explanation": "Callbacks can monitor training, stop early, or save checkpoints."},
        {"id": "tensorflow_020", "skill": "TensorFlow", "topic": "Callbacks", "question": "What does EarlyStopping help prevent?", "options": ["Unnecessary training and possible overfitting", "All prediction errors", "Data collection", "Model evaluation"], "correct_answer": "Unnecessary training and possible overfitting", "explanation": "EarlyStopping can halt training when a monitored metric stops improving."},
        {"id": "tensorflow_021", "skill": "TensorFlow", "topic": "Callbacks", "question": "What is ModelCheckpoint commonly used for?", "options": ["Saving model state during training", "Increasing the dataset size automatically", "Creating HTML files", "Removing labels"], "correct_answer": "Saving model state during training", "explanation": "ModelCheckpoint saves model information according to configured conditions."},
        {"id": "tensorflow_022", "skill": "TensorFlow", "topic": "Overfitting", "question": "What is overfitting?", "options": ["Poor generalization despite strong training performance", "A model with no layers", "A missing Python package", "A file upload"], "correct_answer": "Poor generalization despite strong training performance", "explanation": "Overfitting occurs when a model learns training-specific patterns that do not transfer well to unseen data."},
        {"id": "tensorflow_023", "skill": "TensorFlow", "topic": "Regularization", "question": "Why use dropout?", "options": ["To help reduce overfitting", "To guarantee perfect accuracy", "To add database indexes", "To label every sample"], "correct_answer": "To help reduce overfitting", "explanation": "Dropout randomly disables units during training to encourage more robust representations."},
        {"id": "tensorflow_024", "skill": "TensorFlow", "topic": "Data Pipelines", "question": "What does tf.data help build?", "options": ["Input data pipelines", "Web browser extensions", "SQL schemas only", "Operating system kernels"], "correct_answer": "Input data pipelines", "explanation": "tf.data supports efficient loading, transformation, batching, and prefetching of data."},
        {"id": "tensorflow_025", "skill": "TensorFlow", "topic": "Data Pipelines", "question": "Why use prefetching in a data pipeline?", "options": ["Overlap data preparation with model computation", "Guarantee a lower loss", "Remove all preprocessing", "Replace the optimizer"], "correct_answer": "Overlap data preparation with model computation", "explanation": "Prefetching can reduce waiting by preparing upcoming batches in advance."},
        {"id": "tensorflow_026", "skill": "TensorFlow", "topic": "Computer Vision", "question": "Which layer is commonly used to extract spatial features from images?", "options": ["Conv2D", "DenseText", "SQLJoin", "HttpRoute"], "correct_answer": "Conv2D", "explanation": "Conv2D applies convolution filters to spatial input such as images."},
        {"id": "tensorflow_027", "skill": "TensorFlow", "topic": "Computer Vision", "question": "What is pooling often used for in convolutional networks?", "options": ["Reducing spatial dimensions", "Creating database passwords", "Increasing class labels", "Saving Python scripts"], "correct_answer": "Reducing spatial dimensions", "explanation": "Pooling summarizes local regions and often reduces feature-map width and height."},
        {"id": "tensorflow_028", "skill": "TensorFlow", "topic": "Sequence Models", "question": "What kind of data is an LSTM designed to help process?", "options": ["Sequential data", "Only database indexes", "Only CSS files", "Only random file names"], "correct_answer": "Sequential data", "explanation": "LSTMs are recurrent neural networks designed to model dependencies in sequences."},
        {"id": "tensorflow_029", "skill": "TensorFlow", "topic": "Transfer Learning", "question": "What is transfer learning?", "options": ["Adapting a model trained on another task", "Moving a file between folders", "Changing a variable name", "Deleting training labels"], "correct_answer": "Adapting a model trained on another task", "explanation": "Transfer learning reuses learned representations for a new related task."},
        {"id": "tensorflow_030", "skill": "TensorFlow", "topic": "Transfer Learning", "question": "Why freeze pretrained layers initially?", "options": ["To keep their weights unchanged during training", "To delete the model", "To disable all predictions", "To increase every weight"], "correct_answer": "To keep their weights unchanged during training", "explanation": "Freezing layers preserves their parameters while new or unfrozen layers are trained."},
        {"id": "tensorflow_031", "skill": "TensorFlow", "topic": "Model Saving", "question": "What is the purpose of saving a trained model?", "options": ["Reuse it later without training from scratch", "Guarantee future accuracy", "Automatically collect more data", "Remove its architecture"], "correct_answer": "Reuse it later without training from scratch", "explanation": "Saved models can be loaded for later inference or continued work."},
        {"id": "tensorflow_032", "skill": "TensorFlow", "topic": "Model Saving", "question": "Which Keras method saves a model to a supported format?", "options": ["model.save()", "model.export_csv_only()", "model.compile_file()", "model.erase()"], "correct_answer": "model.save()", "explanation": "model.save() saves model information using a supported Keras format."},
        {"id": "tensorflow_033", "skill": "TensorFlow", "topic": "Hardware", "question": "What is a GPU useful for in deep learning?", "options": ["Parallel numerical computation", "Replacing the training dataset", "Writing source code automatically", "Guaranteeing model correctness"], "correct_answer": "Parallel numerical computation", "explanation": "GPUs can accelerate many tensor operations through parallel computation."},
        {"id": "tensorflow_034", "skill": "TensorFlow", "topic": "Model Architecture", "question": "What is a model's output layer responsible for?", "options": ["Producing the task's final predictions", "Loading Python packages", "Creating the training dataset", "Choosing a computer name"], "correct_answer": "Producing the task's final predictions", "explanation": "The output layer maps learned representations to the task's expected output."},
        {"id": "tensorflow_035", "skill": "TensorFlow", "topic": "Classification", "question": "What is softmax commonly used for?", "options": ["Converting logits into class probabilities", "Removing model layers", "Sorting a database", "Resizing a file"], "correct_answer": "Converting logits into class probabilities", "explanation": "Softmax produces normalized values across classes that can be interpreted as probabilities."},
        {"id": "tensorflow_036", "skill": "TensorFlow", "topic": "Regression", "question": "Which metric is commonly used for regression?", "options": ["Mean squared error", "Number of HTML tags", "Git commit count", "HTTP status only"], "correct_answer": "Mean squared error", "explanation": "Mean squared error averages the squared differences between predictions and targets."},
        {"id": "tensorflow_037", "skill": "TensorFlow", "topic": "Validation", "question": "Why use validation data during training?", "options": ["To assess generalization while tuning the model", "To replace every training sample permanently", "To store passwords", "To guarantee zero error"], "correct_answer": "To assess generalization while tuning the model", "explanation": "Validation data helps compare configurations without using the final test set for every decision."},
        {"id": "tensorflow_038", "skill": "TensorFlow", "topic": "Reproducibility", "question": "Why set random seeds in machine learning experiments?", "options": ["To make randomized steps more repeatable", "To guarantee identical results on every device", "To increase labels", "To remove the need for evaluation"], "correct_answer": "To make randomized steps more repeatable", "explanation": "Seeds improve repeatability, although hardware and operation differences can still affect results."},
        {"id": "tensorflow_039", "skill": "TensorFlow", "topic": "Debugging", "question": "What is a common cause of a shape error in a Dense layer?", "options": ["Input dimensions do not match the expected dimensions", "The code contains comments", "The model has a name", "The dataset is stored in a folder"], "correct_answer": "Input dimensions do not match the expected dimensions", "explanation": "Layer inputs must have dimensions compatible with the layer's configured weights."},
        {"id": "tensorflow_040", "skill": "TensorFlow", "topic": "Deployment", "question": "Why might a trained TensorFlow model be exported?", "options": ["To run it in a target application or serving environment", "To automatically improve its accuracy", "To create new training labels", "To remove the model's predictions"], "correct_answer": "To run it in a target application or serving environment", "explanation": "Exporting prepares a model for use in a supported deployment environment."}
    ],
    "generative ai": [
        {"id": "genai_001", "skill": "Generative AI", "topic": "Fundamentals", "question": "What is Generative AI designed to do?", "options": ["Generate new content from learned patterns", "Only sort existing files", "Only store database records", "Only display web pages"], "correct_answer": "Generate new content from learned patterns", "explanation": "Generative AI can produce text, images, audio, code, and other content."},
        {"id": "genai_002", "skill": "Generative AI", "topic": "Fundamentals", "question": "Which is an example of a generative AI task?", "options": ["Writing a story from a prompt", "Counting rows in a table only", "Checking a disk's free space", "Sorting filenames alphabetically"], "correct_answer": "Writing a story from a prompt", "explanation": "Generating a new story is a content-generation task."},
        {"id": "genai_003", "skill": "Generative AI", "topic": "Models", "question": "What is a foundation model?", "options": ["A broadly trained model adaptable to many tasks", "A database backup", "A CSS framework", "A computer's power supply"], "correct_answer": "A broadly trained model adaptable to many tasks", "explanation": "Foundation models are trained on broad data and can support multiple downstream uses."},
        {"id": "genai_004", "skill": "Generative AI", "topic": "Models", "question": "What is a prompt?", "options": ["Input instructions or context given to a model", "A model's physical processor", "A database index", "A network cable"], "correct_answer": "Input instructions or context given to a model", "explanation": "A prompt guides the model toward a desired response or output."},
        {"id": "genai_005", "skill": "Generative AI", "topic": "Prompting", "question": "What is prompt engineering?", "options": ["Designing inputs to guide model outputs", "Building computer hardware", "Compressing image files", "Writing database indexes only"], "correct_answer": "Designing inputs to guide model outputs", "explanation": "Prompt engineering structures instructions and context to improve the usefulness of responses."},
        {"id": "genai_006", "skill": "Generative AI", "topic": "Prompting", "question": "Why provide clear constraints in a prompt?", "options": ["To make the expected output more specific", "To guarantee every answer is true", "To remove the model's training", "To increase internet speed"], "correct_answer": "To make the expected output more specific", "explanation": "Clear constraints help narrow the format, scope, and style of a response."},
        {"id": "genai_007", "skill": "Generative AI", "topic": "Prompting", "question": "What is a zero-shot prompt?", "options": ["A prompt with no examples of the desired task", "A prompt with zero words", "A prompt that cannot contain instructions", "A prompt used only for images"], "correct_answer": "A prompt with no examples of the desired task", "explanation": "Zero-shot prompting asks the model to perform a task without supplied examples."},
        {"id": "genai_008", "skill": "Generative AI", "topic": "Prompting", "question": "What is few-shot prompting?", "options": ["Providing a small number of examples in the prompt", "Training a model for a few seconds only", "Removing all context", "Using only one output token"], "correct_answer": "Providing a small number of examples in the prompt", "explanation": "Few-shot prompting demonstrates the desired task through a few examples."},
        {"id": "genai_009", "skill": "Generative AI", "topic": "Output Quality", "question": "What is a hallucination in generative AI?", "options": ["A confident-sounding but unsupported or incorrect output", "A correct database backup", "A model that never generates text", "A GPU memory type"], "correct_answer": "A confident-sounding but unsupported or incorrect output", "explanation": "Models can generate plausible language that is not grounded in facts."},
        {"id": "genai_010", "skill": "Generative AI", "topic": "Output Quality", "question": "How can a developer help reduce unsupported factual answers?", "options": ["Provide reliable context and verify important claims", "Assume every output is correct", "Remove all instructions", "Always increase response length"], "correct_answer": "Provide reliable context and verify important claims", "explanation": "Grounding and verification can reduce risk but do not guarantee error-free responses."},
        {"id": "genai_011", "skill": "Generative AI", "topic": "Model Types", "question": "Which model family is commonly used for generating images from text?", "options": ["Text-to-image models", "Relational database engines", "Web browsers", "Sorting algorithms"], "correct_answer": "Text-to-image models", "explanation": "Text-to-image models generate images conditioned on text descriptions."},
        {"id": "genai_012", "skill": "Generative AI", "topic": "Model Types", "question": "What is multimodal AI?", "options": ["AI that can work with more than one type of data or modality", "AI that only stores text", "A database with multiple tables", "A program with multiple files"], "correct_answer": "AI that can work with more than one type of data or modality", "explanation": "Modalities can include text, images, audio, and video."},
        {"id": "genai_013", "skill": "Generative AI", "topic": "Training", "question": "What is pretraining?", "options": ["Initial broad training before possible task adaptation", "Testing a finished website", "Deleting model parameters", "Formatting a database"], "correct_answer": "Initial broad training before possible task adaptation", "explanation": "Pretraining teaches general patterns before additional adaptation or use."},
        {"id": "genai_014", "skill": "Generative AI", "topic": "Training", "question": "What is fine-tuning?", "options": ["Further training a pretrained model for a specific purpose", "Changing a prompt's punctuation only", "Compressing a PDF", "Installing an operating system"], "correct_answer": "Further training a pretrained model for a specific purpose", "explanation": "Fine-tuning adapts learned model parameters using additional task-related data."},
        {"id": "genai_015", "skill": "Generative AI", "topic": "Training", "question": "What is inference?", "options": ["Using a trained model to produce an output", "Collecting every training label", "Writing source code comments", "Deleting a model checkpoint"], "correct_answer": "Using a trained model to produce an output", "explanation": "Inference is the process of running a model on inputs to obtain predictions or generated content."},
        {"id": "genai_016", "skill": "Generative AI", "topic": "Evaluation", "question": "Why evaluate generated content?", "options": ["To check quality, relevance, and potential errors", "To guarantee all outputs are perfect", "To eliminate the need for users", "To change the model's programming language"], "correct_answer": "To check quality, relevance, and potential errors", "explanation": "Evaluation helps determine whether generated results meet the task's requirements."},
        {"id": "genai_017", "skill": "Generative AI", "topic": "Evaluation", "question": "Why can human evaluation be useful for generated text?", "options": ["It can judge qualities such as clarity and relevance", "It guarantees mathematical correctness", "It replaces every automated test", "It increases the model's context window"], "correct_answer": "It can judge qualities such as clarity and relevance", "explanation": "Human reviewers can assess nuanced qualities that simple automatic metrics may miss."},
        {"id": "genai_018", "skill": "Generative AI", "topic": "Temperature", "question": "What does temperature generally control during text generation?", "options": ["Randomness of token selection", "Number of model layers", "Training dataset size", "Screen brightness"], "correct_answer": "Randomness of token selection", "explanation": "Temperature changes how concentrated or varied token selection tends to be."},
        {"id": "genai_019", "skill": "Generative AI", "topic": "Temperature", "question": "What is a common effect of lowering temperature?", "options": ["More predictable token choices", "Guaranteed factual accuracy", "More training examples", "Automatic web access"], "correct_answer": "More predictable token choices", "explanation": "Lower temperatures usually make output choices less varied, but do not guarantee correctness."},
        {"id": "genai_020", "skill": "Generative AI", "topic": "Safety", "question": "What is a prompt injection attack?", "options": ["Malicious instructions designed to override intended behavior", "A normal database query", "A GPU installation", "A harmless change in font size"], "correct_answer": "Malicious instructions designed to override intended behavior", "explanation": "Prompt injection attempts to manipulate a model through untrusted instructions or content."},
        {"id": "genai_021", "skill": "Generative AI", "topic": "Safety", "question": "Why treat retrieved documents as untrusted input?", "options": ["They may contain misleading or malicious instructions", "They always contain malware", "They cannot contain useful facts", "They automatically train the model"], "correct_answer": "They may contain misleading or malicious instructions", "explanation": "External content should be treated as data rather than automatically obeyed as instructions."},
        {"id": "genai_022", "skill": "Generative AI", "topic": "Privacy", "question": "What is a good practice when sending data to an AI service?", "options": ["Avoid sharing sensitive data unless authorized and necessary", "Include all passwords for context", "Publish private records in prompts", "Disable all access controls"], "correct_answer": "Avoid sharing sensitive data unless authorized and necessary", "explanation": "Data minimization reduces privacy and security risks."},
        {"id": "genai_023", "skill": "Generative AI", "topic": "Copyright", "question": "Why should generated content be reviewed before publication?", "options": ["It may contain errors or raise rights and policy concerns", "Generated content is always original", "Review automatically retrains the model", "Publication removes all risks"], "correct_answer": "It may contain errors or raise rights and policy concerns", "explanation": "Review helps identify factual, legal, ethical, and quality problems."},
        {"id": "genai_024", "skill": "Generative AI", "topic": "Applications", "question": "Which is a common generative AI use in software development?", "options": ["Suggesting code from a natural-language request", "Replacing every security review", "Guaranteeing bug-free programs", "Automatically proving all requirements"], "correct_answer": "Suggesting code from a natural-language request", "explanation": "Code generation can assist developers, but generated code still needs testing and review."},
        {"id": "genai_025", "skill": "Generative AI", "topic": "Applications", "question": "How can generative AI help customer support?", "options": ["Drafting responses using relevant support information", "Guaranteeing every customer is satisfied", "Removing the need for privacy controls", "Changing customer passwords without permission"], "correct_answer": "Drafting responses using relevant support information", "explanation": "Generative systems can assist support agents by producing context-aware draft replies."},
        {"id": "genai_026", "skill": "Generative AI", "topic": "Architecture", "question": "What is a token in a language model?", "options": ["A unit of text processed by the model", "A physical security key only", "A database server", "A model's entire training history"], "correct_answer": "A unit of text processed by the model", "explanation": "Tokens may represent words, word pieces, punctuation, or other text units."},
        {"id": "genai_027", "skill": "Generative AI", "topic": "Architecture", "question": "What is a context window?", "options": ["The amount of input and output token context a model can handle", "A browser window size", "The number of installed libraries", "A database connection limit"], "correct_answer": "The amount of input and output token context a model can handle", "explanation": "A context window limits how much token context can be processed in a model request."},
        {"id": "genai_028", "skill": "Generative AI", "topic": "Architecture", "question": "What can happen when a request exceeds the context limit?", "options": ["The request may need truncation or reduction", "The model becomes perfectly accurate", "The training dataset grows automatically", "The computer installs more RAM automatically"], "correct_answer": "The request may need truncation or reduction", "explanation": "Applications often need to shorten or select context to fit the model's limit."},
        {"id": "genai_029", "skill": "Generative AI", "topic": "Tool Use", "question": "What is tool calling in a generative AI application?", "options": ["Allowing the model to request defined external functions", "Installing tools physically inside a GPU", "Training without data", "Changing every output to an image"], "correct_answer": "Allowing the model to request defined external functions", "explanation": "Tool calling lets a model request operations such as searches or calculations through an application."},
        {"id": "genai_030", "skill": "Generative AI", "topic": "Tool Use", "question": "Why should an application validate a model's tool-call arguments?", "options": ["To enforce expected inputs and reduce unsafe actions", "To make every request public", "To remove authentication", "To guarantee the model never errs"], "correct_answer": "To enforce expected inputs and reduce unsafe actions", "explanation": "Validation and authorization checks help prevent malformed or unauthorized operations."},
        {"id": "genai_031", "skill": "Generative AI", "topic": "Structured Output", "question": "Why request JSON output from a generative model?", "options": ["To make results easier for software to parse", "To guarantee every value is correct", "To train the model automatically", "To remove all token limits"], "correct_answer": "To make results easier for software to parse", "explanation": "Structured output can simplify integration when the response follows a defined schema."},
        {"id": "genai_032", "skill": "Generative AI", "topic": "Structured Output", "question": "Why validate generated JSON against a schema?", "options": ["To check that fields and value types meet requirements", "To prove every claim is factual", "To make the model multimodal", "To increase GPU memory"], "correct_answer": "To check that fields and value types meet requirements", "explanation": "Schema validation checks structure, but factual correctness needs separate verification."},
        {"id": "genai_033", "skill": "Generative AI", "topic": "Cost and Latency", "question": "What commonly affects the cost of hosted model usage?", "options": ["Number of processed tokens and service pricing", "Variable names in the application", "The color of the website", "The number of comments in source code"], "correct_answer": "Number of processed tokens and service pricing", "explanation": "Many services charge according to input and output usage, model choice, or other pricing terms."},
        {"id": "genai_034", "skill": "Generative AI", "topic": "Cost and Latency", "question": "What is a common way to reduce unnecessary model latency?", "options": ["Avoid sending irrelevant context", "Always send the entire database", "Use the longest possible prompt", "Repeat the same request many times"], "correct_answer": "Avoid sending irrelevant context", "explanation": "Smaller relevant inputs can reduce processing time and token usage."},
        {"id": "genai_035", "skill": "Generative AI", "topic": "Retrieval", "question": "Why connect a generative model to a document search system?", "options": ["To provide relevant external information for its response", "To guarantee it has learned every fact", "To remove the need for user questions", "To turn it into a database engine"], "correct_answer": "To provide relevant external information for its response", "explanation": "Retrieval can supply current or domain-specific context that may not be in the model's parameters."},
        {"id": "genai_036", "skill": "Generative AI", "topic": "Retrieval", "question": "What is grounding in a generative AI application?", "options": ["Connecting an answer to provided evidence or data", "Running a model only on the ground", "Removing the input prompt", "Increasing the number of model layers"], "correct_answer": "Connecting an answer to provided evidence or data", "explanation": "Grounding aims to base responses on supplied sources rather than unsupported generation."},
        {"id": "genai_037", "skill": "Generative AI", "topic": "Reliability", "question": "Why should an AI application sometimes abstain from answering?", "options": ["The available evidence may be insufficient", "Every question must have a guessed answer", "Abstaining always improves creativity", "It removes the need for monitoring"], "correct_answer": "The available evidence may be insufficient", "explanation": "A controlled refusal or clarification can be safer than inventing an unsupported answer."},
        {"id": "genai_038", "skill": "Generative AI", "topic": "Monitoring", "question": "What should be monitored after deploying a generative AI system?", "options": ["Quality, failures, latency, cost, and safety issues", "Only the website logo", "Only the number of source files", "Only the developer's keyboard speed"], "correct_answer": "Quality, failures, latency, cost, and safety issues", "explanation": "Operational monitoring helps detect performance problems and harmful behavior."},
        {"id": "genai_039", "skill": "Generative AI", "topic": "Responsible AI", "question": "What is bias in AI output?", "options": ["A systematic tendency that may disadvantage some groups or viewpoints", "A guaranteed correct prediction", "A type of file compression", "A database connection"], "correct_answer": "A systematic tendency that may disadvantage some groups or viewpoints", "explanation": "Bias can arise from data, model behavior, and system design and should be assessed."},
        {"id": "genai_040", "skill": "Generative AI", "topic": "Responsible AI", "question": "What is human oversight in an AI workflow?", "options": ["People review or control important system decisions", "The model makes every decision without checks", "Users cannot question the output", "The application disables logging"], "correct_answer": "People review or control important system decisions", "explanation": "Human oversight provides accountability and review, especially for consequential decisions."}
    ],
    "large language models": [
        {"id": "llm_001", "skill": "Large Language Models (LLMs)", "topic": "Fundamentals", "question": "What is a large language model?", "options": ["A model trained to process and generate language", "A relational database", "A CSS layout engine", "A file backup utility"], "correct_answer": "A model trained to process and generate language", "explanation": "LLMs learn language patterns from large datasets and can perform many text-related tasks."},
        {"id": "llm_002", "skill": "Large Language Models (LLMs)", "topic": "Tokenization", "question": "What is tokenization?", "options": ["Splitting text into model-processing units", "Encrypting a hard drive", "Sorting database tables", "Compiling CSS"], "correct_answer": "Splitting text into model-processing units", "explanation": "Tokenizers map text into tokens that a model can process."},
        {"id": "llm_003", "skill": "Large Language Models (LLMs)", "topic": "Tokenization", "question": "Can a single word become more than one token?", "options": ["Yes", "No, every word is exactly one token", "Only in SQL", "Only when the text is an image"], "correct_answer": "Yes", "explanation": "Subword tokenizers may split words into several tokens."},
        {"id": "llm_004", "skill": "Large Language Models (LLMs)", "topic": "Architecture", "question": "Which architecture is widely used by modern LLMs?", "options": ["Transformer", "Binary search tree only", "Relational schema", "Client-server router"], "correct_answer": "Transformer", "explanation": "Transformer networks use attention mechanisms to process token relationships."},
        {"id": "llm_005", "skill": "Large Language Models (LLMs)", "topic": "Architecture", "question": "What does self-attention help a model do?", "options": ["Relate different tokens within a sequence", "Save files to disk", "Create SQL indexes", "Install a GPU driver"], "correct_answer": "Relate different tokens within a sequence", "explanation": "Self-attention lets representations incorporate information from other tokens."},
        {"id": "llm_006", "skill": "Large Language Models (LLMs)", "topic": "Architecture", "question": "Why are positional signals used in transformer models?", "options": ["To provide information about token order or position", "To store user passwords", "To count database rows", "To resize the context window automatically"], "correct_answer": "To provide information about token order or position", "explanation": "Attention alone does not inherently encode the sequence order in the way language tasks require."},
        {"id": "llm_007", "skill": "Large Language Models (LLMs)", "topic": "Training", "question": "What is the common next-token prediction objective?", "options": ["Predicting the next token from previous context", "Predicting the computer's next power failure", "Sorting tokens alphabetically", "Translating every token into a database key"], "correct_answer": "Predicting the next token from previous context", "explanation": "Many autoregressive language models are trained to predict the next token in a sequence."},
        {"id": "llm_008", "skill": "Large Language Models (LLMs)", "topic": "Training", "question": "What is pretraining in an LLM?", "options": ["Learning broad patterns from a large text or multimodal corpus", "Testing a website manually", "Saving a prompt to a file", "Creating user accounts"], "correct_answer": "Learning broad patterns from a large text or multimodal corpus", "explanation": "Pretraining builds general capabilities before possible instruction tuning or other adaptation."},
        {"id": "llm_009", "skill": "Large Language Models (LLMs)", "topic": "Training", "question": "What is instruction tuning?", "options": ["Training a model to follow instructions using examples", "Changing the keyboard layout", "Sorting training files", "Reducing every response to one token"], "correct_answer": "Training a model to follow instructions using examples", "explanation": "Instruction tuning uses instruction-response examples to improve task-following behavior."},
        {"id": "llm_010", "skill": "Large Language Models (LLMs)", "topic": "Alignment", "question": "What is the goal of alignment work?", "options": ["Make model behavior better match intended human goals and constraints", "Increase the number of source code files", "Remove all model training", "Guarantee every answer is true"], "correct_answer": "Make model behavior better match intended human goals and constraints", "explanation": "Alignment techniques aim to improve helpfulness and adherence to desired behavior, though they are imperfect."},
        {"id": "llm_011", "skill": "Large Language Models (LLMs)", "topic": "Context", "question": "What does context length measure?", "options": ["How many tokens a model can consider in a request", "How many computers are in a network", "The size of a Python variable name", "The number of training epochs only"], "correct_answer": "How many tokens a model can consider in a request", "explanation": "Context length limits the tokens available to the model during a request."},
        {"id": "llm_012", "skill": "Large Language Models (LLMs)", "topic": "Context", "question": "What is one effect of a very long prompt?", "options": ["It can use more tokens and increase latency or cost", "It guarantees a better answer", "It removes all hallucinations", "It automatically updates model weights"], "correct_answer": "It can use more tokens and increase latency or cost", "explanation": "Longer input usually requires more processing and may incur higher usage costs."},
        {"id": "llm_013", "skill": "Large Language Models (LLMs)", "topic": "Decoding", "question": "What is greedy decoding?", "options": ["Selecting the highest-scoring next token at each step", "Selecting tokens by alphabetical order", "Training all layers from scratch", "Searching documents by filename"], "correct_answer": "Selecting the highest-scoring next token at each step", "explanation": "Greedy decoding chooses the locally highest-scoring token at each generation step."},
        {"id": "llm_014", "skill": "Large Language Models (LLMs)", "topic": "Decoding", "question": "What does top-k sampling do?", "options": ["Samples from the k highest-scoring candidate tokens", "Keeps only the first k training files", "Uses exactly k model layers", "Returns the k oldest documents"], "correct_answer": "Samples from the k highest-scoring candidate tokens", "explanation": "Top-k sampling restricts candidate tokens to the highest-scoring k choices before sampling."},
        {"id": "llm_015", "skill": "Large Language Models (LLMs)", "topic": "Decoding", "question": "What does top-p sampling use to restrict candidate tokens?", "options": ["A cumulative probability threshold", "A database primary key", "A fixed number of model layers", "The length of the user's name"], "correct_answer": "A cumulative probability threshold", "explanation": "Top-p sampling chooses a candidate set whose cumulative probability reaches the chosen threshold."},
        {"id": "llm_016", "skill": "Large Language Models (LLMs)", "topic": "Decoding", "question": "What is a stop sequence used for?", "options": ["To end generation when a specified pattern is reached", "To delete the model weights", "To stop all internet traffic", "To remove the input prompt"], "correct_answer": "To end generation when a specified pattern is reached", "explanation": "A stop sequence can signal that the application should stop accepting further generated text."},
        {"id": "llm_017", "skill": "Large Language Models (LLMs)", "topic": "Embeddings", "question": "What is an embedding?", "options": ["A numerical vector representing an item", "A compressed Python program", "A type of HTTP header", "A database backup schedule"], "correct_answer": "A numerical vector representing an item", "explanation": "Embeddings encode items such as text into vectors that can capture useful semantic relationships."},
        {"id": "llm_018", "skill": "Large Language Models (LLMs)", "topic": "Embeddings", "question": "What is a common use for text embeddings?", "options": ["Semantic similarity search", "Changing font color", "Installing packages", "Generating a database password automatically"], "correct_answer": "Semantic similarity search", "explanation": "Embedding vectors can help find text with similar meaning."},
        {"id": "llm_019", "skill": "Large Language Models (LLMs)", "topic": "Fine-Tuning", "question": "When might fine-tuning be useful?", "options": ["When a model needs more consistent behavior for a specialized task", "Whenever a prompt contains a typo", "To guarantee access to live websites", "To remove the need for evaluation"], "correct_answer": "When a model needs more consistent behavior for a specialized task", "explanation": "Fine-tuning can adapt a model's parameters to a task, style, or domain using suitable examples."},
        {"id": "llm_020", "skill": "Large Language Models (LLMs)", "topic": "Fine-Tuning", "question": "What is a risk of fine-tuning on a small, poor-quality dataset?", "options": ["The model may learn unwanted patterns or overfit", "The model always becomes multilingual", "All inference becomes free", "The context window must double"], "correct_answer": "The model may learn unwanted patterns or overfit", "explanation": "Limited or low-quality examples can harm generalization and model behavior."},
        {"id": "llm_021", "skill": "Large Language Models (LLMs)", "topic": "Parameter-Efficient Tuning", "question": "What is LoRA designed to do?", "options": ["Adapt models using low-rank trainable updates", "Search websites by location", "Compress every prompt into one word", "Replace tokenization with SQL"], "correct_answer": "Adapt models using low-rank trainable updates", "explanation": "LoRA reduces the number of trainable parameters needed for many fine-tuning tasks."},
        {"id": "llm_022", "skill": "Large Language Models (LLMs)", "topic": "Quantization", "question": "What is model quantization?", "options": ["Representing model values with lower-precision formats", "Adding more training documents", "Changing natural language to SQL", "Increasing every parameter's precision"], "correct_answer": "Representing model values with lower-precision formats", "explanation": "Quantization can reduce memory use and sometimes improve inference speed, with possible quality trade-offs."},
        {"id": "llm_023", "skill": "Large Language Models (LLMs)", "topic": "Quantization", "question": "What is a possible trade-off of aggressive quantization?", "options": ["Some loss in model quality", "Guaranteed higher accuracy", "Unlimited context length", "Automatic retrieval of current facts"], "correct_answer": "Some loss in model quality", "explanation": "Lower precision can reduce memory requirements but may affect output quality."},
        {"id": "llm_024", "skill": "Large Language Models (LLMs)", "topic": "Retrieval", "question": "Why use retrieval with an LLM?", "options": ["Supply relevant external information for a response", "Automatically retrain the model on every question", "Guarantee that all sources are correct", "Eliminate the need for prompts"], "correct_answer": "Supply relevant external information for a response", "explanation": "Retrieval provides source material that can ground a response in external information."},
        {"id": "llm_025", "skill": "Large Language Models (LLMs)", "topic": "Retrieval", "question": "What is a vector database commonly used for in LLM applications?", "options": ["Storing and searching embedding vectors", "Compiling Python code", "Hosting CSS files only", "Replacing the language model"], "correct_answer": "Storing and searching embedding vectors", "explanation": "Vector databases support similarity search over embeddings and related metadata."},
        {"id": "llm_026", "skill": "Large Language Models (LLMs)", "topic": "Tool Calling", "question": "Why let an LLM call a calculator tool?", "options": ["To perform calculations through a defined external function", "To make the model's weights larger", "To eliminate input validation", "To turn all numbers into text only"], "correct_answer": "To perform calculations through a defined external function", "explanation": "A calculator tool can execute arithmetic more reliably than free-form text generation."},
        {"id": "llm_027", "skill": "Large Language Models (LLMs)", "topic": "Tool Calling", "question": "Who should execute and authorize an LLM's requested tool call?", "options": ["The application under its validation and permission rules", "The model with unrestricted system access", "Any retrieved document", "A random user without authentication"], "correct_answer": "The application under its validation and permission rules", "explanation": "The application should validate requests and enforce authorization before executing tools."},
        {"id": "llm_028", "skill": "Large Language Models (LLMs)", "topic": "Reliability", "question": "Why can an LLM produce an incorrect answer confidently?", "options": ["It generates likely outputs rather than directly guaranteeing truth", "It checks every claim against the internet by default", "It cannot process language", "It only copies a verified database"], "correct_answer": "It generates likely outputs rather than directly guaranteeing truth", "explanation": "Language modeling objectives do not guarantee factual correctness for every generated response."},
        {"id": "llm_029", "skill": "Large Language Models (LLMs)", "topic": "Reliability", "question": "What is a useful way to test an LLM application?", "options": ["Use representative test cases and assess factuality and task success", "Test only one easy prompt", "Assume fluent answers are correct", "Skip tests after deployment"], "correct_answer": "Use representative test cases and assess factuality and task success", "explanation": "A varied evaluation set helps reveal failures across different inputs and scenarios."},
        {"id": "llm_030", "skill": "Large Language Models (LLMs)", "topic": "Safety", "question": "What is indirect prompt injection?", "options": ["Malicious instructions hidden in external content the model processes", "A standard tokenization step", "A normal gradient update", "A type of vector dimension"], "correct_answer": "Malicious instructions hidden in external content the model processes", "explanation": "External pages or documents can contain instructions intended to manipulate the model."},
        {"id": "llm_031", "skill": "Large Language Models (LLMs)", "topic": "Safety", "question": "Why is output filtering sometimes used in LLM applications?", "options": ["To detect or restrict outputs that violate defined requirements", "To guarantee every statement is factual", "To improve the model's training data automatically", "To increase context length"], "correct_answer": "To detect or restrict outputs that violate defined requirements", "explanation": "Output checks can help enforce policies, although they may miss some unsafe or incorrect content."},
        {"id": "llm_032", "skill": "Large Language Models (LLMs)", "topic": "Privacy", "question": "What should an application do before logging user prompts?", "options": ["Consider privacy, retention, access, and data minimization", "Log every secret permanently", "Make all logs public", "Disable access controls"], "correct_answer": "Consider privacy, retention, access, and data minimization", "explanation": "Prompts may contain sensitive data, so logging should follow appropriate privacy and security rules."},
        {"id": "llm_033", "skill": "Large Language Models (LLMs)", "topic": "Latency", "question": "What is time to first token?", "options": ["Time until the first generated token is received", "Total time to train the model", "Time to download the entire dataset", "Time to create an embedding index"], "correct_answer": "Time until the first generated token is received", "explanation": "Time to first token measures how quickly generation begins after a request."},
        {"id": "llm_034", "skill": "Large Language Models (LLMs)", "topic": "Latency", "question": "What can reduce the amount of work in an LLM request?", "options": ["Sending only relevant context", "Repeating all previous messages unnecessarily", "Increasing every input without limit", "Requesting duplicate tool calls"], "correct_answer": "Sending only relevant context", "explanation": "Removing irrelevant context can lower token processing, latency, and cost."},
        {"id": "llm_035", "skill": "Large Language Models (LLMs)", "topic": "Structured Output", "question": "Why might a developer require schema-constrained output?", "options": ["To improve the consistency of machine-readable responses", "To guarantee all claims are true", "To eliminate model inference", "To make the model train itself"], "correct_answer": "To improve the consistency of machine-readable responses", "explanation": "A schema helps enforce required fields and data types for downstream processing."},
        {"id": "llm_036", "skill": "Large Language Models (LLMs)", "topic": "Applications", "question": "What is a conversational memory feature intended to do?", "options": ["Retain selected information across interactions when supported", "Increase the model's parameter count", "Replace all user authentication", "Guarantee permanent storage in every model"], "correct_answer": "Retain selected information across interactions when supported", "explanation": "Memory features can preserve useful context, subject to system design and privacy controls."},
        {"id": "llm_037", "skill": "Large Language Models (LLMs)", "topic": "Applications", "question": "What is summarization?", "options": ["Producing a shorter version that preserves key information", "Adding unrelated details to a document", "Converting all text into images", "Deleting the original source automatically"], "correct_answer": "Producing a shorter version that preserves key information", "explanation": "Summarization condenses content while attempting to preserve its important points."},
        {"id": "llm_038", "skill": "Large Language Models (LLMs)", "topic": "Applications", "question": "What is named entity recognition?", "options": ["Identifying items such as people, places, and organizations in text", "Generating a new GPU", "Creating vector database indexes only", "Changing model weights during inference"], "correct_answer": "Identifying items such as people, places, and organizations in text", "explanation": "Named entity recognition identifies and classifies mentions of entities in text."},
        {"id": "llm_039", "skill": "Large Language Models (LLMs)", "topic": "Deployment", "question": "Why use batching when serving multiple LLM requests?", "options": ["To improve hardware utilization when supported", "To guarantee every answer is correct", "To remove tokenization", "To avoid all memory limits"], "correct_answer": "To improve hardware utilization when supported", "explanation": "Batching can process multiple requests together and improve throughput, with latency trade-offs."},
        {"id": "llm_040", "skill": "Large Language Models (LLMs)", "topic": "Deployment", "question": "What is model drift in a deployed AI system?", "options": ["A change in data or behavior that can reduce performance over time", "A syntax error in every Python file", "A guaranteed improvement in accuracy", "A tokenization algorithm"], "correct_answer": "A change in data or behavior that can reduce performance over time", "explanation": "Monitoring helps detect changing input patterns or output quality after deployment."}
    ],
    "rag": [
        {"id": "rag_001", "skill": "RAG", "topic": "Fundamentals", "question": "What does RAG stand for?", "options": ["Retrieval-Augmented Generation", "Random Algorithm Generator", "Rapid Application Gateway", "Runtime Access Graph"], "correct_answer": "Retrieval-Augmented Generation", "explanation": "RAG retrieves relevant information and supplies it to a generative model."},
        {"id": "rag_002", "skill": "RAG", "topic": "Fundamentals", "question": "What is the main purpose of RAG?", "options": ["Ground generated answers in retrieved information", "Replace every database", "Train every model from scratch", "Guarantee perfect answers"], "correct_answer": "Ground generated answers in retrieved information", "explanation": "RAG provides external context that can help answer questions using relevant sources."},
        {"id": "rag_003", "skill": "RAG", "topic": "Architecture", "question": "Which is a typical first step when preparing documents for RAG?", "options": ["Load or collect the source documents", "Generate the final answer before reading them", "Delete all source text", "Train a new language model immediately"], "correct_answer": "Load or collect the source documents", "explanation": "A RAG pipeline first needs source material to process and index."},
        {"id": "rag_004", "skill": "RAG", "topic": "Document Processing", "question": "What is document chunking?", "options": ["Splitting documents into smaller text sections", "Encrypting the entire database", "Combining all files into one image", "Deleting document metadata"], "correct_answer": "Splitting documents into smaller text sections", "explanation": "Chunks let a retrieval system index and retrieve manageable sections of a document."},
        {"id": "rag_005", "skill": "RAG", "topic": "Document Processing", "question": "Why is chunk size important in RAG?", "options": ["It affects context detail and retrieval granularity", "It determines the model's training language", "It guarantees all answers are correct", "It changes a CPU into a GPU"], "correct_answer": "It affects context detail and retrieval granularity", "explanation": "Very small chunks may lack context, while very large chunks may contain irrelevant information."},
        {"id": "rag_006", "skill": "RAG", "topic": "Document Processing", "question": "Why might chunks overlap?", "options": ["To preserve context across chunk boundaries", "To make every chunk identical", "To remove metadata", "To stop vector search"], "correct_answer": "To preserve context across chunk boundaries", "explanation": "Overlap can keep related sentences together when a concept crosses a boundary."},
        {"id": "rag_007", "skill": "RAG", "topic": "Embeddings", "question": "What does an embedding model do in a common RAG pipeline?", "options": ["Converts text into numerical vectors", "Writes the final answer directly in every case", "Deletes the source documents", "Creates user passwords"], "correct_answer": "Converts text into numerical vectors", "explanation": "Embeddings represent text numerically so similar content can be compared."},
        {"id": "rag_008", "skill": "RAG", "topic": "Embeddings", "question": "Why must query and document embeddings generally use compatible representations?", "options": ["So similarity comparisons are meaningful", "So every vector has a different length", "So the model can skip retrieval", "So documents are automatically verified"], "correct_answer": "So similarity comparisons are meaningful", "explanation": "Vectors compared in a shared embedding space need compatible dimensions and representation."},
        {"id": "rag_009", "skill": "RAG", "topic": "Vector Search", "question": "What does a vector store commonly index?", "options": ["Embeddings and associated metadata", "Only CSS selectors", "Only executable Python files", "Only user passwords"], "correct_answer": "Embeddings and associated metadata", "explanation": "Vector stores support similarity retrieval and may retain identifiers or metadata for each item."},
        {"id": "rag_010", "skill": "RAG", "topic": "Vector Search", "question": "What is semantic search?", "options": ["Finding content based on meaning or similarity", "Searching only exact filenames", "Sorting rows by date only", "Searching by file size only"], "correct_answer": "Finding content based on meaning or similarity", "explanation": "Semantic search can retrieve related content even when wording differs."},
        {"id": "rag_011", "skill": "RAG", "topic": "Vector Search", "question": "What is top-k retrieval?", "options": ["Returning the k highest-ranked results", "Returning every document without ranking", "Training the top k model layers", "Selecting k random passwords"], "correct_answer": "Returning the k highest-ranked results", "explanation": "The k value controls how many leading retrieval results are returned."},
        {"id": "rag_012", "skill": "RAG", "topic": "Vector Search", "question": "What is a potential drawback of retrieving too many chunks?", "options": ["Irrelevant context can distract the generator", "The source documents become encrypted automatically", "The model no longer needs a prompt", "All citations become valid"], "correct_answer": "Irrelevant context can distract the generator", "explanation": "Excessive retrieved context may introduce noise and consume the model's context budget."},
        {"id": "rag_013", "skill": "RAG", "topic": "Hybrid Search", "question": "What is hybrid search?", "options": ["Combining different retrieval methods such as keyword and vector search", "Combining two programming languages into one", "Searching only by file date", "Using a model without documents"], "correct_answer": "Combining different retrieval methods such as keyword and vector search", "explanation": "Hybrid retrieval can combine exact-term matching with semantic similarity."},
        {"id": "rag_014", "skill": "RAG", "topic": "Hybrid Search", "question": "Why can keyword search help alongside vector search?", "options": ["It can match exact terms, IDs, or technical names", "It guarantees every result is relevant", "It replaces all document parsing", "It generates the final response by itself"], "correct_answer": "It can match exact terms, IDs, or technical names", "explanation": "Exact lexical matching can find identifiers or phrases that semantic retrieval may rank poorly."},
        {"id": "rag_015", "skill": "RAG", "topic": "Reranking", "question": "What does a reranker do?", "options": ["Reorders retrieved results using a relevance score", "Retrains the entire language model on every query", "Deletes low-quality source files permanently", "Converts documents to audio"], "correct_answer": "Reorders retrieved results using a relevance score", "explanation": "Reranking can improve which retrieved passages are passed to the generator."},
        {"id": "rag_016", "skill": "RAG", "topic": "Reranking", "question": "Where is a reranker commonly used?", "options": ["After initial retrieval and before final context selection", "Before any documents exist", "Only after a user closes the application", "Instead of all document storage"], "correct_answer": "After initial retrieval and before final context selection", "explanation": "A reranker refines a candidate set from an initial retrieval step."},
        {"id": "rag_017", "skill": "RAG", "topic": "Generation", "question": "What is the generator's role in RAG?", "options": ["Create a response using the question and retrieved context", "Store every vector permanently", "Parse all file formats by itself", "Manage database user permissions"], "correct_answer": "Create a response using the question and retrieved context", "explanation": "The generative model uses retrieved passages as additional context for answering."},
        {"id": "rag_018", "skill": "RAG", "topic": "Prompt Design", "question": "Why instruct a RAG generator to use only the supplied sources when appropriate?", "options": ["To discourage unsupported claims beyond the evidence", "To guarantee that retrieval is always correct", "To increase the number of documents", "To remove the need for evaluation"], "correct_answer": "To discourage unsupported claims beyond the evidence", "explanation": "Source-grounding instructions can help, but they do not fully prevent hallucinations."},
        {"id": "rag_019", "skill": "RAG", "topic": "Citations", "question": "Why attach source references to retrieved chunks?", "options": ["To help trace answers back to source material", "To increase vector dimensions", "To replace access control", "To guarantee the source is current"], "correct_answer": "To help trace answers back to source material", "explanation": "Metadata such as document ID and page number supports citations and verification."},
        {"id": "rag_020", "skill": "RAG", "topic": "Citations", "question": "What should an application do if a generated citation does not support its claim?", "options": ["Flag or correct the unsupported citation", "Assume the citation is valid", "Delete all remaining sources", "Increase the temperature automatically"], "correct_answer": "Flag or correct the unsupported citation", "explanation": "Citation checking should confirm that cited evidence actually supports the statement."},
        {"id": "rag_021", "skill": "RAG", "topic": "Data Ingestion", "question": "What is document ingestion?", "options": ["Bringing source data into a pipeline for processing and indexing", "Generating an answer without input", "Removing all metadata from the system", "Training the user's browser"], "correct_answer": "Bringing source data into a pipeline for processing and indexing", "explanation": "Ingestion prepares documents for later retrieval."},
        {"id": "rag_022", "skill": "RAG", "topic": "Data Ingestion", "question": "Why extract text from PDFs before indexing them?", "options": ["To make their content searchable as text", "To guarantee every PDF is accurate", "To convert every page into a database key", "To remove the need for chunking"], "correct_answer": "To make their content searchable as text", "explanation": "Text extraction makes document content available to chunking and embedding steps."},
        {"id": "rag_023", "skill": "RAG", "topic": "Data Ingestion", "question": "What challenge can scanned PDFs create?", "options": ["They may require OCR to extract text", "They always contain perfect text layers", "They cannot contain images", "They automatically generate embeddings"], "correct_answer": "They may require OCR to extract text", "explanation": "Scanned pages may be images, so optical character recognition can be needed."},
        {"id": "rag_024", "skill": "RAG", "topic": "Metadata", "question": "What is metadata filtering in retrieval?", "options": ["Restricting candidates using fields such as date or category", "Changing a model's weights", "Removing every source identifier", "Generating text without searching"], "correct_answer": "Restricting candidates using fields such as date or category", "explanation": "Metadata filters narrow search to documents that meet specific constraints."},
        {"id": "rag_025", "skill": "RAG", "topic": "Metadata", "question": "Why include document permissions in retrieval design?", "options": ["To prevent users from retrieving unauthorized content", "To make every document public", "To increase chunk overlap", "To replace all authentication"], "correct_answer": "To prevent users from retrieving unauthorized content", "explanation": "Access controls should be enforced before restricted material reaches the generator."},
        {"id": "rag_026", "skill": "RAG", "topic": "Updates", "question": "What should happen when a source document changes?", "options": ["Update or reindex its affected chunks and embeddings", "Keep stale vectors forever", "Delete every user's account", "Retrain the foundation model automatically"], "correct_answer": "Update or reindex its affected chunks and embeddings", "explanation": "Keeping the index synchronized helps retrieval reflect current source content."},
        {"id": "rag_027", "skill": "RAG", "topic": "Updates", "question": "Why track document versions in a RAG system?", "options": ["To identify which source version supports a response", "To increase token temperature", "To remove the need for embeddings", "To make all files identical"], "correct_answer": "To identify which source version supports a response", "explanation": "Version information helps with traceability and consistent updates."},
        {"id": "rag_028", "skill": "RAG", "topic": "Evaluation", "question": "What does retrieval recall measure in a retrieval task?", "options": ["How many relevant items were retrieved out of all relevant items", "How fluent the generated answer sounds", "How fast the user's keyboard types", "How many files are stored on disk"], "correct_answer": "How many relevant items were retrieved out of all relevant items", "explanation": "Recall measures the proportion of relevant items successfully retrieved."},
        {"id": "rag_029", "skill": "RAG", "topic": "Evaluation", "question": "What does retrieval precision measure?", "options": ["The proportion of retrieved items that are relevant", "The total number of model parameters", "The average length of all prompts", "The number of GPU cores"], "correct_answer": "The proportion of retrieved items that are relevant", "explanation": "Precision indicates how much of the retrieved result set is relevant."},
        {"id": "rag_030", "skill": "RAG", "topic": "Evaluation", "question": "What is answer faithfulness in RAG evaluation?", "options": ["How well an answer is supported by the supplied context", "How many chunks are in a database", "How quickly a file downloads", "Whether the model uses a particular programming language"], "correct_answer": "How well an answer is supported by the supplied context", "explanation": "Faithfulness evaluates whether claims in the answer are grounded in retrieved evidence."},
        {"id": "rag_031", "skill": "RAG", "topic": "Evaluation", "question": "Why evaluate retrieval and generation separately?", "options": ["To identify whether failures come from search or answer generation", "To guarantee the system never fails", "To eliminate all test data", "To make the index smaller automatically"], "correct_answer": "To identify whether failures come from search or answer generation", "explanation": "Separate evaluation helps diagnose missing evidence versus poor use of retrieved evidence."},
        {"id": "rag_032", "skill": "RAG", "topic": "Debugging", "question": "If the correct document exists but is never retrieved, what should be investigated first?", "options": ["Chunking, embeddings, search settings, and filters", "The website's background color", "The final answer's font", "The user's keyboard layout"], "correct_answer": "Chunking, embeddings, search settings, and filters", "explanation": "Retrieval failures often arise from indexing, representation, ranking, or overly restrictive filters."},
        {"id": "rag_033", "skill": "RAG", "topic": "Debugging", "question": "If relevant context is retrieved but the answer ignores it, what is a useful next step?", "options": ["Inspect the prompt, context formatting, and generator behavior", "Delete the vector database immediately", "Increase the number of source files without testing", "Disable all evaluation"], "correct_answer": "Inspect the prompt, context formatting, and generator behavior", "explanation": "The generation stage may fail to use evidence even when retrieval succeeds."},
        {"id": "rag_034", "skill": "RAG", "topic": "Security", "question": "What is a risk of indexing documents from untrusted sources?", "options": ["They may contain malicious instructions or misleading content", "They always improve answer quality", "They automatically encrypt the vector database", "They remove all hallucinations"], "correct_answer": "They may contain malicious instructions or misleading content", "explanation": "Untrusted content should be validated and treated as data rather than authoritative instructions."},
        {"id": "rag_035", "skill": "RAG", "topic": "Security", "question": "Why enforce tenant or user filters during retrieval?", "options": ["To isolate documents belonging to different users or groups", "To combine all private documents into public results", "To bypass authentication", "To increase the language model's parameter count"], "correct_answer": "To isolate documents belonging to different users or groups", "explanation": "Retrieval-level authorization helps prevent cross-user data exposure."},
        {"id": "rag_036", "skill": "RAG", "topic": "Performance", "question": "What is a common purpose of caching in a RAG application?", "options": ["Avoid repeating expensive work for reusable requests or results", "Guarantee all retrieved documents are current", "Replace all source documents", "Automatically fix incorrect answers"], "correct_answer": "Avoid repeating expensive work for reusable requests or results", "explanation": "Caching can reduce latency and cost when cached results remain valid."},
        {"id": "rag_037", "skill": "RAG", "topic": "Performance", "question": "What can reduce the cost of embedding a large document collection?", "options": ["Avoid re-embedding unchanged content", "Re-embed every document after every query", "Increase chunk overlap without limit", "Generate every answer twice"], "correct_answer": "Avoid re-embedding unchanged content", "explanation": "Incremental indexing can reuse embeddings for unchanged chunks or documents."},
        {"id": "rag_038", "skill": "RAG", "topic": "Advanced Retrieval", "question": "What is query rewriting in a RAG pipeline?", "options": ["Rephrasing a user query to improve retrieval", "Changing the source document's legal owner", "Rewriting all model weights", "Removing every keyword from the index"], "correct_answer": "Rephrasing a user query to improve retrieval", "explanation": "Query rewriting can make the search query clearer or better suited to the retrieval system."},
        {"id": "rag_039", "skill": "RAG", "topic": "Advanced Retrieval", "question": "What is multi-query retrieval?", "options": ["Searching with several query variations and combining results", "Returning only one document forever", "Training several operating systems", "Replacing embeddings with file names only"], "correct_answer": "Searching with several query variations and combining results", "explanation": "Multiple query formulations can retrieve different relevant passages and improve coverage."},
        {"id": "rag_040", "skill": "RAG", "topic": "System Design", "question": "What is a sensible response when RAG retrieves no useful evidence?", "options": ["Say evidence is insufficient or ask for clarification", "Invent a source and answer confidently", "Ignore access controls", "Claim that retrieval was successful"], "correct_answer": "Say evidence is insufficient or ask for clarification", "explanation": "An honest abstention is preferable to presenting unsupported information as fact."}
    ],
    
    "cloud computing": [
        {"id":"cloud_001","skill":"Cloud Computing","topic":"Fundamentals","question":"What is cloud computing?","options":["Using computing resources over a network on demand","Writing code without a computer","A type of keyboard","A database query"],"correct_answer":"Using computing resources over a network on demand","explanation":"Cloud computing provides computing resources such as servers and storage when needed."},
        {"id":"cloud_002","skill":"Cloud Computing","topic":"Service Models","question":"What does IaaS stand for?","options":["Infrastructure as a Service","Internet as a System","Integration as a Software","Information and Storage"],"correct_answer":"Infrastructure as a Service","explanation":"IaaS provides resources such as virtual machines, networking, and storage."},
        {"id":"cloud_003","skill":"Cloud Computing","topic":"Service Models","question":"What does PaaS provide?","options":["A platform for building and running applications","Only physical keyboards","Only source code editors","A local printer"],"correct_answer":"A platform for building and running applications","explanation":"PaaS provides managed tools and environments for application development and deployment."},
        {"id":"cloud_004","skill":"Cloud Computing","topic":"Service Models","question":"What does SaaS mean?","options":["Software as a Service","Storage as a Server","System as a Script","Security as a Switch"],"correct_answer":"Software as a Service","explanation":"SaaS delivers software for users to access, often through a browser."},
        {"id":"cloud_005","skill":"Cloud Computing","topic":"Deployment Models","question":"What is a public cloud?","options":["Cloud services offered to customers by a provider","A computer with no network","A private laptop folder","A database available only offline"],"correct_answer":"Cloud services offered to customers by a provider","explanation":"Public cloud providers offer shared infrastructure and services to multiple customers."},
        {"id":"cloud_006","skill":"Cloud Computing","topic":"Deployment Models","question":"What is a private cloud?","options":["Cloud infrastructure dedicated to one organization","A public website","A free email account","A shared public database with no controls"],"correct_answer":"Cloud infrastructure dedicated to one organization","explanation":"A private cloud is dedicated to a single organization, though it may be hosted internally or externally."},
        {"id":"cloud_007","skill":"Cloud Computing","topic":"Deployment Models","question":"What is a hybrid cloud?","options":["A combination of private and public cloud environments","Two monitors connected together","A single offline server","A database backup format"],"correct_answer":"A combination of private and public cloud environments","explanation":"Hybrid cloud connects or coordinates private and public cloud resources."},
        {"id":"cloud_008","skill":"Cloud Computing","topic":"Scalability","question":"What does scalability mean?","options":["The ability to handle changes in workload by adjusting resources","The ability to change font size","The number of code comments","The number of installed browsers"],"correct_answer":"The ability to handle changes in workload by adjusting resources","explanation":"Scalability allows a system to handle increasing or decreasing demand."},
        {"id":"cloud_009","skill":"Cloud Computing","topic":"Scalability","question":"What is horizontal scaling?","options":["Adding more instances or machines","Increasing only one machine's memory","Deleting every server","Reducing screen brightness"],"correct_answer":"Adding more instances or machines","explanation":"Horizontal scaling adds machines or instances to share the workload."},
        {"id":"cloud_010","skill":"Cloud Computing","topic":"Scalability","question":"What is vertical scaling?","options":["Increasing resources of an existing machine","Adding more independent machines","Changing a database name","Creating another user account"],"correct_answer":"Increasing resources of an existing machine","explanation":"Vertical scaling increases resources such as CPU or memory on one machine."},
        {"id":"cloud_011","skill":"Cloud Computing","topic":"Elasticity","question":"What is cloud elasticity?","options":["Automatically adjusting resources as demand changes","Making software visually attractive","Encrypting every file manually","Keeping resources fixed forever"],"correct_answer":"Automatically adjusting resources as demand changes","explanation":"Elasticity allows resources to expand or shrink as workload changes."},
        {"id":"cloud_012","skill":"Cloud Computing","topic":"Virtualization","question":"What is a virtual machine?","options":["A software-based computer environment","A physical network cable","A database column","A programming language"],"correct_answer":"A software-based computer environment","explanation":"A virtual machine runs an operating system and applications using virtualized hardware."},
        {"id":"cloud_013","skill":"Cloud Computing","topic":"Containers","question":"What is a container commonly used for?","options":["Packaging an application and its dependencies","Replacing all network security","Increasing monitor resolution","Writing database queries only"],"correct_answer":"Packaging an application and its dependencies","explanation":"Containers package applications with the components needed to run them."},
        {"id":"cloud_014","skill":"Cloud Computing","topic":"Containers","question":"How do containers commonly differ from virtual machines?","options":["Containers often share the host OS kernel","Containers always require separate physical hardware","Virtual machines never run an OS","Containers cannot run applications"],"correct_answer":"Containers often share the host OS kernel","explanation":"Containers isolate applications while commonly sharing the host operating system kernel."},
        {"id":"cloud_015","skill":"Cloud Computing","topic":"Storage","question":"What is object storage suited for?","options":["Storing files and unstructured data as objects","Running CPU instructions directly","Replacing every application server","Managing keyboard input"],"correct_answer":"Storing files and unstructured data as objects","explanation":"Object storage is commonly used for images, documents, backups, and other unstructured data."},
        {"id":"cloud_016","skill":"Cloud Computing","topic":"Storage","question":"What is block storage often used for?","options":["Providing disk-like storage to virtual machines","Hosting only web fonts","Managing source code comments","Creating email addresses"],"correct_answer":"Providing disk-like storage to virtual machines","explanation":"Block storage presents storage volumes that operating systems and applications can use like disks."},
        {"id":"cloud_017","skill":"Cloud Computing","topic":"Storage","question":"What is cloud file storage designed to provide?","options":["Files organized in folders and shared through file protocols","Only CPU scheduling","Only application logs on paper","A replacement for all databases"],"correct_answer":"Files organized in folders and shared through file protocols","explanation":"File storage provides shared file-system access to applications and users."},
        {"id":"cloud_018","skill":"Cloud Computing","topic":"Networking","question":"What is a virtual private cloud commonly used for?","options":["Creating an isolated virtual network in a cloud environment","Making every server public","Replacing all storage systems","Training a neural network"],"correct_answer":"Creating an isolated virtual network in a cloud environment","explanation":"A virtual private cloud provides network isolation and configurable connectivity."},
        {"id":"cloud_019","skill":"Cloud Computing","topic":"Networking","question":"What does a load balancer do?","options":["Distributes requests across available servers","Stores passwords in plain text","Writes application code","Creates training datasets"],"correct_answer":"Distributes requests across available servers","explanation":"Load balancing spreads traffic across targets to improve availability and capacity."},
        {"id":"cloud_020","skill":"Cloud Computing","topic":"Networking","question":"What is a CDN mainly used for?","options":["Delivering content from locations closer to users","Creating database schemas","Training cloud models","Replacing authentication"],"correct_answer":"Delivering content from locations closer to users","explanation":"A content delivery network caches and serves content from distributed locations."},
        {"id":"cloud_021","skill":"Cloud Computing","topic":"Compute","question":"What is serverless computing?","options":["Running code without managing the underlying servers directly","Running software without any servers existing","Using only offline computers","Writing code without an operating system"],"correct_answer":"Running code without managing the underlying servers directly","explanation":"The provider manages server infrastructure while customers deploy code or functions."},
        {"id":"cloud_022","skill":"Cloud Computing","topic":"Compute","question":"What is a common benefit of serverless functions?","options":["Scaling execution in response to events or requests","Guaranteed zero cost in all cases","Unlimited execution time for every function","No need to secure application code"],"correct_answer":"Scaling execution in response to events or requests","explanation":"Many serverless platforms scale function execution automatically within configured limits."},
        {"id":"cloud_023","skill":"Cloud Computing","topic":"Availability","question":"What is a cloud availability zone?","options":["An isolated location within a cloud region","A programming language","A type of database query","A user password policy"],"correct_answer":"An isolated location within a cloud region","explanation":"Availability zones are separated locations designed to reduce the impact of certain failures."},
        {"id":"cloud_024","skill":"Cloud Computing","topic":"Availability","question":"Why deploy across multiple availability zones?","options":["To improve resilience if one zone fails","To guarantee that bugs never occur","To remove all network latency","To avoid application monitoring"],"correct_answer":"To improve resilience if one zone fails","explanation":"Redundant deployments can keep an application available during some zone-level failures."},
        {"id":"cloud_025","skill":"Cloud Computing","topic":"Reliability","question":"What is fault tolerance?","options":["Continuing operation despite certain component failures","Preventing every possible software bug","Increasing file names","Removing all backups"],"correct_answer":"Continuing operation despite certain component failures","explanation":"Fault-tolerant systems are designed to continue functioning when some components fail."},
        {"id":"cloud_026","skill":"Cloud Computing","topic":"Disaster Recovery","question":"Why create cloud backups?","options":["To recover data after loss or corruption","To increase every API response time","To make all data public","To replace access controls"],"correct_answer":"To recover data after loss or corruption","explanation":"Backups provide copies that can be restored after accidental deletion, corruption, or other failures."},
        {"id":"cloud_027","skill":"Cloud Computing","topic":"Disaster Recovery","question":"What does RPO describe in disaster recovery?","options":["The acceptable amount of data loss measured in time","The maximum number of users","The speed of a CPU","The number of deployed websites"],"correct_answer":"The acceptable amount of data loss measured in time","explanation":"Recovery Point Objective indicates how far back data recovery may need to go."},
        {"id":"cloud_028","skill":"Cloud Computing","topic":"Disaster Recovery","question":"What does RTO describe?","options":["The target time to restore a service","The number of rows in a database","The age of a cloud account","The number of virtual networks"],"correct_answer":"The target time to restore a service","explanation":"Recovery Time Objective specifies the desired time for service recovery."},
        {"id":"cloud_029","skill":"Cloud Computing","topic":"Security","question":"What is the principle of least privilege?","options":["Granting only the permissions needed for a task","Giving every user administrator access","Sharing all passwords","Disabling authentication"],"correct_answer":"Granting only the permissions needed for a task","explanation":"Least privilege limits access to reduce the impact of mistakes or compromised accounts."},
        {"id":"cloud_030","skill":"Cloud Computing","topic":"Security","question":"What is multi-factor authentication?","options":["Using two or more different authentication factors","Using the same password twice","Logging in without identity checks","Creating multiple usernames only"],"correct_answer":"Using two or more different authentication factors","explanation":"MFA combines factors such as a password and a separate authenticator."},
        {"id":"cloud_031","skill":"Cloud Computing","topic":"Security","question":"Why encrypt sensitive cloud data?","options":["To make it unreadable without appropriate decryption access","To make files smaller in every case","To improve every algorithm's accuracy","To remove the need for permissions"],"correct_answer":"To make it unreadable without appropriate decryption access","explanation":"Encryption helps protect data confidentiality when keys are properly managed."},
        {"id":"cloud_032","skill":"Cloud Computing","topic":"Monitoring","question":"What do cloud monitoring tools commonly track?","options":["Metrics, logs, and service health","Only font styles","Only developer names","Only file extensions"],"correct_answer":"Metrics, logs, and service health","explanation":"Monitoring helps teams detect failures, capacity issues, and unusual behavior."},
        {"id":"cloud_033","skill":"Cloud Computing","topic":"Monitoring","question":"What is an alert in cloud monitoring?","options":["A notification triggered by a condition or threshold","A replacement for application logs","A type of storage volume","A programming language"],"correct_answer":"A notification triggered by a condition or threshold","explanation":"Alerts notify operators when monitored conditions may require attention."},
        {"id":"cloud_034","skill":"Cloud Computing","topic":"Cost Management","question":"What is cloud cost optimization?","options":["Reducing unnecessary spending while meeting requirements","Deleting every backup regardless of risk","Always choosing the largest server","Disabling all monitoring"],"correct_answer":"Reducing unnecessary spending while meeting requirements","explanation":"Cost optimization balances resource use, performance, reliability, and business needs."},
        {"id":"cloud_035","skill":"Cloud Computing","topic":"Cost Management","question":"What is a cloud budget alert used for?","options":["Warning when spending approaches a configured amount","Automatically guaranteeing a fixed bill","Encrypting stored files","Changing the application's programming language"],"correct_answer":"Warning when spending approaches a configured amount","explanation":"Budget alerts help teams notice spending trends, though alerts may not stop charges automatically."},
        {"id":"cloud_036","skill":"Cloud Computing","topic":"Infrastructure as Code","question":"What is Infrastructure as Code?","options":["Defining infrastructure through machine-readable configuration","Drawing infrastructure only on paper","Managing servers without any configuration","Writing only frontend CSS"],"correct_answer":"Defining infrastructure through machine-readable configuration","explanation":"Infrastructure as Code makes infrastructure provisioning repeatable and version-controlled."},
        {"id":"cloud_037","skill":"Cloud Computing","topic":"Automation","question":"Why automate cloud resource provisioning?","options":["To make deployments repeatable and reduce manual errors","To guarantee there will never be outages","To remove the need for permissions","To make every resource free"],"correct_answer":"To make deployments repeatable and reduce manual errors","explanation":"Automation provides consistent setup and can reduce configuration mistakes."},
        {"id":"cloud_038","skill":"Cloud Computing","topic":"Architecture","question":"What is a microservices architecture?","options":["An application split into smaller independently managed services","One enormous function with no boundaries","A single spreadsheet used as a server","A network with no communication"],"correct_answer":"An application split into smaller independently managed services","explanation":"Microservices organize an application into services that communicate through defined interfaces."},
        {"id":"cloud_039","skill":"Cloud Computing","topic":"Shared Responsibility","question":"What does the cloud shared-responsibility model describe?","options":["Which security duties belong to the provider and customer","How to share one password among all users","How to divide source code alphabetically","How to remove customer security duties"],"correct_answer":"Which security duties belong to the provider and customer","explanation":"Security responsibilities differ by service model and provider offering."},
        {"id":"cloud_040","skill":"Cloud Computing","topic":"Architecture","question":"What should guide the choice of a cloud service?","options":["Workload needs, cost, security, reliability, and operational effort","Only the service's name","Only its website color","Only the number of marketing pages"],"correct_answer":"Workload needs, cost, security, reliability, and operational effort","explanation":"Cloud architecture choices should match functional and non-functional requirements."}
    ],
    "aws": [
        {"id":"aws_001","skill":"AWS","topic":"Fundamentals","question":"What does AWS stand for?","options":["Amazon Web Services","Advanced Web Software","Automated Work System","Application Wide Storage"],"correct_answer":"Amazon Web Services","explanation":"AWS is a cloud computing platform offering compute, storage, databases, networking, and more."},
        {"id":"aws_002","skill":"AWS","topic":"Compute","question":"Which AWS service provides virtual servers?","options":["Amazon EC2","Amazon S3","Amazon Route 53","Amazon CloudFront"],"correct_answer":"Amazon EC2","explanation":"EC2 provides resizable compute capacity through virtual server instances."},
        {"id":"aws_003","skill":"AWS","topic":"Storage","question":"Which AWS service provides object storage?","options":["Amazon S3","Amazon EC2","Amazon VPC","AWS IAM"],"correct_answer":"Amazon S3","explanation":"S3 stores objects in buckets and is widely used for files, backups, and data."},
        {"id":"aws_004","skill":"AWS","topic":"Database","question":"Which AWS service is a managed relational database service?","options":["Amazon RDS","Amazon S3","Amazon Route 53","Amazon CloudFront"],"correct_answer":"Amazon RDS","explanation":"RDS manages supported relational database engines and many routine administrative tasks."},
        {"id":"aws_005","skill":"AWS","topic":"Serverless","question":"Which AWS service runs code in response to events without managing servers directly?","options":["AWS Lambda","Amazon EBS","Amazon VPC","AWS Artifact"],"correct_answer":"AWS Lambda","explanation":"Lambda runs functions in response to configured events or requests."},
        {"id":"aws_006","skill":"AWS","topic":"Networking","question":"What does Amazon VPC provide?","options":["A logically isolated virtual network","A document editor","A source code repository","A machine learning dataset"],"correct_answer":"A logically isolated virtual network","explanation":"A VPC lets customers configure networking for resources in AWS."},
        {"id":"aws_007","skill":"AWS","topic":"Identity and Access","question":"What is AWS IAM used for?","options":["Managing identities and permissions","Storing image objects","Running virtual machines only","Registering domain names"],"correct_answer":"Managing identities and permissions","explanation":"IAM controls authentication-related identities and authorization permissions in AWS."},
        {"id":"aws_008","skill":"AWS","topic":"Networking","question":"What is Amazon Route 53 mainly used for?","options":["DNS and domain routing","Object storage","Virtual machine snapshots only","Code compilation"],"correct_answer":"DNS and domain routing","explanation":"Route 53 provides DNS services and related domain-routing capabilities."},
        {"id":"aws_009","skill":"AWS","topic":"Content Delivery","question":"What is Amazon CloudFront?","options":["A content delivery network","A relational database engine","A command-line text editor","A virtual private network only"],"correct_answer":"A content delivery network","explanation":"CloudFront delivers content through a distributed network of edge locations."},
        {"id":"aws_010","skill":"AWS","topic":"Storage","question":"What is Amazon EBS commonly used for?","options":["Block storage volumes for EC2 instances","DNS hosting","Sending email only","Managing source code branches"],"correct_answer":"Block storage volumes for EC2 instances","explanation":"EBS provides persistent block storage volumes for use with EC2."},
        {"id":"aws_011","skill":"AWS","topic":"Storage","question":"What is Amazon EFS designed to provide?","options":["Managed elastic file storage","A serverless function runtime","A DNS resolver only","A message queue only"],"correct_answer":"Managed elastic file storage","explanation":"EFS provides a scalable shared file system for supported workloads."},
        {"id":"aws_012","skill":"AWS","topic":"NoSQL","question":"Which AWS service is a managed key-value and document database?","options":["Amazon DynamoDB","Amazon RDS","Amazon EBS","Amazon CloudFront"],"correct_answer":"Amazon DynamoDB","explanation":"DynamoDB is a managed NoSQL database supporting key-value and document data models."},
        {"id":"aws_013","skill":"AWS","topic":"Containers","question":"What is Amazon ECS used for?","options":["Managing containerized applications","Registering domain names only","Editing images","Creating SQL queries only"],"correct_answer":"Managing containerized applications","explanation":"ECS orchestrates and manages container workloads on AWS."},
        {"id":"aws_014","skill":"AWS","topic":"Containers","question":"What is Amazon EKS?","options":["A managed Kubernetes service","An object storage format","A DNS record type","A relational database engine"],"correct_answer":"A managed Kubernetes service","explanation":"EKS provides managed Kubernetes control-plane capabilities on AWS."},
        {"id":"aws_015","skill":"AWS","topic":"Infrastructure as Code","question":"What is AWS CloudFormation used for?","options":["Defining and provisioning AWS resources as code","Editing photos","Hosting only email inboxes","Generating random passwords only"],"correct_answer":"Defining and provisioning AWS resources as code","explanation":"CloudFormation provisions resources from declarative templates."},
        {"id":"aws_016","skill":"AWS","topic":"Monitoring","question":"Which service collects AWS metrics and logs and supports alarms?","options":["Amazon CloudWatch","Amazon S3 Glacier only","AWS Artifact","Amazon Route 53"],"correct_answer":"Amazon CloudWatch","explanation":"CloudWatch provides monitoring for metrics, logs, and configured alarms."},
        {"id":"aws_017","skill":"AWS","topic":"Auditing","question":"What does AWS CloudTrail record?","options":["Account activity and API events","Only website colors","Only database query results","Only CPU temperature"],"correct_answer":"Account activity and API events","explanation":"CloudTrail helps audit actions taken in an AWS account."},
        {"id":"aws_018","skill":"AWS","topic":"Security","question":"What is AWS KMS used for?","options":["Creating and managing cryptographic keys","Deploying frontend CSS","Managing Git commits","Hosting static websites only"],"correct_answer":"Creating and managing cryptographic keys","explanation":"KMS helps manage encryption keys used by supported AWS services and applications."},
        {"id":"aws_019","skill":"AWS","topic":"Secrets","question":"Which AWS service helps store and manage application secrets?","options":["AWS Secrets Manager","Amazon CloudFront","Amazon Route 53","Amazon EBS"],"correct_answer":"AWS Secrets Manager","explanation":"Secrets Manager stores and controls access to secrets such as credentials and API keys."},
        {"id":"aws_020","skill":"AWS","topic":"Messaging","question":"What is Amazon SQS?","options":["A managed message queuing service","A virtual machine type","An object storage class","A domain registration service"],"correct_answer":"A managed message queuing service","explanation":"SQS lets distributed components exchange messages asynchronously."},
        {"id":"aws_021","skill":"AWS","topic":"Messaging","question":"What is Amazon SNS commonly used for?","options":["Pub/sub messaging and notifications","Block storage volumes","Creating virtual networks only","Managing SQL indexes"],"correct_answer":"Pub/sub messaging and notifications","explanation":"SNS distributes messages to subscribed endpoints or services."},
        {"id":"aws_022","skill":"AWS","topic":"Event-Driven Systems","question":"What is Amazon EventBridge used for?","options":["Routing events between applications and AWS services","Storing files as blocks only","Creating virtual machine images only","Registering Git branches"],"correct_answer":"Routing events between applications and AWS services","explanation":"EventBridge routes events using rules to connect producers and consumers."},
        {"id":"aws_023","skill":"AWS","topic":"Analytics","question":"What is Amazon Athena designed to do?","options":["Query data in S3 using SQL","Run virtual machines only","Manage DNS records only","Store passwords for applications"],"correct_answer":"Query data in S3 using SQL","explanation":"Athena is a serverless interactive query service for supported data stored in S3."},
        {"id":"aws_024","skill":"AWS","topic":"Data Integration","question":"What is AWS Glue commonly used for?","options":["Data integration and ETL workloads","Domain registration only","Container image editing","User authentication only"],"correct_answer":"Data integration and ETL workloads","explanation":"Glue helps discover, prepare, transform, and move data."},
        {"id":"aws_025","skill":"AWS","topic":"Data Warehousing","question":"What is Amazon Redshift?","options":["A cloud data warehouse","A DNS service","A container registry only","A virtual machine operating system"],"correct_answer":"A cloud data warehouse","explanation":"Redshift supports analytical queries over large datasets."},
        {"id":"aws_026","skill":"AWS","topic":"Machine Learning","question":"What is Amazon SageMaker designed to support?","options":["Building, training, and deploying machine learning models","Registering domains only","Sending email newsletters only","Managing network cables"],"correct_answer":"Building, training, and deploying machine learning models","explanation":"SageMaker provides managed capabilities for machine learning workflows."},
        {"id":"aws_027","skill":"AWS","topic":"Cost Management","question":"What is AWS Budgets used for?","options":["Tracking costs or usage against configured budgets","Automatically making all services free","Encrypting every file","Creating database tables"],"correct_answer":"Tracking costs or usage against configured budgets","explanation":"AWS Budgets can track spending or usage and send alerts."},
        {"id":"aws_028","skill":"AWS","topic":"Cost Management","question":"Which tool helps explore AWS service costs and usage over time?","options":["AWS Cost Explorer","Amazon Route 53","AWS Lambda only","Amazon EFS"],"correct_answer":"AWS Cost Explorer","explanation":"Cost Explorer helps analyze historical costs and usage patterns."},
        {"id":"aws_029","skill":"AWS","topic":"Availability","question":"Why spread an application across multiple Availability Zones?","options":["To improve resilience to a zone failure","To guarantee no software bugs","To remove every network charge","To eliminate backups"],"correct_answer":"To improve resilience to a zone failure","explanation":"Multi-zone designs can maintain service when one zone experiences a disruption."},
        {"id":"aws_030","skill":"AWS","topic":"Load Balancing","question":"What does an Elastic Load Balancer do?","options":["Distributes incoming traffic across targets","Stores source code only","Encrypts every file automatically","Replaces IAM permissions"],"correct_answer":"Distributes incoming traffic across targets","explanation":"Elastic Load Balancing routes requests across configured healthy targets."},
        {"id":"aws_031","skill":"AWS","topic":"Autoscaling","question":"What is EC2 Auto Scaling used for?","options":["Adjusting the number of EC2 instances based on conditions","Changing source code variable names","Backing up every database automatically without configuration","Registering domain names"],"correct_answer":"Adjusting the number of EC2 instances based on conditions","explanation":"Auto Scaling adds or removes instances according to policies and demand."},
        {"id":"aws_032","skill":"AWS","topic":"Deployment","question":"What is AWS Elastic Beanstalk?","options":["A managed way to deploy and operate supported applications","A database query language","A hardware security key","A file compression algorithm"],"correct_answer":"A managed way to deploy and operate supported applications","explanation":"Elastic Beanstalk simplifies application deployment while managing supporting resources."},
        {"id":"aws_033","skill":"AWS","topic":"Developer Tools","question":"What is AWS CodeBuild used for?","options":["Building and testing source code","Managing DNS only","Storing object files only","Creating user passwords"],"correct_answer":"Building and testing source code","explanation":"CodeBuild runs configured build and test commands in a managed environment."},
        {"id":"aws_034","skill":"AWS","topic":"Developer Tools","question":"What is AWS CodePipeline used for?","options":["Automating software release workflows","Creating SQL tables only","Serving DNS records only","Managing physical servers"],"correct_answer":"Automating software release workflows","explanation":"CodePipeline coordinates stages in a continuous delivery workflow."},
        {"id":"aws_035","skill":"AWS","topic":"Permissions","question":"Why prefer an IAM role over embedding long-term credentials in code?","options":["Roles provide temporary credentials through controlled access","Roles make code run without authentication","Roles guarantee no security incidents","Roles store passwords in source files"],"correct_answer":"Roles provide temporary credentials through controlled access","explanation":"Roles reduce the need to store long-lived credentials in application code."},
        {"id":"aws_036","skill":"AWS","topic":"Storage Lifecycle","question":"What can an S3 lifecycle policy do?","options":["Transition or expire objects according to rules","Automatically correct all file contents","Run Python functions on every computer","Replace a VPC"],"correct_answer":"Transition or expire objects according to rules","explanation":"Lifecycle policies can move objects between supported storage classes or expire them."},
        {"id":"aws_037","skill":"AWS","topic":"Security","question":"Why avoid making an S3 bucket public unless required?","options":["To reduce the risk of exposing sensitive data","To increase file size","To improve model training automatically","To remove the need for encryption"],"correct_answer":"To reduce the risk of exposing sensitive data","explanation":"Restricting public access helps prevent accidental data exposure."},
        {"id":"aws_038","skill":"AWS","topic":"Networking","question":"What is a security group in AWS?","options":["A virtual firewall controlling traffic for supported resources","A database table","A code deployment package","A file storage class"],"correct_answer":"A virtual firewall controlling traffic for supported resources","explanation":"Security groups define allowed inbound and outbound traffic for associated resources."},
        {"id":"aws_039","skill":"AWS","topic":"Networking","question":"What is a network ACL in a VPC?","options":["A subnet-level network traffic control list","A machine learning model","A storage encryption key","A source code repository"],"correct_answer":"A subnet-level network traffic control list","explanation":"Network ACLs apply allow and deny rules to traffic entering or leaving a subnet."},
        {"id":"aws_040","skill":"AWS","topic":"Architecture","question":"What is a good practice before deploying an AWS workload to production?","options":["Review security, reliability, performance, and cost requirements","Use administrator permissions for every user","Disable all logs","Expose every service publicly"],"correct_answer":"Review security, reliability, performance, and cost requirements","explanation":"A production review helps ensure the architecture meets its operational and security needs."}
    ],
    "redis": [
        {"id":"redis_001","skill":"Redis","topic":"Fundamentals","question":"What is Redis commonly used for?","options":["In-memory data storage and caching","Frontend styling only","Compiling Java code","Creating image files"],"correct_answer":"In-memory data storage and caching","explanation":"Redis is an in-memory data store often used for caching, messaging, and fast data access."},
        {"id":"redis_002","skill":"Redis","topic":"Data Types","question":"Which basic Redis data type stores strings?","options":["String","Table","Class","HTML"],"correct_answer":"String","explanation":"Redis strings can store text, numbers, serialized data, and binary-safe values."},
        {"id":"redis_003","skill":"Redis","topic":"Commands","question":"Which command stores a value under a key?","options":["SET","SELECTROW","INSERTHTML","MAKEKEY"],"correct_answer":"SET","explanation":"SET assigns a value to a key in Redis."},
        {"id":"redis_004","skill":"Redis","topic":"Commands","question":"Which command retrieves a string value by key?","options":["GET","FETCHROW","OPEN","READFILE"],"correct_answer":"GET","explanation":"GET returns the value stored at a string key."},
        {"id":"redis_005","skill":"Redis","topic":"Commands","question":"Which command removes a key?","options":["DEL","REMOVEFILEONLY","DROPHTML","CLEARCPU"],"correct_answer":"DEL","explanation":"DEL deletes one or more specified keys."},
        {"id":"redis_006","skill":"Redis","topic":"Data Types","question":"Which Redis type stores an ordered collection of strings?","options":["List","Hash only","Set only","Boolean"],"correct_answer":"List","explanation":"Redis lists are ordered collections of string elements."},
        {"id":"redis_007","skill":"Redis","topic":"Data Types","question":"Which Redis type stores unique unordered members?","options":["Set","List","String","Stream only"],"correct_answer":"Set","explanation":"Redis sets store unique members without a guaranteed order."},
        {"id":"redis_008","skill":"Redis","topic":"Data Types","question":"What is a Redis hash useful for?","options":["Storing field-value pairs under one key","Storing only ordered image pixels","Creating network interfaces","Running SQL joins"],"correct_answer":"Storing field-value pairs under one key","explanation":"Hashes are useful for representing objects with fields and values."},
        {"id":"redis_009","skill":"Redis","topic":"Data Types","question":"What is a sorted set in Redis?","options":["Unique members associated with scores and ordered by score","A list that cannot contain strings","A relational table with foreign keys","A file system directory"],"correct_answer":"Unique members associated with scores and ordered by score","explanation":"Sorted sets associate each unique member with a score for ordered retrieval."},
        {"id":"redis_010","skill":"Redis","topic":"Commands","question":"Which command increments an integer stored at a key?","options":["INCR","ADDHTML","PLUSROW","COUNTFILE"],"correct_answer":"INCR","explanation":"INCR atomically increments a string value interpreted as an integer."},
        {"id":"redis_011","skill":"Redis","topic":"Expiration","question":"Which command sets a key's expiration in seconds?","options":["EXPIRE","DELETEAFTERBOOT","TIMEOUTSQL","WAITKEY"],"correct_answer":"EXPIRE","explanation":"EXPIRE sets a time-to-live after which the key is removed if not refreshed."},
        {"id":"redis_012","skill":"Redis","topic":"Expiration","question":"Why set a TTL on cached data?","options":["To allow stale entries to expire automatically","To make data permanent","To increase all values by one","To disable memory use"],"correct_answer":"To allow stale entries to expire automatically","explanation":"A time-to-live limits how long cached entries remain available."},
        {"id":"redis_013","skill":"Redis","topic":"Caching","question":"What is a cache hit?","options":["The requested item is found in the cache","The cache server is always offline","A key is deleted","A database schema is changed"],"correct_answer":"The requested item is found in the cache","explanation":"A cache hit lets an application use cached data rather than fetch it again."},
        {"id":"redis_014","skill":"Redis","topic":"Caching","question":"What is a cache miss?","options":["The requested item is not present in the cache","Every item is returned instantly","A Redis server is installed","A value has a TTL"],"correct_answer":"The requested item is not present in the cache","explanation":"A cache miss often requires fetching data from the original source."},
        {"id":"redis_015","skill":"Redis","topic":"Caching","question":"What is cache-aside?","options":["The application checks the cache and loads missing data from the source","Redis always updates every database automatically","The database never receives reads","All cached values are permanent"],"correct_answer":"The application checks the cache and loads missing data from the source","explanation":"In cache-aside, the application manages cache reads and fills missing entries."},
        {"id":"redis_016","skill":"Redis","topic":"Caching","question":"What is cache invalidation?","options":["Removing or updating cached data when it is no longer valid","Adding more CPU cores","Creating a new programming language","Encrypting every source file"],"correct_answer":"Removing or updating cached data when it is no longer valid","explanation":"Invalidation prevents applications from continuing to use outdated cached values."},
        {"id":"redis_017","skill":"Redis","topic":"Persistence","question":"What is RDB persistence in Redis?","options":["Saving point-in-time snapshots of data","Saving only network passwords","Storing every request in a relational table","Disabling data recovery"],"correct_answer":"Saving point-in-time snapshots of data","explanation":"RDB creates snapshots of the dataset at configured times or conditions."},
        {"id":"redis_018","skill":"Redis","topic":"Persistence","question":"What is AOF persistence?","options":["Recording write operations in an append-only log","Saving only images","Storing DNS records","Removing all write operations"],"correct_answer":"Recording write operations in an append-only log","explanation":"Append-only file persistence records write operations that can be replayed during recovery."},
        {"id":"redis_019","skill":"Redis","topic":"Persistence","question":"Why enable persistence in Redis when data must survive restarts?","options":["To recover data from saved state or logs","To guarantee that no data loss is ever possible","To eliminate the need for backups in all cases","To make every read slower intentionally"],"correct_answer":"To recover data from saved state or logs","explanation":"Persistence options help restore data, though durability depends on configuration and failure conditions."},
        {"id":"redis_020","skill":"Redis","topic":"Transactions","question":"What does MULTI do in Redis?","options":["Begins queuing commands for a transaction","Deletes every key","Starts a new operating system","Creates a new database user"],"correct_answer":"Begins queuing commands for a transaction","explanation":"MULTI starts a transaction in which subsequent commands are queued until EXEC or DISCARD."},
        {"id":"redis_021","skill":"Redis","topic":"Transactions","question":"What does EXEC do after MULTI?","options":["Executes the queued transaction commands","Deletes the Redis server","Changes every key's type","Turns off persistence permanently"],"correct_answer":"Executes the queued transaction commands","explanation":"EXEC runs the commands queued in the current transaction."},
        {"id":"redis_022","skill":"Redis","topic":"Atomicity","question":"Why are individual Redis commands useful for counters?","options":["Commands such as INCR execute atomically","They require a relational join","They always run in a browser","They disable concurrent clients"],"correct_answer":"Commands such as INCR execute atomically","explanation":"Atomic commands avoid certain read-modify-write race conditions."},
        {"id":"redis_023","skill":"Redis","topic":"Pub/Sub","question":"What is Redis Pub/Sub used for?","options":["Publishing messages to subscribed channels","Storing only permanent relational records","Compiling applications","Creating cloud virtual machines"],"correct_answer":"Publishing messages to subscribed channels","explanation":"Publishers send messages to channels and active subscribers receive them."},
        {"id":"redis_024","skill":"Redis","topic":"Pub/Sub","question":"What is a limitation of basic Redis Pub/Sub?","options":["Messages are not stored for disconnected subscribers to replay later","Every message is stored forever automatically","Subscribers must use SQL","Messages cannot contain text"],"correct_answer":"Messages are not stored for disconnected subscribers to replay later","explanation":"Basic Pub/Sub is transient; Redis Streams or another durable queue may be more appropriate when replay is needed."},
        {"id":"redis_025","skill":"Redis","topic":"Streams","question":"What are Redis Streams designed to support?","options":["Append-only event streams with IDs and consumer processing","Only static website files","Only relational joins","Operating system booting"],"correct_answer":"Append-only event streams with IDs and consumer processing","explanation":"Streams support event records, range queries, and consumer-group workflows."},
        {"id":"redis_026","skill":"Redis","topic":"Performance","question":"Why are Redis reads often fast?","options":["Data is commonly served from memory","All requests are sent to paper backups","Every read recompiles the server","Redis stores all data only on optical discs"],"correct_answer":"Data is commonly served from memory","explanation":"In-memory access reduces the latency of many operations compared with disk-based access."},
        {"id":"redis_027","skill":"Redis","topic":"Memory Management","question":"What happens when Redis reaches its configured memory limit?","options":["Behavior depends on the configured eviction policy and write conditions","It always adds unlimited RAM automatically","It permanently disables every read","It converts all keys to SQL tables"],"correct_answer":"Behavior depends on the configured eviction policy and write conditions","explanation":"Redis may evict keys according to policy or reject writes, depending on configuration and command type."},
        {"id":"redis_028","skill":"Redis","topic":"Eviction","question":"What does an LRU-style eviction policy aim to remove?","options":["Keys that have been least recently used","Keys with the longest names only","All recently used keys first","Every key in alphabetical order"],"correct_answer":"Keys that have been least recently used","explanation":"LRU approximates removing data that has not been accessed recently."},
        {"id":"redis_029","skill":"Redis","topic":"Security","question":"Why should Redis be protected from unrestricted public access?","options":["Unauthorized clients may read, change, or delete data","Public access always improves security","Redis keys cannot contain private data","Network access has no security impact"],"correct_answer":"Unauthorized clients may read, change, or delete data","explanation":"Network restrictions and authentication help protect Redis from unauthorized use."},
        {"id":"redis_030","skill":"Redis","topic":"Security","question":"What is the purpose of Redis ACLs?","options":["Controlling which users can run commands and access keys","Creating virtual machines","Managing browser cookies only","Compressing log files"],"correct_answer":"Controlling which users can run commands and access keys","explanation":"Access control lists allow fine-grained user permissions in supported Redis versions."},
        {"id":"redis_031","skill":"Redis","topic":"High Availability","question":"What is Redis replication?","options":["Copying data from a primary to one or more replicas","Splitting CSS files into components","Converting strings into images","Deleting all backups"],"correct_answer":"Copying data from a primary to one or more replicas","explanation":"Replication provides copies of data that can support reads or recovery strategies."},
        {"id":"redis_032","skill":"Redis","topic":"High Availability","question":"What is Redis Sentinel used for?","options":["Monitoring primary and replica instances and supporting failover","Writing SQL queries","Serving static images only","Creating cloud billing reports"],"correct_answer":"Monitoring primary and replica instances and supporting failover","explanation":"Sentinel monitors Redis deployments and can coordinate failover for supported configurations."},
        {"id":"redis_033","skill":"Redis","topic":"Sharding","question":"What is Redis Cluster designed to provide?","options":["Sharding data across nodes and supporting availability features","A single local text file","Only a browser-based editor","A replacement for every network protocol"],"correct_answer":"Sharding data across nodes and supporting availability features","explanation":"Redis Cluster distributes key slots across nodes and supports certain failure scenarios."},
        {"id":"redis_034","skill":"Redis","topic":"Data Types","question":"Which Redis structure is useful for ranking players by score?","options":["Sorted set","Plain string only","Unordered file folder","HTML form"],"correct_answer":"Sorted set","explanation":"Sorted sets associate unique members with scores, making them useful for leaderboards."},
        {"id":"redis_035","skill":"Redis","topic":"Data Types","question":"Which Redis structure can support a simple task queue using push and pop operations?","options":["List","String only","Database schema","Network ACL"],"correct_answer":"List","explanation":"Redis lists support operations at both ends and can implement basic queue patterns."},
        {"id":"redis_036","skill":"Redis","topic":"Rate Limiting","question":"How can Redis help implement rate limiting?","options":["Store counters and expiry times for request windows","Compile frontend assets","Store every request only in a PDF","Replace API authentication completely"],"correct_answer":"Store counters and expiry times for request windows","explanation":"Fast atomic counters and TTLs can help enforce request limits."},
        {"id":"redis_037","skill":"Redis","topic":"Sessions","question":"Why use Redis for web sessions?","options":["To access session data quickly across application instances","To make passwords public","To replace HTTPS","To create HTML styles"],"correct_answer":"To access session data quickly across application instances","explanation":"A shared Redis store can let multiple application servers access session state."},
        {"id":"redis_038","skill":"Redis","topic":"Data Modeling","question":"Why choose Redis key names carefully?","options":["Clear names help organize data and avoid collisions","Key names determine the server's physical size","Every key must be a SQL statement","Key names automatically encrypt values"],"correct_answer":"Clear names help organize data and avoid collisions","explanation":"Consistent key naming improves maintainability and supports grouping or access patterns."},
        {"id":"redis_039","skill":"Redis","topic":"Troubleshooting","question":"What should be checked if Redis memory usage grows unexpectedly?","options":["Key counts, value sizes, TTLs, and eviction configuration","Only the website font","Only Python comments","Only the number of monitors"],"correct_answer":"Key counts, value sizes, TTLs, and eviction configuration","explanation":"Memory analysis helps identify oversized values, unexpired keys, or unexpected data growth."},
        {"id":"redis_040","skill":"Redis","topic":"Architecture","question":"When is Redis a poor replacement for a primary relational database?","options":["When the application needs relational joins and durable relational constraints","When fast caching is needed","When counters are needed","When short-lived session storage is needed"],"correct_answer":"When the application needs relational joins and durable relational constraints","explanation":"Redis excels at particular access patterns but is not a direct replacement for every relational database requirement."}
    ],
    "ci/cd": [
        {"id":"cicd_001","skill":"CI/CD","topic":"Fundamentals","question":"What does CI stand for?","options":["Continuous Integration","Code Installation","Central Interface","Computer Inspection"],"correct_answer":"Continuous Integration","explanation":"Continuous Integration frequently merges and validates code changes through automated checks."},
        {"id":"cicd_002","skill":"CI/CD","topic":"Fundamentals","question":"What does CD commonly mean in CI/CD?","options":["Continuous Delivery or Continuous Deployment","Code Deletion only","Central Database","Computer Design"],"correct_answer":"Continuous Delivery or Continuous Deployment","explanation":"Continuous Delivery keeps software ready for release; Continuous Deployment automatically releases qualifying changes."},
        {"id":"cicd_003","skill":"CI/CD","topic":"Version Control","question":"Why is version control important in CI/CD?","options":["It tracks changes and provides events that can trigger workflows","It replaces all tests","It guarantees bug-free code","It removes the need for branches"],"correct_answer":"It tracks changes and provides events that can trigger workflows","explanation":"Version control supports collaboration, history, and automated pipeline triggers."},
        {"id":"cicd_004","skill":"CI/CD","topic":"Builds","question":"What is a build step?","options":["Preparing source code or artifacts for testing or deployment","Deleting the source repository","Changing the computer's wallpaper","Creating user passwords"],"correct_answer":"Preparing source code or artifacts for testing or deployment","explanation":"A build step may compile code, bundle assets, or create a deployable package."},
        {"id":"cicd_005","skill":"CI/CD","topic":"Automated Testing","question":"Why run automated tests in a CI pipeline?","options":["To detect regressions early","To guarantee zero defects forever","To avoid code review in every case","To increase application downtime"],"correct_answer":"To detect regressions early","explanation":"Automated tests provide quick feedback when changes break expected behavior."},
        {"id":"cicd_006","skill":"CI/CD","topic":"Code Quality","question":"What can a static analysis step detect?","options":["Certain code issues without running the program","Every possible runtime failure","Every future security incident","All user experience problems"],"correct_answer":"Certain code issues without running the program","explanation":"Static analysis examines code for configured patterns and potential defects without executing it."},
        {"id":"cicd_007","skill":"CI/CD","topic":"Pipeline Stages","question":"Why separate a pipeline into stages?","options":["To organize build, test, and deployment tasks","To make every task run manually","To hide failures from developers","To remove artifact tracking"],"correct_answer":"To organize build, test, and deployment tasks","explanation":"Stages make workflow dependencies and failure points easier to understand."},
        {"id":"cicd_008","skill":"CI/CD","topic":"Artifacts","question":"What is a build artifact?","options":["A produced package or file used by later pipeline steps","A code review comment only","A database password","A Git branch name"],"correct_answer":"A produced package or file used by later pipeline steps","explanation":"Artifacts can include compiled binaries, packages, containers, or test reports."},
        {"id":"cicd_009","skill":"CI/CD","topic":"Artifacts","question":"Why store and identify build artifacts by version or digest?","options":["To track exactly what is tested and deployed","To change the artifact's contents automatically","To eliminate security checks","To make every release identical by accident"],"correct_answer":"To track exactly what is tested and deployed","explanation":"Traceable artifacts improve reproducibility and release accountability."},
        {"id":"cicd_010","skill":"CI/CD","topic":"Branching","question":"What is a pull request commonly used for?","options":["Reviewing proposed changes before merging","Automatically deleting the main branch","Storing production passwords in code","Replacing all automated tests"],"correct_answer":"Reviewing proposed changes before merging","explanation":"Pull requests provide a place for discussion, review, and automated validation."},
        {"id":"cicd_011","skill":"CI/CD","topic":"Branching","question":"Why require CI checks before merging a pull request?","options":["To catch failures before changes enter the target branch","To prevent all collaboration","To guarantee every feature is correct","To remove commit history"],"correct_answer":"To catch failures before changes enter the target branch","explanation":"Required checks help keep shared branches in a known working state."},
        {"id":"cicd_012","skill":"CI/CD","topic":"Deployment","question":"What is continuous delivery?","options":["Keeping changes in a deployable state with release often requiring approval","Automatically deleting every release","Deploying without any tests in all cases","Writing code only once per year"],"correct_answer":"Keeping changes in a deployable state with release often requiring approval","explanation":"Continuous delivery automates the path to a release-ready state while allowing a release decision."},
        {"id":"cicd_013","skill":"CI/CD","topic":"Deployment","question":"What distinguishes continuous deployment from continuous delivery?","options":["Qualifying changes are released to production automatically","Continuous deployment never uses tests","Continuous delivery cannot build artifacts","Continuous deployment is only source control"],"correct_answer":"Qualifying changes are released to production automatically","explanation":"Continuous deployment automates production release after pipeline requirements pass."},
        {"id":"cicd_014","skill":"CI/CD","topic":"Deployment Strategies","question":"What is a rolling deployment?","options":["Updating instances gradually rather than all at once","Deleting all instances before every test","Deploying only to a developer's laptop","Keeping the application permanently offline"],"correct_answer":"Updating instances gradually rather than all at once","explanation":"Rolling deployment replaces or updates groups of instances over time."},
        {"id":"cicd_015","skill":"CI/CD","topic":"Deployment Strategies","question":"What is a blue-green deployment?","options":["Maintaining two environments and switching traffic to the new one","Changing code colors before release","Deploying only on weekends","Using two programming languages"],"correct_answer":"Maintaining two environments and switching traffic to the new one","explanation":"Blue-green deployment can support fast traffic switching and rollback when environments are prepared correctly."},
        {"id":"cicd_016","skill":"CI/CD","topic":"Deployment Strategies","question":"What is a canary deployment?","options":["Releasing to a small subset before wider rollout","Releasing only to a code editor","Deploying every version to every user immediately","Deleting the old version before testing"],"correct_answer":"Releasing to a small subset before wider rollout","explanation":"A canary release exposes a change to limited traffic to assess its behavior before wider release."},
        {"id":"cicd_017","skill":"CI/CD","topic":"Rollback","question":"What is a deployment rollback?","options":["Returning to a previous working release","Deleting the entire repository","Removing all tests","Changing every database table name"],"correct_answer":"Returning to a previous working release","explanation":"Rollback restores a previous version when a new deployment causes problems."},
        {"id":"cicd_018","skill":"CI/CD","topic":"Configuration","question":"Why keep environment-specific configuration separate from application code?","options":["To use appropriate settings in development, testing, and production","To make all environments identical regardless of needs","To expose credentials publicly","To prevent deployment automation"],"correct_answer":"To use appropriate settings in development, testing, and production","explanation":"Separate configuration supports safer and more flexible deployments."},
        {"id":"cicd_019","skill":"CI/CD","topic":"Secrets","question":"Where should CI/CD credentials generally be stored?","options":["In a protected secret-management facility","Directly in public source code","In a screenshot committed to Git","In a publicly accessible log"],"correct_answer":"In a protected secret-management facility","explanation":"Protected secrets reduce the risk of credentials being exposed in repositories or logs."},
        {"id":"cicd_020","skill":"CI/CD","topic":"Security","question":"What is a least-privilege CI/CD permission policy?","options":["Give a workflow only the access it needs","Give every workflow full administrator access","Share one permanent token with everyone","Disable authentication for deployment"],"correct_answer":"Give a workflow only the access it needs","explanation":"Limited permissions reduce the damage that a compromised workflow could cause."},
        {"id":"cicd_021","skill":"CI/CD","topic":"Containers","question":"How can a container image help a CI/CD process?","options":["Package an application in a consistent deployable format","Guarantee the application has no bugs","Replace source control completely","Automatically approve all pull requests"],"correct_answer":"Package an application in a consistent deployable format","explanation":"Container images help keep application runtime dependencies consistent across environments."},
        {"id":"cicd_022","skill":"CI/CD","topic":"Container Registry","question":"What is a container registry used for?","options":["Storing and distributing container images","Running unit tests only","Managing DNS records","Writing application source code"],"correct_answer":"Storing and distributing container images","explanation":"Registries store versioned images that CI/CD pipelines and deployments can retrieve."},
        {"id":"cicd_023","skill":"CI/CD","topic":"Infrastructure as Code","question":"Why use Infrastructure as Code in delivery pipelines?","options":["To provision environments consistently and repeatably","To remove all infrastructure monitoring","To store credentials in source files","To avoid reviewing configuration changes"],"correct_answer":"To provision environments consistently and repeatably","explanation":"Infrastructure as Code makes infrastructure changes reviewable and automatable."},
        {"id":"cicd_024","skill":"CI/CD","topic":"Database Changes","question":"Why should database migrations be handled carefully during deployment?","options":["Application versions and schema changes must remain compatible","Migrations always delete all data","Database changes cannot be tested","CI pipelines cannot run SQL"],"correct_answer":"Application versions and schema changes must remain compatible","explanation":"Careful migration planning reduces failures when old and new application versions overlap."},
        {"id":"cicd_025","skill":"CI/CD","topic":"Testing","question":"What do unit tests generally verify?","options":["Small units of code in isolation","The entire production infrastructure only","User satisfaction across all regions","Cloud billing accuracy only"],"correct_answer":"Small units of code in isolation","explanation":"Unit tests check individual functions, classes, or components with controlled inputs."},
        {"id":"cicd_026","skill":"CI/CD","topic":"Testing","question":"What do integration tests verify?","options":["Interactions between components or services","Only the spelling in comments","Only a single isolated calculation","The monitor's physical condition"],"correct_answer":"Interactions between components or services","explanation":"Integration tests detect problems at component boundaries and in their interactions."},
        {"id":"cicd_027","skill":"CI/CD","topic":"Testing","question":"What is an end-to-end test?","options":["Testing a complete user or system workflow","Testing only a variable declaration","Testing only a CSS color","Checking the Git username"],"correct_answer":"Testing a complete user or system workflow","explanation":"End-to-end tests exercise integrated behavior through important application paths."},
        {"id":"cicd_028","skill":"CI/CD","topic":"Pipeline Reliability","question":"What is a flaky test?","options":["A test that sometimes passes and sometimes fails under similar conditions","A test that always passes correctly","A deployment artifact","A type of cloud server"],"correct_answer":"A test that sometimes passes and sometimes fails under similar conditions","explanation":"Flaky tests produce inconsistent results and reduce trust in pipeline feedback."},
        {"id":"cicd_029","skill":"CI/CD","topic":"Pipeline Reliability","question":"What should happen when a required CI test fails?","options":["The pipeline should report failure and block the protected release path","The failure should always be hidden","The test results should be deleted","The application should be deployed without review"],"correct_answer":"The pipeline should report failure and block the protected release path","explanation":"Required checks prevent known failures from proceeding through protected release stages."},
        {"id":"cicd_030","skill":"CI/CD","topic":"Automation","question":"What is a pipeline trigger?","options":["An event that starts a workflow","A database field","A compiled executable only","A production password"],"correct_answer":"An event that starts a workflow","explanation":"Triggers may include code pushes, pull requests, schedules, or manual requests."},
        {"id":"cicd_031","skill":"CI/CD","topic":"Parallelization","question":"Why run independent pipeline jobs in parallel?","options":["To reduce total workflow duration","To guarantee that jobs cannot fail","To remove the need for dependencies","To make artifacts untraceable"],"correct_answer":"To reduce total workflow duration","explanation":"Independent jobs can run concurrently when resources and dependencies permit."},
        {"id":"cicd_032","skill":"CI/CD","topic":"Caching","question":"What is dependency caching used for in CI?","options":["Reusing downloaded dependencies to speed up repeated builds","Keeping every dependency permanently up to date","Replacing automated tests","Publishing secrets in logs"],"correct_answer":"Reusing downloaded dependencies to speed up repeated builds","explanation":"Caching can reduce repeated downloads, provided cache keys and invalidation are handled correctly."},
        {"id":"cicd_033","skill":"CI/CD","topic":"Observability","question":"Why collect deployment metrics and logs?","options":["To identify release problems and investigate failures","To guarantee no future outages","To replace all tests","To make every deployment manual"],"correct_answer":"To identify release problems and investigate failures","explanation":"Observability helps teams detect problems and understand system behavior after release."},
        {"id":"cicd_034","skill":"CI/CD","topic":"Quality Gates","question":"What is a quality gate in a pipeline?","options":["A condition that must pass before proceeding","A physical security gate","A Git branch name","A deployment password"],"correct_answer":"A condition that must pass before proceeding","explanation":"Quality gates can enforce tests, coverage thresholds, security checks, or approvals."},
        {"id":"cicd_035","skill":"CI/CD","topic":"Supply Chain Security","question":"Why scan dependencies for known vulnerabilities?","options":["To identify risky third-party components","To guarantee every dependency is safe forever","To increase package download size","To remove the need for updates"],"correct_answer":"To identify risky third-party components","explanation":"Dependency scanning helps identify known vulnerabilities that may require updates or mitigations."},
        {"id":"cicd_036","skill":"CI/CD","topic":"Supply Chain Security","question":"What is artifact signing used for?","options":["Helping verify an artifact's origin and integrity","Making source code execute faster","Replacing every unit test","Automatically fixing vulnerabilities"],"correct_answer":"Helping verify an artifact's origin and integrity","explanation":"Digital signatures can help verify that an artifact came from a trusted signer and was not altered."},
        {"id":"cicd_037","skill":"CI/CD","topic":"Release Management","question":"Why use semantic versioning for releases?","options":["To communicate compatibility changes through version numbers","To determine the CPU temperature","To assign random passwords","To replace source control"],"correct_answer":"To communicate compatibility changes through version numbers","explanation":"Semantic versioning uses major, minor, and patch components to communicate intended change types."},
        {"id":"cicd_038","skill":"CI/CD","topic":"Workflow Configuration","question":"Why pin action or tool versions in a pipeline?","options":["To reduce unexpected changes from moving versions","To guarantee the tool has no vulnerabilities","To avoid all maintenance","To make every build slower"],"correct_answer":"To reduce unexpected changes from moving versions","explanation":"Pinned versions improve reproducibility, though they still need security updates."},
        {"id":"cicd_039","skill":"CI/CD","topic":"Performance","question":"Which metric can indicate a slow CI/CD process?","options":["Time from code change to successful delivery","Number of keyboard keys","Website background color","Number of developer monitors"],"correct_answer":"Time from code change to successful delivery","explanation":"Lead time for changes measures how long changes take to reach delivery."},
        {"id":"cicd_040","skill":"CI/CD","topic":"Best Practices","question":"What is a strong CI/CD practice?","options":["Automate checks, protect secrets, and make releases traceable","Deploy untested changes directly to production","Store credentials in public repositories","Ignore failed pipeline stages"],"correct_answer":"Automate checks, protect secrets, and make releases traceable","explanation":"Reliable delivery combines automation, security, testing, and clear release records."}
    ],
    "data engineering": [
        {"id":"dataeng_001","skill":"Data Engineering","topic":"Fundamentals","question":"What is data engineering mainly concerned with?","options":["Building systems that collect, transform, and deliver data","Designing only website colors","Writing only operating system drivers","Creating presentation slides only"],"correct_answer":"Building systems that collect, transform, and deliver data","explanation":"Data engineering creates reliable pipelines and infrastructure for useful data access."},
        {"id":"dataeng_002","skill":"Data Engineering","topic":"Pipelines","question":"What is a data pipeline?","options":["A sequence of steps that moves or transforms data","A physical water pipe","A programming language","A network firewall rule"],"correct_answer":"A sequence of steps that moves or transforms data","explanation":"Data pipelines collect, process, and deliver data between systems."},
        {"id":"dataeng_003","skill":"Data Engineering","topic":"ETL","question":"What does ETL stand for?","options":["Extract, Transform, Load","Evaluate, Test, Launch","Encode, Transfer, Link","Enter, Track, List"],"correct_answer":"Extract, Transform, Load","explanation":"ETL extracts data, transforms it, and then loads it into a target system."},
        {"id":"dataeng_004","skill":"Data Engineering","topic":"ELT","question":"How does ELT differ from traditional ETL?","options":["It loads extracted data before transforming it in the target environment","It never extracts data","It only transforms images","It replaces data storage with a browser"],"correct_answer":"It loads extracted data before transforming it in the target environment","explanation":"ELT uses the target platform for transformations after data has been loaded."},
        {"id":"dataeng_005","skill":"Data Engineering","topic":"Data Sources","question":"What is structured data?","options":["Data organized according to a defined schema","Data with no recognizable organization at all","Only audio recordings","Only executable programs"],"correct_answer":"Data organized according to a defined schema","explanation":"Structured data commonly uses defined fields, types, and relationships."},
        {"id":"dataeng_006","skill":"Data Engineering","topic":"Data Sources","question":"What is semi-structured data?","options":["Data with organizational markers but a flexible schema","Data that can never be parsed","Only relational database tables","Data that contains no fields"],"correct_answer":"Data with organizational markers but a flexible schema","explanation":"Formats such as JSON and XML include structure without requiring a fixed relational schema."},
        {"id":"dataeng_007","skill":"Data Engineering","topic":"File Formats","question":"What is JSON commonly used for in data pipelines?","options":["Representing structured or semi-structured data","Storing only machine instructions","Replacing every network protocol","Defining physical CPU components"],"correct_answer":"Representing structured or semi-structured data","explanation":"JSON represents objects, arrays, and primitive values in a text-based format."},
        {"id":"dataeng_008","skill":"Data Engineering","topic":"File Formats","question":"Why is Parquet often used for analytical data?","options":["It is a column-oriented format suited to analytical queries","It is only an image format","It stores only passwords","It cannot store typed values"],"correct_answer":"It is a column-oriented format suited to analytical queries","explanation":"Columnar storage can improve analytical scans and compression for supported workloads."},
        {"id":"dataeng_009","skill":"Data Engineering","topic":"File Formats","question":"What is a common advantage of CSV?","options":["It is a simple text format for tabular data","It automatically enforces every data type","It stores executable code only","It always compresses better than columnar formats"],"correct_answer":"It is a simple text format for tabular data","explanation":"CSV is easy to exchange, though data types and complex values require careful handling."},
        {"id":"dataeng_010","skill":"Data Engineering","topic":"Data Warehousing","question":"What is a data warehouse designed for?","options":["Storing integrated data for analysis and reporting","Running only video games","Managing keyboard input","Replacing all application code"],"correct_answer":"Storing integrated data for analysis and reporting","explanation":"Data warehouses organize data for analytical queries and business intelligence."},
        {"id":"dataeng_011","skill":"Data Engineering","topic":"Data Lakes","question":"What is a data lake?","options":["A repository for large amounts of data in varied formats","A relational table with only one row","A tool for styling web pages","A physical computer component"],"correct_answer":"A repository for large amounts of data in varied formats","explanation":"Data lakes can store raw and processed data in multiple formats."},
        {"id":"dataeng_012","skill":"Data Engineering","topic":"Lakehouse","question":"What is a data lakehouse architecture intended to combine?","options":["Data lake flexibility with warehouse-style management and analytics","A keyboard and a monitor","Two programming languages only","Only local file backups"],"correct_answer":"Data lake flexibility with warehouse-style management and analytics","explanation":"Lakehouse designs aim to support diverse data formats alongside reliability and analytical features."},
        {"id":"dataeng_013","skill":"Data Engineering","topic":"Batch Processing","question":"What is batch processing?","options":["Processing collected data in groups at intervals","Processing every event immediately in all cases","Writing source code without testing","Deleting records one by one manually"],"correct_answer":"Processing collected data in groups at intervals","explanation":"Batch workloads process accumulated records according to a schedule or trigger."},
        {"id":"dataeng_014","skill":"Data Engineering","topic":"Stream Processing","question":"What is stream processing?","options":["Processing events continuously as they arrive","Processing data only once per year","Storing only static documents","Converting all data to spreadsheets"],"correct_answer":"Processing events continuously as they arrive","explanation":"Stream processing handles ongoing event flows with low-latency processing goals."},
        {"id":"dataeng_015","skill":"Data Engineering","topic":"Batch vs Streaming","question":"When is stream processing useful?","options":["When recent events must be analyzed with low latency","When data is never updated","When only annual reports are needed","When the source has no events"],"correct_answer":"When recent events must be analyzed with low latency","explanation":"Streaming supports near-real-time use cases such as monitoring and event detection."},
        {"id":"dataeng_016","skill":"Data Engineering","topic":"Orchestration","question":"What does workflow orchestration manage?","options":["Task order, dependencies, scheduling, and retries","Only chart colors","Only user passwords","Only file extensions"],"correct_answer":"Task order, dependencies, scheduling, and retries","explanation":"Orchestration coordinates pipeline tasks and handles execution dependencies."},
        {"id":"dataeng_017","skill":"Data Engineering","topic":"Orchestration","question":"What is a DAG in workflow orchestration?","options":["A directed acyclic graph representing task dependencies","A database access gateway","A data archive generator","A deployment account group"],"correct_answer":"A directed acyclic graph representing task dependencies","explanation":"A DAG represents tasks and directed dependencies without cycles."},
        {"id":"dataeng_018","skill":"Data Engineering","topic":"Data Quality","question":"What is data validation?","options":["Checking data against expected rules or constraints","Encrypting all data automatically","Increasing file size","Creating a new server"],"correct_answer":"Checking data against expected rules or constraints","explanation":"Validation checks that incoming or transformed data meets defined requirements."},
        {"id":"dataeng_019","skill":"Data Engineering","topic":"Data Quality","question":"What is a null value commonly used to represent?","options":["Missing or unknown information","A guaranteed zero","A valid password","A database server"],"correct_answer":"Missing or unknown information","explanation":"Null generally indicates absent or unknown data and should be handled deliberately."},
        {"id":"dataeng_020","skill":"Data Engineering","topic":"Data Cleaning","question":"Why remove duplicate records when appropriate?","options":["To avoid counting the same logical record multiple times","To guarantee every value is accurate","To remove all historical data","To increase missing values"],"correct_answer":"To avoid counting the same logical record multiple times","explanation":"Deduplication prevents duplicate records from distorting downstream analysis."},
        {"id":"dataeng_021","skill":"Data Engineering","topic":"Schema","question":"What is a data schema?","options":["A description of data fields, types, and structure","A list of computer brands","A type of CPU cache","A chart color palette"],"correct_answer":"A description of data fields, types, and structure","explanation":"Schemas describe the expected structure and interpretation of data."},
        {"id":"dataeng_022","skill":"Data Engineering","topic":"Schema Evolution","question":"What is schema evolution?","options":["Managing changes to data structure over time","Increasing the size of a computer screen","Deleting all old records automatically","Converting every file to an image"],"correct_answer":"Managing changes to data structure over time","explanation":"Schema evolution handles additions or changes while considering compatibility with existing consumers."},
        {"id":"dataeng_023","skill":"Data Engineering","topic":"Database Design","question":"What is normalization in relational database design intended to reduce?","options":["Unnecessary duplication and update anomalies","Network security","The number of valid records to zero","The need for all data types"],"correct_answer":"Unnecessary duplication and update anomalies","explanation":"Normalization organizes related data to reduce redundancy and inconsistencies."},
        {"id":"dataeng_024","skill":"Data Engineering","topic":"Analytics Modeling","question":"What is a fact table commonly used for in dimensional modeling?","options":["Storing measurable events and related dimension keys","Storing only application source code","Managing cloud permissions","Keeping only user interface styles"],"correct_answer":"Storing measurable events and related dimension keys","explanation":"Fact tables commonly contain measures and foreign keys to descriptive dimensions."},
        {"id":"dataeng_025","skill":"Data Engineering","topic":"Analytics Modeling","question":"What does a dimension table usually contain?","options":["Descriptive attributes used to analyze facts","Only server logs in binary form","Only application passwords","Only executable instructions"],"correct_answer":"Descriptive attributes used to analyze facts","explanation":"Dimension tables describe entities such as customers, products, dates, or locations."},
        {"id":"dataeng_026","skill":"Data Engineering","topic":"Data Modeling","question":"What is a star schema?","options":["A fact table connected to dimension tables","A single unstructured text file only","A type of computer network cable","A machine learning activation"],"correct_answer":"A fact table connected to dimension tables","explanation":"Star schemas organize analytical data around a central fact table and related dimensions."},
        {"id":"dataeng_027","skill":"Data Engineering","topic":"Distributed Processing","question":"Why distribute data processing across multiple machines?","options":["To handle larger workloads or improve processing capacity","To guarantee no component can fail","To eliminate network communication","To avoid dividing work"],"correct_answer":"To handle larger workloads or improve processing capacity","explanation":"Distributed processing can increase throughput and capacity for workloads that can be partitioned."},
        {"id":"dataeng_028","skill":"Data Engineering","topic":"Distributed Processing","question":"What is partitioning in data processing?","options":["Dividing data into smaller sections for storage or processing","Encrypting every record with the same password","Deleting the entire dataset","Changing the programming language"],"correct_answer":"Dividing data into smaller sections for storage or processing","explanation":"Partitioning can improve parallelism and help queries scan only relevant data."},
        {"id":"dataeng_029","skill":"Data Engineering","topic":"Distributed Processing","question":"What is data skew?","options":["Uneven distribution of data or work across partitions","A perfectly balanced workload","A database backup format","A method for naming variables"],"correct_answer":"Uneven distribution of data or work across partitions","explanation":"Skew can cause some tasks to take much longer than others."},
        {"id":"dataeng_030","skill":"Data Engineering","topic":"Incremental Processing","question":"What is incremental data loading?","options":["Loading only new or changed records since a previous run","Reloading the entire dataset every time","Deleting new records before loading","Converting every row to a string"],"correct_answer":"Loading only new or changed records since a previous run","explanation":"Incremental loading can reduce processing time and resource use for large datasets."},
        {"id":"dataeng_031","skill":"Data Engineering","topic":"Change Data Capture","question":"What is Change Data Capture (CDC)?","options":["Detecting and delivering database changes to downstream systems","Creating screenshots of source code","Changing every database password daily","Removing all updated records"],"correct_answer":"Detecting and delivering database changes to downstream systems","explanation":"CDC tracks inserts, updates, and deletes so other systems can stay synchronized."},
        {"id":"dataeng_032","skill":"Data Engineering","topic":"Reliability","question":"What is an idempotent pipeline operation?","options":["Repeating it with the same input has the same intended result","Every repeated run creates duplicate records","It can only run once ever","It always changes every record"],"correct_answer":"Repeating it with the same input has the same intended result","explanation":"Idempotency helps retries avoid unintended duplicate effects."},
        {"id":"dataeng_033","skill":"Data Engineering","topic":"Reliability","question":"Why are retries used in data pipelines?","options":["To recover from temporary failures","To hide every data quality issue","To guarantee every source is correct","To remove the need for monitoring"],"correct_answer":"To recover from temporary failures","explanation":"Retries can recover from transient errors, ideally with limits and appropriate backoff."},
        {"id":"dataeng_034","skill":"Data Engineering","topic":"Monitoring","question":"What should a data pipeline monitor?","options":["Failures, processing duration, record counts, and data quality","Only the developer's name","Only the user interface theme","Only the number of source files"],"correct_answer":"Failures, processing duration, record counts, and data quality","explanation":"Monitoring helps detect operational problems and unexpected changes in data."},
        {"id":"dataeng_035","skill":"Data Engineering","topic":"Security","question":"Why protect sensitive data in a data pipeline?","options":["To prevent unauthorized access or disclosure","To make all datasets public","To remove data validation","To increase duplicate records"],"correct_answer":"To prevent unauthorized access or disclosure","explanation":"Access controls, encryption, and data minimization help protect sensitive information."},
        {"id":"dataeng_036","skill":"Data Engineering","topic":"Privacy","question":"What is data minimization?","options":["Collecting and retaining only data needed for a purpose","Collecting every possible personal detail","Making all datasets permanent","Removing all access controls"],"correct_answer":"Collecting and retaining only data needed for a purpose","explanation":"Data minimization reduces privacy risk by limiting unnecessary data collection and retention."},
        {"id":"dataeng_037","skill":"Data Engineering","topic":"Performance","question":"Why use column pruning in analytical queries?","options":["To read only the columns needed by the query","To delete all table columns","To increase the number of duplicate rows","To disable query optimization"],"correct_answer":"To read only the columns needed by the query","explanation":"Reading fewer columns can reduce I/O and improve analytical query efficiency."},
        {"id":"dataeng_038","skill":"Data Engineering","topic":"Performance","question":"What is predicate pushdown?","options":["Applying eligible filters closer to the data source","Moving all data to a browser first","Deleting every filter from a query","Converting a database into an image"],"correct_answer":"Applying eligible filters closer to the data source","explanation":"Predicate pushdown reduces unnecessary data transfer by filtering earlier when supported."},
        {"id":"dataeng_039","skill":"Data Engineering","topic":"Data Governance","question":"What is data lineage?","options":["Tracking where data came from and how it was transformed","Tracking keyboard usage","Recording only cloud billing totals","Naming database columns alphabetically"],"correct_answer":"Tracking where data came from and how it was transformed","explanation":"Lineage helps trace data origins, transformations, and downstream dependencies."},
        {"id":"dataeng_040","skill":"Data Engineering","topic":"Best Practices","question":"What is a good data engineering practice?","options":["Build observable, tested, secure, and recoverable pipelines","Ignore schema changes","Store secrets in public files","Assume every input dataset is correct"],"correct_answer":"Build observable, tested, secure, and recoverable pipelines","explanation":"Reliable pipelines combine validation, monitoring, access control, and recovery planning."}
    ],
}
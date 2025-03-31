Variables are the containers for storing the data values or you can also call it a memory location name for the data. Every variable has a:

- Data Type – The kind of data that it can hold. For example, int, string, float, char, etc.
- Variable Name – To identify the variable uniquely within the scope.
- Value – The data assigned to the variable.


![[Pasted image 20250331231122.png]]



From the image, it can be easily perceived that while declaring a variable, we need to take care of two things that are:

1. Datatype: In Java, a data type define the type of data that a variable can hold. 
2. data_name: Name was given to the variable.


**Types of Java Variables**
![[Pasted image 20250331231229.png]]

1. Local Variables : Defined within a block or method or constructor 
	- Local Variable is created at the time of declaration and destroyed after exiting from the block
	- The scope if these variables exists only within the block in which the variables are declared.
2. Instance Variables : These are non-static variables and declared in a class outside the method, constructor or block.
	-  when an object of the class is created and destroyed when the object is destroyed.
	- If we do not specify any access specifier, then the default access specifier will be used.
3. Static Variables : well known as Class Variables.
	- These variables are declared similarly to instance variables. The difference is that static variables are declared using the static keyword within a class outside of any method, constructor, or block.
	- Static variables are created at the start of program execution and destroyed automatically when execution ends.



Up Next - [[Java Operators]]

The most common way to take user input in Java is using Scanner class which is part of 
java.util.package.

Follow these steps to take user input using Scanner class:

- Import the Scanner class using _import java.util.Scanner;
- Create the Scanner object  and connect Scanner with System.in by passing it as an argument i.e. _Scanner scn = new Scanner(System.in);
- Print a message to prompt for user input and you can use the various methods of Scanner class like nextInt(), nextLine(), next(), nextDouble etc according to your need.


| Method                                                                                                   | Description                     |
| -------------------------------------------------------------------------------------------------------- | ------------------------------- |
| [****nextBoolean()****](https://www.geeksforgeeks.org/scanner-nextboolean-method-in-java-with-examples/) | Used for reading Boolean value. |
| [****nextByte()****](https://www.geeksforgeeks.org/scanner-nextbyte-method-in-java-with-examples/)       | Used for reading Byte value.    |
| [****nextDouble()****](https://www.geeksforgeeks.org/scanner-nextdouble-method-in-java-with-examples/)   | Used for reading Double value.  |
| [****nextFloat()****](https://www.geeksforgeeks.org/scanner-nextfloat-method-in-java-with-examples/)     | Used for reading Float value.   |
| [****nextInt()****](https://www.geeksforgeeks.org/scanner-nextint-method-in-java-with-examples/)         | Used for reading Int value.     |
| [****nextLine()****](https://www.geeksforgeeks.org/scanner-nextline-method-in-java-with-examples/)       | Used for reading Line value.    |
| [****nextLong()****](https://www.geeksforgeeks.org/scanner-nextlong-method-in-java-with-examples/)       | Used for reading Long value.    |
| [****nextShort()****](https://www.geeksforgeeks.org/scanner-nextshort-method-in-java-with-examples/)     | Used for reading Short value.   |


BufferedReader vs Scanner Class

| Aspects            | `BufferedReader`                                 | `Scanner`                                                          |
| ------------------ | ------------------------------------------------ | ------------------------------------------------------------------ |
| Primary Use        | Efficient reading of character streams.          | Reading formatted input (e.g., integers, strings).                 |
| Speed              | Faster for large input as it does less parsing.  | Slower due to parsing overhead (e.g., `nextInt()`, `nextFloat()`). |
| Exception Handling | Throws checked exceptions (e.g., `IOException`). | No checked exceptions; easier to use.                              |
| Flexibility        | Allows reading larger input efficiently.         | Best suited for reading simple data types.                         |
| Thread Safety      | Synchronized, making it thread-safe.             | Not thread-safe by default.                                        |
| Common Use         | Used for reading large input efficiently.        | Commonly used for smaller, formatted input.                        |
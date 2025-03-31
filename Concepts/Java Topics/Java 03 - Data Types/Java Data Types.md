Java is statically typed and also a strongly data(such as integer , character, hexadecimal . packed decimal, and so forth)
- Data types in java are of different sizes and values that can be stored in a variable 

**Why Data type Matters in Java?**
- Memory Efficiency 
- Performance
- Code Clarity

**Java Data Type Categories**
- Primitive Data Type: These are the basic building blocks that store simple values directly in memory. Examples of primitive data types are boolean, char, byte, short, int, long, float, and double.****
- Non-Primitive Data Types (Object Types): These are reference types that store memory addresses of objects. Examples of Non-primitive data types are String, Array, Class, Interface, and Object

| Aspect  | Primitive                       | Non-Primitive                       |
| ------- | ------------------------------- | ----------------------------------- |
| Memory  | Stored on the stack             | Stored on heap                      |
| Speed   | Primitive data types are faster | Non-Primitive data types are slower |
| Example | int x = 5;                      | String s = "Greeks";                |


```
import java.io.*;

class GFG{
	public static void main (String[] args)
	{
		int a = 10;
		int b = 20;
		System.out.println(a+b);
	}
}
```


![[Java-Data-Types-1024.png]]

**Primitive Data Types in Java**

|Type|Description|Default|Size|Example Literals|Range of values|
|---|---|---|---|---|---|
|boolean|true or false|false|JVM-dependent (typically 1 byte)|true, false|true, false|
|byte|8-bit signed integer|0|1 byte|(none)|-128 to 127|
|char|Unicode character(16 bit)|\u0000|2 bytes|‘a’, ‘\u0041’, ‘\101’, ‘\\’, ‘\’, ‘\n’, ‘β’|0 to 65,535 (unsigned)|
|short|16-bit signed integer|0|2 bytes|(none)|-32,768 to 32,767|
|int|32-bit signed integer|0|4 bytes|-2,0,1|-2,147,483,648<br><br>to<br><br>2,147,483,647|
|long|64-bit signed integer|0L|8 bytes|-2L,0L,1L|-9,223,372,036,854,775,808<br><br>to<br><br>9,223,372,036,854,775,807|
|float|32-bit IEEE 754 floating-point|0.0f|4 bytes|3.14f, -1.23e-10f|~6-7 significant decimal digits|
|double|64-bit IEEE 754 floating-point|0.0d|8 bytes|


**Non-Primitive Data Types (Reference) **

- String
- Class
- Object
- Interface
- Array




up next - [[Java Variables]]

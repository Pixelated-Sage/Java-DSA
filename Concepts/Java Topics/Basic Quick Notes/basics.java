import java.util.Scanner;

public class basics {
    String name;
    int age;

    public basics(String name, int age){
        this.name = name;
        this.age= age;
    }

    public void introduce(){
        System.out.println("My name is "+name+" and I am "+age+" years old");
    }
    public static void main(String[] args) {


        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number");
        int input = scanner.nextInt();
        System.out.println("Enter a string");
        String line = scanner.nextLine();
        scanner.close();
        System.out.println(input);
        System.out.println(line);



        basics person1 = new basics("abhi",19);
        person1.introduce();


        int[] numbers = {5,3,5,7,8,9,2,1,4,6};

        //print all elements of an array
        for (int i = 0;i<numbers.length;i++){
            System.out.println(numbers[i]);
        }
        System.out.println(" ");

        //Find the max number
        int max = numbers[0];
        for (int i = 0; i<numbers.length;i++){
            if (numbers[i]>max){
                max = numbers[i];
            }
        }   
        System.out.println("Max number is "+max);


    }
}

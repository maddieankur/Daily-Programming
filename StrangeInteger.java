/*
Question : Input : Integer a
you must find a least number that contain 9 or 0 , that are divided by integer a

Example: 5
Output : 90

Bruteforce : Just go through Question
Efficient Solution: You Have Always 2 choice 9 or 0
                    0 can not be leading So start with 9 Then 90 or 99
                    The 900 909 990 999
                    So recursive Solution can be made


*/


import java.util.Scanner;
import java.lang.Math;

public class MyClass {
    static boolean isValid(int a){
        while(a>0){
            int tmp = a%10;
            if(tmp == 9 || tmp == 0){
                a = a;
            }
            else{
                return false;
            }
            a/=10;
        }
        return true;
    }
    public static void main(String args[]) {
      int a;
      Scanner sc = new Scanner(System.in);
      a = sc.nextInt();
      int i = 1;
      int ans;
      while(true){
          int tmp = a*i;
          if (isValid(tmp)){
              ans = tmp;
              break;
          }
          i++;
      }
      System.out.println(ans);  
    }
}

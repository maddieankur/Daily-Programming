/*
Question is Asked in MAQ Software Software Engineering Test
You have a string A, There are a reverse String B. 
Print Valid if |A[i]-A[i-1]| == |B[i]-B[i-1|
BruteForce Solution:
  Just Go through the Sting 

Efficient Solution:
  Go half the Original String A , And check for condition : A[i+1] -A[i] == A[n-i-1] == A[n-i]

*/


import java.util.Scanner;
import java.lang.Math;

public class MyClass {
    public static void main(String args[]) {
      String s,sr="";
      Scanner sc = new Scanner(System.in);
      s = sc.nextLine();
      for(int i = s.length()-1;i>=0;i--){
          sr+=s.charAt(i);
      }
      int flag = 0;
      for(int i = 1;i<s.length();i++){
          if(Math.abs(s.charAt(i)-s.charAt(i-1)) != Math.abs(sr.charAt(i)-s.charAt(i-1)) ){
              flag = 1;
          }
      }
      if (flag == 1){
        System.out.println("Invalid");  
      }
      else{
        System.out.println("Valid");
      }
    }
}

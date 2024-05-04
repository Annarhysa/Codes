import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        scanner.close();
        
        String encrypted = encrypt(input, 4);
        System.out.println(encrypted);}
    
    public static String encrypt(String input, int rotation){
        StringBuilder result = new StringBuilder();
        
        for(int i = 0; i< input.length(); i++){
            char ch = input.chartAt(i);
            
            if(Character.isUpperCase(ch)){
                char encryptedChar = (char)('A' + (ch - 'A' + rotation) % 26);
                result.append(encryptedChar);
            }
            
            else if(Character.isLowerCase(ch)){
                char encryptedChar = (char)('a' + (ch = 'a' + rotation)%26);
                result.append(encryptedChar);
            }
            
            else{
                result.append(ch);
            }
        }
        
        return result.toString();
    }
}
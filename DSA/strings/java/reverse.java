import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str = input.nextLine(); // Input string
        String reversed = reverseString(str); // Calling method to reverse the string
        System.out.println(reversed); // Printing the reversed string
    }
    
    public static String reverseString(String str) {
        char[] chars = str.toCharArray(); // Convert string to character array
        int left = 0, right = chars.length - 1;
        
        // Iterate through the string from both ends
        while (left < right) {
            // Skip non-alphabetic characters
            while (left < right && !Character.isLetter(chars[left])) {
                left++;
            }
            while (left < right && !Character.isLetter(chars[right])) {
                right--;
            }
            
            // Swap alphabetic characters
            if (left < right) {
                char temp = chars[left];
                chars[left] = chars[right];
                chars[right] = temp;
                left++;
                right--;
            }
        }
        
        return new String(chars); // Convert character array back to string
    }
}
                                                                                                                            
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String[] elements = input.nextLine().split(" ");
        
        // Convert string elements to integer array
        int[] arr = new int[elements.length];
        for (int i = 0; i < elements.length; i++) {
            arr[i] = Integer.parseInt(elements[i]);
        }
        
        int result = lastRemainingElement(arr);
        System.out.println(result);
    }
    
    public static int lastRemainingElement(int[] arr) {
        // Check if array contains negative values
        for (int num : arr) {
            if (num < 0) {
                System.out.println("Array should only contain positive values");
                return -1;
            }
        }
        
        // Perform series of rotations and deletions
        for (int i = 0; i < arr.length - 1; i++) {
            int last = arr[arr.length - 1];
            for (int j = arr.length - 1; j > 0; j--) {
                arr[j] = arr[j - 1];
            }
            arr[0] = last;
            
            // Remove last element
            int[] newArr = new int[arr.length - 1];
            System.arraycopy(arr, 0, newArr, 0, newArr.length);
            arr = newArr;
        }
        
        return arr[0];
    }
}
                                                                                                                            
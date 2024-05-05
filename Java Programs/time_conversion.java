import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String time = input.nextLine(); // Input time in 12-hour format
        String militaryTime = convertToMilitary(time); // Calling method to convert to military time
        System.out.println(militaryTime); // Printing the converted military time
    }
    
    public static String convertToMilitary(String time) {
        String[] parts = time.split(":"); // Splitting the time string into hours, minutes, and seconds
        int hours = Integer.parseInt(parts[0]); // Parsing hours from string to integer
        String minutes = parts[1]; // Minutes remain the same
        String secondsAndPeriod = parts[2]; // Seconds and AM/PM period
        
        // Checking if the time is PM and not 12:00:00 PM
        if (time.contains("PM") && hours != 12) {
            hours += 12; // Adding 12 hours to convert to military time
        }
        
        // Checking if the time is AM and it's 12:00:00 AM
        if (time.contains("AM") && hours == 12) {
            hours = 0; // Converting 12:00:00 AM to 00:00:00
        }
        
        // Formatting the military time string
        String militaryTime = String.format("%02d:%s:%s", hours, minutes, secondsAndPeriod.substring(0, 2));
        return militaryTime; // Returning the converted military time
    }
}
                                                                                                                            
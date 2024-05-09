import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        TimeTravelersArchive archive = new TimeTravelersArchive();

        while (input.hasNextLine()) {
            String line = input.nextLine();
            String[] parts = line.split(" ");

            if (parts.length == 0) {
                continue; // skip empty lines
            }

            String command = parts[0];

            if ("Store".equalsIgnoreCase(command) && parts.length == 4) {
                String key = parts[1];
                String value = parts[2];
                int timestamp;

                try {
                    timestamp = Integer.parseInt(parts[3]);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid timestamp");
                    continue;
                }

                archive.Store(key, value, timestamp);
            } else if ("Retrieve".equalsIgnoreCase(command) && parts.length == 3) {
                String key = parts[1];
                int timestamp;

                try {
                    timestamp = Integer.parseInt(parts[2]);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid timestamp");
                    continue;
                }

                System.out.println(archive.Retrieve(key, timestamp));
            } else {
                System.out.println("Wrong method called, please call Store or Retrieve method");
            }
        }
    }

    public static int doSomething(int x, int y) {
        return x + y; // simple placeholder
    }

    static class TimeTravelersArchive {
        private Map<String, TreeMap<Integer, String>> archive;

        public TimeTravelersArchive() {
            archive = new HashMap<>();
        }

        public void Store(String key, String value, int timestamp) {
            if (!archive.containsKey(key)) {
                archive.put(key, new TreeMap<>());
            }
            archive.get(key).put(timestamp, value);
        }

        public String Retrieve(String key, int timestamp) {
            if (!archive.containsKey(key)) {
                return "empty";
            }

            TreeMap<Integer, String> timeMap = archive.get(key);
            Map.Entry<Integer, String> entry = timeMap.floorEntry(timestamp);

            if (entry == null) {
                return "empty"; 
            }

            return entry.getValue();
        }
    }
}

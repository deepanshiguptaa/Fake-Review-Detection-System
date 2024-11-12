import java.io.FileOutputStream;
import java.io.IOException;

public class byte1 {

    public static void main(String[] args) {
        byte[] data = { 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100 }; // Bytes representing "Hello World"

        try (FileOutputStream fos = new FileOutputStream("output.txt")) {
            fos.write(data);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }
}

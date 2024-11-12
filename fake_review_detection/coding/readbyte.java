import java.io.FileInputStream;
import java.io.IOException;

public class readbyte {
    public static void main(String[] args) {
        String fileName = "Read.txt"; 
      try (FileInputStream by = new FileInputStream(fileName)) {
            int byteData;
            while ((byteData = by.read()) != -1) {
                System.out.print((char) byteData);
            }
        System.out.println("\n Data is read.");
        } 
        
        catch (IOException e) {
            System.err.println("Data can't be readed " + e.getMessage());
        }
    }
}

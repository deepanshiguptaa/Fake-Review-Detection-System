import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
public class CopyFiles {
   public static void main(String[] args) throws IOException {
      //Creating a File object to hold the source file
      File source = new File("Read.txt");
      //Creating a File object to hold the destination file
      File destination = new File("Write.txt");
      //Creating an FileInputStream object
      FileInputStream inputStream = new FileInputStream(source);
      //Creating an FileOutputStream object
      FileOutputStream outputStream = new FileOutputStream(destination);
      //Creating a buffer to hold the data
      int length = (int) source.length();
      byte[] buffer = new byte[length];
      while ((length = inputStream.read(buffer)) > 0) {
         outputStream.write(buffer, 0, length);
      }
      inputStream.close();
      outputStream.close();
      System.out.println("File copied successfully.......");
   }
}
import java.io.IOException;   
import java.io.RandomAccessFile;

public class RandomAccessFileExample {  
    static final String FILEPATH = "C:\\coding\\myFile.txt"; 

    public static void main(String[] args) {  
        try {  
            System.out.println(new String(readFromFile(FILEPATH, 0, 18)));  
            writeToFile(FILEPATH, "I love my country and my people", 31);  
        } 
        catch (IOException e) {  
            e.printStackTrace();  
        }  
    }  

    private static byte[] readFromFile(String filePath, int position, int size) throws IOException {  
        RandomAccessFile file = new RandomAccessFile(filePath, "r");  
        file.seek(position);  
        byte[] bytes = new byte[size];  
        int bytesRead = file.read(bytes);  // Read bytes and check how many were read
        file.close();  
        
        if (bytesRead < size) {
            // Handle the case where fewer bytes were read
            byte[] actualBytes = new byte[bytesRead];
            System.arraycopy(bytes, 0, actualBytes, 0, bytesRead);
            return actualBytes;
        }
        return bytes;  
    }  

    private static void writeToFile(String filePath, String data, int position) throws IOException {  
        RandomAccessFile file = new RandomAccessFile(filePath, "rw");  
        file.seek(position);  
        file.write(data.getBytes());  
        file.close();
    }
}

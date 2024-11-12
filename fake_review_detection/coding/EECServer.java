//Server side                  
import java.io.*;
import java.net.*;
class EECServer{
    public static void main(String args[]) throws IOException{
        ServerSocket ss=new ServerSocket(51981);
        Socket s= ss.accept();
        DataInputStream dis= new DataInputStream(s.getInputStream());
        String str= (String) dis.readUTF();
        System.out.println(str);
        ss.close();
    }
}
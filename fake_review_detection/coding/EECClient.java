// Client Side                       
import java.io.*;                                                                 
import java.net.*;
class EECClient{
public static void main(String args[]) throws Exception{
    Socket s= new Socket("localhost", 51981);
    DataOutputStream dout= new DataOutputStream(s.getOutputStream());
    dout.writeUTF("I am fine");
    dout.writeUTF("What about u");
    dout.flush();
    dout.close();
    s.close();
    }
}
import java.net.*;
class InetDemo{
    public static void main(String args[]){
        try{
            InetAddress ip=InetAddress.getByName("www.google.co.in");
            System.out.println(ip.getHostName());
            System.out.println(ip.getHostAddress());
        }
        catch(Exception e){
        }
    }
}
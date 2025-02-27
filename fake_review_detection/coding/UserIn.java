import java.awt.*;  
import java.awt.event.*; 
public class UserIn extends Frame {             
    TextField tf1;             
    TextField tf2;             
    Label l1;             
    Button b;
    UserIn() {                           
        setTitle("Adder");
        setLayout(null);  
        tf1 = new TextField();
        tf1.setBounds(100, 50, 85, 20);                           
        tf2 = new TextField();
        tf2.setBounds(100, 100, 85, 20);                           
        b = new Button("Add");
        b.setBounds(110, 220, 60, 40);                           
        l1 = new Label("");
        l1.setBounds(100, 150, 150, 20);  
        add(b);                           
        add(tf1);                           
        add(tf2);                           
        add(l1);                           
        setSize(300, 300);                           
        setVisible(true);         
        b.addActionListener(new ActionListener() {                
            
        public void actionPerformed(ActionEvent e) {                     
            try {
                int a = Integer.parseInt(tf1.getText());                     
                int b = Integer.parseInt(tf2.getText());                     
                int c = a + b;                     
                l1.setText("Their sum is = " + c);    
            } 
            catch (NumberFormatException ex) {
                l1.setText("Invalid input. Please enter numbers.");
            }                                   
        }        
    });                 
}             
    public static void main(String []args) {                    
        new UserIn();            
    } 
}

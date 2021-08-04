Scanner sc=new Scanner(System.in)
String new;
new=sc.nextLine();
int noint=Integer.parseInt(new);...........................convert str to int......its a integer now
Integer noint=Integer.parseInt(new);



 WRAPPER CLASS:
# CONVERT PRIMITIVE DATATYPE INTO OBJECTS.
# ITS AVAILABLE IN java.util package
# data structure is a collection framework ,such as ArrayList and Vector ,store only object  and not primitive types
# an object is needed to support synchronization in multithreading

STRING TO DATE:
    String s1="31/12/1200"
    Date d1=new SimpleDateFormat(pattern:"dd/MM/YYYY").parse(s1)
    d1
DATE TO STRING:
    Date d1=Calendar.getInstance().getTime();
    DateFormat df=new SimpleDateFormat(pattern:"YYYY-MM-dd hh:mm:ss");
    String s=dateFormat.format(df);
    s
///////////////////////////////////
1.DEC TO HEX/bin/octal:
     int n=12;
     Integer.toHexString(n);
2. octal/bin/hex to dec:
       String octnum="121"
       int deci=Integer.parseInt(octnum,radix:8);
       deci      
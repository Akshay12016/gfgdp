import java.util.Scanner;
import java.lang.String;
public class Editdistance{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String s1=sc.nextLine();
        String s2=sc.nextLine();
        System.out.println(ed(s1,s2,s1.length(),s2.length()));
        sc.close();
    }
    public static int min(int a,int b,int c){
        if(a<b&&a<c) return a;
        if(b<c) return b;
        return c;
    }
    public static int ed(String s1,String s2,int m,int n){
        if(m==0) return n;
        if(n==0) return m;
        if(s1.charAt(m-1)==s2.charAt(n-1)){
            return ed(s1,s2,m-1,n-1);
        }
        else{
            return 1+min(ed(s1,s2,m,n-1),ed(s1,s2,m-1,n),ed(s1,s2,m-1,n-1));
        }
    }
}
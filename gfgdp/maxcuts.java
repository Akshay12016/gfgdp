import java.util.Scanner;
public class maxcuts {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        System.out.println(maxcuts1(n,a,b,c));
        sc.close();
    }
    public static int max(int d,int e){
        if(d>e){return d;}
        return e;
    }
    public static int maxcuts1(int n,int a,int b,int c){
        if(n<0){return -1;}
        if(n==0){return 0;}
        int res=max(maxcuts1(n-a, a, b, c),max(maxcuts1(n-b, a, b, c),maxcuts1(n-c, a, b, c)));
        if(res==-1){return res;}
        else{return (res+1);}
    }
}

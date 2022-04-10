// //recursive function
// import java.util.Scanner;
// import java.lang.String;
// public class Editdistance{
//     public static void main(String args[]){
//         Scanner sc=new Scanner(System.in);
//         String s1=sc.nextLine();
//         String s2=sc.nextLine();
//         System.out.println(ed(s1,s2,s1.length(),s2.length()));
//         sc.close();
//     }
//     public static int min(int a,int b,int c){
//         if(a<b&&a<c) return a;
//         if(b<c) return b;
//         return c;
//     }
//     public static int ed(String s1,String s2,int m,int n){
//         if(m==0) return n;
//         if(n==0) return m;
//         if(s1.charAt(m-1)==s2.charAt(n-1)){
//             return ed(s1,s2,m-1,n-1);
//         }
//         else{
//             return 1+min(ed(s1,s2,m,n-1),ed(s1,s2,m-1,n),ed(s1,s2,m-1,n-1));
//         }
//     }
// }

//Tabulation method
import java.util.Scanner;
import java.lang.String;
public class Editdistance {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        int m=s1.length();
        int n=s2.length();
        int[][] memo = new int[m + 1][n + 1];
        for (int i = 0; i <=m; i++)
            memo[i][0] = i;
        for (int j = 0; j <=n; j++)
            memo[0][j] = j;
        for (int i = 1; i<=m; i++){
            for (int j = 1; j<=n; j++){
                if (s1.charAt(m - 1) == s2.charAt(n - 1))
                    memo[i][j] = memo[i - 1][j - 1];
                else
                    memo[i][j]=1+min(memo[i][j-1],min(memo[i-1][j],memo[i-1][j-1]));
                }
        }
        System.out.println(memo[m][n]);
        sc.close();
    }
    public static int min(int a, int b) {
        if (a < b)
            return a;
        return b;
    }
}


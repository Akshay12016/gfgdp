//recursive
// import java.util.*;
// import java.lang.String;
// public class lcs{
//     public static void main(String args[]){
//        Scanner sc=new Scanner(System.in);
//        String s1,s2;
//        s1=sc.nextLine();
//        s2=sc.nextLine();
//        System.out.println(lcsdp(s1,s2,s1.length(),s2.length()));
//        sc.close(); 
//     }
//     public static int max(int a,int b){
//         if(a>b){
//             return a;
//         }
//         return b;
//     }
//     public static int lcsdp(String s1,String s2,int m,int n){
//         if(m==0||n==0){
//             return 0;
//         }
//         if(s1.charAt(m-1)==s2.charAt(n-1)){
//             return 1+lcsdp(s1,s2,m-1,n-1);
//         }
//         else{
//             return max(lcsdp(s1,s2,m-1,n),lcsdp(s1,s2,m,n-1));
//         }
//     }
// }

// memoisation_dp
// import java.util.*;
// import java.lang.String;

// public class lcs {

//     public static void main(String args[]) {
//         Scanner sc = new Scanner(System.in);
//         String s1, s2;
//         s1 = sc.nextLine();
//         s2 = sc.nextLine();
//         int m=s1.length();
//         int n=s2.length();
//         int[][] memo = new int[m+1][n + 1];
//         for(int i=0;i<m+1;i++)
//             for(int j=0;j<n+1;j++)
//                 memo[i][j]=-1;
//         System.out.println(lcsdp(s1, s2, m,n,memo));
//         sc.close();
//     }

//     public static int max(int a, int b) {
//         if (a > b) {
//             return a;
//         }
//         return b;
//     }

//     public static int lcsdp(String s1, String s2, int m, int n,int[][] memo) {
//         if(memo[m][n]!=-1)
//             return memo[m][n];
//         if (m == 0 || n == 0) {
//             memo[m][n]=0;
//             return memo[m][n];
//         }
//         if (s1.charAt(m - 1) == s2.charAt(n - 1)) {
//             memo[m][n] =1+ lcsdp(s1, s2, m - 1, n - 1,memo);
//         } else {
//             memo[m][n]=max(lcsdp(s1, s2, m - 1, n,memo), lcsdp(s1, s2, m, n - 1,memo));
//         }
//         return memo[m][n];
//     }
// }

import java.util.*;
import java.lang.String;

public class lcs {

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String s1, s2;
        s1 = sc.nextLine();
        s2 = sc.nextLine();
        int m = s1.length();
        int n = s2.length();
        int[][] memo = new int[m + 1][n + 1];
        for (int i = 0; i < m + 1; i++)
            memo[i][0] = 0;
        for (int i = 0; i < n + 1; i++)
            memo[0][i] = 0;
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    memo[i][j] = 1 + memo[i - 1][j - 1];
                } else {
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1]);
                }
            }
        }
        System.out.println(memo[m][n]);
        sc.close();
    }

    public static int max(int a, int b) {
        if (a > b) {
            return a;
        }
        return b;
    }
}
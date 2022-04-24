// //complexity=n*n
// import java.util.ArrayList;
// import java.util.Scanner;
// import java.lang.String;
// public class lis{
//     public static void main(String args[]){
//         Scanner sc=new Scanner(System.in);
//         String str=sc.nextLine();
//         String[] str1=str.split("\\s");
//         ArrayList<Integer> array=new ArrayList<Integer>();
//         for(String w:str1){
//             array.add(Integer.parseInt(w));
//         }
//         ArrayList<Integer> array1 = new ArrayList<Integer>();
//         array1.add(1);
//         int n=array.size();
//         for(int i=0;i<n;i++){
//             array1.add(i,1);
//             for(int j=0;j<i;j++){
//                 if(array.get(j)<array.get(i)){
//                     array1.add(i,max(array1.get(i),array1.get(j)+1));
//                 }
//             }
//         }
//         int res=array1.get(0);
//         for(int i=1;i<n;i++)
//             res=max(res,array1.get(i));
//         System.out.println(res);
//         sc.close();
//     }
//     public static int max(int a,int b){
//         if(a>b) return a;
//         return b;
//     }
// }



//complexity=n(logn)
import java.util.ArrayList;
import java.util.Scanner;
import java.lang.String;

public class lis {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] str1 = str.split("\\s");
        ArrayList<Integer> array = new ArrayList<Integer>();
        for (String w : str1) {
            array.add(Integer.parseInt(w));
        }
        ArrayList<Integer> array1 = new ArrayList<Integer>();
        array1.add(array.get(0));
        int len=1;
        int n = array.size();
        for (int i = 1; i < n; i++) {
            if(array.get(i)>array1.get(len-1)){
                array1.add(array.get(i));
                len++;
            }
            else{
                int c=bs(array1,array.get(i));
                array1.add(c,array.get(i));
            }
        }
        System.out.println(array1.size());
        sc.close();
    }
    public static int bs(ArrayList<Integer> array,int x){
        int l=0;
        int r=array.size();
        while(r>l){
            int m=l+(r-l)/2;
            if(array.get(m)>x){
                r=m;
            }
            else
                l=m+1;
        }
        return r;
    }
    public static int max(int a, int b) {
        if (a > b)
            return a;
        return b;
    }
}
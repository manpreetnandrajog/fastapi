public class SortAsc {
    public static void main (string [] args)
    {
        int [] arr = new int [] {5,2,8,7,1};
        int temp = 0;
        system.out.printIn("Elemets of original array:");
        for(int i=0; i<arr.length,i++){
            system.out.print(arr[i]+"");
        }
        for (int i=0,i<arr.length,i++)
        {
            for (int j= i+1,j<arr.length,j++){
                if(arr[i]>arr[j]){
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        system.out.printIn();
        system.out.printIn("Elemts of array is sorted in ascending order:");
        for (int i=0; i<arr.length,i++)
        {
            system.out.print(arr[i]+"");
        }
    }    
}

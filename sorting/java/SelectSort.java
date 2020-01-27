class SelectSort
{
    // Java implementation of select sort.
    public static void main(String[] args)
    {
        // randomly sorted list
        int[] nums = {87, 76, 81, 53, 11};
        int smallest;
        int temp;

        for (int i=0; i<nums.length; i++)
        {
            // find the smallest element in the array
            smallest = i;
            for (int j=i+1; j < nums.length; j++)
            {
                if (nums[j] < nums[i])
                    smallest = j;
            }

            if (smallest != i)
            {
                // swap nums[i] and nums[smallest]
                temp = nums[smallest];
                nums[smallest] = nums[i];
                nums[i] = temp;
            }
        }
        // print out the result
        for (int i=0; i<nums.length; i++)
            System.out.print(nums[i] + " ");
        System.out.println("");
    }
}


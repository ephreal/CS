class BubbleSort
{
    // Bubblesort implementation in java
    public static void main(String[] args)
    {
        // randomly sorted list
        int[] nums = {87, 76, 81, 53, 11};
        Boolean swapped = true;
        int temp;

        while (swapped)
        {
            swapped = false;
            for (int i=0; i < nums.length-1; i++)
            {
                if (nums[i] > nums[i+1])
                {
                    // swap elements at nums[i] and nums[j]
                    temp = nums[i+1];
                    nums[i+1] = nums[i];
                    nums[i] = temp;
                    swapped = true;
                }
            }
        }

        // print out the sorted list
        for (int i=0; i < nums.length; i++)
        {
            System.out.print(nums[i] + " ");
        }
        System.out.println("");
    }
}


import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++) {
            int compl = target - nums[i];
            Integer complIndex = map.get(compl);
            if (complIndex != null) {
                return new int[]{complIndex, i};
            }
            map.put(nums[i], i);
        }
        return null;
    }
}
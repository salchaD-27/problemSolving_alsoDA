class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        int steps=0, cap=capacity;
        for (int i=0; i<plants.length; i++) {
            if (cap>=plants[i]) {
                steps++;
                cap-=plants[i];
            } else {
                steps+=(i*2)+1;
                cap=capacity-plants[i];
            }
        }
        return steps;
    }
}
// import java.util.ArrayList;

// class FoodRatings {
//     private String[] foods;
//     private String[] cuisines;
//     private int[] ratings;

//     public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
//         this.foods = new String[foods.length];
//         this.cuisines = new String[cuisines.length];
//         this.ratings = new int[ratings.length];
//         for (int i = 0; i < foods.length; i++) {
//             this.foods[i] = foods[i];
//             this.cuisines[i] = cuisines[i];
//             this.ratings[i] = ratings[i];
//         }
//     }

//     public void changeRating(String food, int newRating) {
//         for(int i=0; i<this.foods.length; i++){
//             if (this.foods[i].equals(food)){
//                 this.ratings[i]=newRating;
//             }
//         }
//     }

//     public String highestRated(String cuisine) {
//         ArrayList<Integer> cuisineIndices = new ArrayList<>();
//         for (int i = 0; i < this.cuisines.length; i++) {
//             if (this.cuisines[i].equals(cuisine)) { 
//                 cuisineIndices.add(i);
//             }
//         }
    
//         String bestFood = null;
//         int highestRating = Integer.MIN_VALUE;
//         for (int index : cuisineIndices) {
//             if (this.ratings[index] > highestRating || 
//                (this.ratings[index] == highestRating && this.foods[index].compareTo(bestFood) < 0)) {
//                 highestRating = this.ratings[index];
//                 bestFood = this.foods[index];
//             }
//         }
//         return bestFood;
//     }
// }



import java.util.*;

class FoodRatings {
    private Map<String, String> foodToCuisine;
    private Map<String, Integer> foodToRating;
    private Map<String, TreeMap<Integer, TreeSet<String>>> cuisineRatings;

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        foodToCuisine = new HashMap<>();
        foodToRating = new HashMap<>();
        cuisineRatings = new HashMap<>();

        for (int i = 0; i < foods.length; i++) {
            foodToCuisine.put(foods[i], cuisines[i]);
            foodToRating.put(foods[i], ratings[i]);

            cuisineRatings.putIfAbsent(cuisines[i], new TreeMap<>());
            TreeMap<Integer, TreeSet<String>> ratingMap = cuisineRatings.get(cuisines[i]);
            ratingMap.putIfAbsent(ratings[i], new TreeSet<>());
            ratingMap.get(ratings[i]).add(foods[i]);
        }
    }

    public void changeRating(String food, int newRating) {
        String cuisine = foodToCuisine.get(food);
        int oldRating = foodToRating.get(food);

        TreeMap<Integer, TreeSet<String>> ratingMap = cuisineRatings.get(cuisine);
        ratingMap.get(oldRating).remove(food);
        if (ratingMap.get(oldRating).isEmpty()) {
            ratingMap.remove(oldRating);
        }
        ratingMap.putIfAbsent(newRating, new TreeSet<>());
        ratingMap.get(newRating).add(food);
        foodToRating.put(food, newRating);
    }

    public String highestRated(String cuisine) {
        TreeMap<Integer, TreeSet<String>> ratingMap = cuisineRatings.get(cuisine);
        int highestRating = ratingMap.lastKey();
        return ratingMap.get(highestRating).first();
    }
}

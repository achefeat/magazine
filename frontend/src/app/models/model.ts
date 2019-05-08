export interface Recipe {
  id: number;
  name: string;
  ingredients: Ingredient[];
  method: string;
  ccal: number;
  rating: number;
  type: Type;
  time: number;
  cuisine: Cuisine;
  diet: Diet;
  difficulty: Difficulty;
}
export interface Ingredient {
  id: number;
  name: string;
}
export interface Type {
  id: number;
  name: string;
}
export interface Cuisine {
  id: number;
  name: string;
}
export interface Difficulty {
  id: number;
  name: string;
}
export interface Diet {
  id: number;
  name: string;
}

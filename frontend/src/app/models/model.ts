// import {realpath} from 'fs';

export interface Recipe {
  id: number;
  name: string;
  ingredients: Ingredient[];
  method: Text;
  ccal: number;
  type: Type;
  time: number;
  cuisine: Cuisine;
  likes: Likes;
  diet: Diet;
  difficulty: Difficulty;
  photo: ImageBitmap;
}
export interface Likes {
  id: number;
  recipes: Recipe[];
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
export interface Comments {
  id: number;
  description: string;
  recipes: Recipe[];
}
export interface IAuthResponse {
  token: string;
  username: string;
}

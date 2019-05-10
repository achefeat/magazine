import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {MainService} from './main.service';
import {Cuisine, Diet, Difficulty, IAuthResponse, Ingredient, Recipe, Type} from '../models/model';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }
  getRecipes(): Promise<Recipe[]> {
    return this.get('http://localhost:8000/home/recipelist/', {});
  }
  // createRecipe()
  // like(recipe: Recipe): Promise<Recipe[]> {
  //   return this.put(`http://localhost:8000/home/recipe/like/${recipe.id}/`, {
  //     likes: recipe.likes,
  //     name: recipe.name,
  //     ingredients: recipe.ingredients,
  //     method: recipe.method,
  //     ccal: recipe.ccal,
  //     type: recipe.type,
  //     time: recipe.time,
  //     cuisine: recipe.cuisine,
  //     diet: recipe.diet,
  //     difficulty: recipe.difficulty,
  //     // photo: recipe.photo
  //   });
  // }
  getCurrentRecipe(recipe: Recipe): Promise<Recipe> {
    return this.get(`http://localhost:8000/home/recipe/${recipe.id}/`, {});
  }
  auth(uname: any, pword: any): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/home/login/', {
      username: uname,
      password: pword
    });
  }
  logout(): Promise<any> {
    return this.post(`http://localhost:8000/home/logout/`, {});
  }
}

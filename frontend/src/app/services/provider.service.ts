import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {MainService} from './main.service';
import {Recipe} from '../models/model';

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
  like(recipe: Recipe): Promise<Recipe[]> {
    return this.put(`http://localhost:8000/home/recipe/like/${recipe.id}`, {});
  }
}

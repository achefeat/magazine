import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {MainService} from './main.service';
import {Cuisine, Diet, Difficulty, IAuthResponse, Ingredient, Likes, Recipe, Type} from '../models/model';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  fileData: File = null;

  constructor(http: HttpClient) {
    super(http);
  }
  getRecipes(): Promise<Recipe[]> {
    return this.get('http://localhost:8000/home/recipelist/', {});
  }
  createRecipe(name: string, ingredients: Ingredient[], method: Text, ccal: number,
               time: number, type: Type, cuisine: Cuisine, diet: Diet, diff: Difficulty, photo: ImageBitmap): Promise<Recipe> {
    return this.post('http://localhost:8000/home/recipelist/', {
      name,
      ingredients,
      method,
      ccal,
      time,
      type,
      cuisine,
      diet,
      diff
    });
  }

  fileProgress(fileInput: any) {
    this.fileData = <File> fileInput.target.files[0];
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.fileData);
    this.http.post('http://localhost:8000/home/recipelist/', formData)
      .subscribe(res => {
        console.log(res);
        alert('SUCCESS !!');
      });
  }
  getTypes(): Promise<Type[]> {
    return this.get('http://localhost:8000/home/typelist/', {});
  }
  getCuisine(): Promise<Cuisine[]> {
    return this.get('http://localhost:8000/home/cuisinelist/', {});
  }
  getDiffs(): Promise<Difficulty[]> {
    return this.get('http://localhost:8000/home/difficultylist/', {});
  }
  getDiets(): Promise<Diet[]> {
    return this.get('http://localhost:8000/home/dietlist/', {});
  }
  like(recipe: number): Promise<Recipe> {
    return this.post(`http://localhost:8000/home/likes/`, {
      recipe,
    });
  }
  // getLike(recipe:)
  getCurrentRecipe(id: number): Promise<Recipe> {
    return this.get(`http://localhost:8000/home/recipe/${id}/`, {});
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
  signup(username: string, email: string, password: string): Promise<any> {
    return this.post('http://localhost:8000/home/signup/', {
      username,
      email,
      password
    });
  }

  getIngr(): Promise<Ingredient[]> {
    return this.get('http://localhost:8000/home/ingredientlist/', {});
  }
}

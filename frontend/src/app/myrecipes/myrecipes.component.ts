import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Cuisine, Diet, Difficulty, Ingredient, Recipe, Type} from '../models/model';

@Component({
  selector: 'app-myrecipes',
  templateUrl: './myrecipes.component.html',
  styleUrls: ['./myrecipes.component.css']
})
export class MyrecipesComponent implements OnInit {

  constructor(private provider: ProviderService ) {}

  public name: any;
  public recipeList: Recipe[] = [];
  public ingrList: Ingredient[] = [];
  public  method: string;
  public  ccal: number;
  public  type: Type;
  public  time: number;
  public  cuisine: Cuisine;
  public  diet: Diet;
  public  difficulty: Difficulty;
  public  photo: string;
  ngOnInit() {
  }
  createRecipe() {
    if (this.name !== '') {
      this.provider.createRecipe(this.name, this.ingrList, this.method, this.ccal, this.type,
        this.time, this.cuisine, this.diet, this.difficulty, this.photo).then(res => {
        this.name = '';
        this.recipeList.push(res);
      });
    }
  }
  log() {

  }
}

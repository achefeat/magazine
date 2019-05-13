import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Cuisine, Diet, Difficulty, Ingredient, Recipe, Type} from '../models/model';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient, HttpEventType } from '@angular/common/http';

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
  public  method: Text;
  public  ccal: number;
  public  type: Type;
  public types: Type[] = [];
  public  time: number;
  public  cuisine: Cuisine;
  public  diet: Diet;
  public  diets: Diet[] = [];
  public  difficulty: Difficulty;
  public  difficulties: Difficulty[] = [];
  public  photo: string;

  ngOnInit() {
    this.provider.getDiets().then(res => this.diets = res);
    this.provider.getDiffs().then(res => this.difficulties = res);
    this.provider.getTypes().then(res => this.types = res);
  }
  // createRecipe() {
  //   if (this.name !== '') {
  //     this.provider.createRecipe(this.name, this.ingrList, this.method, this.ccal, this.type,
  //       this.time, this.cuisine, this.diet, this.difficulty, this.photo).then(res => {
  //       this.name = '';
  //       this.recipeList.push(res);
  //     });
  //   }
  // }
  onSubmit() {
    this.provider.onSubmit();
  }
}

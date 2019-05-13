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

  public rname: string;
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
  public  photo: ImageBitmap;
  public show = false;
  userSelects = [];
  userSelectsString = '';

  ngOnInit() {
    this.provider.getDiets().then(res => this.diets = res);
    this.provider.getDiffs().then(res => this.difficulties = res);
    this.provider.getTypes().then(res => this.types = res);
    this.provider.getIngr().then(res => this.ingrList = res);
  }
  createRecipe() {
    if (this.rname !== '') {
      this.provider.createRecipe(this.rname, this.userSelects, this.method, this.ccal,
        this.time, this.type, this.cuisine, this.diet, this.difficulty, this.photo).then(res => {
        this.rname = '';
        this.recipeList.push(res);
      });
    }
  }

  suggest() {
    this.show = true;
  }
  isSelected(s: any) {
    return this.userSelects.findIndex((item) => item.id === s.id) > -1;
  }
  selectSuggestion(s) {
    this.userSelects.find((item) => item.id === s.id) ?
      this.userSelects = this.userSelects.filter((item) => item.id !== s.id) :
      this.userSelects.push(s);
  }
  deleteSelects(s) {
    this.userSelects = this.userSelects.filter((item) => item.id !== s.id);
  }
  assignToNgModel() {
    this.userSelectsString = '';
    this.userSelects.map((item) => this.userSelectsString += item.name + ' ');
  }
  onSubmit() {
    this.provider.onSubmit();
  }
}

import { Component, OnInit } from '@angular/core';
import { ProviderService} from '../services/provider.service';
import {Cuisine, Ingredient, Recipe} from '../models/model';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private provider: ProviderService ) {}
  public recipes: Recipe[] = [];
  public recipe: Recipe;
  // public ingredients: Ingredient[] = [];
  public logged = true;


  ngOnInit() {
    this.provider.getRecipes().then(res => {
      this.recipes = res;
    });
  }
  // likeRecipe(recipe: Recipe) {
  //   this.provider.like(recipe).then(res => {});
  // }
  // getCurRecipe(recipe: Recipe) {
  //   this.provider.getCurrentRecipe(recipe).then(res => {
  //     this.recipe = res;
  //   });
  // }
}


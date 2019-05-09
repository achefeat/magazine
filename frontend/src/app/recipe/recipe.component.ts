import { Component, OnInit } from '@angular/core';
import { ProviderService} from '../services/provider.service';
import {Cuisine, Ingredient, Recipe} from '../models/model';

@Component({
  selector: 'app-recipe',
  templateUrl: './recipe.component.html',
  styleUrls: ['./recipe.component.css']
})
export class RecipeComponent implements OnInit {

  constructor(private provider: ProviderService ) { }
  public recipe: Recipe;
  public ingredients: Ingredient[] = [];


  ngOnInit() {
    this.getCurRecipe(this.recipe);
  }
  getCurRecipe(recipe: Recipe) {
    this.provider.getCurrentRecipe(recipe).then(res => {
      this.recipe = res;
    });
  }
}

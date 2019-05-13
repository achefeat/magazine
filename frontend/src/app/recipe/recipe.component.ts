import { Component, OnInit } from '@angular/core';
import { ProviderService} from '../services/provider.service';
import {Cuisine, Ingredient, Recipe} from '../models/model';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-recipe',
  templateUrl: './recipe.component.html',
  styleUrls: ['./recipe.component.css']
})
export class RecipeComponent implements OnInit {

  public params: any;
  public loading = false;
  public recipe: Recipe;
  public ingredients: Ingredient[] = [];

  constructor(private route: ActivatedRoute, private provider: ProviderService ) { }


  ngOnInit() {
    this.route.params.subscribe(params => {
      this.params = params;
      console.log(this.params.id);
      this.provider.getCurrentRecipe(this.params.id).then(res => {
        this.recipe = res;
      });
    });
  }
  // getCurRecipe(recipe: Recipe) {
  //   this.provider.getCurrentRecipe(recipe.id).then(res => {
  //     this.recipe = res;
  //   });
  // }
}

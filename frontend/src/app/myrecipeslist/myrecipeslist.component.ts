import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Recipe} from '../models/model';

@Component({
  selector: 'app-myrecipeslist',
  templateUrl: './myrecipeslist.component.html',
  styleUrls: ['./myrecipeslist.component.css']
})
export class MyrecipeslistComponent implements OnInit {
  public recipes: Recipe[] = [];
  public recipe: Recipe;

  constructor(private provider: ProviderService ) {}

  ngOnInit() {
    this.provider.getRecForUser().then(res => {
      this.recipes = res;
    });
  }
  updateRec(recipe: Recipe) {
    this.provider.updateRecipe(recipe).then(res => {
      console.log(recipe.name + ' updated');
    });
  }
  deleteRec(recipe: Recipe) {
    this.provider.deleteRecipe(recipe).then(res => {
      console.log(recipe.name + ' updated');
      this.provider.getRecForUser().then(r => {
        this.recipes = r;
      });
    });
  }
}

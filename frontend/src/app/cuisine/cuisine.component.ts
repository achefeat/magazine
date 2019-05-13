import { Component, OnInit } from '@angular/core';
import { ProviderService} from '../services/provider.service';
import {Cuisine, Ingredient, Recipe} from '../models/model';
@Component({
  selector: 'app-cuisine',
  templateUrl: './cuisine.component.html',
  styleUrls: ['./cuisine.component.css']
})
export class CuisineComponent implements OnInit {
  constructor(private provider: ProviderService ) {}
  public recipes: Recipe[] = [];

  ngOnInit() {
    this.provider.getRecipes().then(res => {
      this.recipes = res;
    });

  }

}

import { Component, OnInit } from '@angular/core';
import { ProviderService} from '../services/provider.service';
import {Cuisine, Ingredient, Recipe} from '../models/model';
@Component({
  selector: 'app-diet',
  templateUrl: './diet.component.html',
  styleUrls: ['./diet.component.css']
})
export class DietComponent implements OnInit {
  constructor(private provider: ProviderService ) {}
  public recipes: Recipe[] = [];

  ngOnInit() {
    this.provider.getRecipes().then(res => {
      this.recipes = res;
    });
  }

}

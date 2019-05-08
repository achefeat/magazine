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
  public ingredients: Ingredient[] = [];
  public cuisine: Cuisine[] = [];
  ngOnInit() {
    this.provider.getRecipes().then(res => {
      this.recipes = res;
    });
  }

}

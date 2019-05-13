import { Component, OnInit } from '@angular/core';
import { ProviderService} from '../services/provider.service';
import {Cuisine, Ingredient, Recipe} from '../models/model';
@Component({
  selector: 'app-type',
  templateUrl: './type.component.html',
  styleUrls: ['./type.component.css']
})
export class TypeComponent implements OnInit {
  constructor(private provider: ProviderService ) {}
  
  public recipes: Recipe[] = [];

  ngOnInit() {
    this.provider.getRecipes().then(res => {
      this.recipes = res;
    });
  }

}

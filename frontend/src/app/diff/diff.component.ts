import { Component, OnInit } from '@angular/core';
import { ProviderService} from '../services/provider.service';
import {Cuisine, Ingredient, Recipe} from '../models/model';
@Component({
  selector: 'app-diff',
  templateUrl: './diff.component.html',
  styleUrls: ['./diff.component.css']
})
export class DiffComponent implements OnInit {
  constructor(private provider: ProviderService ) {}
  public recipes: Recipe[] = [];


  ngOnInit() {
    this.provider.getRecipes().then(res => {
      this.recipes = res;
    });
  }

}

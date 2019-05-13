import { Component, OnInit } from '@angular/core';
import { ProviderService} from '../services/provider.service';
import {Cuisine, Ingredient, Recipe, Type, Difficulty, Diet} from '../models/model';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  public types: Type[] = [];  
  public diff: Difficulty[] = [];  
  public diet: Diet[] = []
  constructor(private provider: ProviderService ) {}


  ngOnInit() {
    this.provider.getTypes().then(res => {
      this.types = res;
    });
    this.provider.getDiffs().then(res => {
      this.diff = res;
    });
    this.provider.getDiets().then(res => {
      this.diet = res;
    });
  }

}

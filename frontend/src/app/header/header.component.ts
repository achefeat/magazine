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
  public diet: Diet[] = [];
  public cuisine: Cuisine[] = [];
  public recipes: Recipe[] = [];
  public logged = false;
  public username: any;
  public password: any;

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
    this.provider.getCuisine().then(res => {
      this.cuisine = res;
    });
  }

  //

  auth() {
    if (this.username !== '' && this.password !== '') {
      this.provider.auth(this.username, this.password).then( res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.username = '';
        this.password = '';
        // this.provider.getRecipes().then(r => {
        //   this.recipes = r;
        // });
        console.log('OK');
      });
    }
  }
  logout() {
    this.provider.logout().then( res => {
      localStorage.clear();
      this.logged = false;
    });
  }
}

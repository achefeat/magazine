import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MainComponent} from './main/main.component';
import {RecipeComponent} from './recipe/recipe.component';
import {MyrecipesComponent} from './myrecipes/myrecipes.component';
import { DiffComponent } from './diff/diff.component';
import {DietComponent} from './diet/diet.component';
import {TypeComponent} from './type/type.component';
import {CuisineComponent} from './cuisine/cuisine.component';
import {SignupComponent} from './signup/signup.component';
import {MyrecipeslistComponent} from './myrecipeslist/myrecipeslist.component';


const routes: Routes = [
  {path: 'main', component: MainComponent},
  {path: 'recipe/:id', component: RecipeComponent},
  {path: 'myRecipes', component: MyrecipesComponent},
  {path: 'diff', component: DiffComponent},
  {path: 'diet', component: DietComponent},
  {path: 'type', component: TypeComponent},
  {path: 'cuisine', component: CuisineComponent},
  {path: 'signup', component: SignupComponent},
  {path: 'myRecipesList', component: MyrecipeslistComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

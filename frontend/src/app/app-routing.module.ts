import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MainComponent} from './main/main.component';
import {RecipeComponent} from './recipe/recipe.component';

const routes: Routes = [
  {path: 'main', component: MainComponent},
  {path: 'recipe', component: RecipeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

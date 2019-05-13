import { BrowserModule } from '@angular/platform-browser';
import {ClassProvider, NgModule} from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import {ProviderService} from './services/provider.service';
import {FormsModule} from '@angular/forms';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import { RecipeComponent } from './recipe/recipe.component';
import { SignupComponent } from './signup/signup.component';
import {AuthInterceptor} from './AuthInterceptor';
import { MyrecipesComponent } from './myrecipes/myrecipes.component';
import { DiffComponent } from './diff/diff.component';
import { DietComponent } from './diet/diet.component';
import { TypeComponent } from './type/type.component';
import { CuisineComponent } from './cuisine/cuisine.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    FooterComponent,
    HeaderComponent,
    RecipeComponent,
    SignupComponent,
    MyrecipesComponent,
    DiffComponent,
    DietComponent,
    TypeComponent,
    CuisineComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    ProviderService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    } as ClassProvider
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

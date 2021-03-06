import {Component, Input} from '@angular/core';
import {ProviderService} from './services/provider.service';
import {Recipe} from './models/model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  @Input() name: string;
  title = 'a-Chef-eat!';

  constructor(private provider: ProviderService) { }
  // public recipes: Recipe[] = [];
  // public logged = false;
  // public username: any;
  // public password: any;
  // //
  //
  // auth() {
  //   if (this.username !== '' && this.password !== '') {
  //     this.provider.auth(this.username, this.password).then( res => {
  //       localStorage.setItem('token', res.token);
  //       this.logged = true;
  //
  //       // this.provider.getRecipes().then(r => {
  //       //   this.recipes = r;
  //       // });
  //       console.log('OK');
  //     });
  //   }
  // }
  // logout() {
  //   this.provider.logout().then( res => {
  //     localStorage.clear();
  //     this.logged = false;
  //   });
  // }
}

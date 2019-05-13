import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Recipe} from '../models/model';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  constructor(private provider: ProviderService ) {}

  public recipes: Recipe[] = [];
  public logged = false;
  public username: any;
  public password: any;
  public newusername: any;
  public newpassword: any;
  public email: any;
  public loggedUsername = '';
  ngOnInit() {
  }
  auth() {
    if (this.username !== '' && this.password !== '') {
      this.provider.auth(this.username, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.loggedUsername = res.username;
        this.username = '';
        this.password = '';
        // this.provider.getCategories().then(r => {
        //   this.categories = r;
        // });
      });
    }
  }
  logout() {
    this.provider.logout().then(res => {
      localStorage.removeItem('token');
      this.logged = false;
    });
  }
  signup() {
    if (this.newusername !== '' && this.email && this.newpassword !== '') {
      this.provider.signup(this.newusername, this.email, this.newpassword).then(res =>
        this.provider.auth(this.newusername, this.newpassword).then(r => {
          localStorage.setItem('token', r.token);
          this.logged = true;
          this.loggedUsername = r.username;
          this.newusername = '';
          this.newpassword = '';
        }));
    }
  }
}

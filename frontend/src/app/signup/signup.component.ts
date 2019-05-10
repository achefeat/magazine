import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  constructor(private provider: ProviderService ) {}

  ngOnInit() {
  }

}

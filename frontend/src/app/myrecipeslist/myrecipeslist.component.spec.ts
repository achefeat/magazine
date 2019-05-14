import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MyrecipeslistComponent } from './myrecipeslist.component';

describe('MyrecipeslistComponent', () => {
  let component: MyrecipeslistComponent;
  let fixture: ComponentFixture<MyrecipeslistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MyrecipeslistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MyrecipeslistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

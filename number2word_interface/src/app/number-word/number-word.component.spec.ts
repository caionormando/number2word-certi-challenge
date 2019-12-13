import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NumberWordComponent } from './number-word.component';

describe('NumberWordComponent', () => {
  let component: NumberWordComponent;
  let fixture: ComponentFixture<NumberWordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NumberWordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NumberWordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
